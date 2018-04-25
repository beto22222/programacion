$(".send_email").click(function(e) {
  
    let base="/send_email/";
      console.log('bien');
    

      e.preventDefault();
      $.ajax({
          type: "GET",
          url: base,
          data: { 
            'name':document.getElementById('name').value,
            'email':document.getElementById('email').value,
            'content':document.getElementById('content').value
          },
          success: function(json) {
              console.log('todo bien');
          },
          error: function(result) {
              console.log('error');
          }
      });
    
});