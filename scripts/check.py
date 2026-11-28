"""Check the actual static output without third-party packages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
import json,re
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]/'dist'
class Document(HTMLParser):
    def __init__(self):
        super().__init__()
        self.nodes=[]
        self.jsonld=[]
        self.in_jsonld=False
    def handle_starttag(self,tag,attrs):
        self.nodes.append((tag,dict(attrs)))
        if tag=='script' and dict(attrs).get('type')=='application/ld+json':
            self.in_jsonld=True
    def handle_endtag(self,tag):
        if tag=='script': self.in_jsonld=False
    def handle_data(self,data):
        if self.in_jsonld: self.jsonld.append(data)
    def tags(self,t):
        return [attrs for tag,attrs in self.nodes if tag==t]
seen=set()
total=0
for page in sorted(root.rglob('index.html')):
    d=Document()
    d.feed(page.read_text())
    lang=d.tags('html')[0]['lang']
    assert d.tags('html')[0]['dir']==('rtl' if lang=='fa' else 'ltr'),page
    refresh=next((a for a in d.tags('meta') if a.get('http-equiv')=='refresh'),None)
    if refresh:
        target=refresh['content'].split('0;url=',1)[1]
        destination=(page.parent/target/'index.html').resolve()
        assert destination.is_file() and destination.parent.parent.name==lang,page
        assert destination.parent.name in ('article','tools'),page
        assert d.tags('a')[0]['href']==target,page
        assert any(a.get('name')=='robots' and a.get('content')=='noindex' for a in d.tags('meta')),page
        continue
    for tag in ['main','h1','title']:
        assert len(d.tags(tag))==1,(page,tag)
    ids=[a['id'] for _,a in d.nodes if 'id' in a]
    assert len(ids)==len(set(ids)),page
    canonical=next(x['href'] for x in d.tags('link') if x.get('rel')=='canonical')
    if page.parent!=root:
        assert canonical not in seen,canonical
        seen.add(canonical)
    assert {a.get('hreflang') for a in d.tags('link') if a.get('rel')=='alternate'}=={'en','fa','x-default'}
    assert next(a['content'] for a in d.tags('meta') if a.get('name')=='description').strip()
    graph=json.loads(''.join(d.jsonld))['@graph']
    assert {'Person','WebSite','WebPage'} <= {n['@type'] for n in graph},page
    assert next(n for n in graph if n['@type']=='WebPage')['url']==canonical,page
    assert next(a['content'] for a in d.tags('meta') if a.get('property')=='og:url')==canonical,page
    assert any(a.get('name')=='twitter:card' and a.get('content')=='summary_large_image' for a in d.tags('meta')),page
    if page.parent.name=='article':
        assert any(n['@type']=='Article' and n.get('author') for n in graph),page
    for tag,a in d.nodes:
        for key in ['href','src']:
            if key not in a:continue
            u=urlparse(a[key])
            if u.scheme or u.netloc: continue
            if not u.path:
                if u.fragment:assert u.fragment in ids,(page,u.fragment)
                continue
            dest=page.parent/unquote(u.path)
            if dest.is_dir():dest/= 'index.html'
            assert dest.is_file(),(page,a[key])
            total+=1
    assert all(a.get('aria-label') or 'id' in a for a in d.tags('button'))
for url in re.findall(r'url\(([^)]+)\)',(root/'assets/style.css').read_text()):
    assert (root/'assets'/url).is_file(),url
site=ET.parse(root/'sitemap.xml');assert {e.text for e in site.findall('./{*}url/{*}loc')}==seen
home=Document();home.feed((root/'index.html').read_text())
en=Document();en.feed((root/'en/index.html').read_text())
root_canonical=next(a['href'] for a in home.tags('link') if a.get('rel')=='canonical')
assert root_canonical==next(a['href'] for a in en.tags('link') if a.get('rel')=='canonical')
assert root_canonical in seen and not root_canonical.endswith('/en/')
for u in site.findall('./{*}url'):
    alts=u.findall('./{http://www.w3.org/1999/xhtml}link')
    assert {a.attrib['hreflang'] for a in alts}=={'en','fa','x-default'}
    assert all(a.attrib['href'] in seen for a in alts)
if (root/'llms.txt').exists():
    assert all(url in (root/'llms.txt').read_text() for url in seen)
assert (root/'assets/share.png').is_file()
print(f'{len(seen)} localized pages plus root, {total} internal references, sitemap, alternate languages, metadata and font files passed.')
