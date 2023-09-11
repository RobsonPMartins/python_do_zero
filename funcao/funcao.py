# Uma função em Python é um bloco de código reutilizável que realiza uma tarefa específica.
# Ela pode aceitar zero ou mais argumentos como entrada, executar um conjunto de instruções
# e, opcionalmente, retornar um valor como resultado. As funções ajudam a modularizar
# o código, tornando-o mais organizado, legível e reutilizável, já que você pode chamá-las
# sempre que precisar realizar a mesma tarefa, sem a necessidade de repetir o código.

# Definindo uma função chamada 'saudacao'
def saudacao(nome):
    """Esta função imprime uma saudação personalizada."""
    # O 'def' indica que estamos definindo uma função chamada 'saudacao'.
    # Ela aceita um argumento chamado 'nome'.

    # A string entre aspas triplas ("""...""") é chamada de docstring.
    # Ela fornece uma descrição da função e seu propósito.

    # Aqui, a função imprime uma saudação personalizada usando o nome fornecido.
    print(f"Olá, {nome}!")

# Chamando a função 'saudacao'
saudacao("Alice")
saudacao("Bob")
# Aqui, estamos chamando a função 'saudacao' duas vezes, passando diferentes nomes como argumento.
# A função imprimirá uma saudação personalizada para cada nome.


