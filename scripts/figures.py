"""Original drawings. Cents are mapped clockwise over one octave."""
import math
from html import escape

def point(r, deg):
    a = math.radians(deg - 90)
    return (240+r*math.cos(a), 240+r*math.sin(a))

def coords(r,a):
    return ','.join(f'{n:.2f}' for n in point(r,a))

def dial(lang, step=0):
    title = 'Octave divided into 24 equal model positions' if lang=='en' else 'تقسیم اکتاو به ۲۴ جایگاه مساوی در مدل'
    s=[f'<svg class="dial" viewBox="0 0 480 480" role="img" aria-label="{title}" direction="ltr" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="currentColor">']
    for r in [117,151,159,172,177,203]:
        s.append(f'<circle cx="240" cy="240" r="{r}" opacity=".35" stroke-width="{1 if r!=177 else 2}"/>')
    for i in range(120):
        a=i*3
        s.append(f'<path d="M{coords(178,a)} L{coords(188 if i%5==0 else 182,a)}" opacity="{.9 if i%5==0 else .5}"/>')
    for i in range(24):
        a=i*15
        s.append(f'<path d="M{coords(119,a)} L{coords(171,a)}" opacity=".27"/>')
        if i%2==0:
            note=['C','D♭','D','E♭','E','F','G♭','G','A♭','A','B♭','B'][i//2]
            x,y=point(221,a)
            s.append(f'<text x="{x:.1f}" y="{y+5:.1f}" text-anchor="middle" fill="currentColor" stroke="none" font-family="Georgia,serif" font-size="17">{note}</text>')
    for n in [3,4,6]:
        for shift in range(0,24,24//n):
            a=shift*15
            s.append(f'<path d="M{coords(151,a)} L{coords(151,a+360/n)}" opacity=".32"/>')
    for i in range(24):
        x,y=point(159,i*15)
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{3.8 if i%2==0 else 2}" fill="currentColor" stroke="none"/>')
    s.append('<g class="needle" style="transform:rotate('+str(step*15)+'deg)"><path d="M240 240 L240 77" stroke="#efbd72" stroke-width="2"/><circle cx="240" cy="81" r="6" fill="#efbd72" stroke="#102e32" stroke-width="2"/></g><circle cx="240" cy="240" r="34" fill="#13393c"/><path d="M228 240 Q231 240 233 234 T239 244 T245 235 T252 240" stroke="#eac48b" stroke-width="2"/></g></svg>')
    return ''.join(s)
