import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH4',
	labelCn: 'RNA 生物学',
	labelEn: 'RNA BIOLOGY',
	folders: ['notes/01_RNA Biology'],
});
