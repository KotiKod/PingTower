// Глобальные переменные
let responseTimeChart = null;
const testData = {
    'example.com': {
        data: [120, 150, 130, 140, 160, 125, 135],
        status: 'Работает',
        avgTime: 145,
        lastCheck: '2 минуты назад'
    },
    'google.com': {
        data: [80, 75, 85, 90, 78, 82, 88],
        status: 'Работает',
        avgTime: 82,
        lastCheck: '1 минуту назад'
    },
    'github.com': {
        data: [200, 180, 190, 210, 195, 185, 205],
        status: 'Работает',
        avgTime: 195,
        lastCheck: '3 минуты назад'
    },
    'yandex.ru': {
        data: [100, 95, 110, 105, 98, 102, 108],
        status: 'Работает',
        avgTime: 102,
        lastCheck: '5 минут назад'
    },
    'stackoverflow.com': {
        data: [150, 145, 160, 155, 148, 152, 158],
        status: 'Работает',
        avgTime: 152,
        lastCheck: '4 минуты назад'
    }
};

const testLabels = ['10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30'];

// Инициализация графика
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
                fill: true,
                borderWidth: 2
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
                        text: 'Миллисекунды',
                        color: '#2c3e50',
                        font: {
                            weight: 'bold'
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Время проверки',
                        color: '#2c3e50',
                        font: {
                            weight: 'bold'
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                }
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 14
                        }
                    }
                }
            }
        }
    });
}

// Обновление данных графика
function updateChartData(siteName) {
    if (!responseTimeChart) return;

    const siteInfo = testData[siteName] || {};

    // Обновляем данные графика
    responseTimeChart.data.labels = testLabels;
    responseTimeChart.data.datasets[0].data = siteInfo.data || [];
    responseTimeChart.data.datasets[0].label = `Время ответа - ${siteName}`;

    responseTimeChart.update();

    // Обновляем информацию о сайте
    updateSiteDetails(siteName, siteInfo);
}

// Обновление информации о сайте
function updateSiteDetails(siteName, siteInfo) {
    const statusClass = siteInfo.status === 'Работает' ? 'bg-success' : 'bg-danger';

    document.getElementById('site-details').innerHTML = `
        <h2>${siteName}</h2>
        <div class="mt-4">
            <p>Статистика доступности и времени ответа</p>
            <p>Статус: <span class="badge ${statusClass} status-badge">${siteInfo.status}</span></p>
            <p>Среднее время ответа: ${siteInfo.avgTime || 0} мс</p>
            <p>Последняя проверка: ${siteInfo.lastCheck || 'Неизвестно'}</p>
        </div>
    `;
}

// Обработчик кликов по элементам списка
function setupSiteItemListeners() {
    document.querySelectorAll('.site-item').forEach(item => {
        item.addEventListener('click', function() {
            // Убираем активный класс у всех элементов
            document.querySelectorAll('.site-item').forEach(el => {
                el.classList.remove('active');
            });

            // Добавляем активный класс к выбранному элементу
            this.classList.add('active');

            // Получаем название сайта
            const siteName = this.getAttribute('data-site');

            // Обновляем график и информацию
            updateChartData(siteName);
        });
    });
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    initChart();
    setupSiteItemListeners();

    // Автоматически выбираем первый сайт
    const firstSite = document.querySelector('.site-item');
    if (firstSite) {
        firstSite.click();
    }
});

// Функции для реального использования (заглушки)
function fetchRealData(siteName) {
    // Здесь будет запрос к API
    console.log('Запрос данных для:', siteName);
    return Promise.resolve(testData[siteName]);
}

function setupWebSocketConnection() {
    // Здесь будет подключение WebSocket
    console.log('WebSocket подключение установлено');
}