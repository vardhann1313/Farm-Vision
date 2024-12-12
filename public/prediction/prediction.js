const form = document.getElementById('predictionForm');

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const nitrogen = document.getElementById('nitrogen').value;
    const phosphorus = document.getElementById('phosphorus').value;
    const potassium = document.getElementById('potassium').value;
    const pH = document.getElementById('pH').value;
    const humidity = document.getElementById('humidity').value;
    const temperature = document.getElementById('temperature').value;
    const rainfall = document.getElementById('rainfall').value;

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nitrogen, phosphorus, potassium, pH, humidity, temperature, rainfall }),
    });

    const data = await response.json();
    document.getElementById('predictionResult').innerText = `Predicted Crop: ${data.prediction}`;
});
