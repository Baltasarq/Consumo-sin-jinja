document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("frmConsumo").addEventListener('submit', validarFormulario);
});

function validarFormulario(evento) {
  evento.preventDefault();
  var kilometros = document.getElementById('edkm').value;
  var tiempo = document.getElementById('edtiempo').value;
  var consumo = document.getElementById('edconsumo').value;

  var valoresAceptados = /^[0-9]+$/;

  if(kilometros.length == 0 || !kilometros.match(valoresAceptados)) {
    alert('La entrada de kilometros no es correcta');
    return;
  }
  else if(tiempo.length == 0 || !tiempo.match(valoresAceptados)) {
    alert('La entrada de tiempo no es correcta');
    return;
  }

  if(consumo.length == 0 || !consumo.match(valoresAceptados)) {
    alert('La entrada de consumo no es correcta');
    return;
  }

  this.submit();
}