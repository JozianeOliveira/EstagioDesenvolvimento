function resolveA() {
    // Sequência de números ímpares: 1, 3, 5, 7, ...
    const nextElement = 7 + 2; // O próximo número ímpar após 7
    document.getElementById("resultadoA").innerText = nextElement;
}

function resolveB() {
    // Sequência de potências de 2: 2^1, 2^2, 2^3, 2^4, 2^5, 2^6
    const lastElement = 64;
    const nextElement = lastElement * 2; // O próximo número é 2^7
    document.getElementById("resultadoB").innerText = nextElement;
}

function resolveC() {
    // Sequência de quadrados perfeitos: 0^2, 1^2, 2^2, 3^2, ...
    const lastIndex = 7; //Próximo índice após 6
    const nextElement = lastIndex * lastIndex;
    document.getElementById("resultadoC").innerText = nextElement;
}

function resolveD() {
    // Sequência de quadrados de números pares: 2^2, 4^2, 6^2, 8^2
    const lastIndex = 10; //(Próximo número par após 8)^2
    const nextElement = lastIndex * lastIndex;
    document.getElementById("resultadoD").innerText = nextElement;
}

function resolveE() {
    // Sequência de Fibonacci: 1, 1, 2, 3, 5, 8, ...
    const sequence = [1, 1, 2, 3, 5, 8];
    const nextElement = sequence[sequence.length - 1] + sequence[sequence.length - 2];
    document.getElementById("resultadoE").innerText = nextElement;
}

function resolveF() {
    // Considerando sequência como um padrão crescente após um ponto específico: 2, 10, 12, 16, 17, 18, 19
    const lastElement = 19;
    const nextElement = lastElement + 1;
    document.getElementById("resultadoF").innerText = nextElement;
}
