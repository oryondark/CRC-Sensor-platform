function chartTest_30by30(){
  $.get('{% url "line_chart_json" %}', function(data) {
      var ctx = $("#myChart").get(0).getContext("2d");
      let tempChart = new Chart(ctx, {
          type: 'line', data: data, option:{maintainAspectRatio:false}
      });
  });
}
