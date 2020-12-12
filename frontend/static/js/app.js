function smoothScroll(target,duration,targetPosition){
    target = document.querySelector(target);
    // let targetPosition = 1550;
    console.log(targetPosition)
    // let startPosition = 0;
    let startPosition = window.pageYOffset;
    // let startPosition = documment.getElementById("clickMe2");

    let distance = targetPosition - startPosition;
    let startTime = null;   

    function animation(currentTime){
        if(startTime === null) startTime = currentTime;
        let timeElapsed = currentTime - startTime;
        let run = ease(timeElapsed,startPosition,distance,duration)
        window.scrollTo(0,run);
        if(timeElapsed < duration) requestAnimationFrame(animation);
    }

    function ease(t,b,c,d){
        t /= d/2;
	    if (t < 1) return c/2*t*t + b;
	    t--;
	    return -c/2 * (t*(t-2) - 1) + b;
        }

    requestAnimationFrame(animation);
}

//  ******************************************** weight to traits listener event ************************
let traitsList

document.getElementById("clickMe").addEventListener("click", function()
{
    console.log("weight-button-clicked")

    clear_chars = d3.select("#characteristics")
    d3.selectAll(clear_chars._groups[0][0].childNodes).remove()

    // document.getElementById("#characteristics").selectAll("li").remove()
    const box1=document.getElementById("characteristic-box");
        if(box1.style.display=="none")
        {
            box1.style.display="block";
        }
        else if (box1.style.display=="block")
        {
            document.getElementById("#characteristics").html('')
        }
        

        else
        {
            box1.style.display=="none";
        }
    })

// ******************************************** load list of characteristics as checkboxes based on selected weight ************************ 
function loadChar() {

    charList = d3.select(".characteristics")
    let selected_size
    let options = d3.select("#size").selectAll("option")
    options.each(function (d, i) 
    {
        let current_option = d3.select(this)
        if (current_option.property("selected")) 
        {
            selected_size = current_option._groups[0][0].value
        }
    })
    console.log(selected_size)


    // Reynolds Note
    // This line takes the size the user selected, e.g. "large"
    // and concatenates the string "_traits" to it
    // then assigns the "large_traits" array
    // to the array that will be used below
    // This prevents having to use an if statement
    // to assign the "large_traits" "medium_traits" or "small_traits" 
    // arrays to the code below
    traitsForDogSize = eval(selected_size+"_traits")


    let traitsList = Object.keys(traitsForDogSize[0])
    .forEach(trait => {
        listItem = charList.append("li")
            .classed("char-columns", true)
        listItem.append("input")
            .attr("type", "checkbox")
            .attr("id", trait)
            .attr("id", "check")
            .attr("name", trait)
            .attr("value", trait)
            .attr("class", "checkmark")
                
        listItem.append("label")
            .attr("for", trait)
            
            .text("  " + trait)
    })
    console.log(options)
        // document.getElementById("#characterstic-list").selectAll("li").remove()

}


//  ******************************************** traits to breeds listener event ************************
document.getElementById("clickMe2").addEventListener("click", function()
{
    let targetPosition = 2000;

    console.log("trait-clicked")
    smoothScroll(".breed-results", 1500, 1000);
    const box2=document.getElementById("breed-results");
        if(box2.style.display=="none")
        {
            box2.style.display="block";
        }
        else
        {
            box2.style.display=="none";
        }    
    
    })


//  ******************************************** find & display breeds based on selected characteristics ************************
function loadBreeds() {
        // ---vvv---Reynolds code---vvv---
    let selected_boxes = []
    let boxes = d3.selectAll("input")
    boxes.each(function (d, i) {
                // console.log(d3.select(this).property("checked"))
            let current_box = d3.select(this)
            if (current_box.property("checked")) {
                    selected_boxes.push(current_box._groups[0][0].name)
            } 
    })
    console.log(selected_boxes)

    let selected_size
    let options = d3.select("#size").selectAll("option")
    options.each(function (d, i) {
            let current_option = d3.select(this)
            if (current_option.property("selected")) {
                    selected_size = current_option._groups[0][0].value
            }
    })
    console.log(selected_size)

    var entry = {
            traits: selected_boxes,
            size: selected_size
    } 

    fetch(`${window.origin}/findapup/create-entry`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry), 
        cache: "no-cache",
        headers: new Headers({
                "content-type": "application/json"
        })
        })
        .then(function (response) {
                if (response.status !== 200) {
                console.log(`Looks like there was a problem. Status code: ${response.status}`);
                return;
                }
                response.json().then(function (data) {
                console.log(data)
                
                let clear_results = d3.select("#breed-results").select("ul")
                // console.log(`Breed results has child nodes? ${clear_results._groups[0][0].hasChildNodes()}`)
                // console.log("clear_results #breed-results ul selection:")
                // console.log(clear_results)
                if (clear_results._groups[0][0].hasChildNodes()) {
                    clear_results.selectAll("li").remove()
                    // console.log(`Now does it have child nodes? ${clear_results._groups[0][0].hasChildNodes()}`)
                    // console.log("clear_results #breed-results ul selection:")
                    // console.log(clear_results)
                }

                let results = d3.select("#breed-results").select("ul")
                for (i in data) {
                        console.log(data[i])
                        results.append("li").text(data[i])
                        }
                });
        })
        .catch(function (error) {
                console.log("Fetch error: " + error);
        })

}              


