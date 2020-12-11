// Plot#1: Connect to json data for dog breed 
 d3.json("pet_select.json").then((data) => {
    // console.log(data)
  
    // Create plotly bar plot for dog breed; extract list of dog breed from json dataset
    var breed_data = data[0].primary_breed;
    console.log(breed_data);
    var breed_data_clean = Object.values(breed_data);
    console.log(breed_data_clean);    
  
    // Calculate count by breed
  let occurrences_breed = { };
  for (var i = 0, j = breed_data_clean.length; i < j; i++) {
    occurrences_breed[breed_data_clean[i]] = (occurrences_breed[breed_data_clean[i]] || 0) + 1;
  }
    console.log(occurrences_breed);     
    
  
  var trace1 = {
    x: Object.keys(occurrences_breed),
    y: Object.values(occurrences_breed),
    type: 'bar',
    };  
  
  
  var dataBreed = [trace1];
  
  var layoutBreed = {
    title: 'Count of Dogs by Breed',
    };
  
  Plotly.newPlot('myPlotBreed', dataBreed, layoutBreed);
  ///// THIS }) below is necessary to read data
  });
  
  
// Plot#2: Connect to json data for dog sex
  d3.json("pet_select.json").then((data) => {
    // console.log(data)
  
    // Create plotly bar plot for dog sex; extract list of dog sex from json dataset
    var sex_data = data[0].sex;
    console.log(sex_data);
    var sex_data_clean = Object.values(sex_data);
    console.log(sex_data_clean);
     
    // Calculate count by sex
  let occurrences_sex = { };
  for (var i = 0, j = sex_data_clean.length; i < j; i++) {
     occurrences_sex[sex_data_clean[i]] = (occurrences_sex[sex_data_clean[i]] || 0) + 1;
  }
    console.log(occurrences_sex);    
   
  
  var trace2 = {
    x: Object.keys(occurrences_sex),
    y: Object.values(occurrences_sex),
    type: 'bar',
    };  
  
  
  var dataSex = [trace2];
  
  var layoutSex = {
    title: 'Count of Dogs by Sex',
    };
  
  Plotly.newPlot('myPlotSex', dataSex, layoutSex);
  ///// THIS }) below is necessary to read data
  });
  
  
  // Plot#3: Connect to json data for dog age
  d3.json("pet_select.json").then((data) => {
    // console.log(data)
  
    // Create plotly bar plot for dog age; extract list of dog age from json dataset
    var age_data = data[0].age_years;
    console.log(age_data);
    var age_data_clean = Object.values(age_data);
    console.log(age_data_clean);
   
  
    // Calculate count by age
  let occurrences_age = { };
  for (var i = 0, j = age_data_clean.length; i < j; i++) {
     occurrences_age[age_data_clean[i]] = (occurrences_age[age_data_clean[i]] || 0) + 1;
  }
    console.log(occurrences_age);     
    
  
  var trace3 = {
    x: Object.keys(occurrences_age),
    y: Object.values(occurrences_age),
    type: 'bar',
    };  
  
  
  var dataAge = [trace3];
  
  var layoutAge = {
    title: 'Count of Dogs by Age(Year)',
     };
  
  Plotly.newPlot('myPlotAge', dataAge, layoutAge);
  ///// THIS }) below is necessary to read data
  });
  
  
  
  // Plot#4: Connect to json data for dog color
  d3.json("pet_select.json").then((data) => {
    // console.log(data)  
  
    // Create plotly bar plot for dog condition; extract list of dog condition from json dataset
    var color_data = data[0].primary_color;
    console.log(color_data);
    var color_data_clean = Object.values(color_data);
    console.log(color_data_clean);
      
    // Calculate count by color
  let occurrences_color = { };
  for (var i = 0, j = color_data_clean.length; i < j; i++) {
     occurrences_color[color_data_clean[i]] = (occurrences_color[color_data_clean[i]] || 0) + 1;
  }
    console.log(occurrences_color); 
    
    
  var trace4 = {
    x: Object.keys(occurrences_color),
    y: Object.values(occurrences_color),
    type: 'bar',
    };  
  
  
  var dataColor = [trace4];
  
  var layoutColor = {
    title: 'Count of Dogs by Color',
    };
  
  Plotly.newPlot('myPlotColor', dataColor, layoutColor);
  ///// THIS }) below is necessary to read data
  });
  
  
  // Plot#5: Connect to json data for dog type
  d3.json("pet_select.json").then((data) => {
    // console.log(data)  
  
    // Create plotly bar plot for dog type; extract list of dog type from json dataset
    var type_data = data[0].intake_type;
    console.log(type_data);
    var type_data_clean = Object.values(type_data);
    console.log(type_data_clean);
   
  
    
    // Calculate count by type
  let occurrences_type = { };
  for (var i = 0, j = type_data_clean.length; i < j; i++) {
     occurrences_type[type_data_clean[i]] = (occurrences_type[type_data_clean[i]] || 0) + 1;
  }
    console.log(occurrences_type);     
    
  
  var trace5 = {
    x: Object.keys(occurrences_type),
    y: Object.values(occurrences_type),
    type: 'bar',
    };  
  
  
  var dataType = [trace5];
  
  var layoutType = {
    title: 'Count of Dogs by Type',
    // barmode: 'stack'
  };
  
  Plotly.newPlot('myPlotType', dataType, layoutType);
  ///// THIS }) below is necessary to read data
  });
  
  
  
  // Plot#6: Connect to json data for dog condition
  d3.json("pet_select.json").then((data) => {
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
    
  
  var trace6 = {
    x: Object.keys(occurrences_condition),
    y: Object.values(occurrences_condition),
    type: 'bar',    
    };  
  
  
  var dataCondition = [trace6];
  
  var layoutCondition = {
    title: 'Count of Dogs by Condition',    
  };
  
  Plotly.newPlot('myPlotCondition', dataCondition, layoutCondition);
  ///// THIS }) below is necessary to read data
  });