from pathlib import Path
import re

# ---------- app.js runtime fixes ----------
p = Path('assets/app.js')
s = p.read_text(encoding='utf-8')
s = s.replace('<div class="google-rating-score" dir="ltr">—</div>', '<div class="google-rating-score" dir="ltr">5.0</div>')
s = s.replace('0 تقييم على Google', '86 تقييمًا على Google')
s = s.replace('0 Google reviews', '86 Google reviews')
s = s.replace('.google-rating-stars svg { width: 13px; height: 13px; }', '.google-rating-stars svg { width: 13px; height: 13px; fill: currentColor; stroke: currentColor; }')
s = s.replace('src="https://www.google.com/maps?q=Liwa%20Center%20Building%2C%20King%20Fahd%2C%20Riyadh%2012274%2C%20Saudi%20Arabia&output=embed"', 'src="https://www.google.com/maps?q=Ahmad%20Al%20Hammadi%20Law%20Firm%2C%20Riyadh%2C%20Saudi%20Arabia&output=embed"')
s = s.replace('      filter: saturate(.72) contrast(.96);\n    }', '      filter: saturate(.72) contrast(.96);\n      pointer-events: none;\n    }')
s = s.replace('<div class="office-map-card reveal">', '<div class="office-map-card reveal" role="link" tabindex="0" style="cursor:pointer" onclick="window.open(\'https://maps.app.goo.gl/jYjyMW6sqA4fEF4r7?g_st=ic\',\'_blank\',\'noopener\')">')
s = s.replace('<span class="lang-ar">زورونا في المكتب</span><span class="lang-en">Visit our office</span>', '<span class="lang-ar">زورونا في الشركة</span><span class="lang-en">Visit our firm</span>')
s = s.replace('<span class="lang-ar">مكتبنا في قلب الرياض.</span><span class="lang-en">Our office in the heart of Riyadh.</span>', '<span class="lang-ar">شركتنا في قلب الرياض.</span><span class="lang-en">Our firm in the heart of Riyadh.</span>')

marker = "  document.querySelectorAll('[data-lang-switch]').forEach(btn => {"
consultation_patch = """  document.querySelectorAll('.hero .btn-primary[href=\"#contact\"]').forEach(link => {
    link.addEventListener('click', (ev) => {
      ev.preventDefault();
      ev.stopImmediatePropagation();
      const message = html.lang === 'ar' ? 'السلام عليكم، أحتاج استشارة قانونية.' : 'Hello, I would like to request a legal consultation.';
      window.open(`https://wa.me/966555334489?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
    });
  });

"""
if marker in s and 'أحتاج استشارة قانونية' not in s:
    s = s.replace(marker, consultation_patch + marker, 1)
p.write_text(s, encoding='utf-8')

# ---------- index.html cleanup ----------
index = Path('index.html')
h = index.read_text(encoding='utf-8')

# Shorter hero copy
h = h.replace(
    'تُعد شركة د. أحمد الحمادي للمحاماة والاستشارات القانونية شركة قانونية سعودية متخصصة، تقدم حلولاً قانونية متكاملة للأفراد والشركات، مستندة إلى المعرفة القانونية العميقة، والخبرة العملية، والفهم الدقيق للأنظمة واللوائح في المملكة العربية السعودية.',
    'شركة قانونية سعودية متخصصة تقدم حلولاً عملية للأفراد والشركات، بخبرة عميقة وفهم دقيق للأنظمة في المملكة.'
)
h = h.replace(
    'Dr. Ahmad Al Hammadi Law Firm & Legal Consultancy is a specialised Saudi legal practice providing integrated solutions to individuals and businesses, grounded in deep legal knowledge, practical experience and a precise understanding of Saudi laws and regulations.',
    'A specialised Saudi law firm delivering practical solutions to individuals and businesses with deep experience and precise knowledge of Saudi law.'
)

# Add 20+ stat opposite the hero copy, then remove old side-image figure
hero_stat = '''      <div class="hero-experience reveal">
        <strong dir="ltr">20+</strong>
        <span><span class="lang-ar">عاماً من الخبرة القانونية</span><span class="lang-en">Years of legal experience</span></span>
      </div>'''
if 'class="hero-experience' not in h:
    h = h.replace('      <figure class="hero-visual reveal">', hero_stat + '\n      <figure class="hero-visual reveal">', 1)
h = re.sub(r'\s*<figure class="hero-visual reveal">.*?</figure>', '', h, count=1, flags=re.S)

