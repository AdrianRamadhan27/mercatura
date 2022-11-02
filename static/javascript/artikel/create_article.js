const articlePost = function(article) {
    $.post("/artikel/create/", {
      ...article,
      csrfmiddlewaretoken: "{{ csrf_token }}"
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