$(document).ready(function () {

  //error notification when open
  music_name = $("#music_name").val();
  video_link = $("#video_link").val();
  if (music_name.length < 1) {
    $("#music_name_label").text("Name cannot be null");
    $("#music_name_label").css("color", "red");
    music = 1;
  }
  if (video_link.length < 1) {
    $("#video_link_label").text("Link cannot be null");
    $("#video_link_label").css("color", "red");
    link = 1;
  }

  //music name validation
  $("#music_name").keyup(function () {
    music_name = $("#music_name").val();
    if (music_name.length < 1) {
      $("#music_name_label").text("Name cannot be null");
      $("#music_name_label").css("color", "red");
      music = 1
    }
    else {
      $("#music_name_label").text("");
      music = 0
    }
  });

  //video link validation
  $("#video_link").keyup(function () {
    var matches = /^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((\w|-){11})(?:\S+)?$/;
    video_link = $("#video_link").val();
    if (video_link.length < 1) {
      $("#video_link_label").text("Link cannot be null");
      $("#video_link_label").css("color", "red");
      link = 1;
    }
    else if (!matches.test(video_link)) {
      $("#video_link_label").text("Check format");
      $("#video_link_label").css("color", "red");
      link = 1;
    }
    else {
      $("#video_link_label").text("");
      link = 0;
    }
  })

// validation and submit
  $("#btn").click(function (event) {
    if ((link == 0) && (music == 0)) {
      music_name = $("#music_name").val();
      video_link = $("#video_link").val();
      $("#playlist_items").append(`<li id="row">${music_name}<span id="link_of_vid" style="display:none">${video_link}</span>&nbsp&nbsp&nbsp&nbsp<button class=" btn btn-danger" id="DeleteRow" type="button"><i class="fa fa-times"></i></button>&nbsp&nbsp&nbsp&nbsp<button class=" btn btn-success" id="play" type="button"><i class="fa fa-play"></i></button></li>`)
    }
    else if ((link == 1) || (music == 1)){
      event.preventDefault();
      return false;
    }
 })

  //remove rows
  $("body").on("click", "#DeleteRow", function () {
    $(this).parents("#row").remove();
  })

  //play music
  $("body").on("click", "#play", function () {
    $("#iframe").empty();
    // $(this).parent().css({"color": "red", "border": "2px solid red"});
    tot = $(this).parent().find("span").text();
    console.log(tot);
    verified = `<iframe width="810" height="615"
  src="${tot}">
  </iframe> `;
    $("#iframe").append(verified);
  })
})