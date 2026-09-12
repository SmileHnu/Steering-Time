document.querySelectorAll('audio').forEach((player) => {
  const waveform = player.closest('.audio-card').querySelector('.waveform');
  const updateProgress = () => {
    if (!waveform) return;
    const progress = Number.isFinite(player.duration) && player.duration > 0
      ? Math.max(0, Math.min(100, player.currentTime / player.duration * 100)) : 0;
    waveform.style.setProperty('--remaining', `${100 - progress}%`);
  };
  ['timeupdate', 'seeked', 'loadedmetadata', 'emptied', 'ended'].forEach((event) => {
    player.addEventListener(event, updateProgress);
  });
  updateProgress();
  player.addEventListener('play', () => {
    document.querySelectorAll('audio').forEach((other) => {
      if (other !== player) other.pause();
    });
  });
  const showError = () => {
    player.closest('.audio-card').querySelector('.audio-error').hidden = false;
  };
  player.addEventListener('error', showError);
  player.querySelector('source').addEventListener('error', showError);
});
