// To do list:
// 1. connect to the project database
// 2. figure out the Breed selector and COUNT of Breed
// 3. figure out the x-axis (sex, age, color, type, condition)
// 4. figure out the COUNT of y-axis
// plotly bar plot for dog age??

// 5. use onlyUnique function in right location to filter dropdown
// 6. use indexOf on first list, then ...?
// 7. Correctly send filtered list of dogs to populate_charts
// 8. Add a value to subjectID
// 9. use reduce to group by breed
// 10. Order breeds in dropdown in alphabetical order
// 11. Get data directly from MongoDB rather than .json?
// 12. After filtering to specific breed, return to plots showing data for all breeds

console.log("Good Morning, World!")

let subjectID = "Basset Hound"

// Connect to json data and create initial plots
function init_build() {
  d3.json("static/pet_select.json").then(
      data => {
          // Extract list of breed from json data
          var breed_data = data[0].primary_breed;
          console.log(breed_data);

          var breed_data_clean = Object.values(breed_data);
          console.log(breed_data_clean);

          let unique = breed_data_clean.filter(onlyUnique);
          console.log(unique);
          let unique_sorted = unique.sort(); // works for strings or only for numbers?
          console.log(unique_sorted);

          // Assign list of breeds to dropdown
          var dropDown = d3.select("#selDataset");
          unique_sorted.forEach((breed) => {
            dropDown.append("option").text(breed).property("value", breed);
          })

          console.log(data)
          populate_charts(data)
          let choose_subject = d3.select("#selDataset")
          let breeds = Object.values(data[0].primary_breed)
          console.log(breeds)
          unique.forEach((breed) => {
              choose_subject.append("option").attr("value", breed).text(breed)
          })
          return ""
      })
  }

// Define function for Breed selector; unique 108 breeds
function onlyUnique(value, index, self) {
  return self.indexOf(value) === index;
}

// d3.json("pet_select.json").then(
//   data => {
//     // Extract list of breed from json data
//     var breed_data = data[0].primary_breed;
//     console.log(breed_data);
//     var breed_data_clean = Object.values(breed_data);
//     console.log(breed_data_clean);
//     let unique= breed_data_clean.filter(onlyUnique);
//     console.log(unique);

//     // Assign list of breeds to dropdown
//     var dropDown= d3.select("#selDataset");
//     // dropDown.html("");
//     unique.forEach((sample) => {
//       dropDown.append("option").text(sample).property("value", sample);
//     });
//   })

