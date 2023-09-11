# Usando um loop tradicional
quadrados = []
for numero in range(5):
    quadrados.append(numero ** 2)

# Usando compreensão de lista
quadrados_compreensao = [numero ** 2 for numero in range(5)]

# As duas abordagens produzem a mesma lista 'quadrados'
print(quadrados_compreensao)  # Saída: [0, 1, 4, 9, 16]


# Usando um loop tradicional
quadrados_dict = {}
for numero in range(5):
    quadrados_dict[numero] = numero ** 2

# Usando compreensão de dicionário
quadrados_dict_compreensao = {numero: numero ** 2 for numero in range(5)}

# As duas abordagens produzem o mesmo dicionário 'quadrados_dict_compreensao'
print(quadrados_dict_compreensao)  # Saída: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
