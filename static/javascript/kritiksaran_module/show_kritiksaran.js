$(document).ready(function(){
    $("#submit").click(function(){
    $.ajax({
        type: 'GET',
        url: '/kritiksaran/anon/total/',
        success:function(data){
        alert("Terdapat sebanyak " + data + " kritik dan saran");
        }
    });
return false;
});
});