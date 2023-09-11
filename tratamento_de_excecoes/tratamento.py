try:
    # Bloco de código onde você suspeita que uma exceção possa ocorrer
    resultado = 10 / 0  # Isso causará uma exceção de divisão por zero
except ZeroDivisionError as erro:
    # Tratamento da exceção específica (divisão por zero)
    print(f"Erro: {erro}")
except Exception as erro:
    # Tratamento genérico de exceção (captura qualquer outra exceção)
    print(f"Erro genérico: {erro}")
else:
    # Opcional: código a ser executado se nenhum erro ocorrer no bloco 'try'
    print("Nenhum erro ocorreu.")
finally:
    # Opcional: código a ser executado sempre, independente de ter ocorrido erro ou não
    print("Este bloco será executado independentemente.")

# Continuação do programa após o tratamento de exceções
print("Programa continua...")