function populate_charts(data) {
    // Plot#1: Connect to json data for dog sex **How to do this with data passed through "data" variable?**
    // d3.json("static/pet_select.json").then((data) => {
    //   console.log(data)

    // Create plotly bar plot for dog sex; extract list of dog sex from json dataset
    var sex_data = data[0].sex;
    console.log(sex_data);
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
    // });


    // Plot#2: Connect to json data for dog age
    d3.json("static/pet_select.json").then((data) => {
      // console.log(data)

      // Create plotly bar plot for dog sex; extract list of dog sex from json dataset
      var age_data = data[0].age_years;
      console.log(age_data);
      var age_data_clean = Object.values(age_data);
      console.log(age_data_clean);
      // var occurrences= sex_data_clean.filter(x=>x == "Male").length;  //// This Works

      // Calculate count by sex
    let occurrences_age = { };
    for (var i = 0, j = age_data_clean.length; i < j; i++) {
      occurrences_age[age_data_clean[i]] = (occurrences_age[age_data_clean[i]] || 0) + 1;
    }
      console.log(occurrences_age); 
      
      // var xValues= Object.keys(occurrences);
      // console.log(xValues);

    // var xSex = ['Male', 'Female'];
    // // var ySex = [533, 430];

    var trace2 = {
      x: Object.keys(occurrences_age),
      y: Object.values(occurrences_age),
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


    var dataAge = [trace2];

    var layoutAge = {
      title: 'Count of Dogs by Age(Year)',
      // barmode: 'stack'
    };

    Plotly.newPlot('myPlotAge', dataAge, layoutAge);
    ///// THIS }) below is necessary to read data
    });


    // Plot#3: Connect to json data for dog color
    d3.json("static/pet_select.json").then((data) => {
      // console.log(data)  

      // Create plotly bar plot for dog condition; extract list of dog condition from json dataset
      var color_data = data[0].primary_color;
      console.log(color_data);
      var color_data_clean = Object.values(color_data);
      console.log(color_data_clean);
      // var occurrences= sex_data_clean.filter(x=>x == "Male").length;  //// This Works

      // Calculate count by color
    let occurrences_color = { };
    for (var i = 0, j = color_data_clean.length; i < j; i++) {
      occurrences_color[color_data_clean[i]] = (occurrences_color[color_data_clean[i]] || 0) + 1;
    }
      console.log(occurrences_color); 
      
      // var xValues_type= Object.keys(occurrences_type);
      // console.log(xValues_type);

    var trace3 = {
      x: Object.keys(occurrences_color),
      y: Object.values(occurrences_color),
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


    var dataColor = [trace3];

    var layoutColor = {
      title: 'Count of Dogs by Color',
      // barmode: 'stack'
    };

    Plotly.newPlot('myPlotColor', dataColor, layoutColor);
    ///// THIS }) below is necessary to read data
    });


    // Plot#4: Connect to json data for dog type
    d3.json("static/pet_select.json").then((data) => {
      // console.log(data)  

      // Create plotly bar plot for dog type; extract list of dog type from json dataset
      var type_data = data[0].intake_type;
      console.log(type_data);
      var type_data_clean = Object.values(type_data);
      console.log(type_data_clean);
      // var occurrences= sex_data_clean.filter(x=>x == "Male").length;  //// This Works

      
      // Calculate count by type
    let occurrences_type = { };
    for (var i = 0, j = type_data_clean.length; i < j; i++) {
      occurrences_type[type_data_clean[i]] = (occurrences_type[type_data_clean[i]] || 0) + 1;
    }
      console.log(occurrences_type); 
      
      // var xValues_type= Object.keys(occurrences_type);
      // console.log(xValues_type);

    var trace4 = {
      x: Object.keys(occurrences_type),
      y: Object.values(occurrences_type),
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


    var dataType = [trace4];

    var layoutType = {
      title: 'Count of Dogs by Type',
      // barmode: 'stack'
    };

    Plotly.newPlot('myPlotType', dataType, layoutType);
    ///// THIS }) below is necessary to read data
    });



    // Plot#5: Connect to json data for dog condition
    d3.json("static/pet_select.json").then((data) => {
      // console.log(data)  

      // Create plotly bar plot for dog condition; extract list of dog condition from json dataset
      var condition_data = data[0].intake_condition;
      console.log(condition_data);
      var condition_data_clean = Object.values(condition_data);
      console.log(condition_data_clean);
      // var occurrences= sex_data_clean.filter(x=>x == "Male").length;  //// This Works

      // Calculate count by condition
    let occurrences_condition = { };
    for (var i = 0, j = condition_data_clean.length; i < j; i++) {
      occurrences_condition[condition_data_clean[i]] = (occurrences_condition[condition_data_clean[i]] || 0) + 1;
    }
      console.log(occurrences_condition); 
      
      // var xValues_type= Object.keys(occurrences_type);
      // console.log(xValues_type);

    var trace5 = {
      x: Object.keys(occurrences_condition),
      y: Object.values(occurrences_condition),
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


    var dataCondition = [trace5];

    var layoutCondition = {
      title: 'Count of Dogs by Condition',
      // barmode: 'stack'
    };

    Plotly.newPlot('myPlotCondition', dataCondition, layoutCondition);
    ///// THIS }) below is necessary to read data
      });
    return ""
    // })
}

function clear_all() {
  d3.select("#bar").html("")
}

init_build()

d3.select("#selDataset")
    .on("change", function() {
        // let selection = d3.select(this).property("value")
      // var dataset = dropdownMenu.property("value");
        // console.log(selection)
        clear_all()
        // need to select from .json only those records with the breed selection using a filter or reduce function
        // I think I have a scoping issue here...
        d3.json("static/pet_select.json").then(
          data => {
              let filtered_data = data.filter(function (e) {
              let selection = d3.select(this).property("value")
              populate_charts(filtered_data)
              return e.primary_breed === selection;
           });
          // populate_charts(filtered_data)
        })
    })

console.log("Good Night, World!")

// data[0].primary_breed








  







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



