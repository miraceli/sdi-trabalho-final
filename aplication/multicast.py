from Pyro4 import expose, Proxy
from helpers.utils import get_servers

@expose
class MultiCast:
    def __init__(self):
        self._messages = []
        servers = get_servers()
        print("Servidores replicados no server:", int((len(list(servers.keys()))))+1)

    def echo(self, message):
        self._messages.append(message)
        servers = get_servers()

        if servers:
            for server in list(servers.keys()):
                conn = Proxy(servers[server])
                conn.overwrite_messages(self._messages)
        
        return "Mensagem recebida: {}".format(message)

    @property
    def get_messages(self):
        return self._messages

    def overwrite_messages(self, messages):
        self._messages = messages
