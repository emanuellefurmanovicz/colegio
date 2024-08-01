class Pessoa {
  String nome;
  int idade;
  double altura;
  String profissao;
  double salario;

  Pessoa(this.nome, this.idade, this.altura, this.profissao, this.salario);

  void aumento(double percentual) {
    salario *= (1 + percentual / 100);
    print('$nome teve um aumento de $percentual% e agora ganha R\$ ${salario.toStringAsFixed(2)}');
  }

  void andar() {
    print('$nome está andando.');
  }

  void aniversario() {
    idade++;
    print('Feliz aniversário! $nome completou $idade anos.');
  }

  void dormir() {
    print('$nome está dormindo.');
  }
}


void main() {
  Pessoa pessoa1 = Pessoa('Emanuelle', 17, 1.64, 'médica', 70000);

  pessoa1.andar();
  pessoa1.aumento(10);
  pessoa1.aniversario();
  pessoa1.dormir();
}
