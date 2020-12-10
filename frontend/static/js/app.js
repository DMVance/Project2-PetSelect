function smoothScroll(target,duration){
    target = document.querySelector(target);
    let targetPosition = 5000;
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
    // d3.selectAll(characteristics._groups[0][0].childNodes).remove()
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


    function loadChar() {

        charList = d3.select(".characteristics")
        let selected_size
        let options = d3.select("#size").selectAll("option")
        options.each(function (d, i) {
        let current_option = d3.select(this)
        if (current_option.property("selected")) {
            selected_size = current_option._groups[0][0].value
        }

   
    })

    console.log(selected_size)
   
        if (selected_size === "lg")
        {

            let targetPosition = 1000;

            let traitsList = Object.keys(large_traits[0])
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
        else if (selected_size === "md")
        {
            let targetPosition = 1000;
            // document.getElementById("#characteristics").selectAll("li").remove()
            let traitsList = Object.keys(medium_traits[0])
            traitsList.forEach(trait => {
                
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
        }
        else  (selected_size === "sm")
        {          
            let targetPosition = 1000;
            // document.getElementById("#characteristics").selectAll("li").remove()  
            let traitsList = Object.keys(small_traits[0])
            traitsList.forEach(trait => {
                
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
        }
}


//  ******************************************** traits to breeds listener event ************************


document.getElementById("clickMe2").addEventListener("click", function()
{
    console.log("trait-clicked")
    smoothScroll(".breed-results", 2000);
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

                    // ---vvv---Reynolds code---vvv---
                    let results = d3.select("#results")
                    results.append("h3").text("Your best breeds are:")
                    let resultsList = results.append("ul")
                    for (i in data) {
                            console.log(data[i])
                            resultsList.append("li").text(data[i])
                            }
                    // ---^^^---Reynolds code---^^^---   

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
    smoothScroll(".dog-results", 2000)

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

    function loadDogs() {
        // ---vvv---Reynolds code---vvv---
    console.log("loadDogs")
}              