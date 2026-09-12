document.querySelectorAll('audio').forEach((player) => {
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
