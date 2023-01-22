
import csv  # Biblioteca para manipulação de arquivos csv
from datetime import date  # Biblioteca para captura da data atual
# Biblioteca para ordenação de matrizes de matrizes conforme uma determinada coluna das matrizes internas
from operator import itemgetter


# Classe representativa dos produtos no sistema utilizada para cálculos que envolvam estoque e lucros
class produto ():

    def __init__(self, codigo_produto, descricao_produto, estoque_min, estoque_disponivel, valor_custo, percentual_lucro):
        self.codigo_produto = codigo_produto
        self.descricao_produto = descricao_produto
        self.estoque_min = estoque_min
        self.estoque_disponivel = estoque_disponivel
        self.valor_custo = valor_custo
        self.percentual_lucro = percentual_lucro


# Função para captura da data atual em formato de texto
def dataAtual():

    data_atual = date.today()
    data_texto = data_atual.strftime('%d/%m/%Y')

    return data_texto


# Função para busca de determinados produtos no sistema
def consultaProduto(codigo_produto: int):

    with open("produtos.csv", encoding='latin-1') as produtos:
        produtos_reader = csv.reader(
            produtos, delimiter=';', lineterminator='\r')
        for l in produtos_reader:
            if (int(l[0]) == codigo_produto):
                produto_comprado = produto(l[0], l[1], int(
                    l[2]), int(l[3]), float(l[4]), int(l[5]))
                return produto_comprado

    return None


# Variável que determina se o programa deve ser encerrado
sair_sistema = 2

