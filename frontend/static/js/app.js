console.log("app.js is up")

large_traits[0].forEach((trait, traitDict) => {
    charList = d3.select("characteristics")
    console.log("app.js is up")
    charList.append("li")
        .classed("char-columns", true)
    inputTag = charList.append("input")
        .attr("type", "checkbox")
        .attr("id", traitDict.id)
        .attr("name", traitDict.name)
        .attr("value", traitDict.value)
    inputTag.append("label")
        .attr("for", traitDict.name)
        .text(traitDict.name)
})



