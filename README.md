# Steering-Time

Temporal control in text-to-audio generation.

**[Listen to the audio demos →](https://SmileHnu.github.io/Steering-Time/)**

The demo page can be accessed at: [https://smilehnu.github.io/Steering-Time/](https://smilehnu.github.io/Steering-Time/).

## Code and dataset availability

The code and counterfactual dataset are being organized and will be released progressively as they become ready.

代码和反事实数据集正在整理中，整理完毕后将陆续开放。

## Audio demos

The demo presents one instruction for each of four temporal control tasks: **Ordering**, **Duration**, **Frequency**, and **Timestamp**. Each instruction is shared by seven models: AudioGen, AudioLDM, AudioLDM2, Tango, Tango2, TangoFlux, and TangoFlux + Ours.

## Samples

| Task | Sample | Instruction |
| --- | --- | --- |
| Ordering | syn_107 | Someone coughs twice, followed by a sequence of cricket chirps occurring four times. |
| Duration | syn_1 | A cat meowed for 1.092 seconds, followed by a cowbell ringing for 5.167 seconds. |
| Frequency | syn_100 | A water tap or faucet was turned on twice. |
| Timestamp | syn_181 | A mosquito is heard buzzing from 1.248 to 6.067 seconds and again from 6.798 to 10.0 seconds. |

One audio example is presented for each temporal instruction type. Original WAV files are preserved unchanged.

[`docs/samples.json`](docs/samples.json) records the instructions, model labels, sample IDs, generation seeds, durations, and SHA-256 checksums. Each instruction appears once on the page, with seven corresponding audio players (28 recordings total).

## Preview locally

No installation or build step is required. Open `docs/index.html` in a browser, or serve it locally:

```sh
python -m http.server 8000 --directory docs
```

Then visit `http://localhost:8000`.

## GitHub Pages

The site is served from the **`main` branch, `/docs` folder**. In the repository's **Settings → Pages**, select **Deploy from a branch**, then `main` and `/docs`. Changes pushed to `main` are published automatically.

The page uses plain HTML, CSS, and JavaScript, with relative asset paths compatible with GitHub project Pages. Audio is loaded on demand; starting another recording pauses the previous one.
