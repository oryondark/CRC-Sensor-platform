var PATH = 'input your test path'

function at_daily_temper_test(){
  $.get(PATH, {"name":"hjkim", "Unit":"Test"}, function(data){
    console.log('[Console Log] Testting with get days of range from Input tag in HTML');
    var start_date = document.getElementById("start_date").value;
    var end_date = document.getElementById("end_date").value;
    console.log('[Console Log] daily temperature started date <%s> , ended date <%s>', start_date, end_date);
    console.log('[Console log] responsed data : %s', data);
    at_dail_temper_res_data_read_test(data);

  });
}

function at_dail_temper_res_data_read_test(data){
  console.log("[Console log] responsed data");
  console.log(data.data);
}


function at_daily_temper_resp_test(){
  var start_date = document.getElementById("start_date").value;
  var end_date = document.getElementById("end_date").value;
  $.get("getDailyTemper", {"start_date":start_date, "end_date":end_date}, function(data){
    console.log("[Console log] Success!");
    console.log("[Console log] GET/");
    console.log(data);
  });
}
