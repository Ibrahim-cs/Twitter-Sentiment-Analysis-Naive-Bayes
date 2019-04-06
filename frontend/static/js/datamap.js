var source = new EventSource('/stream', { withCredentials: true });
var bubble_array = [];
var worldmap = new Datamap({
    scope: 'world',
    title: 'Sentiment',
    projection: 'equirectangular',
    element: document.getElementById("worldmap"),
    geographyConfig: {
        popupOnHover: false,
        highlightOnHover: false
    },
    bubblesConfig: {
        radius: 7,
        exitDelay: 30000 // Milliseconds
    },
    responsive: true,
    done: function(datamap) {
        datamap.svg.call(d3.behavior.zoom().on("zoom", redraw));
        //$("#resetZoom").on("click", function(){ resetZoom(); })
        function redraw() {
            datamap.svg.selectAll("g").attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
        }

        function resetZoom() {
            datamap.svg.selectAll("g").attr("transform", "translate(0,0)scale(1.0)");
        }
    },
    fills: {
        defaultFill: '#E5DBD2',
        "0": 'blue',
        "1": 'red'
    }
});

worldmap.legend({
    //legendTitle: "Sentiment",
    labels: {
        "0": 'Positive',
        "1": 'Negative'
    }
});

d3.select(window).on('resize', function() {
    worldmap.resize();
});

function determineColor(sentiment) {
    var newColor = sentiment == 0 ? "blue" : "red";
    return newColor;
}

function determineEmoji(sentiment) {
    var newColor = sentiment == 0 ? "&#128077;" : "&#x1F44E;";
    return newColor;
}

var func = function(geo, data) {
    var url = "https://twitter.com/" + data.name + "/status/" + data.id;
    var tip = "<div><h3><span style='vertical-align:middle'>@" + data.name + '</span><img style="vertical-align:middle" height="70" width="70" src="' + data.pic + '"></h3></div>';
    tip += "<h6>" + data.date + "</h6>";
    tip += "<h4>" + data.text + "</h4>";
    tip += "Naive Bayes:<font size='6em' color=" + determineColor(parseInt(data.fillKey)) + ">" + determineEmoji(parseInt(data.fillKey)) + "</font>";
    tip += "<br>CoreNLP:<font size='6em' color=" + determineColor(parseInt(data.fillKey1)) + ">" + determineEmoji(parseInt(data.fillKey1)) + "</font>";
    return "<div class='hoverinfo tooltip'>" + tip + '</div>';
}

source.onmessage = function(event) {

    if (event.data !== "1") {
        var data = JSON.parse(event.data) || {};
        if (!data.latitude || !data.longitude) return;
        var bubble = {
            "id": data.id,
            "name": data.name,
            "text": data.text,
            "fillKey1": data.nlpKey,
            "fillKey": data.nbKey,
            "latitude": data.latitude,
            "longitude": data.longitude,
            "pic": data.pic,
            "date": data.date
        };
        
        bubble_array.push(bubble);
        worldmap.bubbles(bubble_array, {
            popupTemplate: func
        });
    }

    //Added these placeholders for future reference
    /*d3.selectAll(".datamaps-bubble").on('click', function(bubble) {
        console.log(bubble);
    });

    d3.selectAll('#worldmap').on('mouseout', function(info) {
      if (d3.event.target.tagName == "circle"){
      	console.log(d3.select(d3.event.target).data()[0],"out")
      }
    });
    d3.selectAll('#worldmap').on('mouseover', function(info) {
      if (d3.event.target.tagName == "circle"){
      	console.log(d3.select(d3.event.target).data()[0],"over")
      }
    });*/

};