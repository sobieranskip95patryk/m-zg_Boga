// Helpers + localStorage wrapper
window.$ = (s, p=document) => p.querySelector(s);
window.$$ = (s, p=document) => Array.from(p.querySelectorAll(s));
window.store = {
  get: (k, d=null) => { try { return JSON.parse(localStorage.getItem(k)) ?? d } catch { return d } },
  set: (k, v) => localStorage.setItem(k, JSON.stringify(v))
};
