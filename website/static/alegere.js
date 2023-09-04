function mostrarValorRadio(radio) {
    var semestreInputs = document.querySelectorAll('.semestre-selected');


    semestreInputs.forEach(function (input) {
        input.addEventListener('change', function () {
            var semestreSelecionado = document.querySelector('input[name="sem"]:checked');
            var semestrul1 = document.querySelector('.semestrul1');
            var semestrul2 = document.querySelector('.semestrul2');

            if (radio.value === '1') {
                semestrul1.style.display = 'block';
                semestrul2.style.display = 'none';
            } else if (radio.value === '2') {
                semestrul1.style.display = 'none';
                semestrul2.style.display = 'block';
            }
        });
    });
}

mostrarCamposDisciplinas(); // Chama a função para configurar o evento ao carregar a página


// function mostrarValorRadio(radio) {
//     alert("Valor do rádio selecionado: " + radio.value);
// }

// #.............................................................................................................

// function mostrarCamposDisciplinas(radio){
//     var semestreSelecionado = document.querySelector('input[name="sem"]:checked');
//     alert("Valor do rádio selecionado: " + radio.value);
//
//     var sem1 = document.querySelector('.sem1');
//     var sem2 = document.querySelector('.sem2');
//
//     if(semestreSelecionado === '1'){
//         sem1.style.display = 'block';
//         sem2.style.display = 'none';
//     }else  if (semestreSelecionado === '2') {
//         sem1.style.display = 'none';
//         sem2.style.display = 'block';
//     }
// }
// var semestreInputs = document.querySelectorAll('.semestre-selected');
// semestreInputs.forEach(function (input){
//     input.addEventListener('change', mostrarCamposDisciplinas);
// });
//
// mostrarCamposDisciplinas() //// Executa a função inicialmente para exibir os campos corretos