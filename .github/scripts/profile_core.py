from pathlib import Path
import re

index = Path('index.html')
h = index.read_text(encoding='utf-8')

# Navigation wording from the approved profile.
h = h.replace('<span class="lang-ar">المعرفة القانونية</span><span class="lang-en">Legal Knowledge</span>', '<span class="lang-ar">مصادر معرفية</span><span class="lang-en">Legal Resources</span>')

hero = '''<section class="hero onepage-anchor" id="top">
  <div class="container hero-inner">
    <div class="hero-grid">
      <div class="hero-copy">
        <span class="eyebrow light hero-firm-name"><span class="lang-ar">شركة د. أحمد الحمادي للمحاماة والاستشارات القانونية</span><span class="lang-en">Dr. Ahmad Al Hammadi Law Firm & Legal Consultancy</span></span>
        <h1 class="display"><span class="lang-ar">معرفة قانونية.<br>رأي مستقل.<br>التزام بمصالحك.</span><span class="lang-en">Legal knowledge.<br>Independent judgment.<br>Commitment to your interests.</span></h1>
        <p class="hero-sub"><span class="lang-ar">في شركة د. أحمد الحمادي للمحاماة والاستشارات القانونية، نجمع بين فهم الأنظمة وفهم احتياجات عملائنا، لتقديم مشورة واضحة وعمل قانوني يراعي أهدافهم ومسؤولياتهم وما يترتب على قراراتهم.</span><span class="lang-en">At Dr. Ahmad Al Hammadi Law Firm & Legal Consultancy, we combine an understanding of the law with an understanding of our clients' needs to provide clear advice and legal work that considers their objectives, responsibilities and the consequences of their decisions.</span></p>
        <div class="hero-bottom"><a class="btn-ghost" href="#practice-areas"><span class="lang-ar">استعراض مجالات الممارسة</span><span class="lang-en">Explore practice areas</span></a></div>
      </div>
      <div class="hero-experience reveal"><strong dir="ltr">20+</strong><span><span class="lang-ar">عاماً من الخبرة القانونية</span><span class="lang-en">Years of legal experience</span></span></div>
    </div>
  </div>
</section>'''
h = re.sub(r'<section class="hero onepage-anchor" id="top">[\s\S]*?</section>', hero, h, count=1)

about = '''<section class="section onepage-anchor" id="about">
  <div class="container editorial-split">
    <div class="visual-panel reveal" aria-hidden="true"><img src="assets/logo.png" alt="" loading="lazy"><div class="visual-fallback"><img src="assets/logo.png" alt=""></div></div>
    <div class="copy reveal">
      <span class="eyebrow"><span class="lang-ar">عن الشركة</span><span class="lang-en">About the firm</span></span>
      <h2 class="title-lg"><span class="lang-ar">الصراحة في المشورة، والعناية في الأداء.</span><span class="lang-en">Candour in advice. Care in execution.</span></h2>
      <p class="lead"><span class="lang-ar">شركة د. أحمد الحمادي للمحاماة والاستشارات القانونية، شركة سعودية تقدم خدماتها للأفراد والشركات عبر مجالات متعددة من الممارسة القانونية.</span><span class="lang-en">Dr. Ahmad Al Hammadi Law Firm & Legal Consultancy is a Saudi firm serving individuals and businesses across multiple areas of legal practice.</span></p>
      <p><span class="lang-ar">نرى أن كفاءة العمل القانوني تبدأ بفهم العميل؛ طبيعة أعماله، وأولوياته، والظروف التي تحيط بطلبه. ونستند إلى هذا الفهم في دراسة الموضوع وتقديم الرأي وتحديد نطاق الخدمة.</span><span class="lang-en">We believe effective legal work begins with understanding the client: the nature of their business, priorities and the circumstances surrounding the matter. We rely on that understanding when assessing the issue, giving advice and defining the scope of service.</span></p>
      <p><span class="lang-ar">تقوم علاقتنا المهنية على الصراحة في المشورة والعناية في الأداء. نوضح للعميل الخيارات وآثارها، ونبين ما يدعم موقفه وما قد يحد منه، ليكون قراره قائماً على تقدير واقعي.</span><span class="lang-en">Our professional relationship is built on candid advice and careful performance. We explain the available options and their implications, including what supports the client's position and what may limit it, so decisions are based on a realistic assessment.</span></p>
      <p><span class="lang-ar">ونتعامل مع كل تكليف باعتباره مسؤولية مهنية تستلزم الدقة، وحفظ السرية، والمتابعة، ووضوح التواصل.</span><span class="lang-en">We treat every engagement as a professional responsibility requiring precision, confidentiality, follow-through and clear communication.</span></p>
    </div>
  </div>
</section>'''
h = re.sub(r'<section class="section onepage-anchor" id="about">[\s\S]*?</section>', about, h, count=1)

# Remove the older vision/mission block if present.
h = re.sub(r'\n<section class="section wash">\s*<div class="container">\s*<div class="section-head reveal"><div><span class="eyebrow"><span class="lang-ar">الرؤية والرسالة والأهداف</span>[\s\S]*?</section>\n', '\n', h, count=1)

