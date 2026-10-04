// ─── Navigation active ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const current = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href').split('/').pop();
    if (href === current) {
      a.classList.add('active');
      const dd = a.closest('.nav-dd');
      if (dd) { const t = dd.querySelector('.nav-dd-toggle'); if (t) t.classList.add('active'); }
    }
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

// ─── Menu mobile ─────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const nav = document.querySelector('.nav');
  const links = nav && nav.querySelector('.nav-links');
  if (!nav || !links) return;
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'nav-burger';
  btn.setAttribute('aria-label', 'Menu');
  btn.setAttribute('aria-expanded', 'false');
  btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>';
  nav.appendChild(btn);
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', String(open));
  });
  links.querySelectorAll('.nav-dd-toggle').forEach(t => {
    t.addEventListener('click', () => t.closest('.nav-dd').classList.toggle('open'));
  });
  const active = links.querySelector('.nav-dd-toggle.active');
  if (active) active.closest('.nav-dd').classList.add('open');
});
