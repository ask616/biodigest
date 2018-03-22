function renderCharts(data) {
  const ctx = document.getElementById("myChart").getContext('2d');
  const stackedLine = new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [{
        data: _.values(data)
      }],
      labels: _.keys(data)
    },
    options: {
      scales: {
        yAxes: [{
          stacked: true
        }]
      }
    }
  });
};
