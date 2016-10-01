function graph1(ydata,area,color,ylabel) {

var xdata = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] 
//var ydata = [5,6,7,8,0,4,7,8,9,11,15,13,12,15,16,17,5,2,3,4,4,5,6,7]
var tdata = [xdata,ydata]

var data = transpose([xdata,ydata])

var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 700 - margin.left - margin.right,
    height = 250 - margin.top - margin.bottom;

var x = d3.scale.linear()
    .range([0, width]);

var y = d3.scale.linear()
    .range([height, 0]);

var ticknames = ["12am","1am","2am","3am","4am","5am","6am","7am","8am","9am","10am","11am","12pm","1pm","2pm","3pm","4pm","5pm","6pm","7pm","8pm","9pm","10pm","11pm","12pm"]

var today = new Date()
var currHour = today.getHours()

var xAxis = d3.svg.axis()
    .scale(x)
    .tickValues([1,3,5,7,9,11,13,15,17,19,21,23])
    .tickFormat(function(d, i){return ticknames[(i*2+currHour+1)%24]})
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left");

var line = d3.svg.line()
    .x(function(d) { return x(d[0]); })
    .y(function(d) { return y(d[1]); })

var svg = d3.select(area).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")")

  x.domain(d3.extent(data, function(d) { return d[0]; }));
  y.domain(d3.extent(data, function(d) { return d[1]; }));

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text(ylabel);

        svg.append("g")
      .attr("class", "x axis")
    .append("text")
      .attr("y", 185)
      .attr("x", 640)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Local Time at Browser");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line)
      .attr("fill","none")
      .attr("stroke", color)
      .attr("stroke-width", 2)

    svg.selectAll("text")
       .data(data)
     .enter().append("svg:text")
       .attr("x", function(d, i) { return i*20 + 2 - 3*Math.trunc(Math.log10(d)); })
       .attr("y", function(d, i) { return 420 - y(d); })
       .attr("dy", -1) // padding-right
       .attr("dx", ".35em") // vertical-align: middle
       .attr("text-anchor", "top") // text-align: right
       .attr("fill", "white")
       .attr("font-family", "Arial")
       .attr("font-size", 12)
       .text(String);
}

///////////////////////////
// d3.select("svg").remove();
///////////////////////////

function transpose(a) {

  // Calculate the width and height of the Array
  var w = a.length ? a.length : 0,
    h = a[0] instanceof Array ? a[0].length : 0;

  // In case it is a zero matrix, no transpose routine needed.
  if(h === 0 || w === 0) { return []; }

  /**
   * @var {Number} i Counter
   * @var {Number} j Counter
   * @var {Array} t Transposed data is stored in this array.
   */
  var i, j, t = [];

  // Loop through every item in the outer array (height)
  for(i=0; i<h; i++) {

    // Insert a new row (array)
    t[i] = [];

    // Loop through every item per item in outer array (width)
    for(j=0; j<w; j++) {

      // Save transposed data.
      t[i][j] = a[j][i];
    }
  }

  return t;
};
