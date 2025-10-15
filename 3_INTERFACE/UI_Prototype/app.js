// Placeholder - integracja z Pythonem wymaga backendu (np. Flask)
document.getElementById('phase-display').textContent = "Faza: Punkt 0";
fetch('/api/recommendations') // Przykładowe API
    .then(response => response.json())
    .then(data => {
        const recs = document.getElementById('recommendations');
        data.forEach(rec => {
            recs.innerHTML += `<p>${rec.scenario.goal}: ${rec.probability.toFixed(2)}</p>`;
        });
    })
    .catch(error => console.error('Błąd:', error));

    