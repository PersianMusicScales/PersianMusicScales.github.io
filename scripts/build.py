"""Generate the Persian Music Scales bilingual static edition with Python 3."""
import json,os,shutil,sys
from html import escape
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
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
P['advar-atlas'] = {}
for lang in ('en','fa'):
    source = P['history'][lang]
    P['advar-atlas'][lang] = {
        'title': source['title'],
        'lead': ('An interactive reconstruction of the interval ratios, fret positions and modal cycles described in Ṣafī al-Dīn al-Urmawī’s Book of Cycles.' if lang=='en' else 'بازسازی تعاملی نسبت فواصل، جای دستان‌ها و ادوار موسیقایی در کتاب الادوار صفی‌الدین ارموی.'),
        'sections': source['sections'][:4],
        'links': source['links'][1:],
    }
    P['tools'][lang]['title'] = 'Persian Music Scales App' if lang=='en' else 'برنامهٔ گام‌های موسیقی ایرانی'
shortcut_names = {"en": "Persian Scales", "fa": "گام‌های ایرانی"}
published=('home','article','tools','advar-atlas')
retired=set(P).difference(published)
APP='https://persianmusicscales.github.io/Persian-Music-Scales-App/index.html?lang='
ATLAS='https://persianmusicscales.github.io/urmawi-advar-atlas/'
WORLD='https://worldmusicscalesatlas.github.io/'
AUTHOR='https://drpouyahosseini.github.io/'
def route(k,l):
    slug='' if k=='home' else ('modes/' if k in MODES else '')+k+'/'
    return l+'/'+slug
def canonical_url(k,l):
    return BASE+'/' + ('' if k=='home' and l=='en' else route(k,l))
def link(url,t,css=''):
    return f'<a class="{css}" href="{escape(url,quote=True)}">{escape(t)}</a>'
