import os

from client_handler import ClientHandler
from constants.input_options import InputOptions


if __name__ == "__main__":
    client = ClientHandler()
    option = -1

    while option != InputOptions.EXIT:
        print("\n")
        print("{}) Nova mensagem".format(InputOptions.ECHO))
        print("{}) Listar mensagens".format(InputOptions.LIST))
        print("{}) Converter para maiúscula".format(InputOptions.UPPER))
        print("{}) Sair".format(InputOptions.EXIT))
        print("\n\n")

        try:
            option = int(input('Selecione uma opção: '))

            if option == InputOptions.ECHO:
                os.system('clear')
                message = input('Escreva sua mensagem: ')
                client.echo(message)

            elif option == InputOptions.LIST:
                os.system('clear')
                messages = client.get_messages()
                print('Listando Mensagens: {}'.format(messages))

            elif option == InputOptions.UPPER:
                os.system('clear')
                messages = client.get_messages()
                newmessages = str(messages).upper()
                print('Convertendo mensagens: {}'.format(newmessages))

            elif option == InputOptions.EXIT:
                os.system('clear')
                print('Aplicação encerrada...')

            else:
                print('Opção não existente')

        except ValueError:
            print('Opção inválida')
