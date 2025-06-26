// Utility for DOM selection
const $ = (sel) => document.querySelector(sel);

// Show result or error in a target element
function showResult(target, data, isImage = false, alt = 'Plot') {
    if (isImage && data instanceof Blob) {
        const url = URL.createObjectURL(data);
        target.innerHTML = `<img src="${url}" alt="${alt}">`;
    } else if (data.result !== undefined) {
        target.textContent = `Result: ${data.result}`;
    } else if (data.error) {
        target.textContent = `Error: ${data.error}`;
    } else {
        target.textContent = 'Unknown response.';
    }
}

// Basic Calculator
$('#basicForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const op = $('#basicOp').value;
    const x = parseFloat($('#basicX').value);
    const y = parseFloat($('#basicY').value);
    const resDiv = $('#basicResult');
    resDiv.textContent = 'Calculating...';
    try {
        const resp = await fetch('/calculate/basic', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operation: op, x, y })
        });
        const data = await resp.json();
        showResult(resDiv, data);
    } catch (err) {
        resDiv.textContent = 'Network error.';
    }
});

// Graphical Calculator (y = x^2)
$('#plotBtn').addEventListener('click', async () => {
    const plotDiv = $('#plotResult');
    plotDiv.textContent = 'Loading plot...';
    try {
        const resp = await fetch('/calculate/graphical', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ operation: 'plot_y_equals_x_squared' })
        });
        if (resp.ok) {
            const blob = await resp.blob();
            showResult(plotDiv, blob, true, 'y = x^2 plot');
        } else {
            const data = await resp.json();
            showResult(plotDiv, data);
        }
    } catch (err) {
        plotDiv.textContent = 'Network error.';
    }
});

// Advanced Graphical Calculator
$('#advGraphForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const formula = $('#formula').value;
    const plotDiv = $('#advPlotResult');
    plotDiv.textContent = 'Loading plot...';
    try {
        const resp = await fetch('/calculate/graphical/plot', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ formula })
        });
        if (resp.ok) {
            const blob = await resp.blob();
            showResult(plotDiv, blob, true, 'Custom plot');
        } else {
            const data = await resp.json();
            showResult(plotDiv, data);
        }
    } catch (err) {
        plotDiv.textContent = 'Network error.';
    }
});
