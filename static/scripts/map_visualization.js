function bringToTop(targetElement) {
    // put the element at the bottom of its parent
    let parent = targetElement.parentNode;
    parent.appendChild(targetElement);
}

var selected;

function clicked(d) {
    var x, y, k;

    if (d && centered !== d) {
        var centroid = path.centroid(d);
        x = centroid[0];
        y = centroid[1];
        k = 7;
        centered = d;
        d3.select(this)
            .classed("selected", true);
        d3.select(selected).classed("selected", false);
        selected = this;
    } else {
        x = width / 2;
        y = height / 2;
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
        .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
        .style("stroke-width", 1.5 / k + "px");
}

function tooltipTextFocused(data, d, total) {
    var city, confirmed, suspect, deaths;
    city = d.properties.name;

    if (data[d.properties.name]) {
        suspect = data[city]["suspect_cases"];
        confirmed = data[city]["confirmed_cases"];
        deaths = "-";//data[city]["deaths"];
    } else {
        confirmed = "-";
        suspect = "-";
        deaths = "-";
    }

    return `<div class="row-col">` +
        `<strong>${d.properties.name}</strong>` +
        `<div>Suspeitos: <span class="text-info">${suspect} (${(100 * suspect/total.suspect).toFixed(1)}%)</div>` +
        `<div>Confirmados: <span class="text-warning">${confirmed} (${(confirmed/total.confirmed).toFixed(1)}%)</div>` +
        `<div>Mortes: <span class="text-danger">${deaths}</span></div>` +
        `</div>`;
}

var width = 960,
    height = 500,
    centered;

var projection = d3.geoMercator().scale(13000).center([-36.3, -9.5]);

var path = d3.geoPath()
    .projection(projection);

var svg = d3.select("svg")
    .attr("width", width)
    .attr("height", height);

var g = svg.append("g");

// Define the div for the tooltip
var tooltipDiv = d3.select("body").append("div")
    .attr("class", "tooltip");

legend = svg.append("g")
    .attr("class", "legend")
    .attr("transform", "translate(50,30)")
    .style("font-size", "12px");

d3.json("/static/data/geojs-27-mun.json", function (error, countries) {
    data = JSON.parse($("#data").text());
    var cities = data.cities;

    console.log(data);

    g.append("g")
        .selectAll("path")
        .data(countries.features)
        .enter().append("path")
        .attr("d", path)
        .style("fill", function (d) {
            if (cities[d.properties.name]) {
                console.log(d);
                const r = (cities[d.properties.name]["suspect_cases"] / data.total.suspect_cases);
                const gb = 255 * r;
                return `rgb(255, ${225 - gb}, ${225 - gb})`;
            } else {
                return "light gray";
            }
        })
        .on("mouseover", function (d) {
            d3.select(this)
                .classed("active", true);
            bringToTop(this);
            tooltipDiv.transition()
                .duration(10)
                .style("opacity", .9);


            var tooltipText;
            if (!centered) {
                tooltipText = cities[d.properties.name] ? tooltipTextFocused(cities, d, data.total) : tooltipTextFocused(cities, d, data.total);
            } else {
                tooltipText = "";
            }
            tooltipDiv.html(tooltipText)
                .style("left", (d3.event.pageX + 25) + "px")
                .style("top", (d3.event.pageY - 100) + "px");
        })
        .on("mouseout", function (d) {
            d3.select(this)
                .classed("active", false);
            tooltipDiv.transition()
                .duration(10)
                .style("opacity", 0);
            tooltipDiv
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px")
                .html("");
        })
        .on("click", clicked);
});
