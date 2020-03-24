var width = 960,
    height = 500;

var projection = d3.geoMercator().scale(14000).center([-36.3, -9.5]);

var path = d3.geoPath()
    .projection(projection);

var svg = d3.select("svg")
    .attr("width", width)
    .attr("height", height);


var url1 = "http://enjalot.github.io/wwsd/data/world/world-110m.geojson";
var url2 = "http://enjalot.github.io/wwsd/data/world/ne_50m_populated_places_simple.geojson";
var bairros = "http://dados.al.gov.br/dataset/f292adf1-2c8c-4f45-835d-dd43946b13ad/resource/86a10827-fd51-46ec-aca7-9f65583dfa80/download/bairrosgeojson.geojson";
var url = "http://dados.al.gov.br/dataset/5475461a-02d4-49fe-9a2e-03ec5a84eab6/resource/b60a483a-95c7-45a7-83d7-af965eba47e5/download/malha2015.geojson";
d3.json(url, function (error, countries) {
    if (error) console.log(error);

    console.log(countries.features);

    svg.selectAll("path")
        .data(countries.features)
        .enter().append("path")
        .attr("d", path)
        .on("mouseover", function (d) {
            console.log("just had a mouseover", d3.select(d));
            d3.select(this)
                .classed("active", true)
        })
        .on("mouseout", function (d) {
            d3.select(this)
                .classed("active", false)
        });


    /*svg.selectAll("circle")
        .data(countries.features)
        .enter().append("circle")
        .attr('r', 5)
        .attr('cx', function (d) {
            return projection(d.geometry.coordinates)[0]
        })
        .attr('cy', function (d) {
            return projection(d.geometry.coordinates)[1]
        })
        .on("mouseover", function (d) {
            console.log("just had a mouseover", d3.select(d));
            d3.select(this)
                .classed("active", true)
        })
        .on("mouseout", function (d) {
            d3.select(this)
                .classed("active", false)
        });
*/
});
