import os
from datetime import datetime

def limpar_tela():
    os.system('cls')

# Função para exibir o título do hotel
def titulo_hotel():
    titulo = "\033[33mIsland Noronha Hotel\033[0m\n"
    terminal_width = os.get_terminal_size().columns
    print(titulo.center(terminal_width))

# Função para mostrar as instruções
def mostrar_instrucoes():
    print("\033[34m\nBem-vindo ao Sistema de Reservas do Island Noronha Hotel!\033[0m")
    print("\033[1mSiga as instruções para gerenciar suas reservas com facilidade.\033[0m\n")
    print("\033[33m********************************************************************************************************\033[0m")
    print("\033[34mInstruções de uso:\033[0m")
    print("\033[1m1. Digite seu nome quando solicitado.\033[0m")
    print("\033[1m2. Escolha o tipo de quarto desejado pelo número listado no sistema.\033[0m")
    print("\033[1m3. Informe as datas de entrada e saída no formato DD-MM-AAAA (Ex. 10-10-2024).\033[0m")
    print("\033[1m4. Após visualizar o valor total da estadia, selecione a forma de pagamento.\033[0m")
    print("\033[1m5. Após realizar uma reserva, use o menu para ver, editar, cancelar ou adicionar novas reservas.\033[0m")
    print("\033[1m6. Em 'Editar Reserva', você pode alterar as datas, o tipo de quarto ou o método de pagamento.\033[0m")
    print("\033[33m********************************************************************************************************\033[0m")

# Função para obter o nome do cliente (apenas letras)
def obter_nome_cliente():
    while True:
        nome_cliente = input("\033[1m\nDigite seu nome: \033[0m")
        if nome_cliente.isalpha():
            return nome_cliente
        else:
            print("\033[31mErro: O nome deve conter apenas letras. Tente novamente.\033[0m")

# Função para mostrar todos os quartos disponíveis
def mostrar_quartos_disponiveis(quartos):
    print("\033[36m\nQuartos disponíveis:\033[0m")
    for numero, detalhes in quartos.items():
        print(f"{numero}. {detalhes['tipo'].capitalize()}: {detalhes['camas']} cama(s), R$ {detalhes['preco']} por noite, {detalhes['disponiveis']} disponível(is)")

# Função para mostrar todas as reservas
def mostrar_reservas(reservas):
    if reservas:
        print("\033[36m\nReservas Atuais:\033[0m")
        for i, reserva in enumerate(reservas, 1):
            print(f"\033[35m{i}. {reserva}\033[0m")
    else:
        print("\033[31m\nNão há reservas ativas no momento.\033[0m")

# Função para cancelar uma reserva
def cancelar_reserva(reservas):
    mostrar_reservas(reservas)
    if reservas:
        escolha = int(input("\033[1m\nEscolha o número da reserva para cancelar: \033[0m")) - 1
        if 0 <= escolha < len(reservas):
            del reservas[escolha]
            print("\033[32mReserva cancelada com sucesso.\033[0m")
        else:
            print("\033[31mNúmero de reserva inválido.\033[0m")

# Função para editar uma reserva
def editar_reserva(reservas, quartos):
    mostrar_reservas(reservas)
    if reservas:
        escolha = int(input("\033[1m\nEscolha o número da reserva para editar: \033[0m")) - 1
        if 0 <= escolha < len(reservas):
            reserva = reservas[escolha]
            
            print("\n\033[34mEscolha o que deseja editar:\033[0m")
            print("1. Editar datas de entrada e saída")
            print("2. Editar tipo de quarto")
            print("3. Editar método de pagamento")
            opcao = input("\033[1mDigite a opção desejada: \033[0m")

            if opcao == '1':
                # Editar datas de entrada e saída
                while True:
                    try:
                        nova_data_entrada = datetime.strptime(input("\033[1mNova data de entrada (DD-MM-AAAA): \033[0m"), '%d-%m-%Y')
                        nova_data_saida = datetime.strptime(input("\033[1mNova data de saída (DD-MM-AAAA): \033[0m"), '%d-%m-%Y')
                        if nova_data_entrada < nova_data_saida:
                            reserva['data_entrada'] = nova_data_entrada.strftime('%d-%m-%Y')
                            reserva['data_saida'] = nova_data_saida.strftime('%d-%m-%Y')
                            reserva['noites'] = (nova_data_saida - nova_data_entrada).days
                            reserva['custo_total'] = quartos[reserva['tipo_quarto']]['preco'] * reserva['noites']
                            print("\033[32mDatas atualizadas com sucesso.\033[0m")
                            break
                        else:
                            print("\033[31mErro: a data de saída deve ser posterior à data de entrada.\033[0m")
                    except ValueError:
                        print("\033[31mData inválida. Use o formato DD-MM-AAAA.\033[0m")

            elif opcao == '2':
                # Editar tipo de quarto
                mostrar_quartos_disponiveis(quartos)
                novo_tipo_quarto = input("\033[1mEscolha o novo tipo de quarto (1-6): \033[0m")
                if novo_tipo_quarto in quartos:
                    reserva['tipo_quarto'] = novo_tipo_quarto
                    reserva['custo_total'] = quartos[novo_tipo_quarto]['preco'] * reserva['noites']
                    print("\033[32mTipo de quarto atualizado com sucesso.\033[0m")
                else:
                    print("\033[31mTipo de quarto inválido.\033[0m")

            elif opcao == '3':
                # Editar método de pagamento
                print("\n\033[34mNovas formas de pagamento:\033[0m")
                print("1. Cartão de Crédito")
                print("2. Cartão de Débito")
                print("3. Dinheiro")
                print("4. Transferência")
                novo_pagamento = input("\033[1mEscolha o novo método de pagamento (1-4): \033[0m")
                pagamento_opcoes = {
                    '1': "Cartão de Crédito",
                    '2': "Cartão de Débito",
                    '3': "Dinheiro",
                    '4': "Transferência"
                }
                novo_pagamento = pagamento_opcoes.get(novo_pagamento, "Opção inválida")
                if novo_pagamento != "Opção inválida":
                    reserva['pagamento'] = novo_pagamento
                    print("\033[32mMétodo de pagamento atualizado com sucesso.\033[0m")
                else:
                    print("\033[31mMétodo de pagamento inválido.\033[0m")
            else:
                print("\033[31mOpção inválida.\033[0m")
        else:
            print("\033[31mNúmero de reserva inválido.\033[0m")
    else:
        print("\033[31mNão há reservas para editar.\033[0m")

