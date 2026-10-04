from pathlib import Path
import re

index = Path('index.html')
h = index.read_text(encoding='utf-8')

# Remove pricing / fees wording from the professional-relationship pillar.
h = h.replace('نحدد نطاق الخدمة والأتعاب والمسؤوليات،', 'نحدد نطاق الخدمة والمسؤوليات،')
h = h.replace('We define the scope of service, fees and responsibilities,', 'We define the scope of service and responsibilities,')

# Keep every approved practice-area detail, but collapse the long scope lists by default.
pattern = re.compile(
    r'(<article class="practice-detail reveal"[^>]*>[\s\S]*?<p class="practice-summary">[\s\S]*?</p>)'
    r'(<h4 class="practice-scope">[\s\S]*?</h4>)'
    r'(<div><ul class="lang-ar">[\s\S]*?</ul><ul class="lang-en">[\s\S]*?</ul></div>)'
    r'(</article>)'
)

def collapse_scope(match):
    head, scope_heading, scope_lists, end = match.groups()
    return (
        head
        + '<details class="practice-scope-details">'
          '<summary><span class="lang-ar">عرض نطاق الممارسة</span>'
          '<span class="lang-en">View scope of practice</span>'
          '<span class="scope-toggle" aria-hidden="true">+</span></summary>'
          '<div class="practice-scope-body">'
        + scope_heading + scope_lists
        + '</div></details>' + end
    )

h, count = pattern.subn(collapse_scope, h)

# Fresh CSS query for mobile Safari / CDN caches.
h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261004-compact"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261004-compact"', h)
index.write_text(h, encoding='utf-8')

css = Path('assets/styles.css')
c = css.read_text(encoding='utf-8')
if '/* Compact one-page pass */' not in c:
    c += r'''

/* Compact one-page pass — preserve content, reduce scrolling */
.section {
  padding-block: clamp(62px, 6vw, 82px) !important;
}
.section.compact {
  padding-block: clamp(48px, 5vw, 64px) !important;
}
.section-head {
  margin-bottom: clamp(30px, 3.5vw, 44px) !important;
  gap: clamp(28px, 4vw, 52px) !important;
}

/* Slightly shorter first screen while keeping the KAFD hero prominent. */
.hero {
  min-height: 680px !important;
  height: 88svh !important;
  max-height: 820px !important;
}
.hero-inner { padding-bottom: clamp(48px, 6vw, 70px) !important; }
.hero-bottom { margin-top: 28px !important; }
.hero-sub { margin-top: 20px !important; }

/* About + working principles */
#about .copy p { margin-bottom: 16px !important; }
.profile-pillars .section-head { margin-bottom: 28px !important; }
.profile-pillars .principle {
  padding: 24px !important;
  min-height: 0 !important;
}
.profile-pillars .principle p { margin-bottom: 0 !important; }
.profile-expertise .copy p { margin-bottom: 16px !important; }

/* Practice areas: 9 long sections become a compact card grid. */
.profile-practice-details {
  padding-block: clamp(50px, 5vw, 70px) !important;
}
.profile-practice-details .practice-detail-list {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 1px !important;
  background: var(--line);
  border: 1px solid var(--line);
}
.profile-practice-details .practice-detail {
  padding: 26px !important;
  min-height: 0 !important;
  background: var(--paper);
  border: 0 !important;
  display: flex;
  flex-direction: column;
}
.profile-practice-details .practice-detail-head {
  margin-bottom: 18px !important;
}
.profile-practice-details .practice-detail-head img {
  width: 42px !important;
  height: 42px !important;
}
.profile-practice-details .practice-detail h2 {
  margin-bottom: 10px !important;
  font-size: clamp(22px, 2vw, 30px) !important;
}
.profile-practice-details .practice-summary {
  margin: 0 0 18px !important;
  font-size: 14px !important;
  line-height: 1.75 !important;
}
.practice-scope-details {
  margin-top: auto;
  border-top: 1px solid var(--line);
  padding-top: 14px;
}
.practice-scope-details summary {
  list-style: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  font-size: 13px;
  font-weight: 600;
  color: var(--copper);
  user-select: none;
}
.practice-scope-details summary::-webkit-details-marker { display: none; }
.scope-toggle {
  width: 28px;
  height: 28px;
  border: 1px solid var(--line);
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  font-size: 18px;
  line-height: 1;
  transition: transform .2s ease;
}
.practice-scope-details[open] .scope-toggle { transform: rotate(45deg); }
.practice-scope-body {
  padding-top: 14px;
}
.practice-scope-body .practice-scope {
  margin-top: 0 !important;
}
.practice-scope-body ul {
  margin-block: 8px 0 !important;
  padding-inline-start: 20px !important;
  font-size: 13px !important;
  line-height: 1.7 !important;
}

/* Partners: denser visual wall instead of tall logo cards. */
.profile-partners-grid {
  grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
}
.profile-partners-grid .partner-logo {
  min-height: 145px !important;
  padding: 18px 12px !important;
}
.profile-partners-grid .partner-logo > img {
  height: 54px !important;
  max-width: 115px !important;
}
.profile-partners-grid .partner-logo > span {
  margin-top: 12px !important;
  font-size: 12px !important;
  line-height: 1.45 !important;
}
.profile-partners-grid .partner-wordmark-mark {
  min-width: 54px !important;
  min-height: 54px !important;
  font-size: 16px !important;
}

/* Knowledge/resource cards and office section tighter, without removing features. */
#knowledge .ecosystem-grid { gap: 12px !important; }
#knowledge .eco-card { padding: 20px !important; }
.office-section, #contact { padding-block: clamp(56px, 5vw, 76px) !important; }

@media (max-width: 1050px) {
  .profile-practice-details .practice-detail-list {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
  .profile-partners-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  }
}

@media (max-width: 760px) {
  .section { padding-block: 46px !important; }
  .section-head { margin-bottom: 26px !important; }
  .hero {
    height: auto !important;
    min-height: 690px !important;
    max-height: none !important;
  }
  .hero-inner { padding-bottom: 42px !important; }
  .profile-pillars .principle { padding: 20px !important; }
  .profile-practice-details .practice-detail-list {
    grid-template-columns: 1fr !important;
  }
  .profile-practice-details .practice-detail { padding: 22px !important; }
  .profile-partners-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
  }
  .profile-partners-grid .partner-logo { min-height: 130px !important; }
}
'''
css.write_text(c, encoding='utf-8')

print(f'Collapsed practice scopes: {count}')
