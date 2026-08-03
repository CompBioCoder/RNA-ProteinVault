import { runCollectionAudit } from './run_agent_common.mjs';

await runCollectionAudit({
	chapter: 'CH3',
	labelCn: '文献综述',
	labelEn: 'REVIEWS',
	folders: ['notes/00_Reviews'],
});