print("PADARIA OAK\n--------------------------------\nMENU\n")
while (sair_sistema == 2):

    opcao = input("""
    Escolha uma opção:
    1 - Cadastrar Clientes
    2 - Cadastrar Fornecedores
    3 - Cadastrar Produtos
    4 - Cadastrar Vendas
    5 - Cadastrar Compras
    6 - Relatório de Lucro por Forma de Pagamento
    7 - Relatório de Estado do Estoque
    8 - Sair do programa
    """)

    match opcao:

        # Cadastro de clientes no sistema com salvamento direto no arquivo csv
        case "1":
            print("CADASTRO DE CLIENTE\n____________________________\n")
            codigo_cliente = int(input("Código do cliente: "))
            nome_cliente = input("Nome: ")
            endereco_cliente = input("Endereço: ")
            telefone_cliente = input("Telefone: ")
            tipo_cliente = input("Tipo cliente (Pessoa F ou J): ")
            cadastro_cliente = input("CPF/CNPJ: ")
            ie_cliente = int(
                input("Inscrição estadual ([0] se não possuir): "))
            data_cadastro = dataAtual()
            try:
                with open("clientes.csv", 'a', encoding='utf-8') as clientes:
                    clientes_writer = csv.writer(
                        clientes, delimiter=';', lineterminator='\r')
                    clientes_writer.writerow([codigo_cliente, nome_cliente, endereco_cliente,
                                              telefone_cliente, data_cadastro, tipo_cliente, cadastro_cliente, ie_cliente])
            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1

            except:
                print("Erro de I/O")
                sair_sistema = 1

        # Cadastro de fornecedores no sistema com salvamento direto no arquivo csv
        case "2":
            print("CADASTRO DE FORNECEDOR\n____________________________\n")
            codigo_fornecedor = int(input("Código do fornecedor: "))
            nome_fornecedor = input("Nome: ")
            endereco_fornecedor = input("Endereço: ")
            telefone_fornecedor = input("Telefone: ")
            cadastro_fornecedor = input("CNPJ: ")
            representante_fornecedor = input("Representante: ")

            try:
                with open("fornecedores.csv", 'a', encoding='utf-8') as fornecedores:
                    fornecedores_writer = csv.writer(
                        fornecedores, delimiter=';', lineterminator='\r')
                    fornecedores_writer.writerow(
                        [codigo_fornecedor, nome_fornecedor, endereco_fornecedor, telefone_fornecedor, cadastro_fornecedor, representante_fornecedor])

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

        # Cadastro de produtos no sistema com salvamento direto no arquivo csv
        case "3":
            print("CADASTRO DE PRODUTO\n____________________________\n")
            codigo_produto = int(input("Código do produto: "))
            descricao_produto = input("Descrição: ")
            estoque_min = int(input("Estoque mínimo: "))
            estoque_disponivel = int(input("Estoque disponível: "))
            valor_custo = float(input("Valor de custo (R$): "))
            percentual_lucro = int(input("Percentual de lucro: "))

            try:
                with open("produtos.csv", 'a', encoding='utf-8') as produtos:
                    produtos_writer = csv.writer(
                        produtos, delimiter=';', lineterminator='\r')
                    produtos_writer.writerow(
                        [codigo_produto, descricao_produto, estoque_min, estoque_disponivel, valor_custo, percentual_lucro])

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1

            except:
                print("Erro de I/O")
                sair_sistema = 1

        # Cadastro de vendas no sistema com salvamento direto do arquivo csv
        case "4":
            print("CADASTRO DE VENDA\n____________________________\n")
            data_venda = dataAtual()
            codigo_produto = int(input("Código do produto: "))
            quantidade = int(input("Quantidade: "))
            modo_pagamento = input(
                "Modo de pagamento ($, X, D, C, T, F): ").upper()
            if modo_pagamento.lower() == 'f':
                codigo_cliente = int(input("Código do cliente: "))
            else:
                codigo_cliente = None

            try:
                with open("vendas.csv", 'a', encoding='utf-8') as vendas:
                    vendas_writer = csv.writer(
                        vendas, delimiter=';', lineterminator='\r')
                    vendas_writer.writerow(
                        [codigo_cliente, data_venda, codigo_produto, quantidade, modo_pagamento])

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

        # Cadastro de compras no sistema com salvamento direto do arquivo csv
        case "5":
            print("CADASTRO DE COMPRA\n____________________________\n")
            nota_fiscal = int(input("Número da NF (sem símbolos): "))
            codigo_fornecedor = int(input("Código do fornecedor: "))
            data_compra = dataAtual()
            codigo_produto = int(input("Código do produto: "))
            quantidade = int(input("Quantidade: "))

            try:
                with open("compras.csv", 'a', encoding='utf-8') as compras:
                    compras_writer = csv.writer(
                        compras, delimiter=';', lineterminator='\r')
                    compras_writer.writerow(
                        [nota_fiscal, codigo_fornecedor, data_compra, codigo_produto, quantidade])

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

        # Cálculo de de renda bruta e lucro, com salvamento direto no arquivo csv
        case "6":

            pagamentos = [['$', 0, 0], ['X', 0, 0], ['D', 0, 0],
                          ['C', 0, 0], ['T', 0, 0], ['F', 0, 0]]

            try:
                vendas = open('vendas.csv', encoding='utf-8')
                vendas_reader = csv.reader(
                    vendas, delimiter=';', lineterminator='\r')

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

            for i in vendas_reader:
                codigo_produto = int(i[2])
                x_produto = consultaProduto(codigo_produto)
                receita_bruta = int(i[3]) * (x_produto.valor_custo *
                                             (x_produto.percentual_lucro/100))
                lucro_venda = receita_bruta - \
                    (x_produto.valor_custo * int(i[3]))

                if i[4] == '$':

                    pagamentos[0][1] = receita_bruta
                    pagamentos[0][2] = lucro_venda

                elif i[4] == 'X':

                    pagamentos[1][1] = receita_bruta
                    pagamentos[1][2] = lucro_venda

                elif i[4] == 'D':

                    pagamentos[2][1] = receita_bruta
                    pagamentos[2][2] = lucro_venda

                elif i[4] == 'C':

                    pagamentos[3][1] = receita_bruta
                    pagamentos[3][2] = lucro_venda

                elif i[4] == 'T':

                    pagamentos[4][1] = receita_bruta
                    pagamentos[4][2] = lucro_venda

                elif i[4] == 'F':

                    pagamentos[5][1] = receita_bruta
                    pagamentos[5][2] = lucro_venda

            # Ordenando os pagamentos conforme o lucro
            pagamentos_ordenados = sorted(
                pagamentos, key=itemgetter(2), reverse=True)

            try:
                with open("4-vendaspgto.csv", 'w', encoding='utf-8') as vendaspgto:
                    vendaspgto_writer = csv.writer(
                        vendaspgto, delimiter=';', lineterminator='\r')
                    for p in pagamentos_ordenados:
                        vendaspgto_writer.writerow(
                            [p[0], p[1], p[2]])

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

        # Cálculo de estoque restante dos produtos após as vendas
        case "7":

            try:
                vendas = open('vendas.csv', 'r', encoding='utf-8')
                produtos = open('produtos.csv', 'r', encoding='utf-8')
                vendas_reader = csv.reader(
                    vendas, delimiter=';')
                produtos_reader = csv.reader(
                    produtos, delimiter=';')
            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

            lista_produtos = []

            for p in produtos_reader:
                lista_produtos.append([p[0], p[1], int(p[3]), int(p[2])])

            for v in vendas_reader:
                for p in lista_produtos:
                    if int(v[2]) == int(p[0]):
                        p[2] = p[2] - int(v[3])

            # Ordenando conforme descrição
            lista_ordenada = sorted(lista_produtos, key=itemgetter(1))

            try:
                with open("5-estoque.csv", 'w', encoding='utf-8') as estoques:
                    estoques_writer = csv.writer(estoques,
                                                 delimiter=';', lineterminator='\r')
                    for prod in lista_ordenada:
                        if prod[2] <= prod[3]:
                            estoques_writer.writerow(
                                [prod[0], prod[1], prod[2], 'COMPRAR MAIS'])
                        else:
                            estoques_writer.writerow(
                                [prod[0], prod[1], prod[2], ' '])

            except PermissionError as error:
                print("Erro de I/O")
                sair_sistema = 1
            except:
                print("Erro de I/O")
                sair_sistema = 1

            try:
                vendas.close()
                produtos.close()
            except:
                sair_sistema=2

        # Sair do sistema
        case "8":
            sair_sistema = 1

        # Opção Default
        case _:
            print("\nOpção inválida. Tente novamente.")
