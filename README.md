# The World Today — 24 November 2026

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/edisonhuzs/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/edisonhuzs/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page that sums up the world's news of Tuesday, 24 November 2026, drawn as a single 1024×1024 image. The masthead reads "The World Today" with the date line right underneath, so the day it covers is named on the page itself. The page was drawn from scratch with Python and Pillow — masthead, headlines, body text, rules and the small ship illustration are all drawn by code, with no photographs or borrowed artwork.

## What is in the picture

- **Lead story — the war spreads to new waters.** The EU put forward a 22nd package of sanctions against Russia, and Ukraine said its forces had sunk a Russian warship off the coast of Libya. The front page carries a small drawn scene of the ship on the Mediterranean to go with it.
- **Disaster in Indonesia.** A fire tore through a candy factory in Banten province, killing at least 24 people, with dozens still missing as rescue teams search the wreckage.
- **Climate talks stall.** COP31 in Antalya closed without an agreement on fossil-fuel language, the negotiators still divided.
- **The chip king returns.** Jensen Huang is back as chief executive of Nvidia after a board inquiry, and the company's shares jumped more than 31% in a single day.
- **Also today.** Thousands marched in Lisbon over the cost of living; Max Verstappen won the Las Vegas Grand Prix; India and Nepal flagged off the Saryu–Kamala Express train; and Chicago's O'Hare airport was hit by a brief ground stop during the Thanksgiving travel rush.

## Verification

Run the program from this folder:

```sh
python3 main.py
```

It copies `entry.png` to `/output/entry.png` (creating `/output` if needed), then prints the file's byte count and SHA-256 hash, confirms the copy matches the source, and checks that the output is a valid 1024×1024 PNG. Run `python3 main.py --help` to see the usage text. The image itself is 1024×1024 pixels and 129,120 bytes — well under the 1 MiB limit. Running the program twice writes identical bytes both times, since it is a plain copy of the same file.
