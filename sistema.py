from cliente import menu_cliente
from categoria import menu_categoria

def menu_principal():
    print("|------------------------------------------|")
    print("|    Menu -> Programa                      |")
    print("|------------------------------------------|")
    print("|        1  -  Cliente                     |")
    print("|        2  -  Categoria                   |")
    print("|        3  -  Produto                     |")
    print("|        4  -  Usuario                     |")
    print("|        5  -  Vendas                      |")
    print("|        6  -  Sair do Sistema             |")
    print("|------------------------------------------|")

    while True: 
        opcao = input("Escolha uma opção:  ")

        if opcao == "1":
            menu_cliente()
        elif opcao == "2":
            menu_categoria("Categoria")
        elif opcao == "3":
            print("Cadastro de Produto")
        elif opcao == "4":
            print("Cadastro de Usuario")
        elif opcao == "5":
            print("Cadastro de Vendas")
        elif opcao == "6":
            print("Sair do sistema")
            break
        else:
            print("Opção invalida, tente novamente")
            
    
if __name__ == "__main__":
    menu_principal()