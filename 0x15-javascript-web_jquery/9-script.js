$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    crossDomain: true
  }).done(function (data) {
    $('DIV#hello').text(data.hello);
  });
});
