let traitsList

document.getElementById("clickMe").addEventListener("click", function()
{
    console.log("clicked")
    // document.getElementById("#characteristics").selectAll("li").remove()
    const box1=document.getElementById("characteristic-box");
        if(box1.style.display=="none")
        {
            box1.style.display="block";
        }
        else
        {
            box1.style.display=="none";
        }
    console.log("clicked2") 
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
        }
        else if (selected_size === "md")
        {
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

