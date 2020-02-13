$(document).ready(function () {
  $('#toggle_header').click(function () {
    if ($('header').attr('class') === 'green') {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else if ($('header').attr('class') === 'red') {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
