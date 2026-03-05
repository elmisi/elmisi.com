document.addEventListener('DOMContentLoaded', () => {
  const el = document.querySelector('[data-typing]');
  if (!el) return;

  const text = el.textContent || '';
  const speed = 35;
  let i = 0;

  el.textContent = '';
  el.style.visibility = 'visible';

  const cursor = document.createElement('span');
  cursor.className = 'cursor';
  el.after(cursor);

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        observer.disconnect();
        type();
      }
    });
  }, { threshold: 0.5 });

  observer.observe(el);

  function type() {
    if (i < text.length) {
      el.textContent += text[i];
      i++;
      setTimeout(type, speed);
    } else {
      cursor.remove();
      const finalCursor = document.createElement('span');
      finalCursor.className = 'cursor';
      el.after(finalCursor);
    }
  }
});
