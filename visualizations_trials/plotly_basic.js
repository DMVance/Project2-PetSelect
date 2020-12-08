// To do list:
// 1. connect to the project database
// 2. figure out the Breed selector and COUNT of Breed
// 3. figure out the x-axis (sex, age, color, type, condition)
// 4. figure out the COUNT of y-axis
// plotly bar plot for dog age??


// plotly bar plot for dog sex

var xSex = ['Male', 'Female'];

var ySex = [533, 430];

var trace1 = {
  x: xSex,
  y: ySex,
  type: 'bar',
  text: ySex.map(String),
  textposition: 'auto',
  hoverinfo: 'none',
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.6,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
};

var dataSex = [trace1];

var layoutSex = {
  title: 'Count of Dogs by Sex',
  barmode: 'stack'
};

Plotly.newPlot('myPlotSex', dataSex, layoutSex);



// plotly bar plot for top 5 dog color
var xColor = ['Black', 'Brown', 'White', 'Tan', 'Brown Brindle'];

var yColor = [267, 162, 138, 124, 49];

var trace2 = {
  x: xColor,
  y: yColor,
  type: 'bar',
  text: yColor.map(String),
  textposition: 'auto',
  hoverinfo: 'none',
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.6,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
};

var dataColor = [trace2];

var layoutColor = {
  title: 'Count of Dogs by Color',
  barmode: 'stack'
};

Plotly.newPlot('myPlotColor', dataColor, layoutColor);


// plotly bar plot for dog type
var xType = ['Stray', 'Owner Surrender', 'Public Assist', 'Abandoned'];

var yType = [678, 223, 73, 15];

var trace3 = {
  x: xType,
  y: yType,
  type: 'bar',
  text: yType.map(String),
  textposition: 'auto',
  hoverinfo: 'none',
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.6,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
};

var dataType = [trace3];

var layoutType = {
  title: 'Count of Dogs by Type',
  barmode: 'stack'
};

Plotly.newPlot('myPlotType', dataType, layoutType);



// plotly bar plot for condition
var xCondition = ['Normal', 'Sick'];

var yCondition = [842, 138];

var trace4 = {
  x: xCondition,
  y: yCondition,
  type: 'bar',
  text: yCondition.map(String),
  textposition: 'auto',
  hoverinfo: 'none',
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.6,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
};

var dataCondition = [trace4];

var layoutCondition = {
  title: 'Count of Dogs by Condition',
  barmode: 'stack'
};

Plotly.newPlot('myPlotCondition', dataCondition, layoutCondition);



