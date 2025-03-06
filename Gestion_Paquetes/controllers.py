class Manager:
    def __init__(self, name, n_elements):
        self.name = name
        self.n_elements = n_elements

    def Data(self):
        pass 
    
    def AddRecord(self):
        pass

    def EditRecord(self):
        pass

    def DeletedRecord(self):
        pass

    def Show(self):
        pass

class LoginManager(Manager):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class PaymentsManager(Manager):
    def __init__(self, envio, monto):
        self.envio = envio
        self.monto = monto   