def calculadora():
    while True:
        print("\n--- Menu de Operações ---")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        
        opcao = input("\nDigite o número para a operação correspondente: ")

        if opcao == "0":
            print("Saindo do sistema...")
            break
        
        if opcao not in ["1", "2", "3", "4"]:
            print("Essa opção não existe")
            continue

        try:
            num1 = float(input("Digite o primeiro valor: "))
            num2 = float(input("Digite o segundo valor: "))
        except ValueError:
            print("Erro: Por favor, digite apenas números.")
            continue

        if opcao == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcao == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcao == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: Divisão por zero!")
            else:
                print(f"Resultado: {num1 / num2}")

calculadora()