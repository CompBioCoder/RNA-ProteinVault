import { mkdir, readFile, rename, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const SCRIPT_DIRECTORY = dirname(fileURLToPath(import.meta.url));
export const RUN_LOG_PATH = resolve(SCRIPT_DIRECTORY, '..', 'cache', 'run_log.json');

export async function appendLog(entry) {
	await mkdir(dirname(RUN_LOG_PATH), { recursive: true });
	let current = [];
	try {
		const parsed = JSON.parse(await readFile(RUN_LOG_PATH, 'utf8'));
		if (Array.isArray(parsed)) {
			current = parsed;
		}
	} catch (error) {
		if (error?.code !== 'ENOENT') {
			current = [];
		}
	}

	const next = [
		...current,
		{
			id: `${Date.now()}-${Math.random().toString(16).slice(2, 8)}`,
			timestamp: new Date().toISOString(),
			chapter: String(entry.chapter ?? 'SYSTEM'),
			status: String(entry.status ?? 'info'),
			message: String(entry.message ?? ''),
			detail: String(entry.detail ?? ''),
		},
	].slice(-200);

	const temporaryPath = `${RUN_LOG_PATH}.tmp-${process.pid}`;
	await writeFile(temporaryPath, `${JSON.stringify(next, null, 2)}\n`, 'utf8');
	await rename(temporaryPath, RUN_LOG_PATH);
	return next.at(-1);
}