def page(k,l,root=False):
    fa=l=='fa'
    def T(a,b):return b if fa else a
    path=route(k,l)
    up='./' if root else '../'*path.count('/')
    def loc(j,lang=l):return up+('' if j=='home' and lang=='en' else route(j,lang))
    def il(j,t,c=''):return link(loc(j),t,c)
    p=P[k][l]
    alt='en' if fa else 'fa'
    brand=T('Persian Music Scales','گام‌های موسیقی ایرانی')
    nav=[('article',T('Article','مقاله')),('tools',P['tools'][l]['title']),('advar-atlas',T('Urmawī Advar Atlas','اطلس ادوار ارموی'))]
    navlinks=''.join(f'<a href="{loc(j)}"'+(' aria-current="page"' if j==k else '')+'>'+t+'</a>' for j,t in nav)
    header=f'<header><div class="bar"><a class="brand" href="{loc("home")}"><img src="{up}assets/setar.webp" width="39" height="39" alt="" style="border-radius:20%">{brand}</a><nav aria-label="{T("Main","اصلی")}">{navlinks}</nav><div class="actions"><a lang="{alt}" hreflang="{alt}" href="{loc(k,alt)}">{T("فارسی","English")}</a><button id="theme" aria-label="{T("Change color theme","تغییر حالت رنگ")}">◐</button><button id="menu" hidden aria-expanded="false" aria-controls="mobile">{T("Menu","فهرست")}</button></div></div><nav id="mobile" hidden>{navlinks}</nav></header>'
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
        main=f'<section class="hero" style="display:block"><div class="herocopy" style="max-width:52rem"><div class="eyebrow">{T("PERSIAN CLASSICAL MUSIC","موسیقی دستگاهی ایران")}</div><h1>{T("Persian Music <em>Scales</em>","گام‌های <em>موسیقی ایرانی</em>")}</h1><p>{escape(p["lead"])}</p><div class="buttons">{il("article",T("Read the article","مطالعهٔ مقاله"),"primary")}{link(APP+l,T("Launch interactive app","ورود به برنامه"),"secondary")}</div></div></section>'
        main+=f'<section class="hub-intro"><h2>{T("Explore Persian modes and microtonal intervals","آشنایی با دستگاه‌ها و فواصل ریزپرده‌ای موسیقی ایران")}</h2><p>{T("Study dastgāh and āvāz through interactive pitch circles, cent-based interval diagrams, scale transposition, and audio analysis. The numerical models support learning and comparison; they do not replace the melodic grammar or performance practice of Persian classical music.","دستگاه‌ها و آوازها را با دایره‌های تعاملی نت‌ها، نمودار فواصل بر حسب سنت، انتقال گام و تحلیل صوت بررسی کنید. مدل‌های عددی برای یادگیری و مقایسه‌اند و جایگزین دستور ملودیک یا شیوهٔ اجرای موسیقی دستگاهی ایران نیستند.")}</p></section>'
        main+=f'<section class="project-show app-show"><div><div class="eyebrow">{T("INTERACTIVE APPLICATION","برنامهٔ تعاملی")}</div><h2>{brand}</h2><p>{T("Listen to a mode, transpose its pitch circle, or follow a recorded melody. Select a screenshot to see how each tool works.","یک دستگاه یا آواز را بشنوید، دایرهٔ فواصل آن را انتقال دهید یا مسیر ملودی ضبط‌شده را دنبال کنید. برای دیدن بخش‌های مختلف برنامه، یکی از تصویرها را انتخاب کنید.")}</p><div class="buttons">{link(APP+l,T("Open the app","ورود به برنامه"),"primary")}{il("tools",T("Read the app guide","راهنمای برنامه"),"secondary")}</div></div>{app_gallery()}</section>'
        main+=f'<section class="project-show atlas-show"><div class="eyebrow">{T("HISTORICAL MUSIC THEORY","نظریهٔ تاریخی موسیقی")}</div><h2>{T("Al-Urmawī Advar Atlas","اطلس ادوار صفی‌الدین ارموی")}</h2><p>{T("Explore the fret divisions in the Book of Cycles. Move along the string in the Atlas to hear how a change in sounding length changes the interval.","تقسیم دستان در کتاب الادوار را بررسی کنید. در اطلس روی سیم حرکت کنید و بشنوید که با تغییر طول بخش مرتعش سیم، فاصلهٔ موسیقایی چگونه تغییر می‌کند.")}</p><div class="buttons">{link(ATLAS+"?lang="+l,T("Open the Atlas","ورود به اطلس"),"primary")}{il("advar-atlas",T("About the Atlas","دربارهٔ اطلس"),"secondary")}</div>{atlas_preview()}</section>'
        main+=f'<section class="paths"><div class="eyebrow">{T("RESEARCH ARTICLE","مقالهٔ پژوهشی")}</div><h2>{escape(P["article"][l]["title"])}</h2><p>{escape(P["article"][l]["lead"])}</p>{il("article",T("Read the full article","مطالعهٔ متن کامل مقاله"),"primary")}</section>'
    else:
        bread=il('home',brand)+' / '+(il('modes',T('Modes','دستگاه‌ها و آوازها'))+' / ' if k in MODES else '')+escape(p['title'])
        main=f'<div class="crumb">{bread}</div><article><div class="eyebrow">{brand}</div><h1>{escape(p["title"])}</h1><p class="lead">{escape(p["lead"])}</p>'
        if k=='article':
            main+='<p class="article-byline">'+T('By ','نویسنده: ')+link(AUTHOR,T('Dr. Pouya Hosseini','دکتر پویا حسینی'))+'</p>'
            main+=article.render(l,up)
        if k=='tools':
            main+='<div class="buttons">'+link(APP+l,T('Launch Persian Music Scales','ورود به برنامهٔ گام‌ها'),'primary')+il('article',T('Read the research article','مطالعهٔ مقالهٔ پژوهشی'),'secondary')+'</div>'+app_gallery()
        if k=='advar-atlas':
            main+='<div class="buttons">'+link(ATLAS+'?lang='+l,T('Launch the Advar Atlas','ورود به اطلس ادوار'),'primary')+link(ATLAS+'reference/'+l+'/',T('Scholarly reference and exact pitch data','مرجع پژوهشی و داده‌های دقیق نغمه‌ها'),'secondary')+'</div>'+atlas_preview()
        main+='<div class="prose">'+''.join(f'<section id="reading-{i}"><h2>{escape(h)}</h2><p>{escape(v)}</p></section>' for i,(h,v) in enumerate(p.get('sections',[]),1))+'</div>'
        if p.get('links'):main+='<aside><h2>'+T('Sources & further reading','منابع و مطالعهٔ بیشتر')+'</h2><ul>'+''.join('<li>'+link(url,label)+'</li>' for label,url in p['links'])+'</ul></aside>'
        main+='</article>'
    footer=f'<footer><div><strong>{brand}</strong><p>{T("A project by","پروژه‌ای از")} {link("https://drpouyahosseini.github.io/",T("Dr. Pouya Hosseini","دکتر پویا حسینی"))}</p></div><div>{il("article",T("Article","مقاله"))}{il("tools",P["tools"][l]["title"])}{il("advar-atlas",T("Urmawī Advar Atlas","اطلس ادوار ارموی"))}{link("https://worldmusicscalesatlas.github.io/",T("World Music Scales Atlas","اطلس گام‌های موسیقی جهان"))}</div></footer>'
    page_titles={
        'home': T('Persian Music Scales – Dastgah, Avaz & Microtonal Theory','گام‌های موسیقی ایرانی | دستگاه، آواز و فواصل ریزپرده‌ای'),
        'article': p['title']+' · '+brand,
        'tools': T('Persian Music Scales App – Interactive Scales & Audio Analysis','برنامهٔ گام‌های موسیقی ایرانی | گام و تحلیل صوت'),
        'advar-atlas': T('Urmawī Advar Atlas – Historical Persian Music Theory','اطلس ادوار ارموی | نظریهٔ تاریخی موسیقی ایران'),
    }
    descriptions={
        'home': T('Explore Persian classical music, dastgah, avaz and microtonal intervals through an interactive scale app, historical music atlas and research article by Dr. Pouya Hosseini.','دستگاه‌ها، آوازها و فواصل ریزپرده‌ای موسیقی ایرانی را با برنامهٔ تعاملی گام‌ها، اطلس ادوار ارموی و مقالهٔ دکتر پویا حسینی بررسی کنید.'),
        'tools': T('Explore Persian scales with interactive pitch circles, transposition, playback and browser-based audio analysis.','گام‌های موسیقی ایرانی را با دایرهٔ نت‌ها، انتقال گام، پخش صوت و تحلیل صوت در مرورگر بررسی کنید.'),
    }
    title=escape(page_titles[k],quote=True)
    summary=descriptions.get(k,p['lead'])
    meta=escape(summary,quote=True)
    canonical=canonical_url(k,l)
    alts=''.join(f'<link rel="alternate" hreflang="{a}" href="{canonical_url(k,a)}">' for a in ('en','fa'))
    person={'@type':'Person','@id':AUTHOR+'#person','name':'Dr. Pouya Hosseini','alternateName':'دکتر پویا حسینی','url':AUTHOR}
    website={'@type':'WebSite','@id':BASE+'/#website','name':'Persian Music Scales','alternateName':'گام‌های موسیقی ایرانی','url':BASE+'/','inLanguage':['en','fa'],'creator':{'@id':person['@id']}}
    page_node={'@type':'WebPage','@id':canonical+'#webpage','name':page_titles[k],'description':summary,'inLanguage':l,'url':canonical,'isPartOf':{'@id':website['@id']},'creator':{'@id':person['@id']}}
    graph=[person,website,page_node]
    if k=='article':
        article_node={'@type':'Article','@id':canonical+'#article','headline':p['title'],'description':summary,'inLanguage':l,'author':{'@id':person['@id']},'mainEntityOfPage':{'@id':page_node['@id']},'url':canonical,'image':BASE+'/assets/share.png'}
        graph.append(article_node)
        page_node['mainEntity']={'@id':article_node['@id']}
    structured=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('<',r'\u003c')
    noindex='<meta name="robots" content="noindex,nofollow">' if PREVIEW else '<meta name="robots" content="index,follow,max-image-preview:large">'
    verification='<meta name="google-site-verification" content="bar9iVDKejX30uUGMR7PgldOZCrXmeHWHFh6p5Cgv7w">' if k=='home' and not PREVIEW else ''
    return f'''<!doctype html><html lang="{l}" dir="{T("ltr","rtl")}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">{noindex}{verification}<title>{title}</title><meta name="description" content="{meta}"><link rel="canonical" href="{canonical}">{alts}<link rel="alternate" hreflang="x-default" href="{canonical_url(k,"en")}"><meta property="og:title" content="{title}"><meta property="og:description" content="{meta}"><meta property="og:type" content="{'article' if k=='article' else 'website'}"><meta property="og:site_name" content="{brand}"><meta property="og:locale" content="{T('en_US','fa_IR')}"><meta property="og:locale:alternate" content="{T('fa_IR','en_US')}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{BASE}/assets/share.png"><meta property="og:image:alt" content="{brand}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{meta}"><meta name="twitter:image" content="{BASE}/assets/share.png"><meta name="author" content="Dr. Pouya Hosseini"><link rel="icon" href="{up}assets/setar.webp"><link rel="apple-touch-icon" sizes="180x180" href="{up}apple-touch-icon.png"><meta name="apple-mobile-web-app-title" content="{shortcut_names[l]}"><link rel="manifest" href="{up}{l}/site.webmanifest"><link rel="stylesheet" href="{up}assets/style.css"><script src="{up}assets/theme.js"></script><script src="{up}assets/ui.js" defer></script><script type="application/ld+json">{structured}</script></head><body><a class="skip" href="#content">{T("Skip to content","رفتن به محتوا")}</a>{header}<main id="content">{main}</main>{footer}</body></html>'''
