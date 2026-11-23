"""Generate the Persian Music Scales bilingual static edition with Python 3."""
import json,os,shutil,sys
from html import escape
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from figures import dial
import article
R=Path(__file__).resolve().parents[1]
O=R/'dist'
BASE=os.environ.get('SITE_URL','https://persianmusicscales.github.io').rstrip('/')
PREVIEW=os.environ.get('PREVIEW','0')=='1'
if not urlparse(BASE).netloc: raise ValueError('SITE_URL requires an absolute URL')
if O.exists(): shutil.rmtree(O)
O.mkdir()
shutil.copytree(R/'assets',O/'assets')
def write(path,data):
    p=O/path
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(data)
P={"article": article.META}
for f in sorted((R/'content').glob('*.json')):
    new=json.loads(f.read_text())
    if P.keys() & new.keys(): raise ValueError(f'Duplicate page in {f}')
    P.update(new)
MODES='shur nava segah chahargah homayoun mahur rast-panjgah esfahan abu-ata bayat-e-tork afshari dashti'.split()
APP='https://persianmusicscales.github.io/Persian-Music-Scales-App/index.html?lang='
ATLAS='https://persianmusicscales.github.io/urmawi-advar-atlas/'
def route(k,l):
    slug='' if k=='home' else ('modes/' if k in MODES else '')+k+'/'
    return l+'/'+slug
def link(url,t,css=''):
    return f'<a class="{css}" href="{escape(url,quote=True)}">{escape(t)}</a>'
def logo():
    return '<svg viewBox="0 0 40 40" width="39" height="39" aria-hidden="true" fill="none" stroke="currentColor"><circle cx="20" cy="20" r="17"/><circle cx="20" cy="20" r="12"/><path d="m20 4 14 24H6Zm0 32L6 12h28Z"/><circle cx="20" cy="20" r="3"/></svg>'
