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

const card = function(article) {return`
<div class="shadow hover:shadow-xl hover:shadow-stone-500 w-[80vw] lg:w-[40vw] min-w-lg h-[65vh] bg-gradient-to-r from-purple-2 to-purple-1 rounded-lg shadow-md" id="post-${article.pk}">
  <div class="w-full h-full">
    <img name="img-url" class="article-image-url rounded-t-lg object-fill w-full h-40 p-0 w-full bg-transparent mb-2" src="${article.image_url}" alt="no photo" />
    <div class="px-4">
      <div class="flex justify-between items-center">
        <p name="title" class="article-title truncate overflow-hidden mt-2 text-2xl font-bold tracking-tight text-pink-1">${article.title}</p>
        <div class="flex space-x-2 items-center">
          <button onclick="showEdit(${article.pk})" type="button" class="bottom-0 mr-3 md:mr-0">
            <svg xmlns="http://www.w3.org/2000/svg" fill="blue" viewBox="0 0 24 24" stroke-width="1.5" stroke="pink" class="w-4 h-4 md:w-6 md:h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125" />
            </svg>                        
          </button>
          <button onclick="postDelete(${article.pk})" type="button" class="bottom-0 mr-3 md:mr-0">
            <svg xmlns="http://www.w3.org/2000/svg" fill="red" viewBox="0 0 24 24" stroke-width="1.5" stroke="white" class="w-4 h-4 md:w-6 md:h-6">
              <path stroke-linecap="round" stroke-linejoin="round" d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0" />
            </svg>
          </button>
        </div>
      </div>
      <p name="date" class="article-date mb-3 font-normal text-xs text-white">Dibuat oleh ${article.author} pada ${article.date}</p>
      <div class="max-w-[75vw] max-h-[25vh] lg:max-w-[50vw]">
        <p name="description" class="article-description pb-3 pt-2 md:pt-4 truncate overflow-hidden font-normal text-white">${article.description}</p>
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
$.get("/artikel/json/filter/", function(data) {
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

const showEdit = function(pk) {
post_id = `#post-${pk}`
title = $(post_id).find(".article-title").text();
description = $(post_id).find(".article-description").text();
date = $(post_id).find(".article-date").text();
image_url = $(post_id).find(".article-image-url").attr("src");

$("#form-id").val(pk);
$(".update-title").val(title);
$(".update-description").val(description);
$(".update-img-url").val(image_url);

modalUpdateOpen();
}

function submitUpdate() {
console.log('halo');
var idInput = $('.form-id').val();
var titleInput = $('.update-title').val();
var descriptionInput = $('.update-description').val();
var imgUrlInput = $('.update-img-url').val();

if (titleInput && descriptionInput && imgUrlInput) {
  $.post({
    url: `/artikel/edit/${idInput}/`,
    data: {
      'id': idInput,
      'title': titleInput,
      'description': descriptionInput,
      'image_url': imgUrlInput,
      csrfmiddlewaretoken: getCookie('csrftoken')
    },
    success: function (data) {
      updateArtikel(data.article);
    },
  })
} else {
  alert("Isi dari form tidak valid");
}

$("form#update-article").trigger("reset");
modalUpdateClose();
return false;
}

function updateArtikel(article) {
$(`#post-${article.id} .article-title`).text(article.title)
$(`#post-${article.id} .article-description`).text(article.description)
$(`#post-${article.id} .article-image-url`).attr("src", article.image_url)  
}

const postDelete = function(pk) {
var action = confirm("Apakah Anda yakin ingin menghapus artikel ini?");
if (action != false) {
  $.ajax({
    url: `/artikel/delete/${pk}`,
    type: "DELETE",
    success: function(data) { $(`#post-${pk}`).remove(); }
  });
}
};

$(document).ready(
function() {
  showArticle();

  $(".modal-close").click(function() { modalClose(); });

  $(".modal-update-close").click(function() { modalUpdateClose(); });
}
);