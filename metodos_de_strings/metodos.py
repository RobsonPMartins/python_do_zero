# Exemplo de uma string
texto = "Exemplo de String"

# Métodos de strings
maiusculas = texto.upper()  # Converte para maiúsculas
minusculas = texto.lower()  # Converte para minúsculas
capitalizada = texto.capitalize()  # Primeira letra maiúscula, o resto minúscula
titulo = texto.title()  # Primeira letra de cada palavra maiúscula
sem_espacos = texto.strip()  # Remove espaços em branco no início e no final

# Verificação de prefixo e sufixo
comeca_com = texto.startswith("Exemplo")  # Verifica se começa com "Exemplo"
termina_com = texto.endswith("String")  # Verifica se termina com "String"

# Substituição
substituido = texto.replace("String", "Texto")  # Substitui "String" por "Texto"

# Divisão e junção
dividido = texto.split(" ")  # Divide a string em uma lista de palavras
junto = " ".join(["Exemplo", "de", "String"])  # Junta uma lista em uma única string com espaços

# Busca e contagem
indice = texto.find("de")  # Encontra a posição da primeira ocorrência de "de"
contagem = texto.count("e")  # Conta quantas vezes "e" aparece na string

# Verificações de tipo de caracteres
e_numerico = texto.isnumeric()  # Verifica se a string contém apenas números
e_alfabetico = texto.isalpha()  # Verifica se a string contém apenas letras
e_alnum = texto.isalnum()  # Verifica se a string contém letras e números
