from functions.gerarQRcode import *
from functions.guardarColaborador import *
from functions.lerQRcode import *
from functions.puxarColaborador import *

menu = '''

- 1️⃣ Gerar um QRcode de um colaborador -
- 2️⃣ Ler QRcode -
- 3️⃣ Guardar colaboradores do dia em um aquivo .csv -
- 4️⃣ Puxar colaborador específico de um arquivo .csv -
- 5️⃣ Sair -

'''

print(menu)

while True:
    acao = input('Deseja qual opcão?: ')

    match acao:

        case "1":
            nome_colaborador = input('Nome do colaborador: ')
            gerarQrcode(nome_colaborador)
        case "2":
            lerQrcode()
        case "3":
            guardar_colaborador()
        case "4":
            nome_colaborador = input("Nome do colaborador: ")
            nome_csv = input("Digite o path do arquivo.csv: ")
            print(puxar_colaborador(nome_colaborador, nome_csv))
        case "5":
            break
        case _:
            print('Opção inválida, digite novamente')
