

$(".close_emaling").click(function(e){
  let div=document.getElementById("emailing");

  console.log("cerrar");
  div.style.visibility = "hidden"; 
});



$(".align-spaced").click(function(e){
  let a=$(window).scrollTop() + "px";
  document.getElementById("offCanvas").style.marginTop = a;
});



$(window).scroll(function(){
    let div=document.getElementById("emailing");
    let html_size=$( document ).height();
    let windows_size=$( window ).height();
    mT=-html_size + $(this).scrollTop()+ windows_size - 130;
    div.style.marginTop = mT+"px";
  });