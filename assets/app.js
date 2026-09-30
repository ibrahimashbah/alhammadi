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

    /* Office / Google Maps section */
    .office-location-section {
      background: #f6f6f2;
      border-top: 1px solid rgba(8,10,11,.09);
      overflow: hidden;
    }
    .office-location-grid {
      display: grid;
      grid-template-columns: minmax(0,.88fr) minmax(440px,1.12fr);
      gap: clamp(42px,6vw,86px);
      align-items: stretch;
    }
    .office-location-copy {
      padding-block: 8px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      min-width: 0;
    }
    .office-location-copy .title-lg {
      margin-top: 12px;
      max-width: 700px;
    }
    .office-location-copy .lead {
      max-width: 640px;
      margin: 24px 0 0;
    }
    .office-address {
      margin-top: 34px;
      padding-top: 28px;
      border-top: 1px solid rgba(8,10,11,.12);
      display: grid;
      grid-template-columns: 46px 1fr;
      gap: 16px;
      align-items: start;
    }
    .office-pin {
      width: 46px;
      height: 46px;
      border: 1px solid rgba(8,10,11,.12);
      display: grid;
      place-items: center;
      background: #fff;
      color: var(--copper);
    }
    .office-pin svg { width: 20px; height: 20px; }
    .office-address strong {
      display: block;
      font-size: 16px;
      font-weight: 600;
      margin-bottom: 6px;
    }
    .office-address p {
      margin: 0;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.85;
    }
    .office-location-actions {
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      margin-top: 30px;
    }
    .maps-btn {
      min-height: 52px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 11px;
      padding: 0 22px;
      background: var(--night);
      color: #fff;
      border: 1px solid var(--night);
      font-size: 14px;
      font-weight: 600;
      transition: transform .2s ease, background .2s ease;
    }
    .maps-btn:hover { transform: translateY(-1px); background: #183741; }
    .maps-btn svg { width: 17px; height: 17px; }
    .google-rating-card {
      display: inline-flex;
      align-items: center;
      gap: 14px;
      padding: 10px 14px;
      min-height: 52px;
      border: 1px solid rgba(8,10,11,.12);
      background: #fff;
    }
    .google-rating-score {
      min-width: 48px;
      text-align: center;
      font-size: 22px;
      line-height: 1;
      font-weight: 600;
      color: var(--ink);
    }
    .google-rating-meta { line-height: 1.35; }
    .google-rating-stars {
      display: flex;
      gap: 2px;
      color: #d3a82f;
      direction: ltr;
      margin-bottom: 4px;
    }
    .google-rating-stars svg { width: 13px; height: 13px; }
    .google-rating-meta small {
      display: block;
      color: var(--muted);
      font-size: 10px;
      white-space: nowrap;
    }
    .office-map-card {
      position: relative;
      min-height: 510px;
      background: #e7e8e3;
      border: 1px solid rgba(8,10,11,.10);
      overflow: hidden;
      box-shadow: 0 24px 70px rgba(8,10,11,.10);
    }
    .office-map-card iframe {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      border: 0;
      filter: saturate(.72) contrast(.96);
    }
    .office-map-badge {
      position: absolute;
      z-index: 2;
      inset-inline-start: 18px;
      bottom: 18px;
      background: rgba(16,42,50,.94);
      color: #fff;
      padding: 13px 15px;
      max-width: calc(100% - 36px);
      box-shadow: 0 8px 30px rgba(0,0,0,.18);
      pointer-events: none;
    }
    .office-map-badge strong {
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: var(--gold-2);
      margin-bottom: 2px;
    }
    .office-map-badge span {
      display: block;
      font-size: 11px;
      color: rgba(255,255,255,.74);
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
      .office-location-grid {
        grid-template-columns: 1fr;
        gap: 38px;
      }
      .office-map-card { min-height: 430px; }
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
      .office-location-section { padding-block: 78px !important; }
      .office-location-copy .lead { font-size: 16px; }
      .office-location-actions { align-items: stretch; }
      .maps-btn, .google-rating-card { width: 100%; }
      .google-rating-card { justify-content: center; }
      .office-map-card { min-height: 340px; }
      .office-map-badge { inset-inline-start: 12px; bottom: 12px; max-width: calc(100% - 24px); }
    }

    @media (hover: none) and (pointer: coarse) {
      .practice-card:hover { transform: none !important; }
      .practice-card:hover::before { transform: rotate(45deg) !important; }
      .btn-primary:hover, .float-btn:hover, .maps-btn:hover { transform: none !important; }
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

  /* Office location section. Rating data checked against the current Google Maps listing. */
  const main = document.querySelector('main');
  if (main && !document.querySelector('#office-location')) {
    main.insertAdjacentHTML('beforeend', `
      <section class="section office-location-section onepage-anchor" id="office-location">
        <div class="container office-location-grid">
          <div class="office-location-copy reveal">
            <span class="eyebrow"><span class="lang-ar">زورونا في المكتب</span><span class="lang-en">Visit our office</span></span>
            <h2 class="title-lg"><span class="lang-ar">مكتبنا في قلب الرياض.</span><span class="lang-en">Our office in the heart of Riyadh.</span></h2>
            <p class="lead"><span class="lang-ar">نستقبل عملاءنا في مقر الشركة بحي الملك فهد. يمكنكم فتح الموقع مباشرة على Google Maps للحصول على الاتجاهات والوصول إلى المكتب بسهولة.</span><span class="lang-en">We welcome clients at our King Fahd District office. Open the location directly in Google Maps for directions and easy navigation to the office.</span></p>

            <div class="office-address">
              <div class="office-pin" aria-hidden="true">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>
              </div>
              <div>
                <strong><span class="lang-ar">شركة أحمد الحمادي للمحاماة</span><span class="lang-en">Ahmad Al Hammadi Law Firm</span></strong>
                <p><span class="lang-ar">مبنى مركز ليوا، الدور الأول، مكتب 19، طريق الإمام سعود بن عبدالعزيز بن محمد الفرعي، حي الملك فهد، الرياض 12274</span><span class="lang-en">Liwa Center Building, First Floor, Office 19, Al Imam Saud Ibn Abdul Aziz Branch Rd, King Fahd, Riyadh 12274</span></p>
              </div>
            </div>

            <div class="office-location-actions">
              <a class="maps-btn" href="https://maps.app.goo.gl/jYjyMW6sqA4fEF4r7?g_st=ic" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M20 10c0 5-8 11-8 11S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>
                <span class="lang-ar">فتح الموقع في Google Maps</span><span class="lang-en">Open in Google Maps</span>
                <span aria-hidden="true">↗</span>
              </a>

              <div class="google-rating-card" aria-label="Google Maps rating">
                <div class="google-rating-score" dir="ltr">—</div>
                <div class="google-rating-meta">
                  <div class="google-rating-stars" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z"/></svg>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z"/></svg>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z"/></svg>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z"/></svg>
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="m12 3 2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3l-5.6 2.9 1.1-6.2L3 9.6l6.2-.9L12 3Z"/></svg>
                  </div>
                  <small><span class="lang-ar">0 تقييم على Google</span><span class="lang-en">0 Google reviews</span></small>
                </div>
              </div>
            </div>
          </div>

          <div class="office-map-card reveal">
            <iframe
              title="Ahmad Al Hammadi Law Firm location in Riyadh"
              src="https://www.google.com/maps?q=Liwa%20Center%20Building%2C%20King%20Fahd%2C%20Riyadh%2012274%2C%20Saudi%20Arabia&output=embed"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              allowfullscreen>
            </iframe>
            <div class="office-map-badge">
              <strong><span class="lang-ar">الرياض — حي الملك فهد</span><span class="lang-en">Riyadh — King Fahd District</span></strong>
              <span><span class="lang-ar">مركز ليوا · الدور الأول · مكتب 19</span><span class="lang-en">Liwa Center · First Floor · Office 19</span></span>
            </div>
          </div>
        </div>
      </section>
    `);
  }

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
