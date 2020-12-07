console.log("hello")


function loadChar() {
​
    charList = d3.select(".characteristics")
​
    traitsList = Object.keys(large_traits[0])


​
    traitsList.forEach(trait => {
        console.log(trait)
        listItem = charList.append("li")
            .classed("char-columns", true)
        
        listItem.append("input")
            .attr("type", "checkbox")
            .attr("id", trait)
            .attr("name", trait)
            .attr("value", trait)
            .attr("margin-right", "5px")
​
        listItem.append("label")
            .attr("for", trait)
            // .attr("padding-left", ".4em")
            .text("  " + trait)
    })
}