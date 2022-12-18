// data values
const data = {
  labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
  datasets: [
    {
      label: "# of Votes",
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1,
    },
  ],
};

// configurations
const config = {
  type: "bar",
  data,
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  },
};

// chart display
const barChart = new Chart(
    document.getElementById("bar-chart"),
    config
);

// PapaParse, converts to object (JSON)
const aceInfo = [];
const acsfInfo = [];
const legacyInfo = [];
const labels = [];

const upload = document.getElementById("upload").addEventListener('click', () =>{
    Papa.parse(document.getElementById('document').files[0], {
        download: true,
        header: true,
        skipEmptyLines: true,
        complete: function(results){
            
            // for each of the vals within the csv
            for (i=0; i < results.data.length; i++){
                aceInfo.push(results.data[i].ACE);
                acsfInfo.push(results.data[i].ACSF);
                legacyInfo.push(results.data[i].Legacy);
                labels.push(results.data[i].id);
            } 
        }
    });
});

// update chart based on uploaded values
function updateChart(label){

    // shows row numbers (x-axis)
    barChart.data.labels = labels;

    // change title onclick
    barChart.data.datasets[0].label = label;

    if (label === 'aceInfo'){
        barChart.data.datasets[0].data = aceInfo;
    }
    if (label === 'acsfInfo'){
        barChart.data.datasets[0].data = acsfInfo;
    }
    if (label === 'legacyInfo'){
        barChart.data.datasets[0].data = legacyInfo;
    }
    barChart.update()
};