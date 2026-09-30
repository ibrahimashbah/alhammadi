(() => {
  const uiStyle = document.createElement('style');
  uiStyle.textContent = `
    /* Compact floating contact actions */
    .floating-actions {
      gap: 7px !important;
      align-items: flex-start;
    }
    .float-btn {
      width: 140px !important;
      height: 48px !important;
      min-height: 48px !important;
      padding: 3px 3px 3px 12px !important;
      border-radius: 18px !important;
      border: 1px solid #b9c0c4 !important;
      background: #fff !important;
      color: #26323a !important;
      display: flex !important;
      flex-direction: row !important;
      direction: rtl;
      justify-content: space-between !important;
      align-items: center !important;
      box-shadow: 0 3px 10px rgba(8,10,11,.10) !important;
      font-family: 'IBM Plex Sans Arabic', system-ui, sans-serif !important;
      font-size: 14px !important;
      font-weight: 500 !important;
      line-height: 1 !important;
      overflow: hidden;
      will-change: auto !important;
    }
    .float-btn:hover { transform: translateY(-1px); background:#fff !important; }
    .float-btn svg {
      order: 0;
      width: 40px !important;
      height: 40px !important;
      min-width: 40px;
      padding: 9px;
      border-radius: 12px;
      background: #22c55e;
      color: #fff;
      stroke: currentColor;
      box-sizing: border-box;
    }
    .float-btn::after {
      order: 1;
      flex: 1;
      text-align: center;
      white-space: nowrap;
    }
    html[lang="ar"] .float-btn.whatsapp::after { content: 'واتساب'; }
    html[lang="ar"] .float-btn.call::after { content: 'اتصل بنا'; }
    html[lang="en"] .float-btn.whatsapp::after { content: 'WhatsApp'; }
    html[lang="en"] .float-btn.call::after { content: 'Call us'; }

    /* Performance: avoid expensive live blur while scrolling */
    .site-header.is-sticky {
      background: #f1f2ef !important;
      backdrop-filter: none !important;
      -webkit-backdrop-filter: none !important;
    }

    /* Let the browser defer painting long off-screen sections */
    @supports (content-visibility: auto) {
      main > .section:not(#contact),
      main > section.wash,
      main > section.dark:not(.hero) {
        content-visibility: auto;
        contain-intrinsic-size: auto 850px;
      }
    }

    /* Make the mobile navigation fully opaque after sticky-header activation */
    @media (max-width: 1050px) {
      .nav.mobile-open {
        background: #f7f7f4 !important;
        color: #080A0B !important;
        opacity: 1 !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        isolation: isolate;
      }
      .nav.mobile-open::before {
        content: '';
        position: fixed;
        inset: 0;
        z-index: -1;
        background: #f7f7f4;
        opacity: 1;
      }
      .nav.mobile-open a { color:#080A0B !important; opacity:1 !important; }
      body.menu-open .site-header,
      body.menu-open .site-header.is-sticky {
        background: #f7f7f4 !important;
        color: #080A0B !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        box-shadow: none !important;
      }
      body.menu-open .menu-toggle,
      body.menu-open .lang-switch {
        color:#080A0B !important;
        border-color:#b7bec2 !important;
        background:#fff !important;
      }
    }

    @media (max-width: 680px) {
      .floating-actions {
        inset-inline-end: 10px !important;
        bottom: max(12px, env(safe-area-inset-bottom)) !important;
        gap: 6px !important;
      }
      .float-btn {
        width: 126px !important;
        height: 44px !important;
        min-height: 44px !important;
        padding: 3px 3px 3px 10px !important;
        border-radius: 17px !important;
        font-size: 13px !important;
        box-shadow: 0 2px 8px rgba(8,10,11,.08) !important;
      }
      .float-btn svg {
        width: 36px !important;
        height: 36px !important;
        min-width: 36px;
        padding: 8px;
        border-radius: 10px;
      }
      /* Touch devices: shorter, cheaper transitions for a lighter feel */
      .reveal {
        transition-duration: .32s !important;
        transform: translateY(10px);
      }
      .reveal.in { transform: none; }
      .practice-card,
      .btn-primary,
      .btn-ghost,
      .nav a,
      .link-arrow .arrow {
        transition-duration: .16s !important;
      }
    }

    @media (hover: none) and (pointer: coarse) {
      .practice-card:hover { transform: none !important; }
      .practice-card:hover::before { transform: rotate(45deg) !important; }
      .btn-primary:hover, .float-btn:hover { transform: none !important; }
    }

    @media (prefers-reduced-motion: reduce) {
      html { scroll-behavior: auto !important; }
      *, *::before, *::after {
        animation-duration: .001ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: .001ms !important;
      }
      .reveal { opacity: 1 !important; transform: none !important; }
    }
  `;
  document.head.appendChild(uiStyle);

  const html = document.documentElement;
  const saved = localStorage.getItem('alhammadi-lang');
  const initial = saved === 'en' ? 'en' : 'ar';
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  function setLang(lang) {
    html.lang = lang;
    html.dir = lang === 'ar' ? 'rtl' : 'ltr';
    localStorage.setItem('alhammadi-lang', lang);
    document.querySelectorAll('[data-lang-switch]').forEach(btn => {
      btn.textContent = lang === 'ar' ? 'EN' : 'عربي';
      btn.setAttribute('aria-label', lang === 'ar' ? 'Switch to English' : 'التبديل إلى العربية');
    });
    const arTitle = document.body.dataset.titleAr;
    const enTitle = document.body.dataset.titleEn;
    if (arTitle && enTitle) document.title = lang === 'ar' ? arTitle : enTitle;
  }
  setLang(initial);

  document.querySelectorAll('[data-lang-switch]').forEach(btn => {
    btn.addEventListener('click', () => setLang(html.lang === 'ar' ? 'en' : 'ar'));
  });

  const header = document.querySelector('.site-header');
  let scrollTicking = false;
  const syncHeader = () => {
    header?.classList.toggle('is-sticky', window.scrollY > 72);
    scrollTicking = false;
  };
  syncHeader();
  window.addEventListener('scroll', () => {
    if (!scrollTicking) {
      scrollTicking = true;
      requestAnimationFrame(syncHeader);
    }
  }, {passive:true});

  const menuBtn = document.querySelector('[data-menu-toggle]');
  const nav = document.querySelector('.nav');
  const closeMenu = () => {
    nav?.classList.remove('mobile-open');
    document.body.classList.remove('menu-open');
    if (menuBtn) {
      menuBtn.textContent = '☰';
      menuBtn.setAttribute('aria-expanded','false');
      menuBtn.setAttribute('aria-label', html.lang === 'ar' ? 'فتح القائمة' : 'Open menu');
    }
  };
  menuBtn?.addEventListener('click', () => {
    const open = nav?.classList.toggle('mobile-open');
    document.body.classList.toggle('menu-open', !!open);
    menuBtn.setAttribute('aria-expanded', String(!!open));
    menuBtn.textContent = open ? '×' : '☰';
    menuBtn.setAttribute('aria-label', open ? (html.lang === 'ar' ? 'إغلاق القائمة' : 'Close menu') : (html.lang === 'ar' ? 'فتح القائمة' : 'Open menu'));
  });

  /* Native smooth section navigation, with motion preference respected */
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (ev) => {
      const id = link.getAttribute('href');
      if (!id || id === '#') return;
      const target = document.querySelector(id);
      if (!target) return;
      ev.preventDefault();
      closeMenu();
      target.scrollIntoView({
        behavior: reduceMotion.matches ? 'auto' : 'smooth',
        block: 'start'
      });
      if (history.replaceState) history.replaceState(null, '', id);
    });
  });

  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMenu(); });
  window.addEventListener('resize', () => { if (window.innerWidth > 1050) closeMenu(); }, {passive:true});

  if ('IntersectionObserver' in window && !reduceMotion.matches) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: .06, rootMargin: '0px 0px -12px 0px' });
    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
  }

  /* Image loading policy: eager only for the hero, lazy for the rest */
  const heroImage = document.querySelector('.hero-visual > img');
  if (heroImage) {
    heroImage.loading = 'eager';
    heroImage.fetchPriority = 'high';
    heroImage.decoding = 'async';
  }
  document.querySelectorAll('main img').forEach(img => {
    if (img !== heroImage && !img.closest('.site-header')) {
      if (!img.hasAttribute('loading')) img.loading = 'lazy';
      img.decoding = 'async';
    }
  });

  document.querySelectorAll('.visual-panel > img').forEach(img => {
    const fail = () => img.closest('.visual-panel')?.classList.add('image-missing');
    img.addEventListener('error', fail, {once:true});
    if (img.complete && img.naturalWidth === 0) fail();
  });
  document.querySelectorAll('.partner-logo img').forEach(img => {
    const fail = () => img.closest('.partner-logo')?.classList.add('image-missing');
    img.addEventListener('error', fail, {once:true});
    if (img.complete && img.naturalWidth === 0) fail();
  });
  document.querySelectorAll('.practice-icon, .practice-detail-head img').forEach(img => {
    const fail = () => { img.style.display = 'none'; };
    img.addEventListener('error', fail, {once:true});
    if (img.complete && img.naturalWidth === 0) fail();
  });

  const form = document.querySelector('[data-consultation-form]');
  form?.addEventListener('submit', (ev) => {
    ev.preventDefault();
    const fd = new FormData(form);
    const ar = html.lang === 'ar';
    const msg = ar
      ? `طلب استشارة قانونية\n\nالاسم: ${fd.get('name') || ''}\nرقم التواصل: ${fd.get('phone') || ''}\nالبريد: ${fd.get('email') || ''}\nالموضوع: ${fd.get('subject') || ''}\n\nملخص المسألة:\n${fd.get('message') || ''}`
      : `Legal consultation request\n\nName: ${fd.get('name') || ''}\nPhone: ${fd.get('phone') || ''}\nEmail: ${fd.get('email') || ''}\nSubject: ${fd.get('subject') || ''}\n\nMatter summary:\n${fd.get('message') || ''}`;
    window.open(`https://wa.me/966555334489?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
  });
})();
