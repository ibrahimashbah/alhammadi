from pathlib import Path
import re

# Apply the latest client-requested wording after all profile/compact transforms.
index = Path('index.html')
h = index.read_text(encoding='utf-8')

# Hero tagline: remove the full stops for a cleaner visual treatment.
h = h.replace(
    '<span class="lang-ar">معرفة قانونية.<br>رأي مستقل.<br>التزام بمصالحك.</span>',
    '<span class="lang-ar">معرفة قانونية<br>رأي مستقل<br>التزام بمصالحك</span>'
)
h = h.replace(
    '<span class="lang-en">Legal knowledge.<br>Independent judgment.<br>Commitment to your interests.</span>',
    '<span class="lang-en">Legal knowledge<br>Independent judgment<br>Commitment to your interests</span>'
)

# Remove the integrated legal expertise section requested by the client.
h = re.sub(
    r'\s*<section class="section dark profile-expertise">[\s\S]*?</section>\s*',
    '\n',
    h,
    count=1,
)

# Refresh asset query to avoid stale iPhone/Safari cache.
h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261005-remove-expertise"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261005-remove-expertise"', h)
index.write_text(h, encoding='utf-8')

# Google review count requested by the client.
app = Path('assets/app.js')
s = app.read_text(encoding='utf-8')
s = re.sub(r'\d+\s+تقييم(?:ًا)? على Google', '243 تقييمًا على Google', s)
s = re.sub(r'\d+\s+Google reviews', '243 Google reviews', s)
app.write_text(s, encoding='utf-8')
