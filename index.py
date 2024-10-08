import pandas as pd  # Importa a biblioteca pandas

# Lista para armazenar produtos
produtos = [
    ]

# Lista para armazenar vendas
vendas = []

# Função para cadastrar um novo produto
def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço por unidade: "))

    # Adiciona o produto à lista de produtos
    produtos.append({"codigo": codigo, "nome": nome, "quantidade": quantidade, "preco": preco})
    print("Produto cadastrado com sucesso!")  # Mensagem de sucesso

# Função para registrar uma venda
def registrar_venda():
    codigo = input("Digite o código do produto: ")
    quantidade_vendida = int(input("Digite a quantidade vendida: "))

    # Busca o produto pelo código
    produto_encontrado = None
    for produto in produtos:
        if produto["codigo"] == codigo:
            produto_encontrado = produto
            break

    # Se o produto for encontrado
    if produto_encontrado:
        # Atualiza a quantidade em estoque
        produto["quantidade"] -= quantidade_vendida
        # Calcula o valor total da venda
        valor_total = quantidade_vendida * produto["preco"]
        # Adiciona a venda à lista de vendas
        vendas.append({"codigo": codigo, "nome": produto["nome"], "quantidade": quantidade_vendida, "valor_total": valor_total})
        print("Venda registrada com sucesso!")  # Mensagem de sucesso

# Função para gerar o relatório de vendas em CSV
def gerar_relatorio_vendas():
    df_vendas = pd.DataFrame(vendas)  # Cria um DataFrame com as vendas
    df_vendas.to_csv("relatorio_vendas.csv", index=False)  # Salva em um arquivo CSV
    print("Relatório de vendas gerado com sucesso: relatorio_vendas.csv")  # Mensagem de sucesso

# Função para gerar o relatório de estoque em TXT
def gerar_relatorio_estoque():
    with open("relatorio_estoque.txt", "w") as f:  # Abre um arquivo para escrita
        for produto in produtos:  # Percorre a lista de produtos
            # Escreve as informações de cada produto no arquivo
            f.write(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Quantidade: {produto['quantidade']}\n")
    print("Relatório de estoque gerado com sucesso: relatorio_estoque.txt")  # Mensagem de sucesso

# Função para exibir o menu e gerenciar as opções do usuário
def menu():
    while True:
        print("\nMenu:")  # Exibe o menu
        print("1. Cadastrar Produto")
        print("2. Registrar Venda")
        print("3. Gerar Relatório de Vendas")
        print("4. Gerar Relatório de Estoque")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")  # Solicita a opção do usuário
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            registrar_venda()
        elif opcao == "3":
            gerar_relatorio_vendas()
        elif opcao == "4":
            gerar_relatorio_estoque()
        elif opcao == "5":
            print("Saindo do sistema...")  # Mensagem de saída
            break

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()  # Chama a função do menu