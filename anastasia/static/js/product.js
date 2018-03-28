
$(".a_carrito").click(function(e) {

    let id=this.parentElement.id;

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