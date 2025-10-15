// Motyw / język / menu – inicjalizacje globalne
const $ = (s, p=document) => p.querySelector(s);
const $$ = (s, p=document) => Array.from(p.querySelectorAll(s));

$('#btnTheme')?.addEventListener('click', () => {
  document.documentElement.classList.toggle('invert');
  document.body.classList.toggle('bg-white');
});
$('#btnLang')?.addEventListener('click', (e) => {
  const btn = e.currentTarget;
  btn.textContent = btn.textContent.trim() === 'PL' ? 'EN' : 'PL';
});
$('#btnMenu')?.addEventListener('click', () => $('#menuMobile').classList.toggle('hidden'));
