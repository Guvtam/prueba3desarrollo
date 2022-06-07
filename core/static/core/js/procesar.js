
$(document).ready(function(){
    //se creara una validacion simple
    //el div de alerta se ocultara para que solo se vea cuando hay error
    $("#error").hide();
    //se valida el formulario al enviar los datos
    $("#formulario").submit(function(){
      var mensaje = "";//almacena el mensaje de alerta

      if($("#nombre").val().trim().length==0){
        //se valida que el nombre no este vacio
        mensaje = "El campo no debe estar en blanco";
      }
                  

      if($("#email").val().trim().length==0){
        
        mensaje = "El email esta en blanco";
      }

      if($("#contrasena").val().trim().length < 6 ){

        mensaje = "La contraseña debe tener mínimo 6 caracteres";
      }
      
      if($("#contrasena").val() != $("#contrasena2").val()){

        mensaje = "La contraseña no coindice";
      }


      if($("#comentario").val().trim().length==0){
        
        mensaje = "Escribe un comentario";
      }

      //evitamos que se envien los datos del formulario
      if(mensaje != ""){
        $("#error").html(mensaje);//permite mostrar el mensaje de error en el div
        $("#error").show();//permite mostrar el div
        event.preventDefault();//evitamos el envio de los datos
      }
    })


})
