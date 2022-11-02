$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (settings.type == 'POST' || settings.type == 'PUT' || settings.type == 'DELETE') {
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
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    }
});

const card = function(article) {return`
    <div class="shadow hover:shadow-xl hover:shadow-stone-500 w-[80vw] lg:w-[40vw] min-w-lg h-[70vh] bg-gradient-to-r from-purple-2 to-purple-1 rounded-lg shadow-md" id="post-${article.pk}">
      <div class="w-full h-full">
        <img name="img-url" class="article-image-url rounded-t-lg object-fill w-full h-40 p-0 w-full bg-transparent mb-2" src="${article.image_url}" alt="no photo" />
        <div class="p-4">
          <p name="title" class="article-title truncate overflow-hidden text-2xl font-bold tracking-tight text-pink-1">${article.title}</p>
          <p name="date" class="article-date mb-3 font-normal text-xs text-white">Dibuat oleh ${article.author} pada ${article.date}</p>
          <div class="max-w-[75vw] max-h-[25vh] lg:max-w-[50vw]">
            <p name="description" class="article-description truncate overflow-hidden pb-3 pt-4 font-normal text-white">${article.description}</p>
          </div>
          <button onclick="showDetailArticle(${article.pk})" type="button" class="bottom-0 text-blue-200 hover:text-blue-400 hover:underline bg-transparent font-bold rounded-full text-sm text-center">
            Lihat selengkapnya
          </button>
        </div>
      </div>
    </div>
  `}
  
  const modalOpen = function() {  $(".modal-article").removeClass("hidden") }

  const modalClose = function() { $(".modal-article").addClass("hidden") }

  const modalUpdateOpen = function() {  $(".modal-update").removeClass("hidden") }

  const modalUpdateClose = function() { $(".modal-update").addClass("hidden") }

  const showArticle = function() {
    $.get("/artikel/json/", function(data) {
      console.log(data)
      for(var i = 0; i < data.length; i++){
        var article = {
          pk : data[i].pk,
          ...data[i].fields
        };

        $(".post-cards").append(card(article));
      }
    }
  )
  };

  const showDetailArticle = function(pk) {
    post_id = `#post-${pk}`
    title = $(post_id).find(".article-title").text();
    description = $(post_id).find(".article-description").text();
    date = $(post_id).find(".article-date").text();
    image_url = $(`#post-${pk} .article-image-url`).attr("src");


    $(".detail-title").text(title);
    $(".detail-description").text(description);
    $(".detail-date").text(date);
    $(".detail-image-url").attr("src", image_url);

    modalOpen();
  };


  $(document).ready(
    function() {
      showArticle();

      $(".modal-close").click(function() { modalClose(); });

    }
  );