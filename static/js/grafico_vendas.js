const labelsJSON = JSON.parse(document.getElementById('labels').textContent);
const dataJSON = JSON.parse(document.getElementById('data').textContent);

const ctx = document.getElementById('vendasPorMesChart').getContext('2d');
const vendasChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labelsJSON,
        datasets: [{
            label: 'Vendas',
            data: dataJSON,
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});