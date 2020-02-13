$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/people/5/?format=json',
    crossDomain: true
  }).done(function (data) {
    $('#character').text(data.name);
  });
});
