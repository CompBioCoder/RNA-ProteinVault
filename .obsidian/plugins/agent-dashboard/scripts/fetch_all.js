import { fetchAllSources } from './fetch_utils.mjs';

const results = await fetchAllSources();
for (const result of results) {
	if (result.ok) {
		process.stdout.write(`${result.source}: ${result.count} items\n`);
	} else {
		process.stderr.write(`${result.source}: ${result.error}\n`);
		process.exitCode = 1;
	}
}
