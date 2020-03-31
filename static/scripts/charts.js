function barChart(selector, data, options) {
    const element = $(selector);
    d3.selectAll(`${selector} > *`).remove();

    options.width = options.width === undefined ? element.width() -
        2 * (options.margin.left + options.margin.right) : options.width;
    options.height = options.height === undefined ? element.height() -
        2 * (options.margin.top + options.margin.bottom) : options.height;

    const x = d3.scaleBand().range([0, options.width]).padding(0.5);
    const y = d3.scaleLinear().range([options.height, 0]);
    const color = d3.scaleOrdinal().range(options.colors);
    const svg = d3.select(selector)
        .attr("width", options.width + options.margin.left + options.margin.right)
        .attr("height", options.height + 2 * (options.margin.top + options.margin.bottom))
        .append("g")
        .attr("transform", `translate(${options.margin.left + (options.yAxis.label ? 10 : 0)}, ` +
            `${options.margin.top + (options.title ? options.margin.top : 0)})`);

    x.domain(data.map(function (d) {
        return d.label;
    }));
    y.domain([0, d3.max(data, function (d) {
        return d.value;
    })]);

    svg.selectAll("bar")
        .data(data)
        .enter()
        .append("rect")
        .attr("width", options.width + 2 * (options.margin.left + options.margin.right))
        .attr("height", options.height + 2 * (options.margin.top + options.margin.bottom))
        .attr("class", options.barCssClass)
        .attr("x", function (d) {
            return x(d.label) + options.margin.left;
        })
        .attr("width", x.bandwidth())
        .attr("y", options.height)
        .attr("height", 0)
        .style("fill", function (d) {
            return color(d.value);
        })
        .transition()
        .duration(1000)
        .attr("y", function (d) {
            return y(d.value);
        })
        .attr("height", function (d) {
            return options.height - y(d.value);
        });

    svg.append("g")
        .attr("transform", `translate(${options.margin.left}, ${options.height})`)
        .call(d3.axisBottom(x));

    svg.append("text")
        .attr("transform", `translate(${(options.width + (options.margin.left + options.margin.right)) / 2}, ${options.height + 2 * options.margin.bottom})`)
        .style("text-anchor", "middle")
        .text(options.xAxis.label);

    svg.append("g")
        .attr("transform", `translate(${options.margin.left}, 0)`)
        .call(d3.axisLeft(y));

    svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", -(options.height + 2 * (options.margin.top + options.margin.bottom)) / 2)
        .attr("y", -options.margin.left / 4)
        .text(options.yAxis.label);

    svg.append("text")
        .attr("transform", `translate(${options.width / 2}, -${options.margin.top})`)
        .style("font-weight", "bold")
        .style("text-anchor", "middle")
        .text(options.title);
}


function pieChart(selector, data, options) {
    const element = $(selector);
    d3.selectAll(`${selector} > *`).remove();

    console.log(options);

    options.width = options.width === undefined ? element.width() - 2 * (options.margin.left + options.margin.right) : options.width;
    options.height = options.height === undefined ? element.height() - 2 * (options.margin.top + options.margin.bottom) : options.height;
    options.innerRadius = options.innerRadius === undefined ? 0 : options.innerRadius;
    options.outerRadius = options.outerRadius === undefined ? (Math.min(options.width, options.height) -.5 * (options.margin.left + options.margin.top)) / 2 : options.outerRadius;

    const color = d3.scaleOrdinal().range(options.colors);
    const arc = d3.arc()
        .outerRadius(options.outerRadius)
        .innerRadius(options.innerRadius);
    const labelArc = d3.arc()
        .innerRadius((options.innerRadius + options.outerRadius) / 2)
        .outerRadius((options.innerRadius + options.outerRadius) / 2);
    const pie = d3.pie()
        .sort(null)
        .value(function (d) {
            return d.value;
        });
    const percentage = d3.scaleLinear().range([0, 1]).domain([0, d3.sum(data, function(d){return d.value;})]);
    const svg = d3.select(selector)
        .attr("width", options.width + 2 * (options.margin.left + options.margin.right))
        .attr("height", options.height + 2 * (options.margin.left + options.margin.right))
        .append("g")
        .attr("transform", `translate(${options.outerRadius + options.margin.left}, ${options.outerRadius + 2 * (options.margin.top + (options.title ? options.margin.top : 0))})`);

    const g = svg.selectAll("arc")
        .data(pie(data))
        .enter()
        .append("g")
        .attr("class", options.arcCssClass);

    g.append("path")
        .attr("d", arc)
        .style("fill", function (d, i) {
            return color(d.index)
        })
        .transition()
        .ease(d3.easeLinear)
        .duration(1000)
        .attrTween("d", function (d) {
            d.innerRadius = 0;
            const i = d3.interpolate({startAngle: 0, endAngle: 0}, d);
            return function (t) {
                return arc(i(t));
            }
        });

    // Labels
    g.append("text")
        .attr("transform", function (d) {
            return "translate(" + labelArc.centroid(d) + ")";
        })
        .style("fill", "white")
        .style("opacity", 0)
        .transition()
        .duration(2000)
        .style("opacity", 1)
        .style("text-anchor", "middle")
        .style("font-weight", "bold")
        .attr("dy", ".35em")
        .text(function (d) {
            return `${(100 * percentage(d.data.value)).toFixed(1)}%`;
        });

    g.append("rect")
        .attr("transform", function(d, i){ return `translate(${options.height / 2 + options.margin.bottom}, ${-options.height / data.length + 30 * i})`;})
        .attr("width", 20)
        .attr("height", 10)
        .style("fill", function(d){return color(d.index);});

    g.append("text")
        .attr("transform", function(d, i){ return `translate(${25 + options.height / 2 + options.margin.bottom}, ${-options.height / data.length + 10 + 30 * i})`;})
        .text(function(d){
            return d.data.label
        });

    // Title
    svg.append("text")
        .attr("transform", `translate(${0}, -${options.height / 2 + 0.5 * options.margin.top})`)
        .style("text-anchor", "middle")
        .style("font-weight", "bold")
        .text(options.title);
}