# Concise About section
h = h.replace(
    'شركة د. أحمد الحمادي للمحاماة والاستشارات القانونية كيان قانوني سعودي متخصص، يقدم خدمات قانونية متكاملة للأفراد والشركات من خلال فريق من المحامين والمستشارين ذوي الخبرات القانونية التي تتجاوز عشرين عاماً في مهنة المحاماة والاستشارات القانونية.',
    'شركة قانونية سعودية متخصصة تخدم الأفراد والشركات من خلال فريق من المحامين والمستشارين ذوي خبرة عملية وقضائية ممتدة.'
)
h = h.replace(
    'Dr. Ahmad Al Hammadi Law Firm & Legal Consultancy is a specialised Saudi legal practice providing integrated services to individuals and businesses through lawyers and consultants with more than twenty years of legal experience.',
    'A specialised Saudi legal practice serving individuals and businesses through lawyers and consultants with extensive practical and judicial experience.'
)
h = h.replace(
    'نستند في أعمالنا إلى المعرفة القانونية العميقة، والخبرة العملية، والفهم الدقيق للأنظمة واللوائح في المملكة العربية السعودية. ونعمل على دراسة كل قضية بعناية، ووضع الاستراتيجية القانونية الملائمة، وتقديم حلول دقيقة وفعالة تحمي حقوق عملائنا وتدعم مصالحهم.',
    'ندرس كل مسألة بعناية، ونحدد المسار القانوني الأنسب، ونقدم حلولاً واضحة تحمي حقوق العميل وتدعم مصالحه.'
)
h = h.replace(
    'Our work is grounded in deep legal knowledge, practical experience and a precise understanding of Saudi laws and regulations. We study each matter carefully, develop the appropriate legal strategy and provide precise, effective solutions that protect client rights and support their interests.',
    'We assess each matter carefully, identify the appropriate legal path and provide clear solutions that protect client rights and interests.'
)
repeated_about = '<p><span class="lang-ar">نقدّم خدماتنا من خلال محامين ومستشارين ومحكمين ذوي خبرات واسعة ومعرفة قضائية متخصصة، مع الحرص على تلبية احتياجات العملاء في القطاعات العامة والخاصة بمهنية ووضوح، والالتزام بأعلى معايير الجودة والاحترافية والسرية.</span><span class="lang-en">Our services are delivered by lawyers, consultants and arbitrators with broad experience and specialist judicial knowledge, serving public and private sector clients with professionalism, clarity and a strong commitment to quality and confidentiality.</span></p>'
h = h.replace(repeated_about, '')

# Remove generic/repeated sections
h = re.sub(r'\n<section class="section wash">\s*<div class="container">\s*<div class="section-head reveal"><div><span class="eyebrow"><span class="lang-ar">الرؤية والرسالة والأهداف</span>[\s\S]*?</section>\n', '\n', h, count=1)
h = re.sub(r'\n<section class="section dark">\s*<div class="container approach-grid">[\s\S]*?</section>\n', '\n', h, count=1)
h = re.sub(r'\n<section class="section compact">\s*<div class="container metrics reveal">[\s\S]*?</section>\n', '\n', h, count=1)

# Practice intro: one concise paragraph
old_practice = '<div class="copy reveal"><p class="lead"><span class="lang-ar">تقدم الشركة خدماتها القانونية ضمن تسعة مجالات ممارسة رئيسية، بما يسهّل على العميل الوصول إلى التخصص المناسب وفهم نطاق الخدمة بوضوح. والاستشارة القانونية جزء أساسي من جميع مجالات الممارسة.</span><span class="lang-en">The firm’s services are organised into nine core practice areas, helping clients identify relevant expertise and understand the scope of support clearly. Legal advisory is embedded across every practice area.</span></p><p><span class="lang-ar">عندما تتقاطع المسألة بين أكثر من مجال، يُنظر إليها كوحدة قانونية متكاملة بدلاً من تجزئتها إلى ملفات منفصلة.</span><span class="lang-en">When a matter crosses more than one discipline, it is approached as an integrated legal matter rather than fragmented into separate files.</span></p></div>'
new_practice = '<div class="copy reveal"><p class="lead"><span class="lang-ar">تغطي خدماتنا تسعة مجالات رئيسية، ونتعامل مع المسائل المتقاطعة كملف قانوني متكامل.</span><span class="lang-en">Our services cover nine core areas, with cross-disciplinary matters handled as one integrated legal engagement.</span></p></div>'
h = h.replace(old_practice, new_practice)

# Remove duplicate CTAs in lower sections
knowledge_cta = '<a class="link-arrow" href="#contact"><span class="lang-ar">طلب استشارة قانونية</span><span class="lang-en">Request legal advice</span> <span class="arrow">↗</span></a>'
h = h.replace(knowledge_cta, '')
contact_actions = '<div class="contact-actions"><a class="btn-primary" href="https://wa.me/966555334489" target="_blank" rel="noopener">WhatsApp ↗</a><a class="btn-ghost" href="tel:+966555334489"><span class="lang-ar">اتصال مباشر</span><span class="lang-en">Call now</span> ↗</a></div>'
h = h.replace(contact_actions, '')

