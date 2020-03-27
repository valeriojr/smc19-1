var width = 960,
    height = 500;

var projection = d3.geoMercator().scale(13000).center([-36.3, -9.5]);

var path = d3.geoPath()
    .projection(projection);

var svg = d3.select("svg")
    .attr("width", width)
    .attr("height", height);

// Define the div for the tooltip
var tooltipDiv = d3.select("body").append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);

var url1 = "http://enjalot.github.io/wwsd/data/world/world-110m.geojson";
var url2 = "http://enjalot.github.io/wwsd/data/world/ne_50m_populated_places_simple.geojson";
var bairros = "http://dados.al.gov.br/dataset/f292adf1-2c8c-4f45-835d-dd43946b13ad/resource/86a10827-fd51-46ec-aca7-9f65583dfa80/download/bairrosgeojson.geojson";
var url = "http://dados.al.gov.br/dataset/5475461a-02d4-49fe-9a2e-03ec5a84eab6/resource/b60a483a-95c7-45a7-83d7-af965eba47e5/download/malha2015.geojson";
d3.json("/static/data/geojs-27-mun.json", function (error, countries) {
    console.log(countries.features);

    svg.selectAll("path")
        .data(countries.features)
        .enter().append("path")
        .attr("d", path)
        .style("fill", function(d){
            if (d.properties.name.startsWith("Ma")){
                return "red";
            }
            else {
                return "blue";
            }
        })
        .on("mouseover", function (d) {
            tooltipDiv.transition()
                .duration(10)
                .style("opacity", .9);
            tooltipDiv.html(d.properties.name)
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        })
        .on("mouseout", function (d) {
            d3.select(this)
                .classed("active", false);
            tooltipDiv.transition()
                .duration(10)
                .style("opacity", 0);
            tooltipDiv.html("")
                .style("left", (d3.event.pageX) + "px")
                .style("top", (d3.event.pageY - 28) + "px");
        });
});
