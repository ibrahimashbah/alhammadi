from pathlib import Path
import re

index = Path('index.html')
h = index.read_text(encoding='utf-8')

intro = '''<section class="section onepage-anchor service-intro" id="practice-areas">
  <div class="container split">
    <div class="sticky reveal"><span class="eyebrow"><span class="lang-ar">مجالات الممارسة</span><span class="lang-en">Practice areas</span></span><h2 class="title-lg"><span class="lang-ar">تخصصات متكاملة برؤية شاملة.</span><span class="lang-en">Integrated disciplines. A comprehensive view.</span></h2></div>
    <div class="copy reveal"><p class="lead"><span class="lang-ar">تغطي خدمات الشركة تسعة مجالات رئيسية من الممارسة القانونية، مع التعامل مع المسائل المتقاطعة ضمن معالجة قانونية متكاملة.</span><span class="lang-en">The firm's services cover nine core areas of legal practice, with cross-disciplinary matters handled through an integrated legal approach.</span></p></div>
  </div>
</section>'''
h = re.sub(r'<section class="section onepage-anchor service-intro" id="practice-areas">[\s\S]*?</section>', intro, h, count=1)

practices = [
('01','assets/source-images/small-services.svg','الشركات والمعاملات التجارية','Corporate & Commercial','نقدم الدعم القانوني للشركات في مراحل التأسيس والتوسع وإعادة الهيكلة، ونعالج مسائل الملكية والإدارة والحوكمة، بما يراعي طبيعة النشاط ومصالح الشركة والشركاء.','We support companies through formation, expansion and restructuring, and address ownership, management and governance matters with regard to the nature of the business and the interests of the company and its partners.',
 ['تأسيس الشركات وإعادة هيكلتها.','حوكمة الشركات وتنظيم العلاقة بين الشركاء.','حوكمة الشركات العائلية وإعداد المواثيق العائلية.','الاندماج والاستحواذ.','الإفلاس وإعادة التنظيم.','برامج أسهم العاملين.','المعاملات التجارية ومسائل الملكية الفكرية المرتبطة بالأعمال.'],
 ['Company formation and restructuring.','Corporate governance and regulation of partner relationships.','Family business governance and family charters.','Mergers and acquisitions.','Bankruptcy and reorganisation.','Employee share programmes.','Commercial transactions and business-related intellectual property matters.']),
('02','assets/source-images/contracts.svg','العقود والاتفاقيات','Contracts & Agreements','نصوغ العقود ونراجعها على أساس فهم المعاملة وأهداف أطرافها، مع ضبط الحقوق والالتزامات، وتوزيع المسؤوليات، ومعالجة المخاطر التي قد تؤثر في التنفيذ.','We draft and review contracts based on an understanding of the transaction and the parties objectives, defining rights and obligations, allocating responsibilities and addressing risks that may affect performance.',
 ['صياغة العقود ومراجعتها.','التفاوض بشأن الشروط التعاقدية.','إعداد الاتفاقيات التجارية.','دراسة الالتزامات التعاقدية وإدارتها.','العقود والمعاملات التمويلية والمصرفية.'],
 ['Contract drafting and review.','Negotiation of contractual terms.','Commercial agreements.','Assessment and management of contractual obligations.','Financing and banking contracts and transactions.']),
('03','assets/source-images/commercial.svg','التقاضي وتسوية المنازعات','Litigation & Dispute Resolution','نتولى تمثيل العملاء في المنازعات، بدءاً من تقييم الموقف القانوني ودراسة الأدلة، وصولاً إلى إعداد المطالبات والدفوع ومتابعة الإجراءات. ونبحث مسارات التسوية وفق طبيعة النزاع ومصلحة العميل.','We represent clients in disputes from assessing the legal position and evidence through preparing claims and defences and following proceedings. We also consider settlement paths according to the nature of the dispute and the client interests.',
 ['المنازعات التجارية والمدنية والإدارية.','التمثيل أمام الجهات القضائية وشبه القضائية.','إعداد الدعاوى والمذكرات والاعتراضات.','التسويات والمصالحات.','المنازعات التمويلية والمصرفية والتأمينية.'],
 ['Commercial, civil and administrative disputes.','Representation before judicial and quasi-judicial bodies.','Claims, submissions and objections.','Settlements and amicable resolutions.','Financing, banking and insurance disputes.']),
('04','assets/source-images/insurance-1.svg','التحكيم','Arbitration','نقدم المشورة والتمثيل في التحكيم التجاري، مع العناية باتفاق التحكيم والقواعد المنظمة للإجراءات، وبناء الموقف القانوني وإعداد الأدلة والمرافعات.','We advise and represent clients in commercial arbitration, with close attention to the arbitration agreement, procedural rules, legal position, evidence and pleadings.',
 ['دراسة اتفاقيات التحكيم وصياغتها.','تمثيل الأطراف في المنازعات التحكيمية.','إعداد المذكرات والمرافعات.','متابعة إجراءات تنفيذ أحكام التحكيم.'],
 ['Review and drafting of arbitration agreements.','Representation in arbitration disputes.','Submissions and pleadings.','Following enforcement of arbitral awards.']),
('05','assets/source-images/court.svg','العقار والأوقاف','Real Estate & Awqaf','نقدم المشورة في المعاملات العقارية وشؤون الأوقاف، وندرس الحقوق والالتزامات المرتبطة بالملكية والتطوير والاستثمار والإدارة، ونتولى التمثيل في المنازعات الناشئة عنها.','We advise on real estate transactions and awqaf, assess rights and obligations relating to ownership, development, investment and management, and represent clients in related disputes.',
 ['العقود والتصرفات العقارية.','التطوير والاستثمار العقاري.','المنازعات العقارية.','المسائل القانونية المتعلقة بالأوقاف وإدارتها.'],
 ['Real estate contracts and dispositions.','Real estate development and investment.','Real estate disputes.','Legal matters relating to awqaf and their administration.']),
('06','assets/source-images/group-profile.svg','العمل والتوظيف','Employment & Labour','نساند العملاء في تنظيم علاقات العمل ومعالجة المسائل الناشئة عنها، من إعداد العقود والسياسات الداخلية إلى دراسة الحقوق والالتزامات والتمثيل في المنازعات العمالية.','We support clients in structuring employment relationships and addressing related matters, from contracts and internal policies to rights and obligations and representation in labour disputes.',
 ['صياغة عقود العمل ومراجعتها.','إعداد السياسات واللوائح الداخلية ومراجعتها.','الاستشارات المتعلقة بعلاقات العمل وانتهائها.','التمثيل في المنازعات العمالية.'],
 ['Employment contract drafting and review.','Internal policies and regulations.','Advice on employment relationships and termination.','Representation in labour disputes.']),
('07','assets/source-images/customs.svg','الزكاة والضرائب والجمارك','Zakat, Tax & Customs','نقدم المشورة والتمثيل في المنازعات الزكوية والضريبية والجمركية، من خلال دراسة القرارات والمطالبات وأسانيدها، وإعداد الاعتراضات ومتابعة الإجراءات أمام الجهات المختصة.','We advise and represent clients in zakat, tax and customs disputes by reviewing decisions, claims and their grounds, preparing objections and following proceedings before the competent authorities.',
 ['المنازعات الزكوية والضريبية.','إعداد الاعتراضات والتظلمات.','المنازعات الجمركية.','التمثيل أمام اللجان والجهات المختصة.'],
 ['Zakat and tax disputes.','Objections and appeals.','Customs disputes.','Representation before committees and competent authorities.']),
('08','assets/source-images/profile.svg','الأحوال الشخصية والتركات','Personal Status & Estates','نعالج مسائل الأحوال الشخصية والتركات بعناية تراعي الحقوق وخصوصية العلاقات، ونقدم المشورة والتمثيل في تنظيم التركات وتسويتها وما ينشأ عنها من منازعات.','We handle personal status and estate matters with care for rights and the privacy of relationships, advising and representing clients in estate organisation, settlement and related disputes.',
 ['التركات وتصفيتها وقسمتها.','الوصايا.','التسويات بين الورثة.','المنازعات المتعلقة بالأحوال الشخصية.'],
 ['Estate administration, liquidation and division.','Wills.','Settlements among heirs.','Personal status disputes.']),
('09','assets/source-images/case-2.svg','القضايا الجزائية','Criminal Matters','نقدم المشورة والتمثيل والدفاع في القضايا الجزائية، استناداً إلى دراسة الوقائع والأدلة والتكييف النظامي، مع متابعة الإجراءات وإعداد المذكرات والدفوع بحسب مرحلة القضية.','We advise, represent and defend clients in criminal matters based on a review of facts, evidence and legal characterisation, while following procedures and preparing submissions and defences according to the stage of the case.',
 ['المشورة القانونية في المسائل الجزائية.','التمثيل والدفاع أمام الجهات المختصة.','إعداد المذكرات والدفوع.','القضايا الجزائية المرتبطة بالأعمال.'],
 ['Legal advice in criminal matters.','Representation and defence before competent authorities.','Submissions and defences.','Business-related criminal matters.'])
]

