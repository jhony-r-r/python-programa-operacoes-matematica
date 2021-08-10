
numero_um = int(input("Digite o primeiro valor:"))
numero_dois = int(input("Digite o segundo valor:"))

selecionado = 0

while selecionado != 5:
    print(
        '[1] Adição',
        '[2] Subtração',
        '[3] Multiplicação',
        '[4] Divisão',
        '[5] Sair' 
        )

    selecionado = int(input("Selecione (conforme o número) a operação matematica que deseja realizar:"))

    if selecionado == 1:
        resultado = numero_um + numero_dois
        print("A adição dos valores atribuÍdos é de", resultado)
    
    elif selecionado == 2:
        resultado = numero_um - numero_dois
        print("A subtração dos valores atribuÍdos é de", resultado)

    elif selecionado == 3:
        resultado = numero_um * numero_dois
        print("A multiplicação dos valores atribuÍdos é de", resultado)

    elif selecionado == 4:
        resultado = numero_um / numero_dois
        print("A divisão dos valores atribuÍdos é de", resultado)

    elif selecionado == 5:
        print("Programa finalizado com sucesso.")
        
    else: 
        print("Informe uma opção válida.")