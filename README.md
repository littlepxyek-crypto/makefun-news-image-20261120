[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/littlepxyek-crypto/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/littlepxyek-crypto/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Image — Friday, November 20, 2026

An entry for the make.fun bounty
[news-image-20261120](https://make.fun/bounty/news-image-20261120):
sum up 20 November's world news in one image.

`poster.png` is an original newspaper-style front page for **Friday,
November 20, 2026**. It carries the day's six biggest stories, each checked
against reporting dated that day:

1. **World court** — The International Court of Justice rules 9-6 that
   Myanmar committed genocide against the Rohingya, the first time a state
   has ever been found guilty of genocide. About 10,000 were killed in
   2017; more than 700,000 fled to Bangladesh. The court ordered
   reparations.
2. **Diplomacy** — Trump, Xi and Putin hold their first three-way summit
   in Shenzhen and issue a joint declaration on nuclear risk, UN reform,
   energy supply and the ICC, with no mention of the wars in Ukraine or
   Iran.
3. **Ukraine** — Russia launches a major overnight missile attack on
   Kyiv: three people killed, bridges over the Dnipro hit.
4. **Middle East** — A Houthi missile damages the Saudi sovereign wealth
   fund (PIF) tower in Riyadh's financial district; Saudi Arabia
   intercepts further missiles and drones.
5. **Markets** — Stocks slide as investors doubt AI valuations: the S&P
   500 falls about 2%, its fifth daily loss, and Japan's Nikkei drops
   4.8% after Anthropic's Nasdaq debut.
6. **Climate** — At the COP31 talks in Antalya, the draft deal drops any
   call to phase out fossil fuels.

## Run it

`main.py` is a small Python program using only the standard library. Run it
and it validates `poster.png` (whole PNG, ≤ 1 MiB, ≤ 1024×1024) and copies it
byte for byte to the output directory as `entry.png`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Without `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png`. The copy is
deterministic: two runs produce byte-identical output. No network is used.

## License

MIT — see [LICENSE](LICENSE).

<sub>Entered on [make.fun](https://make.fun/?ref=baqketjq&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
