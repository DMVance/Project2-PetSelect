// To do list:
// 1. connect to the project database
// 2. figure out the Breed selector and COUNT of Breed
// 3. figure out the x-axis (sex, age, color, type, condition)
// 4. figure out the COUNT of y-axis
// plotly bar plot for dog age??


// Define function for Breed selector; unique 108 breeds
function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

// Connect to json data
d3.json("pet_select.json").then((data) => {
  console.log(data)

  // Extract list of breed from json data
  var breed_data = data[0].primary_breed;
  console.log(breed_data);
  var breed_data_clean = Object.values(breed_data);
  console.log(breed_data_clean);
  let unique= breed_data_clean.filter(onlyUnique);
  console.log(unique);

  // Assign list of breeds to dropdown
  var dropDown= d3.select("#selDataset");
  // dropDown.html("");
  unique.forEach((sample)=>{
    dropDown.append("option").text(sample).property("value", sample);
  });

});


// Connect to json data
d3.json("pet_select.json").then((data) => {
  // console.log(data)

  // Create plotly bar plot for dog sex; extract list of dog sex from json dataset
  var sex_data = data[0].sex;
  var sex_data_clean = Object.values(sex_data);
  console.log(sex_data_clean);
  // var occurrences= sex_data_clean.filter(x=>x == "Male").length;  //// This Works

  // Calculate count by sex
let occurrences = { };
for (var i = 0, j = sex_data_clean.length; i < j; i++) {
   occurrences[sex_data_clean[i]] = (occurrences[sex_data_clean[i]] || 0) + 1;
}
  console.log(occurrences); 
  
  // var xValues= Object.keys(occurrences);
  // console.log(xValues);

// var xSex = ['Male', 'Female'];
// // var ySex = [533, 430];


var trace1 = {
  x: Object.keys(occurrences),
  y: Object.values(occurrences),
  type: 'bar',
  // text: Object.values(occurrences).map(String),
  // textposition: 'auto',
  // hoverinfo: 'none',
  // marker: {
  //   color: 'rgb(158,202,225)',
  //   opacity: 0.6,
  //   line: {
  //     color: 'rgb(8,48,107)',
  //     width: 1.5
    };  


var dataSex = [trace1];

var layoutSex = {
  title: 'Count of Dogs by Sex',
  // barmode: 'stack'
};

Plotly.newPlot('myPlotSex', dataSex, layoutSex);
///// THIS }) below is necessary to read data
});



// // plotly bar plot for top 5 dog color
// var xColor = ['Black', 'Brown', 'White', 'Tan', 'Brown Brindle'];

// var yColor = [267, 162, 138, 124, 49];

// var trace2 = {
//   x: xColor,
//   y: yColor,
//   type: 'bar',
//   text: yColor.map(String),
//   textposition: 'auto',
//   hoverinfo: 'none',
//   marker: {
//     color: 'rgb(158,202,225)',
//     opacity: 0.6,
//     line: {
//       color: 'rgb(8,48,107)',
//       width: 1.5
//     }
//   }
// };

// var dataColor = [trace2];

// var layoutColor = {
//   title: 'Count of Dogs by Color',
//   barmode: 'stack'
// };

// Plotly.newPlot('myPlotColor', dataColor, layoutColor);


// // plotly bar plot for dog type
// var xType = ['Stray', 'Owner Surrender', 'Public Assist', 'Abandoned'];

// var yType = [678, 223, 73, 15];

// var trace3 = {
//   x: xType,
//   y: yType,
//   type: 'bar',
//   text: yType.map(String),
//   textposition: 'auto',
//   hoverinfo: 'none',
//   marker: {
//     color: 'rgb(158,202,225)',
//     opacity: 0.6,
//     line: {
//       color: 'rgb(8,48,107)',
//       width: 1.5
//     }
//   }
// };

// var dataType = [trace3];

// var layoutType = {
//   title: 'Count of Dogs by Type',
//   barmode: 'stack'
// };

// Plotly.newPlot('myPlotType', dataType, layoutType);



// // plotly bar plot for condition
// var xCondition = ['Normal', 'Sick'];

// var yCondition = [842, 138];

// var trace4 = {
//   x: xCondition,
//   y: yCondition,
//   type: 'bar',
//   text: yCondition.map(String),
//   textposition: 'auto',
//   hoverinfo: 'none',
//   marker: {
//     color: 'rgb(158,202,225)',
//     opacity: 0.6,
//     line: {
//       color: 'rgb(8,48,107)',
//       width: 1.5
//     }
//   }
// };

// var dataCondition = [trace4];

// var layoutCondition = {
//   title: 'Count of Dogs by Condition',
//   barmode: 'stack'
// };

// Plotly.newPlot('myPlotCondition', dataCondition, layoutCondition);



