function bringToTop(targetElement) {
    // put the element at the bottom of its parent
    let parent = targetElement.parentNode;
    parent.appendChild(targetElement);
}

var selected;
var zommLevel = "state";

function clicked(d) {
    var xCenter, yCenter, k;

    if (d && centered !== d) {
        var centroid = path.centroid(d);
        xCenter = centroid[0];
        yCenter = centroid[1];
        k = 7;
        centered = d;
        d3.select(this)
            .classed("selected", true);
        d3.select(selected).classed("selected", false);
        selected = this;
    } else {
        xCenter = width / 2;
        yCenter = height / 2;
        k = 1;
        centered = null;
        d3.select(selected).classed("selected", false);
    }

    g.selectAll("path")
        .classed("active", centered && function (d) {
            return d === centered;
        });

    g.transition()
        .duration(750)
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -xCenter + "," + -yCenter + ")")
        .style("stroke-width", 1.5 / k + "px");
        // .on("end", function () {
        //     if (zommLevel === "state") {
        //         //d3.selectAll("svg > *").remove();
        //         zommLevel = "city";
        //         // plotMap({
        //         //     dataSrc: "/static/data/bairrosgeojson.geojson",
        //         //     center: [xCenter, yCenter],
        //         //     featureName: "Bairro",
        //         //     scale: k * 13000
        //         // });
        //     }
        // });
}

function tooltipTextFocused(data, featureName, d, total) {
    var city, confirmed, suspect, deaths;
    city = d.properties[featureName];

    if (data[d.properties[featureName]]) {
        suspect = data[city]["suspect_cases"] ? data[city]["suspect_cases"] : "-";
        confirmed = data[city]["confirmed_cases"] ? data[city]["confirmed_cases"] : "-";
        deaths = "-";//data[city]["deaths"];
    } else {
        confirmed = "-";
        suspect = "-";
        deaths = "-";
    }

    return `<div class="row-col">` +
        `<strong>${city}</strong>` +
        `<div>Suspeitos: <span class="text-info">${suspect} ${(total.suspect_cases) ? "(" + (100 * suspect / total.suspect_cases).toFixed(1) + "%)" : ""}</div>` +
        `<div>Confirmados: <span class="text-warning">${confirmed} ${(total.confirmed_cases) ? "(" + (100 * confirmed / total.confirmed_cases).toFixed(1) + "%)" : ""}</div>` +
        `<div>Mortes: <span class="text-danger">${deaths}</span></div>` +
        `</div>`;
}

function tooltipMouseover(t, d, options) {
    d3.select(t)
        .classed("active", true);
    bringToTop(t);
    tooltipDiv.transition()
        .duration(10)
        .style("opacity", .9);

    var tooltipText;
    if (!centered) {
        tooltipText = tooltipTextFocused(cities, options.featureName, d, data.total);
    } else {
        tooltipText = "";
    }
    tooltipDiv.html(tooltipText)
        .style("left", (d3.event.pageX + 25) + "px")
        .style("top", (d3.event.pageY - 100) + "px");
}

function tooltipMouseout(t, d, options) {
    d3.select(t)
        .classed("active", false);
    tooltipDiv.transition()
        .duration(10)
        .style("opacity", 0);
    tooltipDiv
        .style("left", (d3.event.pageX) + "px")
        .style("top", (d3.event.pageY - 28) + "px")
        .html("");
}

function cityFill(d, options) {
    if (cities[d.properties[options.featureName]]) {
        console.log(d);
        const r = (cities[d.properties[options.featureName]]["suspect_cases"] / data.total.suspect_cases);
        const gb = 255 * r;
        return `rgb(255, ${225 - gb}, ${225 - gb})`;
    } else {
        return "light gray";
    }
}

var width = 960,
    height = 500,
    centered;

var cities;
var projection;
var path;
var svg;
var g;
// Define the div for the tooltip
var tooltipDiv;

function plotMap(options) {
    projection = d3.geoMercator().scale(options.scale).center(options.center);
    path = d3.geoPath().projection(projection);
    svg = d3.select("svg")
        .attr("width", width)
        .attr("height", height);
    g = svg.append("g");

    tooltipDiv = d3.select("body").append("div")
        .attr("class", "tooltip");

    d3.json("/static/data/geojs-27-mun.geojson", function (error, citiesGeoData) {
        if (error) alert(error);

        console.log(citiesGeoData);

        data = JSON.parse($("#data").text());
        cities = data.cities;

        g.append("g")
            .selectAll("path")
            .data(citiesGeoData.features)
            .enter().append("path")
            .attr("d", path)
            .style("fill", function (d) {
                return cityFill(d, options);
            })
            .on("mouseover", function (d) {
                tooltipMouseover(this, d, options);
            })
            .on("mouseout", function (d) {
                tooltipMouseout(this, d, options);
            })
            .on("click", clicked);

        // g.append("g")
        //     .selectAll("path")
        //     .data(neighbourhooodGeoData.features)
        //     .enter().append("path")
        //     .attr("d", path)
        //     .style("fill", cityFill)
        //     .on("mouseover", function(d){tooltipMouseover(d, options);})
        //     .on("mouseout", function(d){tooltipMouseout(d, options);})
        //     .on("click", clicked);
    });
}

state = {
    dataSrc: "/static/data/geojs-27-mun.geojson",
    center: [-36.3, -9.5],
    featureName: "name",
    scale: 13000
};

maceio = {
    dataSrc: "/static/data/bairrosgeojson.geojson",
    center: [-36.3, -9.5],
    featureName: "Bairro",
    scale: 30000
};

plotMap(state);
