import pandas as pd
import os
class Manager:
    def __init__(self, name):
        self.name = name
        self.n_elements = None
        self.data = None

    def Data(self):
        self.path = "./data/" + self.name + ".csv"   
        df = pd.read_csv(self.path) 
        self.data = df
    
    def AddRecord(self, record):
        NewRecord = pd.DataFrame([[record.values()]], columns = record.keys())
        self.data = pd.concat([self.data, NewRecord], ignore_index=True)
        self.data.to_csv(self.path, index=False)
        print("Datos agregados con exito")

    def EditRecord(self,record):
        SearchID = record['ID']
        for SearchID in self.data["ID"].values:
            self.data.loc[self.data["ID"] == SearchID] = record
            self.data.to_csv(self.path, index=False)
        else:
            print("No se encontro el registro a editar")

    def DeletedRecord(self,record):
        SearchID = record['ID']
        for SearchID in self.data["ID"].values:
            self.data.drop(self.data[self.data["ID"] == SearchID].index, inplace=True)
            self.data.to_csv(self.path, index=False)
        else:
            print("No se encontro el registro a eliminar")

    def Show(self):
        print(self.data)

class LoginManager(Manager):
    def __init__(self, username, password):
        self.username = username
        self.password = password

class PaymentsManager(Manager):
    def __init__(self, envio, monto):
        self.envio = envio
        self.monto = monto   