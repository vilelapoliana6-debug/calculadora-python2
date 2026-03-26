def calcular_idade():
    nome = input("Digite seu nome completo: ")
    
    while True:
        try:
            
            # Pergunta o ano
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            
            # Verifica se está no intervalo correto
            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"\n--- Resultado ---")
                print(f"Nome: {nome}")
                print(f"Idade em 2022: {idade} anos")
                break # Se estiver tudo certo, o break encerra o laço
            else:
                print("Erro: O ano deve estar entre 1922 e 2021.")
                
        except ValueError:
            # Se o usuário digitar letras, este erro é ativado
            print("Erro: Por favor, digite um número válido para o ano.")

# Chama a função para rodar
calcular_idade()