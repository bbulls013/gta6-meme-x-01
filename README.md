# gta6-meme-x-01

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/bbulls013/gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/bbulls013/gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

Entry for make.fun's "Post a GTA 6 meme on X" bounty. The meme: make.fun's
ghost mascot on a Vice City beach at sunset, captioned "WAITED 13 YEARS
FOR GTA 6 — DIED. STILL SHOWED UP FOR LAUNCH WEEK." Thirteen years since
GTA V is a long time to wait; the ghost didn't make it, and still isn't
missing launch week.

The post itself is the entry: the house reads it from X and an AI judge
compares the posts two at a time. This repository hands in the post's
address in `POST.json`, and `main.ts` copies it to `/output` for the
grader. The meme picture is `meme.png`; `make_meme.py` composes it from
the AI-generated scene in `assets/scene.png` (drawn from make.fun's
official press mark, https://make.fun/press/) by adding the caption in
large letters.

`POST.json` currently holds a placeholder address. It is replaced with
the real post's address once the meme is posted on X, before submission.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`out/POST.json` is then byte for byte this directory's `POST.json`.
Requires Node.js 22.18 or later. To rebuild the meme picture:
`python3 make_meme.py` (Pillow).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
