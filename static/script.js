document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('fraudForm').addEventListener('submit', async function (e) {
        e.preventDefault();
        const formData = new FormData(e.target);
        const data = {};

        formData.forEach((value, key) => {
            data[key] = parseFloat(value);
        });

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById('result').innerHTML = `
            <h2>${result.prediction}</h2>
            <p>Fraud Probability: ${(result.probability * 100).toFixed(2)}%</p>
        `;
    });
});
