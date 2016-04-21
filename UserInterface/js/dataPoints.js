function renderDataPoints() {
var width=500,
            height=400,
            margin = {top:30,bottom:35,left:50,right:20},
            innerWidth = width-margin.left-margin.right,
            innerHeight = height-margin.top-margin.bottom;
var data = [];
var chart = d3.select("#viz")

var xGroup = chart.append("g")
    .attr("transform","translate("+margin.left+","+(innerHeight+margin.top)+")");
var yGroup = chart.append("g")
    .attr("transform","translate("+margin.left+","+margin.top+")");
var dotGroup = chart.append("g")
    .attr("transform","translate("+margin.left+","+margin.top+")");

// text label for the x axis
var xLabel = chart.append("text")
            .style("text-anchor", "middle")
            .attr("dx", 260 )
            .attr("dy", 395 );

// text label for the y axis
var yLabel = chart.append("text")
            .attr("transform", "rotate(-90)")
            .style("text-anchor", "middle")
            .attr("dx", -90 )
            .attr("dy", 20 );
    
function renderChart(data) {
    chart.attr("width",width)
        .attr("height",height);
    
    var xScale = d3.scale.linear()
                .range([0,innerWidth])
                .domain([0,d3.max(data,function(d) { return +d["metascore"] })]);
    
    
    var yScale = d3.scale.linear()
                .range([innerHeight,0])
                .domain(d3.extent(data,function(d) { return +d["awards"] }));
        
    var xAxis = d3.svg.axis()
                    .scale(xScale)
                    .orient("bottom");
    var colorScale  = d3.scale.category10();
    
    xLabel.text("Metascore");
    yLabel.text("Awards");
    
    xGroup.call(xAxis);
            
    var yAxis = d3.svg.axis()
                    .scale(yScale)
                    .orient("left");
            
    yGroup.call(yAxis);
    
    
    var selection = dotGroup.selectAll("circle")
                            .data(data);
    selection.enter()
                .append("circle")
                .attr("r",5)
                .attr("cx",function(d,i) { return xScale(d["metascore"]) })
                .attr("cy",function(d,i) { return yScale(d["awards"]) })
                .attr("fill",function(d,i) {return colorScale(d["rating"]) })
                .attr("opacity","0.7")
                .on("click",function(d,i) {
                    $("#outcome").empty();
                    renderOutcome(d["rating"]);
                    $(".display").show();
                })
                .on("mouseenter",function(d,i) { 
                    d3.select("#tooltip").style({
                        visibility:"visible",
                        top:(d3.event.pageY-200) + "px",
                        left:(d3.event.pageX-20) + "px",
                        opacity:1
                    }).html("<b>"+d["title"]+"</b><br/>"+"Rating : "+d["rating"]+"<br/>"+"Metascore : "+d["metascore"]+"<br/>"+"Awards : "+d["awards"]);
                    $("#outcome").empty();
                    renderOutcome(d["rating"]);
                    $(".display").show();
                })
                .on("mouseleave",function(d,i) { 
                    d3.select("#tooltip").style({
                        visibility:"hidden",
                        opacity:0
                    }).html("");
                });
            
    selection.exit().remove();
    selection.transition()
            .attr("r",5)
            .attr("cx",function(d,i) { return xScale(d["metascore"]) })
            .attr("cy",function(d,i) { return yScale(d["awards"]) })
            .attr("fill",function(d,i) {return colorScale(d["rating"]) });
    
    // draw legend    
    var legend = chart.selectAll(".legend")
      .data(colorScale.domain())
       .enter().append("g")
      .attr("class", "legend")
      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

    // draw legend colored rectangles
    legend.append("rect")
      .attr("x", 60)
      .attr("width", 18)
      .attr("height", 18)
      .style("fill", colorScale);

    // draw legend text
    legend.append("text")
      .attr("x", 60+30)
      .attr("y", 9)
      .attr("dy", ".35em")
      .style("text-anchor", "end")
      .text(function(d) { return d;})
}
function render(data) {
        renderChart(data);
}
    d3.csv("data/featureSelect.csv").row(function(d){
        return { title : d.Title , metascore : +d.Metascore , awards : +d.Awards , rating : +d.rate  }; 
    })
    .get(function(error,rows) {
         rows.sort(function(a,b) {
              return d3.descending(a.rating,b.rating);
       });
        render(rows);
    });

}