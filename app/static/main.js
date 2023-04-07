$(document).ready(function () {
  $("#spinner-box").hide();
  //on page load calling the post processing api
  call_api();

});

function call_api() {
  $("#spinner-box").show();
  $.getJSON('http://35.82.29.117:8000',
    { library_layout: 'PAIRED' }, function (data, textStatus, jqXHR) {
      //alert("task id returned "+data.task_id);

      get_progress(data.task_id, data.timestamp);
    })
    .done(function () {

      console.log("request completed");

    })
    .fail(function (jqxhr, settings, ex) { console.log('failed, ' + ex); });
}

async function get_progress(task_id, timestamp) {
  var completed = false;
  while (!completed) {

    await new Promise(resolve => setTimeout(resolve, 1000));


    try {
      let res = await fetch(
        "http://35.82.29.117:8000/celery-progress/" + task_id
      );

      let data = await res.json();
      console.log(data)
      if (!data.complete) {
        $("#message-box").html("progress " + data.progress.current + " - " + data.progress.description);
      }
      else {
        completed = true;
        $("#spinner-box").hide();
        $("#url-1").attr("href", "https://view.qiime2.org/visualization/?type=html&src=https://qiime2storage.s3.us-west-2.amazonaws.com/merged_results/" + timestamp + "-" + task_id + "/merged_feature_tables.qzv");
        $("#url-2").attr("href", "https://view.qiime2.org/visualization/?type=html&src=https://qiime2storage.s3.us-west-2.amazonaws.com/merged_results/" + timestamp + "-" + task_id + "/taxonomy_bar_plot.qzv");
        $("#message-box").hide();

        $("#url-1").show();
        $("#url-2").show();
      }

    } catch (err) {
      console.log(err);
    }
  }
}