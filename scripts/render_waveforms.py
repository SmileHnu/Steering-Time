"""Regenerate inline waveform previews from the original WAVs (numpy, soundfile)."""
from pathlib import Path
import html
import re
import numpy as np
import soundfile as sf

site = Path(__file__).resolve().parents[1] / 'docs'
page = site / 'index.html'
text = page.read_text(encoding='utf-8')
text = re.sub(r'\n\s*<div class="waveform">.*?</div>', '', text, flags=re.S)
count = 0

def render(match):
    global count
    audio = match.group(0)
    path = re.search(r'src="([^"]+)"', audio).group(1)
    label = re.search(r'aria-label="([^"]+)"', audio).group(1)
    samples, rate = sf.read(site / path, always_2d=True)
    if not np.isfinite(samples).all():
        raise ValueError(f'Non-finite samples in {path}')
    # Preserve stereo peaks instead of averaging channels, which can cancel them.
    edges = np.linspace(0, len(samples), 241, dtype=int)
    scale = 27 / max(1.0, float(np.abs(samples).max()))
    commands = []
    for i in range(240):
        block = samples[edges[i]:edges[i+1]]
        low, high = float(block.min()), float(block.max())
        commands.append(f'M{i+.5:.1f},{30-high*scale:.2f}V{30-low*scale:.2f}')
    waveform = ' '.join(commands)
    duration = len(samples) / rate
    count += 1
    return audio + f'''
          <div class="waveform">
            <svg viewBox="0 0 240 60" preserveAspectRatio="none" role="img" aria-label="{label} waveform">
              <title>{label} — amplitude over {duration:g} seconds</title>
              <path class="wave-axis" d="M0 30H240"/>
              <path class="wave-base" d="{waveform}"/>
              <path class="wave-played" d="{waveform}"/>
            </svg>
            <span class="wave-times" aria-hidden="true"><span>0 s</span><span>{duration:g} s</span></span>
          </div>'''

text = re.sub(r'<audio\b[^>]*>.*?</audio>', render, text, flags=re.S)
page.write_text(text, encoding='utf-8')
print(f'Rendered {count} waveform previews from original WAV samples.')
