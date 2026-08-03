import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const SCRIPT_DIRECTORY = dirname(fileURLToPath(import.meta.url));
const CACHE_DIRECTORY = resolve(SCRIPT_DIRECTORY, '..', 'cache');

const SOURCE_FILE = {
	pubmed: 'pubmed.json',
	preprints: 'preprints.json',
	github: 'github.json',
	arxiv: 'arxiv.json',
};

const PUBMED_SEARCH =
	'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=%28%22RNA%20structure%20prediction%22%5BTitle%2FAbstract%5D%20OR%20%22RNA%20sequence%20design%22%5BTitle%2FAbstract%5D%20OR%20%22protein%20structure%20prediction%22%5BTitle%2FAbstract%5D%20OR%20%22protein%20design%22%5BTitle%2FAbstract%5D%29&retmode=json&retmax=5&sort=pub%2Bdate';
const PREPRINT_SEARCH =
	'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=SRC%3APPR%20AND%20%28%22RNA%20structure%20prediction%22%20OR%20%22RNA%20sequence%20design%22%20OR%20%22protein%20structure%20prediction%22%20OR%20%22protein%20design%22%29&format=json&pageSize=5&sort_date=y';
const GITHUB_RNA_SEARCH =
	'https://api.github.com/search/repositories?q=RNA%20secondary%20structure%20prediction%20in%3Aname%2Cdescription%20stars%3A%3E2&sort=stars&order=desc&per_page=5';
const GITHUB_PROTEIN_SEARCH =
	'https://api.github.com/search/repositories?q=protein%20design%20in%3Aname%2Cdescription%20stars%3A%3E10&sort=stars&order=desc&per_page=5';
const ARXIV_ATOM =
	'https://export.arxiv.org/api/query?search_query=%28cat%3Aq-bio.BM%20OR%20cat%3Aq-bio.GN%29%20AND%20%28all%3ARNA%20OR%20all%3Aprotein%29&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending';

export async function runSourceCli(source) {
	try {
		const payload = await fetchAndCache(source);
		process.stdout.write(`${source}: ${payload.count} items\n`);
	} catch (error) {
		process.stderr.write(`${source}: ${message(error)}\n`);
		process.exitCode = 1;
	}
}

export async function fetchAndCache(source) {
	if (!(source in SOURCE_FILE)) {
		throw new Error(`Unknown source: ${source}`);
	}
	const items = await fetchSource(source);
	const payload = {
		source,
		fetchedAt: new Date().toISOString(),
		count: items.length,
		items: items.slice(0, 5),
	};
	await mkdir(CACHE_DIRECTORY, { recursive: true });
	await writeFile(
		resolve(CACHE_DIRECTORY, SOURCE_FILE[source]),
		`${JSON.stringify(payload, null, 2)}\n`,
		'utf8',
	);
	return payload;
}

export async function fetchAllSources() {
	const sources = Object.keys(SOURCE_FILE);
	const settled = await Promise.allSettled(sources.map((source) => fetchAndCache(source)));
	return settled.map((result, index) => {
		const source = sources[index];
		return result.status === 'fulfilled'
			? { source, ok: true, count: result.value.count }
			: { source, ok: false, count: 0, error: message(result.reason) };
	});
}

async function fetchSource(source) {
	switch (source) {
		case 'pubmed':
			return fetchPubMed();
		case 'preprints':
			return fetchPreprints();
		case 'github':
			return fetchGitHub();
		case 'arxiv':
			return parseAtom(await requestText(ARXIV_ATOM));
		default:
			throw new Error(`Unsupported source: ${source}`);
	}
}

async function fetchPubMed() {
	const search = JSON.parse(await requestText(PUBMED_SEARCH));
	const ids = Array.isArray(search?.esearchresult?.idlist)
		? search.esearchresult.idlist.map(String).filter(Boolean).slice(0, 5)
		: [];
	if (ids.length === 0) {
		return [];
	}
	const summaryUrl = `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=${encodeURIComponent(ids.join(','))}&retmode=json`;
	const summary = JSON.parse(await requestText(summaryUrl));
	return ids
		.map((id) => summary?.result?.[id])
		.filter((record) => record && typeof record === 'object')
		.map((record) => ({
			title: cleanText(typeof record.title === 'string' ? record.title : ''),
			url: record.uid ? `https://pubmed.ncbi.nlm.nih.gov/${record.uid}/` : '',
			published: typeof record.pubdate === 'string' ? record.pubdate : '',
			summary: [record.sortfirstauthor, record.fulljournalname]
				.filter((value) => typeof value === 'string' && value)
				.join(' · '),
		}))
		.filter((item) => item.title && item.url);
}

