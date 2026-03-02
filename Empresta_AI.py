#Login
materiais = [
    "1 " " Caneta"
    "2 " " Regua"
    "3 " " Lapis"
    "4 " " Borracha"
    "5 " " Calculadora"
    "6 " " Conteudos"
]
while True:
    print("\nDigite \n 1 Pedir material\n 2 Cadastrar(Login)\n")
    inicial = int(input())
    if inicial == 2:
        nome = input("Nome: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        continue
    elif inicial == 1:
        print(nome)
        verificação= input("senha: ")
        if verificação == senha:
            print(materiais)   
            cm = int(input("Material que deseja: "))    
            if cm == 1:
                print("Você pode usar esse material por 5 dias")
                break
            elif cm == 2:
                print("Você pode usar esse material por 3 dias")
                break
            elif cm == 3:
                print("Você pode usar esse material por 4 dias")
                break
            elif cm == 4:
                print("Você pode usar esse material por 14 dias")
                break
            elif cm == 5:
                print("Você pode usar esse material por 3 dias")
                break
            else:
                print("Você pode usar esse material por 1 dias")
                break


