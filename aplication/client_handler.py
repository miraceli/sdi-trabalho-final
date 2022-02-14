import sys

from helpers.utils import get_replica

class ClientHandler:

    noRoutesMessage = 'Não há servidores ativos'

    def echo(self, message):
        conn = get_replica()

        if conn:
            conn.echo(message)
        else:
            print(noRoutesMessage)
            sys.exit(0)

    def get_messages(self):
        try:
            conn = get_replica()
            return conn.get_messages
        except AttributeError:
            print(noRoutesMessage)
            sys.exit(0)
