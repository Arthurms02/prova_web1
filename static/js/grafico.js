
const labelsJSON = JSON.parse(document.getElementById('labels').textContent);
const dataJSON = JSON.parse(document.getElementById('data').textContent);
const labelsJSON2 = JSON.parse(document.getElementById('labels_produtos').textContent);
const dataJSON2 = JSON.parse(document.getElementById('data_produtos').textContent);

const ctx = document.getElementById('vendasPorMesChart').getContext('2d');
const ctx2 = document.getElementById('grafico-bar').getContext('2d');

const meuGrafico = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labelsJSON,
        datasets: [{
            label: 'Vendas Mensais',
            data: dataJSON,
            backgroundColor: 'rgba(54, 162, 235, 0.6)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const meuGrafico2 = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: labelsJSON2,
        datasets: [{
            label: 'Total de venda do produto',
            data: dataJSON2,
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