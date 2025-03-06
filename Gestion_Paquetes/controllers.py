import pandas as pd
import os
from models import Package,User,Shipment,Invoice
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

    def SearchRecord(self,parameters):
        filtro = pd.Series(True, index=self.data.index)

        for columna, valor in parameters.items():
            if columna in self.data.columns:  
                filtro &= self.data[columna] == valor  
            else:
                print(f"Advertencia: La columna '{columna}' no existe en el DataFrame.")

        resultado = self.data[filtro]

        return resultado if not resultado.empty else "No se encontraron coincidencias."


    def Show(self):
        print(self.data)

class LoginManager(Manager):
    def __init__(self):
        super.__init__("Users")
        self.data = None
        self.Verify = ["Username","Password"]
        self.Data()

    def Login(self):
        Parameters = {"Username": input("Username: "),
                       "Password": input("Password: ")}
        resultado = self.SearchRecord(Parameters)
        return resultado.empty()
    
    def SignIn(self, User):
        self.AddRecord(User)

class PaymentsManager(Manager):
    def __init__(self):
        super.__init__("Payments")
        self.data = None
        self.Data()
    
    def AddPayment(self, payment):
        self.AddRecord(payment)
    
    def ShowPayments(self):
        self.Show()

class ShipmentsManager(Manager):
    def __init__(self):
        super().__init__("Shipments")
        self.data = None
        self.Data()

class PackagesManager(Manager):
    def __init__(self):
        super().__init__("Packages")
        self.data = None
        self.Data()