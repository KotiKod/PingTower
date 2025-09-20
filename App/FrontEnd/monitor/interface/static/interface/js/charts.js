let responseTimeChart = null;

function initChart() {
    const ctx = document.getElementById('responseTimeChart').getContext('2d');

    responseTimeChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: 'Время ответа (мс)',
                data: [],
                borderColor: '#3498db',
                backgroundColor: 'rgba(52, 152, 219, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Миллисекунды'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Время'
                    }
                }
            }
        }
    });
}

function updateChartData(siteData) {
    if (!responseTimeChart) return;

    // Очищаем старые данные
    responseTimeChart.data.labels = [];
    responseTimeChart.data.datasets[0].data = [];

    // Добавляем новые данные (заглушка)
    responseTimeChart.data.labels = ['10:00', '10:05', '10:10', '10:15'];
    responseTimeChart.data.datasets[0].data = [120, 150, 90, 180];

    responseTimeChart.update();
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', initChart);