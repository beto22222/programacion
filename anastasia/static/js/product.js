
$(".a_carrito").click(function(e) {

    let id=this.parentElement.parentElement.id;

    let base="/add_to_car/";

    let end_cost = document.getElementById('end_cost');

      e.preventDefault();
      $.ajax({
          type: "GET",
          url: base+id,
          data: { 
          },
          success: function(result) {
              console.log('ok');
          },
          error: function(result) {
              console.log('error');
          }
      });
});

$(".evaluacion").click(function(e) {

    let id=this.parentElement.parentElement.id;

    let base="/like/";

      e.preventDefault();
      $.ajax({
          type: "GET",
          url: base+id,
          data: { 
          },
          success: function(result) {
              console.log('ok');
              let v0=parseInt(document.getElementById(id).getElementsByTagName("li")[0].textContent);
              console.log(v0);
              document.getElementById(id).getElementsByTagName("li")[0].innerHTML=v0+1;
          },
          error: function(result) {
              console.log('error');
          }
      });
});