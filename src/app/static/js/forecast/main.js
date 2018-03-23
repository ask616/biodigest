function renderCharts(outData) {
  const ctx = document.getElementById("myChart").getContext('2d');
  console.log(outData);
  const stackedLine = new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [{
        data: outData.ys
      }],
      labels: outData.xs
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