async function fetchPreprints() {
	const parsed = JSON.parse(await requestText(PREPRINT_SEARCH));
	const results = Array.isArray(parsed?.resultList?.result) ? parsed.resultList.result : [];
	return results
		.filter((record) => record && typeof record === 'object')
		.map((record) => ({
			title: cleanText(typeof record.title === 'string' ? record.title : ''),
			url:
				typeof record.doi === 'string' && record.doi
					? `https://doi.org/${encodeURIComponent(record.doi)}`
					: record.source && record.id
						? `https://europepmc.org/article/${encodeURIComponent(record.source)}/${encodeURIComponent(record.id)}`
						: '',
			published:
				typeof record.firstPublicationDate === 'string'
					? record.firstPublicationDate
					: String(record.pubYear ?? ''),
			summary: [record.authorString, record.journalTitle]
				.filter((value) => typeof value === 'string' && value)
				.join(' · '),
		}))
		.filter((item) => item.title && item.url)
		.slice(0, 5);
}

async function requestText(url) {
	const response = await fetch(url, {
		headers: {
			Accept: 'application/json, application/atom+xml, application/rss+xml, text/xml',
			'User-Agent': 'RNAProteinDashboard/0.2.2',
		},
		signal: AbortSignal.timeout(30_000),
	});
	if (!response.ok) {
		throw new Error(`HTTP ${response.status}`);
	}
	return response.text();
}

async function fetchGitHub() {
	const [rnaItems, proteinItems] = await Promise.all([
		fetchGitHubQuery(GITHUB_RNA_SEARCH),
		fetchGitHubQuery(GITHUB_PROTEIN_SEARCH),
	]);
	const combined = [...rnaItems.slice(0, 3), ...proteinItems];
	return combined
		.filter((item, index) => combined.findIndex((candidate) => candidate.url === item.url) === index)
		.slice(0, 5);
}

async function fetchGitHubQuery(url) {
	const parsed = JSON.parse(await requestText(url));
	if (!Array.isArray(parsed.items)) {
		throw new Error('GitHub response did not contain an items array.');
	}
	return parsed.items
		.map((item) => ({
			title: typeof item.full_name === 'string' ? item.full_name : '',
			url: safeUrl(item.html_url),
			published: typeof item.updated_at === 'string' ? item.updated_at : '',
			summary: cleanText(typeof item.description === 'string' ? item.description : ''),
		}))
		.filter((item) => item.title && item.url)
		.slice(0, 5);
}

function parseAtom(xml) {
	return extractBlocks(xml, 'entry')
		.map((block) => ({
			title: cleanText(readXmlTag(block, 'title')),
			url: safeUrl(readAtomLink(block) || readXmlTag(block, 'id')),
			published: readXmlTag(block, 'published') || readXmlTag(block, 'updated'),
			summary: cleanText(readXmlTag(block, 'summary')),
		}))
		.filter((item) => item.title && item.url)
		.slice(0, 5);
}

function extractBlocks(xml, tag) {
	const expression = new RegExp(`<${tag}(?:\\s[^>]*)?>([\\s\\S]*?)</${tag}>`, 'giu');
	return [...xml.matchAll(expression)].map((match) => match[1] ?? '');
}

function readXmlTag(block, tag) {
	const expression = new RegExp(`<${tag}(?:\\s[^>]*)?>([\\s\\S]*?)</${tag}>`, 'iu');
	const value = block.match(expression)?.[1] ?? '';
	return decodeXml(value.replace(/^<!\[CDATA\[|\]\]>$/gu, '').trim());
}

function readAtomLink(block) {
	const alternate = block.match(
		/<link\s+[^>]*rel=["']alternate["'][^>]*href=["']([^"']+)["'][^>]*\/?\s*>/iu,
	)?.[1];
	if (alternate) {
		return decodeXml(alternate);
	}
	return decodeXml(
		block.match(/<link\s+[^>]*href=["']([^"']+)["'][^>]*\/?\s*>/iu)?.[1] ?? '',
	);
}

function cleanText(value) {
	return decodeXml(value.replace(/<[^>]+>/gu, ' ')).replace(/\s+/gu, ' ').trim();
}

function decodeXml(value) {
	const named = { amp: '&', apos: "'", gt: '>', lt: '<', quot: '"' };
	return value
		.replace(/&([a-z]+);/giu, (match, entity) => named[entity.toLowerCase()] ?? match)
		.replace(/&#(x?[0-9a-f]+);/giu, (match, code) => {
			const radix = code.toLowerCase().startsWith('x') ? 16 : 10;
			const point = Number.parseInt(radix === 16 ? code.slice(1) : code, radix);
			return Number.isFinite(point) ? String.fromCodePoint(point) : match;
		});
}

function safeUrl(value) {
	if (typeof value !== 'string') {
		return '';
	}
	try {
		const url = new URL(value.trim());
		return url.protocol === 'http:' || url.protocol === 'https:' ? url.toString() : '';
	} catch {
		return '';
	}
}

function message(error) {
	return error instanceof Error ? error.message : String(error);
}
