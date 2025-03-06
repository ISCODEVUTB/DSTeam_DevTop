import pandas as pd
import os
import re
from models import Package,User,Shipment,Invoice
class Manager:
    def __init__(self, name):
        self.name = name
        self.path = "./data/" + self.name + ".csv"  
        self.data = self.Data()

    def Data(self): 
        if os.path.exists(self.path):
            return pd.read_csv(self.path)
        else:
            print("Data no encontrada")
            return None 
        
    def SaveData(self):
        self.data.to_csv(self.path, index=False)
        print("Datos agregados con exito")

    def IDGenerator(self):
        if not self.data.empty and "ID" in self.data.columns:
            # Extraer números de los IDs existentes y encontrar el siguiente número
            existing_ids = self.data["ID"].dropna().astype(str)
            numbers = [int(re.search(r'\d+', id).group()) for id in existing_ids if re.search(r'\d+', id)]
            next_number = max(numbers) + 1 if numbers else 1
        else:
            next_number = 1  # Si no hay registros, empezar desde 1

        return f"{self.prefix}{next_number:04d}"  # Formato tipo U0001, P0001, etc.

    def AddRecord(self, record):
        NewRecord = pd.DataFrame([record], columns = record.keys())
        self.data = pd.concat([self.data, NewRecord], ignore_index=True)
        self.SaveData()

    def EditRecord(self,record):
        SearchID = record['ID']
        if SearchID in self.data["ID"].values:
            self.data.loc[self.data["ID"] == SearchID] = record
            self.SaveData()
        else:
            print("No se encontro el registro a editar")

    def DeletedRecord(self,record):
        SearchID = record['ID']
        if SearchID in self.data["ID"].values:
            self.data.drop(self.data[self.data["ID"] == SearchID].index, inplace=True)
            self.SaveData()
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
        super().__init__("Users")
        self.data = None
        self.Verify = ["Username","Password"]
        self.Data()

    def Login(self):
        Parameters = {"Username": input("Username: "),
                       "Password": input("Password: ")}
        resultado = self.SearchRecord(Parameters)
        return not resultado.empty
    
    def SignIn(self):
        User = User(self.IDGenerator())
        self.AddRecord(User)

class PaymentsManager(Manager):
    def __init__(self):
        super().__init__("Payments")
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