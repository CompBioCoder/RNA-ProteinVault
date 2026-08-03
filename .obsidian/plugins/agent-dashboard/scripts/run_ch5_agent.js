import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH5',
	labelCn: 'RNA 结构',
	labelEn: 'RNA STRUCTURE',
	folders: ['notes/02_RNA Structure'],
});
