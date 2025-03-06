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
        self.prefix = "U"  # Prefijo para generar IDs de usuarios
        self.required_fields = ["Username", "Password"]  # Campos requeridos para el login
        self.Data()  # Cargar datos al inicializar

    def Login(self):
        """
        Método para autenticar a un usuario.
        Solicita el nombre de usuario y la contraseña, y verifica si coinciden con un usuario registrado.
        """
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if not username or not password:
            print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
            return False

        # Buscar el usuario en los registros
        user = self.SearchRecord({"Username": username, "Password": password})
        if user.empty:
            print("Error: Usuario o contraseña incorrectos.")
            return False

        print(f"Bienvenido, {username}!")
        return True

    def SignIn(self):
        """
        Método para registrar un nuevo usuario.
        Solicita los datos del usuario y lo registra en el sistema si no existe.
        """
        print("Registro de nuevo usuario:")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        email = input("Email: ").strip()
        address = input("Address: ").strip()
        permissions = input("Permissions: ").strip()

        # Validar que los campos obligatorios no estén vacíos
        if not username or not password:
            print("Error: El nombre de usuario y la contraseña son obligatorios.")
            return

        # Verificar si el usuario ya existe
        if not self.SearchRecord({"Username": username}).empty:
            print("Error: El nombre de usuario ya está en uso.")
            return

        # Generar un ID único para el nuevo usuario
        user_id = self.IDGenerator()

        # Crear el nuevo usuario y agregarlo al sistema
        new_user = User(user_id, username, password, email, address, permissions)
        self.AddRecord(new_user.__dict__)
        print(f"Usuario {username} registrado con éxito.")

    def ValidateInput(self, input_data):
        """
        Método para validar que los datos de entrada no estén vacíos.
        """
        for key, value in input_data.items():
            if not value:
                print(f"Error: El campo {key} no puede estar vacío.")
                return False
        return True

class PaymentsManager(Manager):
    def __init__(self):
        super().__init__("Payments")
        self.data = None
        self.Data()
    
    def AddPayment(self, payment):
        self.AddRecord(payment)
    
    def ShowPayments(self):
        self.Show()

class ShipmentManager(Manager):
    def __init__(self):
        super().__init__("Shipments")
        self.prefix = "S"  # Prefijo para generar IDs de envíos

    def CreateShipment(self):
        shipment_id = self.IDGenerator()
        package_id = input("ID del paquete: ")
        recipient_name = input("Nombre del destinatario: ")
        recipient_address = input("Dirección del destinatario: ")
        status = "Recolectado"  # Estado inicial del envío
        
        shipment = Shipment(shipment_id, package_id, recipient_name, recipient_address, status)
        self.AddRecord(shipment.__dict__)

    def UpdateShipmentStatus(self):
        shipment_id = input("ID del envío a actualizar: ")
        new_status = input("Nuevo estado (Recolectado, En tránsito, Entregado): ")
        
        shipment = self.SearchRecord({"ID": shipment_id})
        if not shipment.empty:
            shipment["Status"] = new_status
            self.EditRecord(shipment.iloc[0].to_dict())
        else:
            print("Envío no encontrado.")

    def SearchShipment(self):
        search_criteria = {
            "ID": input("ID del envío: "),
            "PackageID": input("ID del paquete: "),
            "RecipientName": input("Nombre del destinatario: "),
            "Status": input("Estado del envío: ")
        }
        result = self.SearchRecord(search_criteria)
        print(result)

class PackageManager(Manager):
    def __init__(self):
        super().__init__("Packages")
        self.prefix = "P"  # Prefijo para generar IDs de paquetes

    def AddPackage(self):
        ID = self.IDGenerator()
        dimensions = input("Dimensiones: ")
        weight = input("Peso: ")
        package_type = input("Tipo de paquete (básico, estándar, dimensionado): ")
        
        package = Package(ID, dimensions, weight, package_type)
        self.AddRecord(package.__dict__)

    def EditPackage(self):
        package_id = input("ID del paquete a editar: ")
        dimensions = input("Nuevas dimensiones: ")
        weight = input("Nuevo peso: ")
        package_type = input("Nuevo tipo de paquete (básico, estándar, dimensionado): ")
        
        package = Package(package_id, dimensions, weight, package_type)
        self.EditRecord(package.__dict__)

    def DeletePackage(self):
        package_id = input("ID del paquete a eliminar: ")
        package = Package(package_id, None, None, None)
        self.DeletedRecord(package.__dict__)

    def SearchPackage(self):
        search_criteria = {
            "ID": input("ID del paquete: "),
            "Dimensions": input("Dimensiones: "),
            "Weight": input("Peso: "),
            "Type": input("Tipo de paquete: ")
        }
        result = self.SearchRecord(search_criteria)
        print(result)

    class InvoiceManager(Manager):
        def __init__(self):
            super().__init__("Invoices")
            self.prefix = "I"  # Prefijo para generar IDs de facturas

        def GenerateInvoice(self):
            invoice_id = self.IDGenerator()
            shipment_id = input("ID del envío: ")
            payment_method = input("Método de pago (Tarjeta, PayPal, etc.): ")
            amount = input("Monto a pagar: ")
            
            invoice = Invoice(invoice_id, shipment_id, payment_method, amount)
            self.AddRecord(invoice.__dict__)

        def SearchInvoice(self):
            search_criteria = {
                "ID": input("ID de la factura: "),
                "ShipmentID": input("ID del envío: "),
                "PaymentMethod": input("Método de pago: "),
                "Amount": input("Monto: ")
            }
            result = self.SearchRecord(search_criteria)
            print(result)