def page(k,l,root=False):
    fa=l=='fa'
    def T(a,b):return b if fa else a
    path=route(k,l)
    up='./' if root else '../'*path.count('/')
    def loc(j,lang=l):return up+route(j,lang)
    def il(j,t,c=''):return link(loc(j),t,c)
    p=P[k][l]
    alt='en' if fa else 'fa'
    brand=T('Persian Music Scales','گام‌های موسیقی ایرانی')
    nav=[('theory',T('Theory','مبانی')),('modes',T('Modes','دستگاه‌ها و آوازها')),('tools',T('Tools','ابزارها')),('history',T('History','تاریخ')),('research',T('Research','پژوهش'))]
    navlinks=''.join(f'<a href="{loc(j)}"'+(' aria-current="page"' if j==k else '')+'>'+t+'</a>' for j,t in nav)
    header=f'<header><div class="bar"><a class="brand" href="{loc("home")}">{logo()}{brand}</a><nav aria-label="{T("Main","اصلی")}">{navlinks}</nav><div class="actions"><a lang="{alt}" hreflang="{alt}" href="{loc(k,alt)}">{T("فارسی","English")}</a><button id="theme" aria-label="{T("Change color theme","تغییر حالت رنگ")}">◐</button><button id="menu" hidden aria-expanded="false" aria-controls="mobile">{T("Menu","فهرست")}</button></div></div><nav id="mobile" hidden>{navlinks}</nav></header>'
    def plate():
        return f'<figure class="plate"><figcaption>{T("INTERVAL STUDY","مطالعهٔ فاصله‌ها")} <span>{T("MODEL · 24 EDO","مدل · ۲۴ قسمت مساوی")}</span></figcaption>{dial(l)}<div class="dialctrl"><button data-step="-1" aria-label="{T("Previous pitch position","جایگاه قبلی")}">−</button><output aria-live="polite" data-unit="{T("cents","سنت")}">0 {T("cents","سنت")}</output><button data-step="1" aria-label="{T("Next pitch position","جایگاه بعدی")}">+</button></div><small>{T("One step = 50 cents in this model.","هر گام در این مدل برابر با ۵۰ سنت است.")}</small></figure>'
    def cards(items):
        return '<div class="cards">'+''.join(f'<a href="{loc(j)}"><span class="glyph" aria-hidden="true">{g}</span><h3>{escape(P[j][l]["title"])}</h3><p>{escape(P[j][l]["lead"])}</p></a>' for j,g in items)+'</div>'
    def index():
        def entry(j):
            other=P[j][alt]['title']
            search=escape(' '.join([P[j]['en']['title'],P[j]['fa']['title'],j]),quote=True)
            return f'<a data-search="{search}" href="{loc(j)}"><strong>{escape(P[j][l]["title"])}</strong><span lang="{alt}">{escape(other)}</span></a>'
        families=[('shur',MODES[8:]),('homayoun',['esfahan'])]
        out=f'<div class="filter" hidden><label for="filter">{T("Find a mode","جست‌وجوی دستگاه یا آواز")}</label><input id="filter" type="search"></div><p id="empty" hidden>{T("No matching entry.","مدخلی پیدا نشد.")}</p>'
        for parent,children in families:
            out+=f'<section class="family"><h2>{T("The "+P[parent]["en"]["title"]+" family","خانوادهٔ "+P[parent]["fa"]["title"])}</h2><div class="kin"><div><h3>{T("Dastgāh","دستگاه")}</h3><div class="modes">{entry(parent)}</div></div><div><h3>{T("Related āvāz","آوازهای وابسته") if len(children)>1 else T("Related āvāz","آواز وابسته")}</h3><div class="modes">{"".join(entry(j) for j in children)}</div></div></div></section>'
        others=[j for j in MODES[:7] if j not in ('shur','homayoun')]
        return out+f'<section class="family"><h2>{T("Other dastgāhs in this guide","دیگر دستگاه‌ها در این راهنما")}</h2><div class="modes">{"".join(entry(j) for j in others)}</div></section>'
    def role_study():
        roles=[
            (T('Emphasis','تأکید'),T('C · Shāhed','دو · شاهد'),T('Listen for phrases circling this pitch.','به گردش جمله پیرامون این نت گوش کنید.')),
            (T('Temporary pause','مکث موقت'),T('A-koron · Ist','لاکُرُن · ایست'),T('Listen past the pause. Does the phrase continue?','پس از مکث چه می‌شنوید؟ آیا جمله ادامه دارد؟')),
            (T('Conclusion','خاتمه'),T('G · Finalis','سل · نت پایان'),T('Hear the arrival in the context of the whole passage.','رسیدن به این نت را در بافت کل عبارت بشنوید.'))]
        return '<figure class="role-study"><figcaption><strong>'+T('Three note functions in Abu Ata','سه نقش ملودیک در ابوعطا')+'</strong><span>'+T('Read this example from Gen’ichi Tsuge as a map of functions. The boxes have no prescribed time order.','نمونه‌ای از آوانگاری گِن‌ایچی تسوگه. کادرها نقش نت‌ها را نشان می‌دهند؛ ترتیب زمانی جمله را از روی آن‌ها نخوانید.')+'</span></figcaption><dl>'+''.join('<div><dt>'+heading+'</dt><dd><b>'+note+'</b><span>'+desc+'</span></dd></div>' for heading,note,desc in roles)+'</dl>'+link('https://www.iranicaonline.org/articles/abu-ata/',T('Read Tsuge’s Abu Ata entry','مدخل ابوعطا به قلم تسوگه'))+'</figure>'
    def app_gallery():
        shots = [
            ('shur', T('Shur', 'شور'), T('Shur on C, with the pitch circle and playback controls.', 'دایرهٔ فواصل شور روی دو، همراه با کنترل‌های پخش.')),
            ('bayat-tork-new', T('Bayat-e Tork', 'بیات ترک'), T('A highlighted pitch on the Bayat-e Tork wheel.', 'نمایش یک نت روی دایرهٔ بیات ترک.')),
            ('scale-notes', T('Modal notes', 'نقش نت‌ها'), T('The modal-role notes and sources for Bayat-e Tork.', 'توضیح نقش نت‌ها و منابع بیات ترک.')),
            ('track-analyzer-new', T('Analyzer', 'تحلیل‌گر'), T('Recording and analysis settings in the track analyzer.', 'گزینه‌های ضبط و تحلیل در بخش تحلیل‌گر قطعه.')),
        ]
        views = []
        for i,(file,label,caption) in enumerate(shots):
            selected = ' checked' if i == 0 else ''
            views.append(f'<input type="radio" name="screen" id="screen-{i}"{selected}><label for="screen-{i}">{label}</label><figure><a href="{up}assets/{file}.webp"><img loading="lazy" width="490" height="1000" src="{up}assets/{file}.webp" alt="{caption}"></a><figcaption>{caption}</figcaption></figure>')
        return '<fieldset class="app-gallery"><legend>'+T('App screenshots','تصویرهای برنامه')+'</legend>'+''.join(views)+'</fieldset>'
    def atlas_preview():
        description=T('The Atlas maps historical fret divisions onto a modern four-string setar.', 'در اطلس، تقسیمات تاریخی دستان روی سه‌تار چهار‌سیم امروزی نمایش داده شده‌اند.')
        return f'<figure class="instrument"><a href="{ATLAS}?lang={l}&amp;panel=explore"><img src="{up}assets/atlas-combined.webp" width="1361" height="414" alt="{description}" loading="lazy"></a><figcaption>{description}</figcaption></figure>'
    if k=='home':
        main=f'<section class="hero"><div class="herocopy"><div class="eyebrow">{T("PERSIAN CLASSICAL MUSIC","موسیقی دستگاهی ایران")}</div><h1>{T("Persian Music <em>Scales</em>","گام‌های <em>موسیقی ایرانی</em>")}</h1><p>{escape(p["lead"])}</p><div class="buttons">{il("modes",T("Explore the modes","آشنایی با دستگاه‌ها"),"primary")}{link(APP+l,T("Launch interactive app","ورود به برنامه"),"secondary")}</div></div>{plate()}</section><section class="paths"><div class="eyebrow">{T("FIELD GUIDE","راهنمای مطالعه")}</div><h2>{T("Ways to explore","مسیرهای مطالعه")}</h2>{cards([("theory","♩"),("radif","♫"),("notation","♭")])}</section>'
        main+=f'<section class="project-show app-show"><div><div class="eyebrow">{T("INTERACTIVE APPLICATION","برنامهٔ تعاملی")}</div><h2>{brand}</h2><p>{T("Listen to a mode, transpose its pitch circle, or follow a recorded melody. Select a screenshot to see how each tool works.","یک دستگاه یا آواز را بشنوید، دایرهٔ فواصل آن را انتقال دهید یا مسیر ملودی ضبط‌شده را دنبال کنید. برای دیدن بخش‌های مختلف برنامه، یکی از تصویرها را انتخاب کنید.")}</p><div class="buttons">{link(APP+l,T("Open the app","ورود به برنامه"),"primary")}{il("tools",T("Read the app guide","راهنمای برنامه"),"secondary")}</div></div>{app_gallery()}</section>'
        main+=f'<section class="project-show atlas-show"><div class="eyebrow">{T("HISTORICAL MUSIC THEORY","نظریهٔ تاریخی موسیقی")}</div><h2>{T("Al-Urmawī Advar Atlas","اطلس ادوار صفی‌الدین ارموی")}</h2><p>{T("Explore the fret divisions in the Book of Cycles. Move along the string in the Atlas to hear how a change in sounding length changes the interval.","تقسیم دستان در کتاب الادوار را بررسی کنید. در اطلس روی سیم حرکت کنید و بشنوید که با تغییر طول بخش مرتعش سیم، فاصلهٔ موسیقایی چگونه تغییر می‌کند.")}</p><div class="buttons">{link(ATLAS+"?lang="+l,T("Open the Atlas","ورود به اطلس"),"primary")}{il("history",T("Read the historical guide","راهنمای تاریخی"),"secondary")}</div>{atlas_preview()}</section>'
        main+=f'<section class="paths"><div class="eyebrow">{T("RESEARCH ARTICLE","مقالهٔ پژوهشی")}</div><h2>{escape(P["article"][l]["title"])}</h2><p>{escape(P["article"][l]["lead"])}</p>{il("article",T("Read the full article","مطالعهٔ متن کامل مقاله"),"primary")}</section>'
    else:
        bread=il('home',brand)+' / '+(il('modes',T('Modes','دستگاه‌ها و آوازها'))+' / ' if k in MODES else '')+escape(p['title'])
        main=f'<div class="crumb">{bread}</div><article><div class="eyebrow">{brand}</div><h1>{escape(p["title"])}</h1><p class="lead">{escape(p["lead"])}</p>'
        if k=='article':main+=article.render(l,up)
        if k in ('research','tools'):main+='<p>'+il('article',P['article'][l]['title'],'secondary')+'</p>'
        if k=='tools':main+=app_gallery()
        if k=='history':main+=atlas_preview()
        if k=='modes':main+=index()
        if k=='notation':main+=plate()
        if k in ('theory','abu-ata'):main+=role_study()
        if k in ('theory','radif'):
            jump=''.join(link('#reading-'+str(i),h) for i,(h,_) in enumerate(p['sections'],1))
            main+=f'<nav class="reading-index" aria-label="{T("On this page","در این صفحه")}"><strong>{T("On this page","در این صفحه")}</strong><div>{jump}</div></nav>'
        main+='<div class="prose">'+''.join(f'<section id="reading-{i}"><h2>{escape(h)}</h2><p>{escape(v)}</p></section>' for i,(h,v) in enumerate(p.get('sections',[]),1))+'</div>'
        if k in ('theory','radif') or k in MODES:
            other='theory' if k=='radif' else 'radif'
            main+=il(other,P[other][l]['title'],'secondary')+' '
        if k=='theory':main+=il('notation',T('Study the interval circle','مطالعهٔ دایرهٔ فاصله‌ها'),'primary')+' '+il('modes',T('Browse the modes','فهرست دستگاه‌ها و آوازها'),'secondary')
        if k in MODES:main+=link(APP+l,T('Explore in the application','کاوش در برنامه'),'primary')+' '+il('modes',T('All modes','همهٔ دستگاه‌ها و آوازها'),'secondary')
        if k=='tools':main+=link(APP+l,T('Open the scale explorer','ورود به برنامهٔ گام‌ها'),'primary')
        if k=='history':main+=link(ATLAS+'?lang='+l,T('Open the Advar Atlas','ورود به اطلس ادوار'),'primary')
        relatives={'shur':['abu-ata','bayat-e-tork','afshari','dashti','nava'],'homayoun':['esfahan'],'esfahan':['homayoun'],'mahur':['rast-panjgah'],'rast-panjgah':['mahur'],'nava':['shur'],**{x:['shur'] for x in MODES[8:]}}
        if k in relatives:main+='<aside><h2>'+T('Related modes','دستگاه‌ها و آوازهای مرتبط')+'</h2>'+ ' · '.join(il(j,P[j][l]['title']) for j in relatives[k])+'</aside>'
        if p.get('links'):main+='<aside><h2>'+T('Sources & further reading','منابع و مطالعهٔ بیشتر')+'</h2><ul>'+''.join('<li>'+link(url,label)+'</li>' for label,url in p['links'])+'</ul></aside>'
        main+='</article>'
    footer=f'<footer><div><strong>{brand}</strong><p>{T("A project by","پروژه‌ای از")} {link("https://drpouyahosseini.github.io/",T("Dr. Pouya Hosseini","دکتر پویا حسینی"))}</p></div><div>{il("about",T("About the project","دربارهٔ پروژه"))}{il("research",T("Research & references","پژوهش و منابع"))}{il("search",T("Search the site","جست‌وجو در سایت"))}</div></footer>'
    if k=='search':
        items=[(j,a[l]['title'],a[l]['lead']) for j,a in P.items() if j not in ('search','home')]
        main=main.replace('</article>','<div class="filter" hidden><label for="filter">'+T('Search pages','جست‌وجوی صفحه‌ها')+'</label><input id="filter" type="search"></div><p id="empty" hidden>'+T('No matching pages.','صفحه‌ای پیدا نشد.')+'</p><ul class="results">'+''.join(f'<li data-search="{escape(title+" "+lead+" "+P[j][alt]["title"])}">{il(j,title)}<p>{escape(lead)}</p></li>' for j,title,lead in items)+'</ul></article>')
    title=escape(p['title']+' · '+brand) if k!='home' else brand
    meta=escape(p['lead'],quote=True)
    alts=''.join(f'<link rel="alternate" hreflang="{a}" href="{BASE}/{route(k,a)}">' for a in ['en','fa'])
    structured=json.dumps({'@context':'https://schema.org','@type':'WebPage','name':p['title'],'inLanguage':l,'url':BASE+'/'+path},ensure_ascii=False)
    noindex='<meta name="robots" content="noindex,nofollow">' if PREVIEW else ''
    verification='<meta name="google-site-verification" content="bar9iVDKejX30uUGMR7PgldOZCrXmeHWHFh6p5Cgv7w">' if k=='home' and not PREVIEW else ''
    return f'''<!doctype html><html lang="{l}" dir="{T("ltr","rtl")}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{noindex}{verification}<title>{title}</title><meta name="description" content="{meta}"><link rel="canonical" href="{BASE}/{path}">{alts}<link rel="alternate" hreflang="x-default" href="{BASE}/{route(k,"en")}"><meta property="og:title" content="{title}"><meta property="og:description" content="{meta}"><meta property="og:type" content="website"><meta property="og:url" content="{BASE}/{path}"><meta property="og:image" content="{BASE}/assets/share.png"><link rel="icon" href="{up}assets/icon.svg"><link rel="stylesheet" href="{up}assets/style.css"><script src="{up}assets/theme.js"></script><script src="{up}assets/ui.js" defer></script><script type="application/ld+json">{structured}</script></head><body><a class="skip" href="#content">{T("Skip to content","رفتن به محتوا")}</a>{header}<main id="content">{main}</main>{footer}</body></html>'''
for k in P:
    for lang in ['en','fa']:
        write(route(k,lang)+'index.html',page(k,lang))
write('index.html',page('home','en',True))
write('assets/icon.svg',logo().replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" color="#699b8b" '))
write('.nojekyll','')
verification_file = 'googled2e5da6be79bd23d.html'
(O/'assets'/verification_file).replace(O/verification_file)
s=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for k in P:
    for l in ['en','fa']:ET.SubElement(ET.SubElement(s,'url'),'loc').text=BASE+'/'+route(k,l)
write('sitemap.xml',ET.tostring(s,encoding='unicode'))
write('robots.txt','User-agent: *\n'+('Disallow: /\n' if PREVIEW else 'Allow: /\nSitemap: '+BASE+'/sitemap.xml\n'))
print('Generated',len(P)*2+1,'HTML pages')