pillars = '''<section class="section profile-pillars">
  <div class="container">
    <div class="section-head reveal"><div><span class="eyebrow"><span class="lang-ar">ركائز العمل</span><span class="lang-en">Working principles</span></span><h2 class="title-lg"><span class="lang-ar">خمسة مبادئ تحكم علاقتنا المهنية وطريقة عملنا.</span><span class="lang-en">Five principles that shape our professional relationship and our work.</span></h2></div></div>
    <div class="principles-grid">
      <article class="principle reveal"><span>01</span><h3><span class="lang-ar">فهم احتياج العميل</span><span class="lang-en">Understanding client needs</span></h3><p><span class="lang-ar">نبدأ بتحديد ما يحتاج إليه العميل وما يسعى إلى تحقيقه، مع مراعاة طبيعة أعماله وظروفه وأولوياته.</span><span class="lang-en">We begin by identifying what the client needs and seeks to achieve, taking into account the nature of their business, circumstances and priorities.</span></p></article>
      <article class="principle reveal"><span>02</span><h3><span class="lang-ar">استقلال الرأي</span><span class="lang-en">Independent judgment</span></h3><p><span class="lang-ar">نقدم تقييماً مهنياً صريحاً، ونوضح نقاط القوة والمخاطر والقيود التي تؤثر في الخيارات المتاحة.</span><span class="lang-en">We provide a candid professional assessment and explain the strengths, risks and constraints that affect the available options.</span></p></article>
      <article class="principle reveal"><span>03</span><h3><span class="lang-ar">الدقة في العمل</span><span class="lang-en">Precision in our work</span></h3><p><span class="lang-ar">ندرس المستندات والأحكام النظامية ذات الصلة، ونعنى بسلامة التحليل والصياغة واتساقهما مع موضوع التكليف.</span><span class="lang-en">We review relevant documents and legal provisions, with close attention to sound analysis, drafting and consistency with the engagement.</span></p></article>
      <article class="principle reveal"><span>04</span><h3><span class="lang-ar">وضوح العلاقة المهنية</span><span class="lang-en">Clarity in the professional relationship</span></h3><p><span class="lang-ar">نحدد نطاق الخدمة والأتعاب والمسؤوليات، ونوضح للعميل الإجراءات والمستجدات التي تستلزم مشاركته أو قراره.</span><span class="lang-en">We define the scope of service, fees and responsibilities, and clarify the procedures and developments that require the client's participation or decision.</span></p></article>
      <article class="principle reveal"><span>05</span><h3><span class="lang-ar">الالتزام بالمتابعة</span><span class="lang-en">Commitment to follow-through</span></h3><p><span class="lang-ar">نتابع المواعيد والإجراءات المرتبطة بالتكليف، ونطلع العميل على التطورات المؤثرة في سير العمل.</span><span class="lang-en">We follow deadlines and procedures related to the engagement and keep the client informed of developments that affect progress.</span></p></article>
    </div>
  </div>
</section>'''
h = re.sub(r'<section class="section">\s*<div class="container">\s*<div class="section-head reveal">[\s\S]*?<span class="lang-ar">ركائز العمل</span>[\s\S]*?</section>', pillars, h, count=1)

expertise = '''<section class="section dark profile-expertise">
  <div class="container split">
    <div class="sticky reveal"><span class="eyebrow light"><span class="lang-ar">منظومة متكاملة من الخبرات القانونية</span><span class="lang-en">An integrated legal expertise model</span></span><h2 class="title-lg"><span class="lang-ar">فرق متخصصة، وبحث وصياغة ومتابعة تحت قيادة واحدة.</span><span class="lang-en">Specialist teams, research, drafting and follow-through under one lead.</span></h2></div>
    <div class="copy reveal">
      <p class="lead"><span class="lang-ar">تضم الشركة فرقاً داخلية متخصصة في مجالات الممارسة القانونية، تساندها أقسام للبحث والصياغة والمتابعة.</span><span class="lang-en">The firm includes internal teams specialised across its areas of legal practice, supported by research, drafting and follow-up functions.</span></p>
      <p><span class="lang-ar">وللقضايا الكبرى والمسائل المعقدة، نكوّن فرقاً موسعة تجمع كفاءات الشركة وخبرات خارجية رفيعة، وفق ما يتطلبه الملف من تخصص وعمق مهني.</span><span class="lang-en">For major cases and complex matters, we form expanded teams combining the firm's capabilities with high-level external expertise, according to the specialisation and professional depth the matter requires.</span></p>
      <p><span class="lang-ar">وتتولى الشركة قيادة هذه الفرق والإشراف على أعمالها، بما يحقق تكامل الخبرات واتساق المعالجة القانونية.</span><span class="lang-en">The firm leads and supervises these teams to ensure integrated expertise and a consistent legal approach.</span></p>
    </div>
  </div>
</section>'''
if 'profile-expertise' not in h:
    h = h.replace(pillars, pillars + '\n\n' + expertise, 1)

h = re.sub(r'href="assets/styles\.css(?:\?[^\"]*)?"', 'href="assets/styles.css?v=20261004-profile"', h)
h = re.sub(r'src="assets/app\.js(?:\?[^\"]*)?"', 'src="assets/app.js?v=20261004-profile"', h)
index.write_text(h, encoding='utf-8')
