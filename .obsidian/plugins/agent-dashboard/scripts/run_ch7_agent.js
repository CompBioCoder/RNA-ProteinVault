import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH7',
	labelCn: 'RNA 结构评估',
	labelEn: 'RNA ASSESSMENT',
	folders: ['notes/04_RNA Structure Assessment'],
});
