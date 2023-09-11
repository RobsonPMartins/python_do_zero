# Uma estrutura de repetição em Python é um bloco de código que permite executar
# uma ou mais instruções repetidamente com base em uma condição. Isso é útil
# quando você deseja realizar a mesma tarefa várias vezes sem repetir o código
# manualmente. Python oferece dois tipos principais de estruturas de repetição:
# 'for' para iterações definidas e 'while' para iterações baseadas em condição.

# Definindo uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# Imprimindo uma mensagem antes do loop
print("Iterando por uma lista usando um loop 'for':")

# Usando um loop 'for' para iterar por cada fruta na lista
for fruta in frutas:
    print("Eu gosto de", fruta)  # Imprimindo uma mensagem para cada fruta


# Inicializando um contador com valor zero
contador = 0

# Imprimindo uma mensagem antes do loop
print("\nUsando um loop 'while' para contar até 5:")

# Usando um loop 'while' para contar até 5
while contador < 5:
    print("Contagem:", contador)  # Imprimindo o valor do contador
    contador += 1  # Incrementando o contador em cada iteração
