from random import randint
#Login
materiais = [
    {"Mat": " Caneta", "tempo": randint(2, 15)},
    {"Mat": " Regua", "tempo": randint(2, 15)},
    {"Mat": " Lapis", "tempo": randint(2, 15)},
    {"Mat": " Borracha", "tempo": randint(2, 15)},
    {"Mat": " Calculadora", "tempo": randint(2, 15)},
    {"Mat": " Conteudos", "tempo": randint(2, 15)},
]
print("\nFazer Login")
nome = input("Nome: ")
email = input("E-mail: ")
senha = input("Senha: ")
    

print(f"\nOlá {nome}")
verificação= input("senha: ")
if verificação == senha:
    escolha = int(input('Emprestar para alguem(1)  |  Pegar emprestado(2)\n'))
    if escolha == 2:
        for i, mats in enumerate(materiais, start=1):
            print(f"\n{i}  {mats['Mat']}  por {mats["tempo"]} dias")
            print("  "+ "-" *40)   
        opc2 = input("\nDeseja escolher um desses materiais? (s/n)").lower()
        if opc2 == "s":
            print("\n+++ Busca por Material +++")
            busca = input("Digite o nome do material: ").lower()
            encontrado = False
            for mats in materiais:
                if busca in mats["Mat"].lower():
                    print(f'Aproveite seu {mats["Mat"]} por {mats["tempo"]} dias')
                    encontrado = True
            if not encontrado:
                print ("Nenhum material com esse nome.")
    else:
        Material = input("Material que vai emprestar: ")
        Tempo = int(input("Tempo: "))


        material_novo = {
            "Mat": Material,
            "tempo": Tempo,
        }
        materiais.append(material_novo)
        print("\nMaterial novo adicionado")
        for i, mats in enumerate(materiais, start=1):
            print(f"\n{i}  {mats['Mat']}  por {mats["tempo"]} dias")
            print("  "+ "-" *40)   

