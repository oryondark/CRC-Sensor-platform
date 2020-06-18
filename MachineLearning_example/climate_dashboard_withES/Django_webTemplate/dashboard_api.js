/*
현재 REST API 구현을 최종적으로 마무리하려면, 각 API 요청에 따른 Error Handler도 구현해야만 한다.
*/

/*
Temperature Function
*/
function at_daily_temper(){
  const width_threshold = 480;
  var start_date = document.getElementById("start_date").value;
  var end_date = document.getElementById("end_date").value;
  $.get('<<daily Temperature PATH>>', {"start_date":start_date, "end_date":end_date}, function(data){
    var ctx = $("#DailyTemper").get(0).getContext("2d");
    var sub_o = "o"
    var celsius_text = sub_o.sub() + "C"
    optionsLine = {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: celsius_text
            },
            ticks:{
              suggestedMax:100
            }
          }
        ]
      },
      elements:{
        line:{
          fill:false
        }
      }
    };

    // Set aspect ratio based on window width
    optionsLine.maintainAspectRatio = $(window).width() < width_threshold ? false : true;
    let tempChart = new Chart(ctx, {
        type: 'line', data: data, options:optionsLine
    });
  });
}

function at_now_temper(){
  const width_threshold = 480;
  $.get('<<now Temperature PATH>>', function(data) {
      console.log(data);
      var ctx = $("#NowTemper").get(0).getContext("2d");
      var sub_o = "o"
      var celsius_text = sub_o.sub() + "C"
      optionsLine = {
        scales: {
          yAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: celsius_text
              },
              ticks:{
                suggestedMax:100
              }
            }
          ]
        },
        elements:{
          line:{
            fill:false
          }
        }
      };

      // Set aspect ratio based on window width
      optionsLine.maintainAspectRatio = $(window).width() < width_threshold ? false : true;
      let tempChart = new Chart(ctx, {
          type: 'line', data: data, options:optionsLine
      });
  });
}

/*
Humidity Function
*/

function at_daily_humi(){
  const width_threshold = 480;
  var start_date = document.getElementById("start_date").value;
  var end_date = document.getElementById("end_date").value;
  $.get('<<daily Humidity PATH>>', {"start_date":start_date, "end_date":end_date}, function(data){
    var ctx = $("#DailyHumi").get(0).getContext("2d");
    var sub_o = "o"
    var celsius_text = sub_o.sub() + "C"
    optionsLine = {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: celsius_text
            },
            ticks:{
              suggestedMax:100
            }
          }
        ]
      },
      elements:{
        line:{
          fill:false
        }
      }
    };

    // Set aspect ratio based on window width
    optionsLine.maintainAspectRatio = $(window).width() < width_threshold ? false : true;
    let tempChart = new Chart(ctx, {
        type: 'line', data: data, options:optionsLine
    });
  }).fail(function(){
    console.log("error ... ???")
  });
}

function at_now_humi(){
  const width_threshold = 480;
  $.get('<<now Hemperature PATH>>', function(data) {
      console.log(data);
      var ctx = $("#NowHumi").get(0).getContext("2d");
      const humidity_text = "Humidity(%)"
      optionsLine = {
        scales: {
          yAxes: [
            {
              scaleLabel: {
                display: true,
                labelString: humidity_text
              },
              ticks:{
                suggestedMax:100
              }
            }
          ]
        },
        elements:{
          line:{
            fill:false
          }
        }
      };

      // Set aspect ratio based on window width
      optionsLine.maintainAspectRatio = $(window).width() < width_threshold ? false : true;
      let tempChart = new Chart(ctx, {
          type: 'line', data: data, options:optionsLine
      });
  }).fail(function(){
    console.log("it is not implemented error!!")
  });
}
