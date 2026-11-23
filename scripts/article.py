"""Bilingual edition of Pouya Hosseini's scale-visualization article."""
from html import escape
from math import cos, sin, radians

TITLE = ('Exploring Persian Music Scales through Interactive Visualizations', 'کاوش در گام‌های موسیقی ایرانی با نمودارهای تعاملی')
LEAD = ('How can a circle show the difference between a change of starting pitch and a change of mode? A study of seven pitch collections, their intervals, and the limits of a visual model.', 'تفاوت انتقال به نتی دیگر با تغییر دستگاه را چگونه می‌توان روی یک دایره دید؟ در این مقاله مجموعهٔ نت‌های هفت نمونه، فاصله‌های آن‌ها و حدود کاربرد این مدل تصویری بررسی می‌شود.')
META = {lang: {'title': TITLE[i], 'lead': LEAD[i]} for i, lang in enumerate(('en','fa'))}
APP = 'https://github.com/PersianMusicScales/Persian-Music-Scales-App'
OLD = 'https://sites.google.com/view/persianmusicscales/article'

# Original Table 1 scope, using cumulative angular positions from the application.
MODELS = [
    ('Šur','شور',(0,45,90,150,210,240,300)),
    ('Segāh','سه‌گاه',(0,60,105,150,210,255,300)),
    ('Navā','نوا',(0,60,90,150,210,255,300)),
    ('Homāyun','همایون',(0,45,120,150,210,240,300)),
    ('Čahārgāh','چهارگاه',(0,45,120,150,210,255,330)),
    ('Bayāt-e Esfahān','بیات اصفهان',(0,60,90,150,210,255,330)),
    ('Māhur','ماهور',(0,60,120,150,210,270,330)),
]
SECTIONS = [
(('Introduction', 'مقدمه'), [
('A musician can transpose a familiar phrase and still recognize its shape. A circle makes one part of that recognition visible: the distances between its pitches survive the move. This study sets a Persian pitch collection against a diatonic reference so that a reader can rotate the reference, read new note names, and hear the result. It asks which features survive transposition and which require listening to a melody.',
'نوازنده می‌تواند جمله‌ای آشنا را از نت دیگری آغاز کند و همچنان طرح آن را بشناسد. نمودار دایره‌ای یکی از علت‌های این بازشناسی را نشان می‌دهد: با انتقال جمله، فاصلهٔ میان نت‌ها حفظ می‌شود. در این بررسی، یک مجموعهٔ صوتی ایرانی در کنار مرجعی دیاتونیک قرار می‌گیرد تا خواننده با چرخاندن مرجع، نام نت‌های تازه را بخواند و نتیجه را بشنود. کدام ویژگی‌ها با انتقال حفظ می‌شوند و برای شناخت کدام ویژگی‌ها باید به ملودی گوش داد؟'),
('The historical setting matters. Al-Fārābī and Ṣafī al-Dīn al-Urmawī examined intervals and their organization in earlier theoretical traditions. The later dastgāh repertoire has its own history of oral transmission. A teacher conveys a gusheh through phrasing, emphasis, ornament and return. The wheel isolates pitch distance from that lesson so that one aspect can be studied closely.',
'فارابی و صفی‌الدین ارموی در دو دورهٔ تاریخی متفاوت دربارهٔ فاصله‌ها و سازمان آن‌ها نوشتند. ردیف دستگاهی را باید در بستر متأخرتر و سنت شفاهی خودش شناخت. استاد هنگام آموزش گوشه، جمله‌بندی، تأکید، تزیین و شیوهٔ فرود را نیز منتقل می‌کند. دایره به هنرجو امکان می‌دهد از میان این عناصر، فاصلهٔ صوتی را جداگانه بررسی کند.')]),
(('The diatonic reference circle','دایرهٔ مرجع دیاتونیک'),[
('Place C at twelve o’clock and follow the scale clockwise through D, E, F, G, A and B to the next C. For the equal-tempered major scale the steps in cents are 200, 200, 100, 200, 200, 200 and 100. An octave occupies the full turn. A whole tone therefore occupies 60° and a semitone 30°. The narrow sectors at E–F and B–C are the feature to look for in Figure 1.',
'دو را بالای دایره بگذارید و در جهت عقربه‌های ساعت از ر، می، فا، سل، لا و سی به دوی بعدی برسید. در گام ماژور با کوک معتدل مساوی، فاصله‌های پیاپی به سنت عبارت‌اند از ۲۰۰، ۲۰۰، ۱۰۰، ۲۰۰، ۲۰۰، ۲۰۰ و ۱۰۰. یک دور کامل برابر یک اکتاو است؛ بنابراین یک پرده ۶۰ درجه و نیم‌پرده ۳۰ درجه از دایره را می‌گیرد. در شکل ۱ به دو قطاع باریکِ می تا فا و سی تا دو توجه کنید.')]),
(('Vaziri, koron and sori','وزیری، کُرُن و سُری'),[
('Ali-Naqi Vaziri’s twentieth-century theory and teaching brought a division of the octave into twenty-four equal parts into Iranian music pedagogy. On this grid each step is 50 cents. Koron lowers a written pitch and sori raises it. In the application’s model each alteration amounts to one grid step. This makes the notation practical for calculation, comparison and transposition.',
'علینقی وزیری در نظریه و آموزش موسیقی در سدهٔ بیستم، تقسیم اکتاو به بیست‌وچهار قسمت مساوی را مطرح کرد. هر قسمت در این الگو ۵۰ سنت است. علامت کُرُن نت نوشته‌شده را پایین می‌آورد و سُری آن را بالا می‌برد. در مدل برنامه، مقدار هر تغییر یک خانهٔ شبکه است؛ قراردادی که محاسبه، مقایسه و انتقال را آسان می‌کند.'),
('Urmawī’s string divisions and Vaziri’s equal grid address different theoretical questions. A koron heard in a particular performance also depends on the musician and melodic context. A plotted point is a reproducible target for the software. A claim about a performer’s intonation requires a recording, an identified passage and a measurement.',
'تقسیمات طول سیم نزد ارموی و شبکهٔ مساوی وزیری به پرسش‌های نظری متفاوتی پاسخ می‌دهند. زیراییِ یک نت کرن‌دار در اجرا نیز به نوازنده و بافت ملودی بستگی دارد. جای هر نقطه در نرم‌افزار مشخص و تکرارپذیر است. برای داوری دربارهٔ کوک یک اجرا باید ضبط، عبارت مورد بررسی و روش اندازه‌گیری را مشخص کرد.')]),
(('From cents to angles','از سنت تا زاویه'),[
('For frequencies f and f₀, the distance in cents is c = 1200 log₂(f/f₀). The angular position is θ = 360° × c/1200 = 0.3° × c. Doubling the frequency gives 1200 cents and one complete turn. A pitch 850 cents above the starting note is marked at 255°. The width of the preceding sector depends on where the preceding note lies.',
'اگر بسامد نت آغاز f₀ و بسامد نت مورد نظر f باشد، فاصله بر حسب سنت از رابطهٔ c = 1200 log₂(f/f₀) به دست می‌آید. برای جایابی همان نت روی دایره داریم θ = 360° × c/1200. با دو برابر شدن بسامد، یک اکتاو یا یک دور کامل طی می‌شود. نتی که ۸۵۰ سنت بالاتر از مبدأ است در زاویهٔ ۲۵۵ درجه قرار می‌گیرد. پهنای قطاع پیش از آن به جای نت قبلی بستگی دارد.'),
('Read Table 1 across a row. The second column gives positions from the origin. The third gives the same positions in degrees. The last gives neighbor-to-neighbor steps including the return to the octave. For example, the Segāh model goes from 200 to 350 cents in a 150-cent step. The 250-cent step discussed in the early edition can be seen in Homāyun, from 150 to 400 cents. It is wider than a 200-cent whole tone.',
'جدول ۱ را سطربه‌سطر بخوانید. ستون دوم جای نت‌ها نسبت به مبدأ و ستون سوم همان جایگاه‌ها را به درجه نشان می‌دهد. ستون آخر فاصلهٔ نت‌های مجاور را تا اکتاو بعدی می‌دهد. برای نمونه در مدل سه‌گاه، حرکت از جایگاه ۲۰۰ به ۳۵۰ سنت، فاصله‌ای ۱۵۰ سنتی است. نمونهٔ فاصلهٔ ۲۵۰ سنتی که در نگارش نخست مطرح شده بود، در همایون میان جایگاه‌های ۱۵۰ و ۴۰۰ دیده می‌شود. این فاصله از یک پردهٔ ۲۰۰ سنتی بزرگ‌تر است.')]),
(('Representing seven modal collections','نمایش هفت مجموعهٔ صوتی'),[
('Figure 2 compares the seven models in the original study. Each boundary marks an available pitch. Each sector spans the interval to the next pitch. The early diagrams used black, pink, gray and green to distinguish 100, 150, 200 and 250 cents. The diagrams below use the corresponding app colors and repeat the sizes in the table so that the comparison is readable without color.',
'شکل ۲ هفت مدل به‌کاررفته در پژوهش نخست را کنار هم نشان می‌دهد. هر مرز جای یک نت و هر قطاع فاصله تا نت بعدی است. نمودارهای قدیمی برای فاصله‌های ۱۰۰، ۱۵۰، ۲۰۰ و ۲۵۰ سنتی به‌ترتیب از سیاه، صورتی، خاکستری و سبز استفاده می‌کردند. نمودارهای زیر رنگ‌بندی برنامه را به کار می‌برند. اندازه‌ها در جدول نیز آمده‌اند تا مقایسه بدون تشخیص رنگ ممکن باشد.'),
('The shared opening of Šur and Homāyun is instructive. Both models place the second note at 150 cents. In Šur the next note is another 150 cents away. In Homāyun it is 250 cents away. Conversely, Navā and Bayāt-e Esfahān agree through the 850-cent position in these settings and separate at the seventh note. A visual comparison is most useful when it identifies the particular transition to listen for.',
'مقایسهٔ آغاز شور و همایون آموزنده است. در هر دو مدل، نت دوم در ۱۵۰ سنت قرار دارد. در شور برای رسیدن به نت بعدی ۱۵۰ سنت دیگر بالا می‌رویم، اما در همایون این حرکت ۲۵۰ سنت است. در مقابل، نوا و بیات اصفهان در این تنظیم تا جایگاه ۸۵۰ سنت بر هم منطبق‌اند و در نت هفتم از هم جدا می‌شوند. ارزش مقایسهٔ دیداری در این است که دقیقاً بدانیم به کدام حرکت گوش دهیم.')]),
(('Mapping note names and transposition','نام نت‌ها، سرکلید و انتقال'),[
('In Šur on C the seven boundary angles are 0°, 45°, 90°, 150°, 210°, 240° and 300°. The second pitch is D-koron in the grid. Starting the collection on D shifts every pitch up 200 cents, a rotation of 60°. The new second pitch is E-koron. The first sector still spans 45°. Figure 3 shows both the starting pitch and its relation to the next note; the live application lets the reader check the change by ear.',
'در شورِ دو، مرزها در صفر، ۴۵، ۹۰، ۱۵۰، ۲۱۰، ۲۴۰ و ۳۰۰ درجه‌اند. روی شبکه، نت دوم رِ کرن است. اگر مجموعه را از ر آغاز کنیم، همهٔ نت‌ها ۲۰۰ سنت بالا می‌روند؛ یعنی دایره ۶۰ درجه می‌چرخد. نت دوم اکنون می‌کرن است و قطاع نخست همچنان ۴۵ درجه پهنا دارد. شکل ۳ جای نت آغاز و نسبت آن با نت دوم را نشان می‌دهد. نتیجه را می‌توان در برنامه شنید.'),
('For comparison, moving the major reference from C to D gives D, E, F♯, G, A, B and C♯. The F♯ and C♯ illustrate the change of key signature. For Persian models, read the displayed accidentals as a spelling of the selected collection. A written key signature alone does not specify how a performer approaches a shāhed or shapes a forud.',
'برای مقایسه، با انتقال دو ماژور به ر ماژور نت‌ها عبارت‌اند از ر، می، فا دیز، سل، لا، سی و دو دیز. فا دیز و دو دیز تغییر سرکلید را نشان می‌دهند. در مدل‌های ایرانی، علائم عرضی نام نت‌های مجموعهٔ انتخاب‌شده را روشن می‌کنند. از سرکلید به‌تنهایی نمی‌توان شیوهٔ نزدیک شدن نوازنده به شاهد یا چگونگی فرود او را دریافت.')]),
(('Results and discussion','نتایج و بحث'),[
('Theoretical findings. Māhur and the major reference share all seven plotted positions. Segāh diverges from them already at its third point, 350 cents, halfway between 300 and 400 on this grid. The Esfahān point at 850 cents similarly lies between two adjacent semitone positions. Calling this point an augmented sixth would imply a spelling and harmonic function that the angle cannot establish.',
'یافته‌های نظری. در این مدل، هفت جایگاه ماهور و مرجع ماژور بر هم منطبق‌اند. سه‌گاه در نت سوم، در ۳۵۰ سنت، از آن‌ها جدا می‌شود؛ یعنی در این شبکه درست میان ۳۰۰ و ۴۰۰ سنت. جایگاه ۸۵۰ سنتی اصفهان نیز میان دو خانهٔ مجاور نیم‌پرده‌ای قرار می‌گیرد. نامیدن آن به «ششم افزوده» به املای نت و کارکرد هارمونیک معینی نیاز دارد که از زاویهٔ نمودار به دست نمی‌آید.'),
('Comparative findings. Against natural minor, the Homāyun model shares 0, 500, 700, 800 and 1000 cents; the differing positions are 150 versus 200 and 400 versus 300. Thus 800 cents is a point of agreement. To hear the distinction, alternate short phrases on the first three degrees while keeping the starting pitch fixed. Then repeat from another starting pitch: the contrast remains.',
'یافته‌های تطبیقی. مدل همایون در جایگاه‌های صفر، ۵۰۰، ۷۰۰، ۸۰۰ و ۱۰۰۰ سنت با مینور طبیعی مشترک است. تفاوت‌ها در ۱۵۰ در برابر ۲۰۰ و ۴۰۰ در برابر ۳۰۰ سنت‌اند. پس ۸۰۰ سنت یکی از نقاط اشتراک است. برای شنیدن تفاوت، از مبدأیی یکسان با سه درجهٔ نخست هر مدل جمله‌ای کوتاه بنوازید. سپس هر دو جمله را انتقال دهید و دوباره مقایسه کنید.'),
('Tonal relationships. The model gives immediate feedback when the reference moves. It can show the preservation of an interval pattern and help two musicians describe the same pitch distance. Tonal hierarchy needs other evidence: phrase endings, repeated emphasis and characteristic returns in an identified gusheh. The same breadth of sector can lead to a passing note in one phrase and a sustained focal note in another. In particular, the resemblance of the Māhur pitch set to major leaves their melodic practices open for study.',
'روابط مدال. با چرخش مرجع، برچسب‌های برنامه بلافاصله تغییر می‌کنند. از این راه دو نوازنده می‌توانند دربارهٔ یک فاصله با مقیاسی مشترک گفت‌وگو کنند. برای بررسی سلسله‌مراتب مدال باید پایان جمله‌ها، محل تأکیدهای مکرر و فرودهای شاخص یک گوشهٔ مشخص را شنید. قطاعی با پهنای یکسان ممکن است در یک جمله به نت گذر و در جمله‌ای دیگر به نتی کشیده و محوری برسد. شباهت مجموعهٔ نت‌های ماهور به ماژور نیز نقطهٔ آغاز بررسی تفاوت‌های ملودیک آن‌هاست.')]),
(('Teaching and research applications','کاربرد آموزشی و پژوهشی'),[
('In a lesson, play the first three notes of Šur twice. Ask a learner to sing the second note, mark its position and predict where it will move after transposition. Then let the learner operate the wheel and check by ear. As a second task, compare a radif phrase with the static model and mark each pause. The first task tests an interval prediction. The second asks how a musician gives those pitches different weight.',
'در کلاس، سه نت نخست شور را دو بار بنوازید. از هنرجو بخواهید نت دوم را بخواند، جای آن را مشخص کند و پیش‌بینی کند که پس از انتقال کجا قرار می‌گیرد. سپس خودش دایره را بچرخاند و پاسخ را با گوش بیازماید. در تمرینی دیگر، عبارتی از ردیف را با مدل مقایسه کند و محل مکث‌ها را علامت بزند. تمرین اول پیش‌بینی فاصله و تمرین دوم تشخیص اهمیت متفاوت نت‌ها در اجرا را می‌سنجد.'),
('For a reproducible comparison, record the mode, starting pitch, model version, recording, performer and time span. List the model’s cent positions alongside observations from the excerpt. Explain any difference before treating it as an error. This is a method for testing a musical question; the diagrams themselves supply no measurement of learning gains or evidence for a universal tuning.',
'برای مقایسه‌ای تکرارپذیر، نام دستگاه یا آواز، نت آغاز، نسخهٔ مدل، مشخصات ضبط، نام اجراکننده و بازهٔ زمانی را ثبت کنید. جای نت‌ها در مدل را کنار داده‌های شنیده‌شده یا اندازه‌گیری‌شده بنویسید. پیش از آنکه اختلافی را خطا بنامید، علت احتمالی آن را بررسی کنید. نمودار به طرح پرسش کمک می‌کند؛ میزان پیشرفت هنرجو یا کوک رایج میان نوازندگان را باید جداگانه سنجید.')]),
(('Future directions and conclusion','چشم‌انداز و نتیجه‌گیری'),[
('The original study proposed adding sound. The application now supports playback and recorded-audio analysis, so a student can move between diagram and listening. A possible extension is comparison with Arabic maqām, Ottoman/Turkish makam and Indian rāga. Each would need sources specific to its repertoire, tuning and melodic behavior. A shared unit of distance is only the starting point for such a comparison.',
'در نگارش نخست، افزودن صدا پیشنهاد شده بود. برنامه اکنون امکان پخش و تحلیل صدای ضبط‌شده دارد و هنرجو می‌تواند میان نمودار و شنیدن رفت‌وآمد کند. مقایسه با مقام عربی، مقام در سنت عثمانی و ترکیه، و راگای هندی از مسیرهای توسعه است. هر مقایسه به منابع ویژهٔ همان رپرتوار، کوک و سیر ملودی نیاز دارد. واحد مشترک اندازه‌گیری فقط نقطهٔ آغاز است.'),
('The central result is practical. A circle preserves the size and ordering of intervals while allowing their note names to change. It makes a transposition inspectable, exposes numerical mistakes and suggests precise listening comparisons. Read alongside notation and a named performance, it can support teaching, composition and inquiry across musical traditions.',
'حاصل اصلی این بررسی عملی است: دایره اندازه و ترتیب فاصله‌ها را حفظ می‌کند و هم‌زمان تغییر نام نت‌ها را نشان می‌دهد. از این راه می‌توان انتقال را بررسی کرد، ناسازگاری عددی را دید و پرسش شنیداری دقیقی طرح کرد. همراهی نمودار با نت‌نویسی و نمونهٔ اجرایی مشخص، آن را برای آموزش، آهنگسازی و پژوهش تطبیقی سودمند می‌کند.')]),
(('Supplementary information','اطلاعات تکمیلی'),[
('Software, dataset and implementation. The repository contains the web interface, JavaScript and documentation. The scale definitions pair ordered angle lists with sector colors. The current explorer draws sectors using CSS conic gradients and rotates the reference using JavaScript. Earlier descriptions referred to D3 and SVG. The figures reproduced from data on this page use SVG, so they stay sharp when enlarged.',
'نرم‌افزار، داده‌ها و پیاده‌سازی. مخزن پروژه شامل رابط وب، کد جاوااسکریپت و راهنماست. در تعریف هر مجموعه، فهرست مرتب زاویه‌ها و رنگ قطاع‌ها آمده است. در کاوشگر کنونی، قطاع‌ها با گرادیان مخروطی CSS ترسیم می‌شوند و مرجع با جاوااسکریپت می‌چرخد. در توضیح اولیه از D3 و SVG یاد شده بود. نمودارهای بازترسیم‌شدهٔ این صفحه از نوع SVG هستند و هنگام بزرگ‌نمایی وضوح خود را حفظ می‌کنند.'),
('Usage and reproduction. Open the application, choose a model and starting pitch, and play it before rotating the wheel. To reproduce Table 1, take the angles in the scale definitions, multiply each by 1200/360 and subtract consecutive values, closing the octave at 1200. For a local installation use the setup instructions in the repository. For extensions, document the provenance and tuning of any additional collection and retain a version identifier for published results.',
'روش استفاده و بازتولید. برنامه را باز کنید، مجموعه و نت آغاز را برگزینید و پیش از چرخاندن دایره به آن گوش دهید. برای بازسازی جدول ۱، هر زاویه را در ۱۲۰۰/۳۶۰ ضرب کنید، تفاضل جایگاه‌های پیاپی را بگیرید و آخرین فاصله را تا ۱۲۰۰ سنت حساب کنید. برای اجرای محلی از دستور راه‌اندازی مخزن استفاده کنید. هنگام پیشنهاد مجموعه‌ای تازه، منبع و کوک آن را بنویسید و در انتشار نتایج، شناسهٔ نسخه را ثبت کنید.'),
('Authorship, citation and permissions. Pouya Hosseini is the author of the original 2024 article. Cite the article for the visualization method and the software separately for the implementation and dataset. The current software license is proprietary. Third-party components have their own notices. Use the repository’s citation file and license below when citing the software or seeking permission for reuse.',
'پدیدآورنده، ارجاع و مجوز. نویسندهٔ مقالهٔ اصلی سال ۲۰۲۴ پویا حسینی است. برای روش نمایش به مقاله و برای پیاده‌سازی و داده‌ها جداگانه به نرم‌افزار ارجاع دهید. نرم‌افزار کنونی مجوز اختصاصی دارد و شرایط اجزای شخص ثالث جداگانه درج شده است. برای شیوهٔ ارجاع و شرایط استفادهٔ مجدد به پرونده‌های استناد و مجوز در پیوندهای زیر مراجعه کنید.')])]

