// Linear core y = a*x + b
document.addEventListener('DOMContentLoaded', () => {
  const coreA = $('#coreA'), coreB = $('#coreB'), coreX = $('#coreX'), coreY = $('#coreY');
  // load saved params
  (() => {
    const saved = store.get('coreParams');
    if (saved && typeof saved.a === 'number' && typeof saved.b === 'number') {
      coreA.value = saved.a;
      coreB.value = saved.b;
    }
  })();
  $('#coreSave')?.addEventListener('click', () => {
    const a = Number(coreA.value||0), b = Number(coreB.value||0);
    store.set('coreParams', { a, b });
  });
  $('#coreCalc')?.addEventListener('click', () => {
    const a = Number(coreA.value||0), b = Number(coreB.value||0), x = Number(coreX.value||0);
    const y = a*x + b;
    coreY.textContent = `y = ${y}`;
  });
});
