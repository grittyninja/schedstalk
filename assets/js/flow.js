  $(".button-collapse").sideNav();
$(document).ajaxStart(function(){
   $("#logo").css("height", "50px");
   $("#input_field").removeClass("l10");
   $("#input_field").addClass("s12");
   $("#search_query").prop('disabled', true);
   $("html").css("background", "url('assets/img/loading.gif') no-repeat center center fixed"); 
   $("html").css("background-size", "cover"); 
   $("#stalk_button").hide();
   $("#result").hide();
   $("nav").hide();
   $("footer").hide();
});
$(document).ajaxStop(function(){
   $("#input_field").removeClass("s12");
   $("#input_field").addClass("l10");
   $("#stalk_button").show();
   $("html").css("background", ""); 
   $("#result").show();
   $("#search_query").prop('disabled', false);
});
    function sendQuery(){
        if(!($("#search_query").val())){
            Materialize.toast('search query kosong', 4000);
        }
        else {
            q = $('#search_query').val();
            console.log(q);
            $.post("engine/engine.php",{q: q,csrf_token: token},
           function(data) {
                $("#resultString").html(data);
            });
        }
    }
    $(document).keypress(function(e) {
        if (e.which == 13) {
            sendQuery();
        }
    });
    $('#stalk_button').click(function() {
        sendQuery();
    });