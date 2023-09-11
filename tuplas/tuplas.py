# Criando uma tupla simples
minha_tupla = (1, 2, 3, "quatro", "cinco")

# Acessando elementos da tupla por índice
primeiro_elemento = minha_tupla[0]  # Retorna 1
segundo_elemento = minha_tupla[1]   # Retorna 2

# Tuplas são imutáveis, portanto, você não pode modificar seus elementos após a criação.
# Isso gerará um erro: minha_tupla[2] = 10

# Verificando o comprimento da tupla
tamanho_da_tupla = len(minha_tupla)  # A tupla tem 5 elementos
print(f"O tamanho da tupla e: {tamanho_da_tupla}")

# Iterando pela tupla usando um loop 'for'
for elemento in minha_tupla:
    print(elemento)  # Isso imprimirá cada elemento da tupla

# Você também pode criar uma tupla sem usar parênteses, separando os elementos por vírgulas:
outra_tupla = 1, 2, 3

for elementos in outra_tupla:
    print(elementos) 