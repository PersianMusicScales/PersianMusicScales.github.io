const page = document.documentElement;
const fa = page.lang === 'fa';
const theme = document.querySelector('#theme');
theme.addEventListener('click', () => {
  const dark = getComputedStyle(page).colorScheme === 'dark';
  page.dataset.theme = dark ? 'light' : 'dark';
  try { localStorage.setItem('pms-theme', page.dataset.theme); } catch {}
});
const menu = document.querySelector('#menu');
const mobile = document.querySelector('#mobile');
menu.hidden = false;
menu.addEventListener('click', () => {
  mobile.hidden = !mobile.hidden;
  menu.setAttribute('aria-expanded', String(!mobile.hidden));
});
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && !mobile.hidden) { mobile.hidden = true; menu.setAttribute('aria-expanded','false'); menu.focus(); }
});
document.querySelectorAll('.plate').forEach(plate => {
  let step = 0;
  const output = plate.querySelector('output');
  plate.querySelectorAll('[data-step]').forEach(button => button.addEventListener('click', () => {
    step = (step + Number(button.dataset.step) + 24) % 24;
    plate.querySelector('.needle').style.transform = 'rotate(' + step * 15 + 'deg)';
    output.value = new Intl.NumberFormat(page.lang).format(step * 50) + ' ' + output.dataset.unit;
  }));
});
const filter = document.querySelector('#filter');
if (filter) {
  filter.parentElement.hidden = false;
  const norm = s => s.normalize('NFKD').toLowerCase().replace(/[\u064B-\u065F\u0300-\u036f\u200c\s’-]/g,'').replace(/ي/g,'ی').replace(/ك/g,'ک');
  filter.addEventListener('input', () => {
    let shown = 0;
    document.querySelectorAll('[data-search]').forEach(el => {
      el.hidden = !norm(el.dataset.search).includes(norm(filter.value));
      if (!el.hidden) shown++;
    });
    document.querySelector('#empty').hidden = shown > 0;
  });
}
