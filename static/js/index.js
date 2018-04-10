
$("button").click(function(e) {

    let id=this.id;
    let base="/add_to_car/";
    console.log(this.className);
    if (this.className=='add') {

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
    }
});