for k in published:
    for lang in ['en','fa']:
        write(route(k,lang)+'index.html',page(k,lang))
for k in retired:
    for lang in ('en','fa'):
        old=route(k,lang)
        target='tools' if k in ('history','search') else 'article'
        dest='../'*old.count('/')+route(target,lang)
        title={'tools':{'en':'Tools','fa':'ابزارها'},'article':{'en':'Article','fa':'مقاله'}}[target][lang]
        canonical=BASE+'/'+route(target,lang)
        write(old+'index.html',f'<!doctype html><html lang="{lang}" dir="{("rtl" if lang=="fa" else "ltr")}"><head><meta charset="utf-8"><title>{title}</title><meta name="robots" content="noindex"><link rel="canonical" href="{canonical}"><meta http-equiv="refresh" content="0;url={dest}"></head><body><main><a href="{dest}">{title}</a></main></body></html>')
write('index.html',page('home','en',True))
shutil.copyfile(R/'scripts/setar.webp', O/'assets/setar.webp')
for size, filename in ((180, 'apple-touch-icon.png'), (192, 'icon-192.png'), (512, 'icon-512.png')):
    shutil.copyfile(R/'scripts'/filename, O/filename)
for lang, short_name in shortcut_names.items():
    manifest = {
        'id': '../', 'name': short_name, 'short_name': short_name, 'lang': lang,
        'start_url': './', 'scope': '../', 'display': 'standalone',
        'theme_color': '#10292c', 'background_color': '#10292c',
        'icons': [{'src': f'../icon-{size}.png', 'sizes': f'{size}x{size}', 'type': 'image/png'}
                  for size in (192, 512)],
    }
    write(f'{lang}/site.webmanifest', json.dumps(manifest, ensure_ascii=False))
