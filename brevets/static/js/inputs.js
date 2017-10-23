function calc_times(control) {
    var km = control.find("input[name='km']").val();
    var open_time_field = control.find("input[name='open']");
    var close_time_field = control.find("input[name='close']");
    var begin_date = $('#begin_date').val();
    var begin_time = $('#begin_time').val();
    var brevet_km = $('#brevet_dist_km').val();
    var time = moment(begin_date + ' ' + begin_time, 'YYYY-MM-DD HH:mm').toISOString();

    var km_string = String(km);

    for (i = 0; i < km_string.length; i++) {
      if (! "1234567890".includes(km_string[i])) {
        alert("Control distance must be a number!");
        open_time_field.val(" ");
        close_time_field.val(" ");
        return
       }
    }

   $.getJSON("/_calc_times", { km: km,
    brevet_km: brevet_km, time: time},
      // response handler
      function(data) {
        var times = data.result;
        console.log("Got a response: " +  times);
        console.log("Response.open = " + times.open);
        console.log("Response.close = " + times.close);
        if (times.open) {
           open_time_field.val(moment(times.open).format("ddd M/D H:mm"));
           close_time_field.val(moment(times.close).format("ddd M/D H:mm"));
        } else {
            alert('control distance is too large!');
            open_time_field.val(" ");
            close_time_field.val(" ");
        }
     } // end of handler function
    );// End of getJSON
  }

$(document).ready(function(){
// Do the following when the page is finished loading

    $('input[name="miles"]').change(
        function() {
             var miles = parseFloat($(this).val());
             var km = (1.609344 * miles).toFixed(1);
             console.log("Converted " + miles + " miles to " + km + " kilometers");
             var control_entry = $(this).parents(".control");
             var target = control_entry.find("input[name='km']");
             target.val( km );
             // Then calculate times for this entry
             loop_and_calc();
         });

    $('input[name="km"]').change(
         function() {
             var km = parseFloat($(this).val());
             var miles = (0.621371 * km).toFixed(1);
             console.log("Converted " + km + " km to " + miles + " miles");
             var control_entry = $(this).parents(".control");
             var target = control_entry.find("input[name='miles']");
             target.val( miles );
             // Then calculate times for this entry
             loop_and_calc();
         });

    // link: https://stackoverflow.com/questions/19528531/detect-with-jquery-when-a-select-changes
    $(document).on('change','#brevet_dist_km', loop_and_calc);

    $('input[name="begin_date"], input[name="begin_time"]').change(
        loop_and_calc
    );

    function loop_and_calc() {
        $(".control").each(function(index) {
            var kilos = $(this).find('#km').val();
            console.log("kilos: " + kilos);
            if (kilos) {
                calc_times($(this));
            }
        });
    }

});   // end of what we do on document ready