def render(lang, up):
    i = int(lang == 'fa')
    def t(en, fa):
        return (en, fa)[i]
    def anchor(url, label):
        return f'<a href="{escape(url, quote=True)}">{escape(label)}</a>'
    def wheel(angles, labels=(), offset=0):
        svg = ['<svg aria-hidden="true" viewBox="0 0 120 120" style="width:100%;max-width:13rem">']
        colors = {30:'#111',45:'#f7e7c6',60:'#48625f',75:'#1a3b66'}
        def xy(deg, r):
            a = radians(deg + offset)
            return f'{60+r*sin(a):.2f},{60-r*cos(a):.2f}'
        for j,(a,b) in enumerate(zip(angles, (*angles[1:],360))):
            svg.append(f'<path d="M60,60 L{xy(a,45)} A45,45 0 0 1 {xy(b,45)} Z" fill="{colors[b-a]}" stroke="white" stroke-width=".8"/>')
            if labels:
                x,y=xy(a,54).split(',')
                svg.append(f'<text x="{x}" y="{y}" text-anchor="middle" dominant-baseline="central" fill="currentColor" font-size="8">{labels[j]}</text>')
        return ''.join(svg)+'</svg>'
    def caption(title, desc):
        return f'<figcaption><strong>{title}</strong> {desc}</figcaption>'
    major = MODELS[-1][2]
    fig1 = '<figure>'+wheel(major, 'CDEFGAB')+caption(t('Figure 1.','شکل ۱.'),t('C major. The two half steps occupy half the angle of a whole step.','دو ماژور. زاویهٔ نیم‌پرده نصف زاویهٔ یک پرده است.'))+'</figure>'
    rows = []
    plots = []
    def series(values):
        return '<bdi dir="ltr">'+', '.join(map(str,values))+'</bdi>'
    for en,fa,angles in MODELS:
        cents = tuple(a*10//3 for a in angles)
        steps = tuple(b-a for a,b in zip(cents,(*cents[1:],1200)))
        name = t(en,fa)
        rows.append(f'<tr><th scope="row">{name}</th>'+''.join(f'<td>{series(nums)}</td>' for nums in (cents,angles,steps))+'</tr>')
        plots.append(f'<div style="text-align:center">{wheel(angles)}<div>{name}</div></div>')
    heads=[t('Model','مدل'),t('Pitch positions (cents)','جای نت‌ها (سنت)'),t('Boundaries (degrees)','مرزها (درجه)'),t('Steps to the next pitch (cents)','فاصله تا نت بعد (سنت)')]
    table='<div tabindex="0" role="region" aria-label="'+t('Seven-model comparison table','جدول مقایسهٔ هفت مدل')+'" style="overflow-x:auto"><table style="width:100%;border-spacing:.7em;text-align:start"><caption><strong>'+t('Table 1. Seven illustrated pitch collections','جدول ۱. هفت مجموعهٔ صوتی در مدل برنامه')+'</strong></caption><thead><tr>'+''.join(f'<th scope="col">{h}</th>' for h in heads)+'</tr></thead><tbody>'+''.join(rows)+'</tbody></table></div>'
    fig2='<figure><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,8rem),1fr));gap:.8rem">'+''.join(plots)+'</div>'+caption(t('Figure 2.','شکل ۲.'),t('Seven collections redrawn from the app data. Black = 100, cream = 150, teal = 200 and blue = 250 cents. Start at twelve o’clock and read clockwise.','هفت مجموعه بر پایهٔ داده‌های برنامه. سیاه: ۱۰۰، کرم: ۱۵۰، سبزآبی: ۲۰۰ و آبی: ۲۵۰ سنت. از بالای دایره در جهت عقربه‌های ساعت بخوانید.'))+'</figure>'
    fig3=f'<figure><a href="{up}assets/shur.webp"><img src="{up}assets/shur.webp" alt="'+t('Scale explorer showing Šur on C with the pitch wheel and playback controls.','نمای کاوشگر در شورِ دو با دایرهٔ نت‌ها و دکمهٔ پخش.')+'" style="display:block;width:min(100%,19rem);height:auto;margin:auto" loading="lazy"></a>'+caption(t('Figure 3.','شکل ۳.'),t('Šur on C in the app. Read C → D-koron here; after transposition to D the same 150 cents gives D → E-koron. Select the screenshot to enlarge it.','شورِ دو در برنامه. فاصلهٔ دو تا رِ کرن پس از انتقال به ر، به ر تا می‌کرن تبدیل می‌شود؛ در هر دو حالت ۱۵۰ سنت. برای بزرگ‌نمایی تصویر را انتخاب کنید.'))+'</figure>'
    byline=t('Pouya Hosseini · Revised edition of the 2024 article','پویا حسینی · ویرایش تازهٔ مقالهٔ ۲۰۲۴')
    parts=[f'<p><strong>{byline}</strong></p>', '<nav class="reading-index" aria-label="'+t('Article contents','فهرست مقاله')+'"><strong>'+t('Contents','فهرست مقاله')+'</strong><div>']
    for j,(heading,_) in enumerate(SECTIONS,1):
        parts.append(anchor(f'#part-{j}', heading[i]))
    parts.append('</div></nav><div class="prose">')
    figures = {2:fig1,4:table,5:fig2,6:fig3}
    for j,(heading,paragraphs) in enumerate(SECTIONS,1):
        parts.append(f'<section id="part-{j}"><h2>{heading[i]}</h2>')
        for paragraph in paragraphs:
            parts.append(f'<p>{escape(paragraph[i])}</p>')
        parts.append(figures.get(j,'')+'</section>')
    links=[
        (OLD,t('Original article and historical figures','مقالهٔ اصلی و شکل‌های نسخهٔ نخست')),
        ('https://www.academia.edu/126192335/Exploring_Persian_Music_Scales_through_Interactive_Visualizations',t('Author’s paper on Academia.edu','نسخهٔ نویسنده در آکادمیا')),
        ('https://persianmusicscales.github.io/Persian-Music-Scales-App/index.html?lang='+lang,t('Open the interactive scale explorer','ورود به کاوشگر تعاملی')),
        (APP,t('Application source and setup instructions','کد برنامه و راهنمای راه‌اندازی')),
        (APP+'/blob/main/src/index.js',t('Pitch positions and wheel implementation','جایگاه نت‌ها و پیاده‌سازی دایره')),
        (APP+'/wiki/'+lang.upper()+'-Scientific-Methodology',t('Methodology and documentation','روش‌شناسی و مستندات')),
        (APP+'/blob/main/CITATION.cff',t('Software citation','شیوهٔ استناد به نرم‌افزار')),
        (APP+'/blob/main/LICENSE',t('Current software license','مجوز کنونی نرم‌افزار')),
        ('https://www.iranicaonline.org/articles/dastgah/',t('Encyclopaedia Iranica on dastgāh','مدخل دستگاه در دانشنامهٔ ایرانیکا')),
        ('https://drpouyahosseini.github.io/',t('Author website','وب‌سایت نویسنده')),
        ('https://de.linkedin.com/in/drpouyahosseini','LinkedIn'),
        ('mailto:hoseini.ph@gmail.com',t('Contact the author about permissions','تماس با نویسنده برای کسب اجازه'))]
    parts.append('</div><aside><h2>'+t('Sources, software and correspondence','منابع، نرم‌افزار و مکاتبه')+'</h2><ul>'+''.join('<li>'+anchor(url,label)+'</li>' for url,label in links)+'</ul></aside>')
    return ''.join(parts)
