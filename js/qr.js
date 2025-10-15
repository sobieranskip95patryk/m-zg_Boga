// QR code module
document.addEventListener('DOMContentLoaded', () => {
  const qrUrl = $('#qrUrl');
  const qrWrap = $('#qrCanvasWrap');

  const makeQR = async (url) => {
    qrWrap.innerHTML = '';
    const canvas = document.createElement('canvas');
    qrWrap.appendChild(canvas);
    await QRCode.toCanvas(canvas, url, { width: 220, margin: 1 });
    canvas.id = 'qrCanvas';
  };

  $('#qrUseHere')?.addEventListener('click', () => { qrUrl.value = location.href; });
  $('#qrMake')?.addEventListener('click', () => makeQR(qrUrl.value || location.href));
  $('#qrDownload')?.addEventListener('click', () => {
    const c = $('#qrCanvas');
    if (!c) return;
    const link = document.createElement('a');
    link.download = 'PinkManAI_QR.png';
    link.href = c.toDataURL('image/png');
    link.click();
  });

  qrUrl.value = location.href;
  makeQR(qrUrl.value);
});