articles=[]
for no,icon,ar,en,summary_ar,summary_en,bullets_ar,bullets_en in practices:
    la=''.join(f'<li>{x}</li>' for x in bullets_ar)
    le=''.join(f'<li>{x}</li>' for x in bullets_en)
    articles.append(f'''<article class="practice-detail reveal" id="p-{no}"><div class="practice-detail-head"><span class="no">{no}</span><img src="{icon}" alt="" loading="lazy"></div><h2><span class="lang-ar">{ar}</span><span class="lang-en">{en}</span></h2><p class="practice-summary"><span class="lang-ar">{summary_ar}</span><span class="lang-en">{summary_en}</span></p><h4 class="practice-scope"><span class="lang-ar">نطاق الممارسة</span><span class="lang-en">Scope of practice</span></h4><div><ul class="lang-ar">{la}</ul><ul class="lang-en">{le}</ul></div></article>''')

details='<section class="section wash profile-practice-details"><div class="container"><div class="practice-detail-list">'+''.join(articles)+'</div></div></section>'
h = re.sub(r'<section class="section wash">\s*<div class="container">\s*<div class="practice-detail-list">[\s\S]*?</section>', details, h, count=1)
index.write_text(h, encoding='utf-8')

css=Path('assets/styles.css')
c=css.read_text(encoding='utf-8')
if '/* Profile practice copy */' not in c:
    c += '''\n/* Profile practice copy */\n.profile-practice-details .practice-detail{padding-block:clamp(44px,5vw,70px)}\n.practice-summary{max-width:920px;margin:14px 0 20px;color:var(--muted);font-size:16px;line-height:1.9}\n.practice-scope{margin:18px 0 12px;font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--copper)}\nhtml[dir="rtl"] .practice-scope{letter-spacing:0}\n'''
css.write_text(c,encoding='utf-8')
