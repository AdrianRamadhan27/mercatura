function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
          var cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

const articlePost = function(article) {
    $.post("/artikel/create/", {
      ...article,
      csrfmiddlewaretoken: getCookie('csrftoken'),
    },
    
    function(data) {
      window.location.href = "/artikel/";
      console.log(data);
    })
  }

  $(document).ready(
    function() {
      $(".submit-article").click(function() {
        const article = {
          title: $(".inp-title").val(),
          image_url: $(".inp-img-url").val(),
          description: $(".inp-description").val()
        }
    
        articlePost(article);
        return false;
      });
    }
  )