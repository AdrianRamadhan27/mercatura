        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
                    
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                        // Only send the token to relative URLs i.e. locally.
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
                }
            }
        });
        
        $(document).on('submit', '#post-form',function(e){
            e.preventDefault();
            $.ajax({
                type:'POST',

                url:'/kritiksaran/',
                data:{
                    username:$('#username').val(),
                    title:$('#title').val(),
                    id:$('#id').val(),
                    setuju:$('setuju').val(),
                    num_setuju:$('#total-setuju').val(),
                    contact:$('#contact').val(),
                    description:$('#description').val(),
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
                },
                success:function(json){
                    document.getElementById("post-form").reset();
                    const url = '/kritiksaran/setuju/'
                    var csrf_token = getCookie("csrftoken");
                    $(".posts").append('<div class = "col-sm-3 col-md-10">'+
                        '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-outline h-md-250 position-relative">' +
                            '<div class="col p-4 d-flex flex-column position-static" style="background-color: #E2DBFD">' +
                                '<h3 class="mb-0" style="color: #150433;">' + json.title + '</h3>' +
                                '<h5 class="mb-auto" style="color: #5A5A5A; font-weight: lighter;">' + json.description + '</h5>' +

                                '<p class ="mb-auto" style="color: #5E239D;"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-person-circle" viewBox="0 0 16 16" style="color: #5E239D;">' +
                                    '<path d="M11 6a3 3 0 1 1-6 0 3 3 0 0 1 6 0z"/>' + 
                                    '<path fill-rule="evenodd" d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8zm8-7a7 7 0 0 0-5.468 11.37C3.242 11.226 4.805 10 8 10s4.757 1.225 5.468 2.37A7 7 0 0 0 8 1z"/>' +
                                '</svg>' +   json.username + '</p>' + 
                                '<hr>' +                                
                                '<div class="right floated">'+
                                    '<form action="' + url +'" method="POST" class="setuju-form" id="' + json.id +'">' + 
                                        '<input name="csrfmiddlewaretoken" value="'+csrf_token+'" type="hidden">' + 
                                        '<input type="hidden" name="post_id" value=' + json.id + '>'+
                                            '<button type="submit" class="ui button setuju-btn{{'+json.id+'}} btn btn-dark btn-rounded" style="background-color: #00F0B5; color: black;">'+
                                                'Setuju'+
                                            '</button>'+
                                            '<div class="ui grid">'+
                                                '<div class="column">'+
                                                    '<div class="setuju-count{{'+json.id+'}}">' + json.setuju + ' pengguna setuju</div>'+
                                                '</div>'+
                                            '</div>'+                                    
                                    '</form>'+
                                '</div>'+                                

                            '</div>' +
                        '</div>' +
                    '</div>' 
                    )
                },
                error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>");
                console.log(xhr.status + ": " + xhr.responseText); 
            }
            });

        });


        $( document ).ready(function() {
            $('.setuju-form').submit(function(e){
                e.preventDefault()
                
                const post_id = $(this).attr('id')
                
                const likeText = $(`.setuju-btn${post_id}`).text()
                const trim = $.trim(likeText)

                const url = $(this).attr('action')
                
                let res;
                const setujus = $(`.setuju-count${post_id}`).text()
                const trimCount = parseInt(setujus)
                
                $.ajax({
                    type: 'POST',
                    url: '/kritiksaran/setuju/',
                    data: {
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').text(),
                        'post_id':post_id,
                    },
                    success: function(response) {
                            res = trimCount + 1
                        $(`.setuju-count${post_id}`).text(res + " pengguna setuju")
                    },
                    
                });

            });

        });


        $(document).ready(function(){
                $("#submit").click(function(){
                $.ajax({
                    type: 'GET',
                    url: '/kritiksaran/total/',
                    success:function(data){
                    alert("Terdapat sebanyak " + data + " kritik dan saran");
                    }
                });
            return false;
            });
        });
            
