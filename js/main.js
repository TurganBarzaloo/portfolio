// ─── Navigation active ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href').split('/').pop();
    if (href === current) a.classList.add('active');
  });

  // Animate skill bars on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const fill = e.target.querySelector('.skill-bar-fill');
        if (fill) {
          const w = fill.dataset.width;
          fill.style.transition = 'width .8s cubic-bezier(.4,0,.2,1)';
          fill.style.width = w;
        }
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.skill-bar-item').forEach(el => {
    const fill = el.querySelector('.skill-bar-fill');
    if (fill) {
      const target = fill.style.width;
      fill.dataset.width = target;
      fill.style.width = '0%';
      observer.observe(el);
    }
  });

  // Card click → navigate
  document.querySelectorAll('.card[data-href]').forEach(card => {
    card.addEventListener('click', () => {
      window.location.href = card.dataset.href;
    });
    card.setAttribute('role', 'link');
    card.setAttribute('tabindex', '0');
    card.addEventListener('keydown', e => {
      if (e.key === 'Enter') window.location.href = card.dataset.href;
    });
  });
});

// ─── Back button ─────────────────────────────────────────────────────────────
function goBack() {
  if (document.referrer && document.referrer.includes(window.location.hostname)) {
    history.back();
  } else {
    window.location.href = '../index.html';
  }
}
