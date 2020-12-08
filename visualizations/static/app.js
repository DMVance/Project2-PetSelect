console.log("Good Morning, World!")

// Get data from dogs_df (full database), combined_dogs_df (for user selection data). Convert to json and make plots.
// Plot breed counts that are available, most common attributes, most

// Most-selected traits, most present traits, where found?
// See mongo-query app, copy/paste and set CONN w/ username+password, call functions - 

// get data
// bar charts 
// breed selector

let subjectID = 940 // insert first element in the dropdown list
let info = d3.select("#sample-metadata") 


function init_build() {
    d3.json("dogs.json").then(
        data => {
            populate_charts(data, subjectID)
            let choose_subject = d3.select("#selDataset")
            let names = data.names
            names.forEach((name) => {
                choose_subject.append("option").attr("value", name).text(name)
            })
            return ""
        })
    }

function populate_charts(data, subject_num) {
    let samples = data.samples
        samples.forEach((subject) => {
            if (subject.id === subject_num.toString()) {
                console.log(subject)
                let subject_array = []
                for (var i = 0; i < subject.dog_labels.length; i++) {
                    subject_array.push({
                        "dog_labels": subject.dog_labels[i],
                        "dog_ids": subject.dog_ids[i],
                        "dog_counts": subject.dog_counts[i],
                    })
                }
                subject_sorted = _.orderBy(subject_array, "dog_counts", "desc").slice(0, 10)
                subject_sorted_reverse = _.reverse(subject_sorted)

                let trace1 = {
                    x: subject_sorted_reverse.map(d => d.dog_counts),
                    y: subject_sorted_reverse.map(d => d.dog_ids),
                    text: subject_sorted_reverse.map(d => d.dog_labels),
                    hovertemplate: "Breed: %{text}",
                    hoverlabel: {namelength: 0},
                    type: "bar",
                    orientation: "h"
                }
                let plotData = [trace1]
                let plotLayout = {
                    title: "Breed Counts",
                    yaxis: {
                        type: "category",
                    }
                }
                Plotly.newPlot("bar", plotData, plotLayout)

                // let trace2 = {
                //     x: subject_array.map(d => d.otu_ids),
                //     y: subject_array.map(d => d.sample_values),
                //     mode: "markers",
                //     marker: {
                //         size: subject_array.map(d => d.sample_values),
                //         color: subject_array.map(d => d.otu_ids),
                //         cmin: Math.min(...subject_array.map(d => d.otu_ids)),
                //         cmax: Math.max(...subject_array.map(d => d.otu_ids)),
                //         colorscale: "Viridis",
                //     },
                //     text: subject_array.map(d => d.otu_labels),
                //     hovertemplate: "Species: %{text}",
                //     hoverlabel: {namelength: 0},
                // }
                // let plotData2 = [trace2]
                // let plotLayout2 = {
                //     title: "Microbial Diversity",
                // }
                // Plotly.newPlot("bubble", plotData2, plotLayout2)
            }
        })
    })
    return ""
}

function clear_all() {
    d3.select("#bar").html("")
    // d3.select("#bubble").html("")
    d3.select("#sample-metadata").html("")
}

init_build()

d3.select("#selDataset")
    .on("change", function() {
        let choice = d3.select(this).property("value")
        console.log(choice)
        clear_all()
        d3.json("dogs.json").then(
        data => {
            populate_charts(data, choice)
        })
    })

console.log("Good Night, World!")
