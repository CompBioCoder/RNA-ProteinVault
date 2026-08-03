import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH10',
	labelCn: 'AI 方法与数据集',
	labelEn: 'AI AND DATA',
	folders: ['notes/08_AI Methods', 'notes/09_Datasets & Databases'],
});