# Função para limpar o sistema para uma nova reserva

def sair():
    os.system('cls')
    titulo_hotel()
    mostrar_instrucoes()
    obter_nome_cliente()


# Função para processar uma nova reserva
def processar_reserva(nome_cliente, quartos, reservas):
    while True:
        mostrar_quartos_disponiveis(quartos)
        tipo_quarto = input("\033[1m\nEscolha o número do quarto (1 ao 6): \033[0m")
        if tipo_quarto in quartos:
            # Loop para garantir a entrada correta de datas
            while True:
                try:
                    data_entrada = datetime.strptime(input("\033[1mData de entrada (DD-MM-AAAA): \033[0m"), '%d-%m-%Y')
                    data_saida = datetime.strptime(input("\033[1mData de saída (DD-MM-AAAA): \033[0m"), '%d-%m-%Y')
                    if data_entrada < data_saida:
                        num_noites = (data_saida - data_entrada).days
                        custo_total = quartos[tipo_quarto]['preco'] * num_noites
                        break
                    else:
                        print("\033[31mErro: a data de saída deve ser posterior à data de entrada. Tente novamente.\033[0m")
                except ValueError:
                    print("\033[31mData inválida. Use o formato DD-MM-AAAA.\033[0m")

            # Exibir o valor total da reserva antes de escolher o pagamento
            print(f"\n\033[33m{nome_cliente.capitalize()}, o valor total da sua estadia de {num_noites} noite(s) será de: R$ {custo_total}\033[0m")

            # Formas de pagamento
            print("\n\033[34mFormas de pagamento:\033[0m")
            print("1. Cartão de Crédito")
            print("2. Cartão de Débito")
            print("3. Dinheiro")
            print("4. Transferência")
            pagamento = input("\033[1mEscolha a forma de pagamento (1-4): \033[0m")
            pagamento_opcoes = {
                '1': "Cartão de Crédito",
                '2': "Cartão de Débito",
                '3': "Dinheiro",
                '4': "Transferência"
            }
            pagamento = pagamento_opcoes.get(pagamento, "Opção inválida")

            # Confirmação da reserva
            if pagamento != "Opção inválida":
                quartos[tipo_quarto]['disponiveis'] -= 1
                reserva = {
                    'cliente': nome_cliente,
                    'tipo_quarto': tipo_quarto,
                    'data_entrada': data_entrada.strftime('%d-%m-%Y'),
                    'data_saida': data_saida.strftime('%d-%m-%Y'),
                    'noites': num_noites,
                    'pagamento': pagamento,
                    'custo_total': custo_total
                }
                reservas.append(reserva)
                print("\033[32m\nReserva confirmada!\033[0m")
            else:
                print("\033[31mReserva não concluída. Forma de pagamento inválida.\033[0m")
            break
        else:
            print("\033[31mOpção de quarto inválida. Tente novamente.\033[0m")

# Lista com tipos de quartos
quartos_hotel = {
    '1': {'tipo': 'solteiro', 'camas': 1, 'preco': 100, 'disponiveis': 5},
    '2': {'tipo': 'solteiro', 'camas': 2, 'preco': 200, 'disponiveis': 5},
    '3': {'tipo': 'duplo', 'camas': 1, 'preco': 180, 'disponiveis': 3},
    '4': {'tipo': 'duplo', 'camas': 2, 'preco': 360, 'disponiveis': 3},
    '5': {'tipo': 'suite', 'camas': 3, 'preco': 350, 'disponiveis': 2},
    '6': {'tipo': 'suite', 'camas': 4, 'preco': 700, 'disponiveis': 2}
}

reservas = []

# Executar o sistema
limpar_tela()
titulo_hotel()
mostrar_instrucoes()
nome_cliente = obter_nome_cliente()
processar_reserva(nome_cliente, quartos_hotel, reservas)

# Menu exibido ao fazer uma reserva
while True:
    print("\n\033[34mEscolha uma opção:\033[0m")
    print("1. Ver todas as reservas")
    print("2. Editar uma reserva")
    print("3. Cancelar uma reserva")
    print("4. Fazer mais uma reserva")
    print("5. Sair")
    opcao = input("\033[1mDigite a opção desejada: \033[0m")
    if opcao == '1':
        mostrar_reservas(reservas)
    elif opcao == '2':
        editar_reserva(reservas, quartos_hotel)
    elif opcao == '3':
        cancelar_reserva(reservas)
    elif opcao == '4':
        processar_reserva(nome_cliente, quartos_hotel, reservas)
    elif opcao == '5':
        sair()
    else:
        print("\033[31mOpção inválida. Tente novamente.\033[0m")