write('.nojekyll','')
verification_file = 'googled2e5da6be79bd23d.html'
(O/'assets'/verification_file).replace(O/verification_file)
ET.register_namespace('xhtml','http://www.w3.org/1999/xhtml')
s=ET.Element('urlset',xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for k in published:
    for l in ('en','fa'):
        node=ET.SubElement(s,'url')
        ET.SubElement(node,'loc').text=canonical_url(k,l)
        for a in ('en','fa','x-default'):
            ET.SubElement(node,'{http://www.w3.org/1999/xhtml}link',rel='alternate',hreflang=a,href=canonical_url(k,'en' if a=='x-default' else a))
write('sitemap.xml',ET.tostring(s,encoding='unicode',xml_declaration=True))
if not PREVIEW:
    write('llms.txt', '# Persian Music Scales\n\n> Bilingual educational project by Dr. Pouya Hosseini on Persian classical music, interactive pitch models and historical interval theory. Scale diagrams are simplified models, not substitutes for melodic practice.\n\n## Main resources\n\n'+'\n'.join(f'- [{P[k][l]["title"]}]({canonical_url(k,l)}): {P[k][l]["lead"]}' for k in published for l in ('en','fa'))+'\n\n## Related projects\n\n- [Persian Music Scales App]('+APP+'en)\n- [Urmawī Advar Atlas]('+ATLAS+')\n- [World Music Scales Atlas]('+WORLD+')\n- [Author website]('+AUTHOR+')\n')
write('robots.txt','User-agent: *\n'+('Disallow: /\n' if PREVIEW else 'Allow: /\nSitemap: '+BASE+'/sitemap.xml\nSitemap: '+ATLAS+'sitemap.xml\n'))
print('Generated',len(published)*2+1,'content pages and',len(retired)*2,'redirects')
