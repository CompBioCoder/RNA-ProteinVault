import { readdir, readFile, stat } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { appendLog } from './agent_log.mjs';

const SCRIPT_DIRECTORY = dirname(fileURLToPath(import.meta.url));

export async function runCollectionAudit({ chapter, labelCn, labelEn, folders }) {
	await appendLog({
		chapter,
		status: 'running',
		message: `${labelCn}审计启动 · ${labelEn} AUDIT STARTED`,
		detail: folders.join(', '),
	});

	try {
		const vaultRoot = process.env.AGENT_DASHBOARD_VAULT || (await findVaultRoot(SCRIPT_DIRECTORY));
		if (!vaultRoot) {
			throw new Error('Vault root was not found.');
		}
		const markdownFiles = [];
		for (const folder of folders) {
			markdownFiles.push(...(await collectMarkdown(resolve(vaultRoot, folder))));
		}

		let references = 0;
		let withPdf = 0;
		let withAbstract = 0;
		let openTasks = 0;
		for (const file of markdownFiles) {
			const contents = await readFile(file, 'utf8');
			if (/^zotero_key:\s*["']?[^\s"']/mu.test(contents)) {
				references += 1;
				if (/^has_pdf:\s*true\s*$/imu.test(contents)) withPdf += 1;
				if (/^has_abstract:\s*true\s*$/imu.test(contents)) withAbstract += 1;
			}
			openTasks += (contents.match(/^\s*[-*+]\s+\[ \]\s+/gmu) ?? []).length;
		}

		await appendLog({
			chapter,
			status: 'progress',
			message: `${labelCn}分类已扫描 · COLLECTION SCANNED`,
			detail: `${markdownFiles.length} notes · ${references} Zotero references`,
		});
		await appendLog({
			chapter,
			status: 'progress',
			message: `PDF ${withPdf}/${references} · 摘要 ${withAbstract}/${references}`,
			detail: `${openTasks} open tasks · read-only research audit`,
		});
		await appendLog({
			chapter,
			status: 'complete',
			message: `${labelCn}审计完成 · ${labelEn} AUDIT COMPLETE`,
			detail: 'No research notes were modified.',
		});
	} catch (error) {
		await appendLog({
			chapter,
			status: 'error',
			message: `${labelCn}审计失败 · ${labelEn} AUDIT FAILED`,
			detail: error instanceof Error ? error.message : String(error),
		});
		throw error;
	}
}

async function collectMarkdown(directory) {
	try {
		const entries = await readdir(directory, { withFileTypes: true });
		const files = [];
		for (const entry of entries) {
			const path = resolve(directory, entry.name);
			if (entry.isDirectory()) {
				files.push(...(await collectMarkdown(path)));
			} else if (entry.isFile() && entry.name.toLowerCase().endsWith('.md')) {
				files.push(path);
			}
		}
		return files;
	} catch (error) {
		if (error?.code === 'ENOENT') return [];
		throw error;
	}
}

async function findVaultRoot(startDirectory) {
	let current = resolve(startDirectory);
	while (true) {
		try {
			if ((await stat(resolve(current, '.obsidian'))).isDirectory()) return current;
		} catch {
			// Continue walking toward the filesystem root.
		}
		const parent = dirname(current);
		if (parent === current) return '';
		current = parent;
	}
}
