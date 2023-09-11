# Definindo a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Definindo uma classe Aluno que herda de Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Matrícula: {self.matricula}")

# Definindo uma classe Professor que herda de Pessoa
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Disciplina: {self.disciplina}")

# Função genérica para exibir informações de qualquer pessoa, independentemente do tipo
def mostrar_informacoes_pessoa(pessoa):
    pessoa.mostrar_info()

# Criando objetos (instanciando as classes)
pessoa1 = Aluno("Alice", 30, "12345")
pessoa2 = Professor("Bob", 45, "CODE")

# Usando a função de polimorfismo para exibir informações
mostrar_informacoes_pessoa(pessoa1)  # Isso chamará o método 'mostrar_info' de Aluno
mostrar_informacoes_pessoa(pessoa2)  # Isso chamará o método 'mostrar_info' de Professor
