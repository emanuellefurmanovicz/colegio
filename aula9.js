const mensagensDivertidas =
[
" Qual é o peixe que caiu do 10º andar?",
" O aaaaaaatuuuuuuum. ",
];

let botaoDivertido = document.getElementById("botaodivertido");
let mensagemdivertida = document.getElementById("mensagemdivertida");

botaoDivertido.addEventListener('click', function(){
    //Math.floor(x) retorna o numero inteiro dentre o numero "x"
    //Math.random() retorna um numero pseudo-aleatorio no intervalo

    const mensagemAleatoria = mensagensDivertidas[Math.floor(Math.random() * mensagensDivertidas.lenght)]

    mensagemDivertida.textContent = mensagemAleatoria
}
)
