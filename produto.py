from conexao import conecta_db
from menu import opcoes_menu_resumido

def menu_produto(titulo):
    opcoes_menu_resumido(titulo)
    while True: 
        opcao = input("Escolha uma opção:  ")
        conexao = conecta_db()

        if opcao == "1":
            listar_produto(conexao)
            opcoes_menu_resumido(titulo)
        elif opcao == "2":
            listar_produto(conexao)
            consultar_produto_por_id(conexao)
            opcoes_menu_resumido(titulo)
        elif opcao == "3":
            inserir_produto(conexao)
            listar_produto(conexao)
            opcoes_menu_resumido(titulo)
        elif opcao == "4":
            listar_produto(conexao)
            atualizar_produto(conexao)
            listar_produto(conexao)
            opcoes_menu_resumido(titulo)
        elif opcao == "5":
            listar_produto(conexao)
            deletar_produto(conexao)
            listar_produto(conexao)
            opcoes_menu_resumido(titulo)
        elif opcao == "6":
            print("Sair")
            break
        else:
            print("Opção invalida, tente novamente")

def listar_produto(conexao):
    cursor = conexao.cursor()
    sql_listar = """ select p.id,p.nome,p.valor_venda,p.estoque,
                            p.categoria_id  as categoria_id,
                            c.id as id_categoria,
                            c.nome as nome_categoria 
                        from  produto p
                     inner join categoria c on (p.categoria_id = c.id)
                     order by p.id asc    
                  """

    # Execução do select no banco de dados
    cursor.execute(sql_listar)
    # recuperar todos registros
    registros = cursor.fetchall()
    print("|--------------------------------------------------------------------------|")
    for registro in registros:
        print(f"| ID: {registro[0]}  - Nome: {registro[1]} - Valor Venda: {registro[2]} - Estoque: {registro[3]} - Categoria: {registro[6]} ")
    print("|--------------------------------------------------------------------------|")

def consultar_produto_por_id(conexao):
    id = input("Digite o ID: ")
    cursor = conexao.cursor()
    cursor.execute("select id,nome,valor_venda, estoque from produto where id = " + id)
    registro = cursor.fetchone()

    if registro is None:
        print("Produto não encontrado:")
    else:
        print(f"| ID        ..: {registro[0]} ")
        print(f"| Nome        : {registro[1]} ")
        print(f"| Valor Venda : {registro[2]} ")
        print(f"| Estoque     : {registro[3]} ")

def inserir_produto(conexao):
    print("Inserindo o Produto ..: ")
    cursor = conexao.cursor()
   
    nome = input("Nome :")
    valor_venda = float(input("Valor Venda :"))
    estoque = float(input("Estoque :"))
    categoria_id = int(input("ID Categoria: "))

    sql_insert = "insert into produto (nome,valor_venda,estoque,categoria_id) values ( %s, %s,%s, %s )"
    dados = (nome,valor_venda,estoque,categoria_id)
    cursor.execute(sql_insert, dados)
    conexao.commit()

def atualizar_produto(conexao):
    print("Alterando dados dos Produtos")
    cursor = conexao.cursor()

    id   = input("Digite o ID : ")
    nome = input("Nome :")
    valor_venda = float(input("Valor Venda :"))
    estoque = float(input("Estoque :"))

    sql_update = "update produto set nome = %s, valor_venda = %s, estoque = %s where id = %s"
    dados = (nome,valor_venda,estoque,id)

    cursor.execute(sql_update,dados)
    conexao.commit()

def deletar_produto(conexao):
    print("Deletando Produto")
    cursor = conexao.cursor()
    id   = input("Digite o ID : ")
    sql_delete = "delete from produto where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
