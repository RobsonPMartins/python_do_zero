# Definindo uma classe chamada 'Pessoa'
class Pessoa:
    # Construtor (método especial) para inicializar objetos
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método para exibir informações da pessoa
    def mostrar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Definindo uma classe 'Aluno' que herda da classe 'Pessoa'
class Aluno(Pessoa):
    # Construtor para inicializar objetos de Aluno
    def __init__(self, nome, idade, matricula):
        # Chamando o construtor da classe pai (Pessoa) usando 'super()'
        super().__init__(nome, idade)
        self.matricula = matricula

    # Método para exibir informações do aluno, incluindo a matrícula
    def mostrar_info(self):
        # Chamando o método da classe pai (Pessoa) usando 'super().mostrar_info()'
        super().mostrar_info()
        print(f"Matrícula: {self.matricula}")

# Criando objetos (instanciando as classes)
pessoa1 = Pessoa("Alice", 30)
aluno1 = Aluno("Bob", 25, "12345")

# Acessando atributos e chamando métodos
pessoa1.mostrar_info()
aluno1.mostrar_info()
