# Um dicionário em Python é uma estrutura de dados que permite armazenar informações
# em pares chave-valor, onde cada chave é única e mapeia para um valor associado.

# Criando um dicionário simples
pessoa = {
    "nome": "Alice",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores do dicionário por chave
nome_da_pessoa = pessoa["nome"]  # Retorna "Alice"
idade_da_pessoa = pessoa["idade"]  # Retorna 30

# Modificando valores no dicionário
pessoa["idade"] = 31  # Altera a idade para 31

# Adicionando novos pares chave-valor ao dicionário
pessoa["profissao"] = "Engenheira"

# Removendo pares chave-valor do dicionário
del pessoa["cidade"]

# Verificando se uma chave existe no dicionário
tem_nome = "nome" in pessoa  # Retorna True
tem_altura = "altura" in pessoa  # Retorna False

# Iterando pelas chaves e valores do dicionário
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
