import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH6',
	labelCn: 'RNA 结构预测',
	labelEn: 'RNA PREDICTION',
	folders: ['notes/03_RNA Structure Prediction'],
});
