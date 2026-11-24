You compare two strategy analyses (ANALYSIS 1 and ANALYSIS 2), produced independently from the same subject dossier. You will receive PAIRWISE_INPUT containing the DOSSIER, an ANSWER KEY (unknown to both analysts) and the two analyses. The order of the two analyses is random. Ignore order and length.

For each dimension, decide which analysis is better, or "tie" if you can't separate them:
- D1 hedgehog match to the key
- D2 stop-doing list includes the key's decision
- D3 brutal facts include the key's fact
- D5 decline risk flags the key's decline mechanism (use "na" if the key has no decline info)
- D7 calibration and honesty (no invented figures; uncertainty and missing data flagged)
- D8 one-screen verdict: concise and actionable
- overall: which would you rather hand to the subject's leader?

Return only JSON, with no other text:
```json
{"D1": "1|2|tie", "D2": "...", "D3": "...", "D5": "1|2|tie|na", "D7": "...", "D8": "...", "overall": "1|2|tie", "why": "two sentences"}
```
