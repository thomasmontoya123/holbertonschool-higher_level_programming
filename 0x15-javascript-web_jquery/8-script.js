let result;
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi.co/api/films/?format=json',
    crossDomain: true
  }).done(function (data) {
    result = data.results;
    for (let i = 0; i < result.length; i++) {
      $('UL#list_movies').append('<li>' + result[i].title + '</li>');
    }
  });
});