//  ******************************************** breeds to dogs listener event ************************
document.getElementById("clickMe3").addEventListener("click", function()
{
    console.log("breed-clicked")
    
    smoothScroll(".dog-results", 1500, 1800)

    const box3=document.getElementById("dog-results");
        if(box3.style.display=="none")
        {
            box3.style.display="block";
        }
        else
        {
            box3.style.display=="none";
        } 
    })


//  ******************************************** find & display dogs based on search inputs ************************
function loadDogs() {
    console.log("loadDogs")

    let selected_breed = d3.select("#breed-text").property("value")
    console.log(selected_breed)


    let selected_sexes = []
    let sexes = d3.select("#sexes").selectAll("input")
    sexes.each(function (d, i) {
                // console.log(d3.select(this).property("checked"))
            let current_sex = d3.select(this)
            if (current_sex.property("checked")) {
                    selected_sexes.push(current_sex.property("value"))
            } 
    })

    let sex
    if (selected_sexes.length === 0) {
        sex = ""
    } else if (selected_sexes.length === 2) {
        sex = ""
    } else if (selected_sexes[0] === "female") {
        sex = "female"
    } else {
        sex = "male"
    }
    console.log(sex)


    let selected_color
    let options = d3.select("#colors").selectAll("option")
    options.each(function (d, i) {
            let current_option = d3.select(this)
            if (current_option.property("selected")) {
                selected_color = current_option.property("value")
            }
    })
    console.log(selected_color)

    let young_yrs
    if (Number.isInteger(parseInt(d3.select("#youngest-years").property("value")))) {
        young_yrs = parseInt(d3.select("#youngest-years").property("value"))
    } else {
        young_yrs = 0
    }
    let young_mos
    if (Number.isInteger(parseInt(d3.select("#youngest-months").property("value")))) {
        young_mos = parseInt(d3.select("#youngest-months").property("value"))
    } else {
        young_mos = 0
    }
    let old_yrs
    if (Number.isInteger(parseInt(d3.select("#oldest-years").property("value")))) {
        old_yrs = parseInt(d3.select("#oldest-years").property("value"))
    } else {
        old_yrs = 99
    }
    let old_mos
    if (Number.isInteger(parseInt(d3.select("#oldest-months").property("value")))) {
        old_mos = parseInt(d3.select("#oldest-months").property("value"))
    } else {
        old_mos = 12
    }


    let select_injured
    if (d3.select("#injured").property("checked")) {
        select_injured = true
    } else {
        select_injured = false
    }
    console.log(select_injured)


    var entry = {
        search_breed: selected_breed,
        youngest_yrs: young_yrs,
        youngest_mos: young_mos,
        oldest_yrs: old_yrs,
        oldest_mos: old_mos,
        search_sex: sex,
        search_color: selected_color,
        search_injured: select_injured,
    }

    fetch(`${window.origin}/findapup/mongo-query`, {
        method: "POST",
        credentials: "include",
        body: JSON.stringify(entry), 
        cache: "no-cache",
        headers: new Headers({
                "content-type": "application/json"
        })
        })
        .then(function (response) {
                if (response.status !== 200) 
                {
                    console.log(`Looks like there was a problem. Status code: ${response.status}`);
                    return;
                }
                console.log(response)
                response.json().then(function (data) 
                {
                    console.log(data)
                    columns = [
                        "name", 
                        "sex",
                        "primary_breed", 
                        "secondary_breed", 
                        "primary_color", 
                        "secondary_color", 
                        "age_years", 
                        "age_months", 
                        "age_days", 
                        "intake_condition"
                        ]
                    column_names = [
                        "Name", 
                        "Male/Female",
                        "Primary breed", 
                        "...mixed with", 
                        "Primary color", 
                        "...and", 
                        "Years old", 
                        "Months old", 
                        "Days old", 
                        "Health"
                    ]
                    tabulate(data, columns, column_names, "#dog-results-table")
                })
            })
        .catch(function (error) {
                console.log("Fetch error: " + error);
            })
    
}              


//  ******************************************** create table from json ************************
function tabulate(data, columns, column_names, divName) {
    if (d3.select("#current-table")) {
        d3.select("#current-table").remove()
    }
    // if (deleteDiv._groups[0][0]) {
    //     d3.selectAll(deleteDiv._groups[0][0].childNodes).remove()
    // }

    var table = d3.select(divName).append('table').attr("id", "current-table")
    var thead = table.append('thead')
    var	tbody = table.append('tbody');

    // append the header row
    thead.append('tr')
        .selectAll('th')
        .data(column_names).enter()
        .append('th')
        .text(function (column_name) { return column_name; });

    // create a row for each object in the data
    var rows = tbody.selectAll('tr')
        .data(data)
        .enter()
        .append('tr');

    // create a cell in each row for each column
    var cells = rows.selectAll('td')
        .data(function (row) {
        return columns.map(function (column) {
            return {column: column, value: row[column]};
        });
        })
        .enter()
        .append('td')
        .text(function (d) { return d.value; });

    return table;
}