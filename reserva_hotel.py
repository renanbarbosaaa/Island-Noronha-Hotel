import os
os.system('cls')
from datetime import datetime

def titulo_hotel():
    titulo = "\033[33mIsland Noronha Hotel\033[0m\n"

    terminal_width = os.get_terminal_size().columns
    print(titulo.center(terminal_width))
    

titulo_hotel()

def mostrar_instrucoes():
    print("\033[34m\nBem-vindo ao Island Noronha Hotel!\033[0m")
    print("\033[1mSiga as instruções para realizar sua reserva.\033[0m\n")
    print("\033[33m********************************************************************************************************\033[0m")
    print("\033[34mInstruções de uso:\033[0m")
    print("\033[1m1. Digite seu nome quando solicitado.\033[0m")
    print("\033[1m2. Informe as datas de entrada e saída no formato DD-MM-AAAA. (Ex. 10-10-2024)\033[0m")
    print("\033[1m3. Escolha o tipo de quarto: solteiro, duplo ou suite.\033[0m")
    print("\033[1m4. Informe a quantidade de camas desejada, dentro do limite disponível para o tipo de quarto.\033[0m")
    print("\033[1m5. Escolha a forma de pagamento: Cartão de Crédito, Débito, Dinheiro ou Transferência.\033[0m")
    print("\033[33m********************************************************************************************************\033[0m")

mostrar_instrucoes()

cama_dispS = 5
cama_dispD = 4
cama_dispSu = 8

quartos_hotel = {
    '1. solteiro': {'camas': 1, 'preco': 100, 'disponiveis': 5},
    '2. solteiro': {'camas': 2, 'preco': 200, 'disponiveis': 5},
    '3. duplo': {'camas': 1, 'preco': 180, 'disponiveis': 3},
    '4. duplo': {'camas': 2, 'preco': 360, 'disponiveis': 3},
    '5. suite': {'camas': 3, 'preco': 350, 'disponiveis': 2},
    '6. suite': {'camas': 4, 'preco': 700, 'disponiveis': 2}
}

nome_cliente = input("\033[1m\nDigite seu nome: \033[0m")


print("\nQuartos disponíveis:")
for tipo, detalhes in quartos_hotel.items():
    print(f"{tipo.capitalize()}: {detalhes['camas']} cama(s), R$ {detalhes['preco']} por noite, {detalhes['disponiveis']} disponível(is)")


tipo_quarto = None
tipo_quarto = input("\nEscolha o tipo de quarto (1 ao 6): ").lower()
    

if tipo_quarto == 1:
    print(f"\n{nome_cliente}, você escolheu o quarto {tipo_quarto.capitalize()} com {num_camas} cama(s) por {num_noites} noite(s).") 


data_entrada = None
data_saida = None
data_valida = False
while not data_valida:
    try:
        data_entrada = datetime.strptime(input("Data de entrada (DD-MM-AAAA): "), '%d-%m-%Y')
        data_saida = datetime.strptime(input("Data de saída (DD-MM-AAAA): "), '%d-%m-%Y')
        if data_entrada < data_saida:
            data_valida = True
        else:
            print("Data de saída deve ser após a data de entrada.")
    except ValueError:
        print("Data inválida. Use o formato DD-MM-AAAA.")

num_noites = (data_saida - data_entrada).days
custo_total = quartos_hotel[tipo_quarto]['preco'] * num_noites
print(f"\n{nome_cliente}, você escolheu o quarto {tipo_quarto.capitalize()} com {num_camas} cama(s) por {num_noites} noite(s).")
print(f"Custo total: R$ {custo_total}")


print("\nFormas de pagamento:")
print("1. Cartão de Crédito")
print("2. Cartão de Débito")
print("3. Dinheiro")
print("4. Transferência")

pagamento = input("Escolha a forma de pagamento (1-4): ")
if pagamento == '1':
    pagamento = "Cartão de Crédito"
elif pagamento == '2':
    pagamento = "Cartão de Débito"
elif pagamento == '3':
    pagamento = "Dinheiro"
elif pagamento == '4':
    pagamento = "Transferência"
else:
    pagamento = "Opção inválida"


if pagamento != "Opção inválida":
    quartos_hotel[tipo_quarto]['disponiveis'] -= 1
    print(f"\nReserva confirmada! Pagamento via: {pagamento}")
    print(f"Obrigado, {nome_cliente}, por reservar conosco!")
else:
    print("Reserva não concluída. Forma de pagamento inválida.")
