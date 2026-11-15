import json
import asyncio
import edge_tts
import os
import re

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

PATTERNS = data['PATTERNS']
WORD_FAMILIES = data['WORD_FAMILIES']

VOICE = "en-US-AriaNeural"
RATE = "-10%"

async def gen(text, path, sem):
    async with sem:
        if not text or not text.strip() or os.path.exists(path):
            return
        os.makedirs(os.path.dirname(path), exist_ok=True)
        try:
            comm = edge_tts.Communicate(text, VOICE, rate=RATE)
            await comm.save(path)
            print(f"✅ {path}")
        except Exception as e:
            print(f"❌ {path}: {e}")
        await asyncio.sleep(0.3)

async def main():
    tasks = []

    for i, p in enumerate(PATTERNS, 1):
        en = p['en']
        m = re.match(r'^(.*?)\s*___\s*([.,?!]?)\s*$', en)
        if m:
            skeleton = m.group(1).strip()
            punctuation = m.group(2) or ''
        else:
            skeleton = en.replace('___', '').strip()
            punctuation = ''

        pat_id = f"pat_{i:02d}"
        tasks.append((skeleton, f"audio/patterns/{pat_id}.mp3"))

        for j, c in enumerate(p['chunks'], 1):
            chunk_id = f"chk_{i:02d}_{j:02d}"
            tasks.append((c['en'], f"audio/chunks/{chunk_id}.mp3"))

            full = skeleton + " " + c['en'] + punctuation
            full_id = f"full_{i:02d}_{j:02d}"
            tasks.append((full, f"audio/sentences/{full_id}.mp3"))

    for fam in WORD_FAMILIES:
        rhyme = fam['r']
        tasks.append((rhyme, f"audio/rhymes/{rhyme}.mp3"))
        for item in fam['w']:
            w = item[0]
            tasks.append((w, f"audio/words/{w}.mp3"))

    sem = asyncio.Semaphore(5)
    print(f"总共 {len(tasks)} 个音频，开始生成...")
    await asyncio.gather(*[gen(t, p, sem) for t, p in tasks])
    print(f"\n✅ 全部完成")

asyncio.run(main())