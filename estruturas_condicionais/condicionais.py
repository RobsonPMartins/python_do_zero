# Estruturas Condicionais em Python

# Exemplo 1: Verificando a idade
idade = 18

if idade < 18:
    print("Você é menor de idade.")
elif idade == 18:
    print("Você tem 18 anos, a maioridade legal.")
else:
    print("Você é maior de idade.")

# Exemplo 2: Verificando um número positivo, negativo ou zero
numero = 5

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# Exemplo 3: Verificando se um número é par ou ímpar
numero = 7

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
