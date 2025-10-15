// 369 Navigator
document.addEventListener('DOMContentLoaded', () => {
  const reduce9 = (s) => {
    const digits = (s.match(/\d/g)||[]).map(Number);
    if (!digits.length) return { sum:0, mod9:0 };
    const sum = digits.reduce((a,b)=>a+b,0);
    const mod9 = sum % 9 || 9;
    return { sum, mod9 };
  };
  $('#n369go')?.addEventListener('click', () => {
    const val = $('#n369in').value || '';
    const { sum, mod9 } = reduce9(val);
    const bands = [3,6,9].map(k => ({ k, hit: (mod9===k) }));
    $('#n369out').innerHTML = `
      <div class="font-mono">Σ(digits) = ${sum}, Σ mod 9 → <b>${mod9}</b></div>
      <div class="mt-1 text-xs text-gray-400">Faza: ${bands.map(b=> b.hit?'<b>'+b.k+'</b>':b.k).join(' → ')}</div>
      <div class="mt-2">Interpretacja: ${mod9===9? 'Zamknięcie cyklu i skok na nowy poziom (9→1).':'W trakcie cyklu — dążenie do 9.'}</div>
    `;
  });
  window._n369 = { reduce9 };
});
