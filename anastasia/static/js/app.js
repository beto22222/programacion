$(document).foundation()

$('[data-toggle-dia]').click(function () {
  $('#lineup-tabs').foundation('selectTab', $(this).data('toggleDia'))
});

var $offCanvas = $('#offCanvas');
var $sticky = $('#sticky');

$offCanvas.find('li').click(() => {
  $offCanvas.foundation('close');
  setTimeout(() => {
    $sticky.css('left', '0px');
  }, 300)
})