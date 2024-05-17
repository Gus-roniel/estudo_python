class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.name = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password


c1 = Connection()

# usando uma função para atribuir um nome para o usuário
c1.set_user('Luiz')
print(c1.user)
