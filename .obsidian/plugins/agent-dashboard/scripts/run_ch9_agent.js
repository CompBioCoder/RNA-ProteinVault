import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH9',
	labelCn: '蛋白预测与设计',
	labelEn: 'PROTEIN',
	folders: ['notes/06_Protein Prediction', 'notes/07_Protein Design'],
});
