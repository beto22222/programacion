$(".qty").click(function(e) {
 

    let id=this.parentElement.parentElement.id;

    let base="/set_new_value_to_car/";
    let input = document.getElementById(id).getElementsByTagName("input")[0];
    let end_cost = document.getElementById('end_cost');

    console.log(input.value);
    if (this.className=='qty') {
      e.preventDefault();
      $.ajax({
          type: "GET",
          url: base+id,
          data: { 'value':input.value
          },
          success: function(json) {

              end_cost.innerHTML=json['end_cost']
          },
          error: function(result) {
              console.log('error');
          }
      });
    } 
});

$(".delete").click(function(e) {

    let bar=this.parentElement.parentElement;
    let id=bar.id;

    let base="/quit_to_car/";

    let end_cost = document.getElementById('end_cost');

      e.preventDefault();
      $.ajax({
          type: "GET",
          url: base+id,
          data: { 
          },
          success: function(json) {
              
              end_cost.innerHTML=json['end_cost']
              bar.remove();
          },
          error: function(result) {
              console.log('error');
          }
      });
    
});