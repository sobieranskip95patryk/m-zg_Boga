// main.js – logika GlobalVision

// Przykładowa funkcja: generowanie mapy i integracja z pipeline GOK:AI
function renderGlobalMap(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;
    container.innerHTML = `<div class="globalvision-map" style="width:100%;height:400px;background:#e0e0e0;border-radius:10px;display:flex;align-items:center;justify-content:center;">
        <span style="font-size:2em;color:#1E90FF;">Mapa GlobalVision (placeholder)</span>
    </div>`;
}

// Przykład integracji z pipeline GOK:AI
function updateGlobalStatus(data) {
    // data: { phase, matrix, energy, probability }
    const statusPanel = document.getElementById('globalvision-status');
    if (!statusPanel) return;
    statusPanel.innerHTML = `<b>GlobalVision Status:</b><br>
        Faza: ${data.phase}<br>
        Matryca: ${data.matrix}<br>
        Energia: ${data.energy}<br>
        P(S): ${data.probability}`;
}

// Inicjalizacja po załadowaniu strony
window.addEventListener('DOMContentLoaded', () => {
    renderGlobalMap('globalvision-map-container');
});