# Footer simplification + X + maps
footer_long = '<p><span class="lang-ar">شركة قانونية سعودية متخصصة، تقدم حلولاً قانونية متكاملة للأفراد والشركات، مستندة إلى المعرفة القانونية العميقة والخبرة العملية والفهم الدقيق للأنظمة واللوائح في المملكة العربية السعودية.</span><span class="lang-en">A specialised Saudi law firm providing integrated legal solutions to individuals and businesses, grounded in legal knowledge, practical experience and a precise understanding of Saudi laws and regulations.</span></p>'
footer_short = '<p><span class="lang-ar">شركة قانونية سعودية متخصصة مقرها الرياض.</span><span class="lang-en">A specialised Saudi law firm based in Riyadh.</span></p>'
h = h.replace(footer_long, footer_short)
footer_contact = '<div><h4><span class="lang-ar">التواصل</span><span class="lang-en">Contact</span></h4><div class="footer-links"><a href="tel:+966555334489" dir="ltr">+966 55 533 4489</a><a href="https://wa.me/966555334489" target="_blank" rel="noopener">WhatsApp</a><span><span class="lang-ar">الرياض، المملكة العربية السعودية</span><span class="lang-en">Riyadh, Saudi Arabia</span></span></div></div>'
footer_social = '<div><h4><span class="lang-ar">تابعونا</span><span class="lang-en">Follow</span></h4><div class="footer-links"><a href="https://x.com/Ahmadlaw81" target="_blank" rel="noopener">X · @Ahmadlaw81 ↗</a><a href="https://maps.app.goo.gl/jYjyMW6sqA4fEF4r7?g_st=ic" target="_blank" rel="noopener">Google Maps ↗</a><span><span class="lang-ar">الرياض، المملكة العربية السعودية</span><span class="lang-en">Riyadh, Saudi Arabia</span></span></div></div>'
h = h.replace(footer_contact, footer_social)

# Justice tile
aramco = '      <div class="partner-logo reveal"><img src="assets/source-images/aramco.png" alt="أرامكو السعودية" loading="lazy"><span><span class="lang-ar">أرامكو السعودية</span><span class="lang-en">Saudi Aramco</span></span></div>'
justice = '      <div class="partner-logo reveal"><img src="assets/source-images/justice.svg" alt="وزارة العدل" loading="lazy"><span><span class="lang-ar">وزارة العدل</span><span class="lang-en">Ministry of Justice</span></span></div>'
if 'assets/source-images/justice.svg' not in h and aramco in h:
    h = h.replace(aramco, aramco + '\n' + justice, 1)

h = h.replace('صورة الرياض: B.alotaby / Wikimedia Commons، ترخيص CC BY-SA 4.0 — تم قصّها بصرياً داخل التصميم.', 'صورة الرياض: Kolaiel / Wikimedia Commons، CC0.')
h = h.replace('Riyadh photo: B.alotaby / Wikimedia Commons, CC BY-SA 4.0 — visually cropped in layout.', 'Riyadh photo: Kolaiel / Wikimedia Commons, CC0.')
h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261004-finalhero2"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261004-finalhero2"', h)
index.write_text(h, encoding='utf-8')

# ---------- CSS final overrides ----------
css = Path('assets/styles.css')
c = css.read_text(encoding='utf-8')
c += '''

/* FINAL HERO — local KAFD image, clearly visible */
.hero {
  position: relative !important;
  min-height: 820px !important;
  background:
    linear-gradient(90deg, rgba(5,18,23,.16) 0%, rgba(5,18,23,.44) 48%, rgba(5,18,23,.86) 100%),
    url('kafd-hero.jpg') center 48% / cover no-repeat !important;
}
html[dir="ltr"] .hero {
  background:
    linear-gradient(90deg, rgba(5,18,23,.86) 0%, rgba(5,18,23,.44) 52%, rgba(5,18,23,.16) 100%),
    url('kafd-hero.jpg') center 48% / cover no-repeat !important;
}
.hero::before { background: none !important; opacity: 0 !important; }
.hero::after { display: none !important; }
.hero .hero-grid { display:block !important; }
.hero .hero-copy { max-width:790px !important; position:relative; z-index:2; }
.hero .hero-visual { display:none !important; }
.hero .hero-sub { max-width:690px !important; color:rgba(255,255,255,.88) !important; }
.hero .display, .hero .hero-sub { text-shadow:0 2px 24px rgba(0,0,0,.42); }
.hero-experience {
  position:absolute;
  left:0;
  top:50%;
  transform:translateY(-42%);
  width:185px;
  z-index:3;
  padding-top:18px;
  border-top:1px solid rgba(255,255,255,.50);
  color:#fff;
}
html[dir="ltr"] .hero-experience { left:auto; right:0; }
.hero-experience strong { display:block; font-size:72px; line-height:.95; font-weight:400; color:var(--gold-2); }
.hero-experience span { display:block; margin-top:12px; font-size:14px; line-height:1.6; color:rgba(255,255,255,.86); }
@media (max-width:1050px) {
  .hero { min-height:760px !important; }
  .hero-experience { display:none !important; }
}
@media (max-width:680px) {
  .hero {
    min-height:720px !important;
    background:
      linear-gradient(180deg, rgba(5,18,23,.32) 0%, rgba(5,18,23,.56) 44%, rgba(5,18,23,.88) 100%),
      url('kafd-hero.jpg') 56% center / cover no-repeat !important;
  }
  .hero .hero-copy { padding-top:28px; }
}
'''
css.write_text(c, encoding='utf-8')
