# Em Python, uma classe é uma estrutura que define um tipo de objeto.
# É uma "receita" que descreve os atributos e comportamentos que os objetos dessa classe terão.

# Para criar uma classe, usamos a palavra-chave 'class', seguida do nome da classe (geralmente com letra maiúscula).

# Exemplo de definição de uma classe chamada 'Pessoa':

    # O código da classe vem aqui...
class Pessoa:
    # Construtor (método especial) para inicializar objetos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para exibir informações da pessoa
    def mostrar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Criando objetos (instanciando a classe)
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Acessando atributos e chamando métodos
pessoa1.mostrar_info()
pessoa2.mostrar_info()
