from pathlib import Path
import re

index = Path('index.html')
h = index.read_text(encoding='utf-8')

# 1) Hero: use the full firm name as the eyebrow / identity line.
h = h.replace(
    '<span class="eyebrow light"><span class="lang-ar">شركة قانونية سعودية متخصصة</span><span class="lang-en">Specialised Saudi Law Firm</span></span>',
    '<span class="eyebrow light hero-firm-name"><span class="lang-ar">شركة د. أحمد الحمادي للمحاماة والاستشارات القانونية</span><span class="lang-en">Dr. Ahmad Al Hammadi Law Firm & Legal Consultancy</span></span>',
    1,
)

# 2) Remove the Request a Consultation button from the hero completely.
h = re.sub(
    r'\s*<a class="btn-primary" href="#contact"><span class="lang-ar">طلب استشارة قانونية</span><span class="lang-en">Request a consultation</span>\s*<span>↗</span></a>',
    '',
    h,
    count=1,
)

# 3) Make the About experience statement explicit: more than twenty years.
h = h.replace(
    'شركة قانونية سعودية متخصصة تخدم الأفراد والشركات من خلال فريق من المحامين والمستشارين ذوي خبرة عملية وقضائية ممتدة.',
    'شركة قانونية سعودية متخصصة تخدم الأفراد والشركات من خلال فريق من المحامين والمستشارين ذوي خبرة عملية وقضائية ممتدة لأكثر من عشرين عاماً.',
    1,
)
h = h.replace(
    'A specialised Saudi legal practice serving individuals and businesses through lawyers and consultants with extensive practical and judicial experience.',
    'A specialised Saudi legal practice serving individuals and businesses through lawyers and consultants with more than twenty years of practical and judicial experience.',
    1,
)

# If the older source copy survived for any reason, normalize it too.
h = h.replace(
    'شركة قانونية سعودية متخصصة تخدم الأفراد والشركات من خلال فريق من المحامين والمستشارين ذوي خبرة عملية وقضائية ممتدة',
    'شركة قانونية سعودية متخصصة تخدم الأفراد والشركات من خلال فريق من المحامين والمستشارين ذوي خبرة عملية وقضائية ممتدة لأكثر من عشرين عاماً',
    1,
)

# Fresh asset query so iPhone Safari does not keep the older visual rules.
h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261004-client-notes"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261004-client-notes"', h)
index.write_text(h, encoding='utf-8')

# 4) Visual fixes: keep 20+ visible on mobile and remove the excessive gap around About.
css = Path('assets/styles.css')
c = css.read_text(encoding='utf-8')
c += r'''

/* Client notes — 2026-10-04 */
.hero-firm-name {
  max-width: 760px;
  line-height: 1.7;
}

/* Keep the experience marker visible on every viewport. */
.hero-experience {
  display: flex !important;
  flex-direction: column;
  justify-content: flex-end;
  align-self: end;
  justify-self: start;
  position: relative;
  z-index: 3;
  color: #fff;
  min-width: 190px;
  padding: 18px 0 4px;
  border-top: 1px solid rgba(255,255,255,.38);
  text-shadow: 0 2px 18px rgba(0,0,0,.35);
}
.hero-experience strong {
  font-size: clamp(46px,5vw,76px);
  line-height: .95;
  font-weight: 500;
  letter-spacing: -.04em;
}
.hero-experience > span {
  margin-top: 10px;
  max-width: 180px;
  font-size: 14px;
  line-height: 1.65;
  color: rgba(255,255,255,.88);
}

/* Remove the unnecessarily large vertical void between About and the next section. */
#about.section {
  padding-bottom: clamp(42px,5vw,70px) !important;
}
#about + .section {
  padding-top: clamp(42px,5vw,70px) !important;
}
#about .editorial-split {
  align-items: center !important;
}

@media (max-width: 900px) {
  .hero .hero-grid {
    grid-template-columns: 1fr !important;
    gap: 26px !important;
  }
  .hero-experience {
    display: flex !important;
    width: min(100%, 360px);
    min-width: 0;
    justify-self: stretch;
    align-self: auto;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    gap: 16px;
    margin-top: 4px;
    padding: 18px 0 0;
  }
  .hero-experience strong {
    flex: 0 0 auto;
    font-size: 42px;
  }
  .hero-experience > span {
    margin-top: 0;
    max-width: 190px;
    font-size: 13px;
  }
  #about.section {
    padding-bottom: 36px !important;
  }
  #about + .section {
    padding-top: 36px !important;
  }
}
'''
css.write_text(c, encoding='utf-8')
