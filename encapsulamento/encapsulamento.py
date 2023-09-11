# Definindo uma classe chamada 'Pessoa'
class Pessoa:
    # O construtor '__init__' é chamado quando um objeto da classe é criado
    def __init__(self, nome, idade):
        # Atributos da classe (privados)
        # Nota: Em Python, não existe um verdadeiro encapsulamento como em algumas outras linguagens.
        # Por convenção, usamos um sublinhado prefixado (_nome) para indicar que um atributo é "protegido".
        # Isso significa que o atributo não deve ser acessado diretamente fora da classe, mas ainda é acessível.
        self._nome = nome
        self._idade = idade

    # Método para exibir informações da pessoa
    def mostrar_info(self):
        # Usamos 'self' para acessar os atributos da instância (mesmo os "protegidos")
        print(f"Nome: {self._nome}, Idade: {self._idade}")

# Criando objetos (instanciando a classe)
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

# Acessando atributos e chamando métodos
pessoa1.mostrar_info()  # Isso chamará o método 'mostrar_info' para 'pessoa1'
pessoa2.mostrar_info()  # Isso chamará o método 'mostrar_info' para 'pessoa2'

# Nota: Os atributos '_nome' e '_idade' são "protegidos" por convenção,
# mas ainda podem ser acessados diretamente se necessário, embora não seja recomendado.
