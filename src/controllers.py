import pandas as pd
import os
from models import Package,User,Shipment,Invoice
from utils import validate_input, generate_id

NO_FOUND = "NO_FOUND"
class Manager:
    def __init__(self, name):
        """
        Inicializa el Manager con un nombre de archivo CSV.
        """
        self.name = name
        self.path = f"./data/{self.name}.csv"
        self.data = self.load_data()

    def load_data(self):
        """
        Carga los datos desde el archivo CSV.
        Si el archivo no existe, devuelve un DataFrame vacío.
        """
        if os.path.exists(self.path):
            return pd.read_csv(self.path)
        else:
            print(f"Advertencia: No se encontró el archivo {self.path}.")
            return pd.DataFrame()

    def save_data(self):
        """
        Guarda los datos en el archivo CSV.
        """
        self.data.to_csv(self.path, index=False)
        print("Datos guardados con éxito.")

    def id_generator(self):
        """
        Genera un ID único basado en los IDs existentes en el DataFrame.
        """
        existing_ids = self.data["ID"].dropna().astype(str)
        return generate_id(self.prefix, existing_ids)

    def add_record(self, record):
        """
        Agrega un nuevo registro al DataFrame y guarda los datos.
        """
        new_record = pd.DataFrame([record], columns=record.keys())
        self.data = pd.concat([self.data, new_record], ignore_index=True)
        self.save_data()

    def edit_record(self, record):
        """
        Edita un registro existente en el DataFrame y guarda los datos.
        """
        search_id = record['ID']
        if search_id in self.data["ID"].values:
            self.data.loc[self.data["ID"] == search_id] = record
            self.save_data()
        else:
            print(f"Error: No se encontró el registro con ID {search_id}.")

    def delete_record(self, record):
        """
        Elimina un registro del DataFrame y guarda los datos.
        """
        search_id = record['ID']
        if search_id in self.data["ID"].values:
            self.data.drop(self.data[self.data["ID"] == search_id].index, inplace=True)
            self.save_data()
        else:
            print(f"Error: No se encontró el registro con ID {search_id}.")

    def search_record(self, parameters):
        """
        Busca registros en el DataFrame basados en los parámetros proporcionados.
        """
        filtro = pd.Series(True, index=self.data.index)

        for columna, valor in parameters.items():
            if columna in self.data.columns:
                filtro &= self.data[columna] == valor
            else:
                print(f"Advertencia: La columna '{columna}' no existe en el DataFrame.")

        resultado = self.data[filtro]

        return resultado if not resultado.empty else print(NO_FOUND)

    def show(self):
        """
        Muestra el contenido actual del DataFrame.
        """
        print(self.data)

class LoginManager(Manager):
    def __init__(self):
        super().__init__("Users")
        self.prefix = "U"  # Prefijo para generar IDs de usuarios

    def login(self, username, password):
        """
        Autentica a un usuario en el sistema.
        """
        if not validate_input(username, password):
            print("Error: El nombre de usuario y la contraseña no pueden estar vacíos.")
            return False

        # Buscar el usuario en los registros
        user = self.search_record({"Username": username, "Password": password})
        if not user.empty:
            print(f"Bienvenido, {username}!")
            return True
        else:
            print("Error: Usuario o contraseña incorrectos.")
            return False

    def sign_in(self, username, password, name, email, address, permissions):
        """
        Registra un nuevo usuario en el sistema.
        """
        if not validate_input(username, password, name, email):
            print("Error: Todos los campos obligatorios deben ser completados.")
            return

        # Verificar si el usuario ya existe
        if not self.search_record({"Username": username}).empty:
            print("Error: El nombre de usuario ya está en uso.")
            return

        # Generar un ID único para el nuevo usuario
        user_id = self.id_generator()

        # Crear el nuevo usuario y agregarlo al sistema
        new_user = User(user_id, username, password, name, email, address, permissions)
        self.add_record(new_user.__dict__)
        print(f"Usuario {username} registrado con éxito.")

class PaymentsManager(Manager):
    def __init__(self):
        super().__init__("Payments")
        self.data = None
        self.save_data()
    
    def AddPayment(self, payment):
        self.AddRecord(payment)
    
    def ShowPayments(self):
        self.Show()

class ShipmentManager(Manager):
    def __init__(self):
        super().__init__("Shipments")
        self.prefix = "S"  # Prefijo para generar IDs de envíos

    def create_shipment(self, user_id, package_id, cost, date, state):
        """
        Crea un nuevo envío en el sistema.
        """
        shipment_id = self.id_generator()
        new_shipment = Shipment(shipment_id, user_id, package_id, cost, date, state)
        self.add_record(new_shipment.__dict__)
        print(f"Envío {shipment_id} creado con éxito.")

    def update_shipment_state(self, shipment_id, new_state):
        """
        Actualiza el estado de un envío existente.
        """
        shipment = self.search_record({"ID": shipment_id})
        if not shipment.empty:
            shipment["State"] = new_state
            self.edit_record(shipment.iloc[0].to_dict())
            print(f"Estado del envío {shipment_id} actualizado a {new_state}.")
        else:
            print(f"Error: No se encontró el envío con ID {shipment_id}.")

    def delete_shipment(self, shipment_id):
        """
        Elimina un envío del sistema.
        """
        shipment = self.search_record({"ID": shipment_id})
        if not shipment.empty:
            self.delete_record(shipment.iloc[0].to_dict())
            print(f"Envío {shipment_id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró el envío con ID {shipment_id}.")

    def search_shipment(self, search_criteria):
        """
        Busca envíos basados en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print(NO_FOUND)

class PackageManager(Manager):
    def __init__(self):
        super().__init__("Packages")
        self.prefix = "P"  # Prefijo para generar IDs de paquetes

    def add_package(self, description, sizes, weight, type):
        """
        Registra un nuevo paquete en el sistema.
        """
        package_id = self.id_generator()
        new_package = Package(package_id, description, sizes, weight, type)
        self.add_record(new_package.__dict__)
        print(f"Paquete {package_id} registrado con éxito.")

    def update_package(self, package_id, description = None , sizes = None, weight=None, type=None):
        """
        Actualiza los datos de un paquete existente.
        """
        package = self.search_record({"ID": package_id})
        if not package.empty:
            if description is not None:
                package["Description"] = description
            if sizes is not None:
                package["Sizes"] = sizes
            if weight is not None:
                package["Weight"] = weight
            if type is not None:
                package["Type"] = type
            self.edit_record(package.iloc[0].to_dict())
            print(f"Paquete {package_id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró el paquete con ID {package_id}.")

    def delete_package(self, package_id):
        """
        Elimina un paquete del sistema.
        """
        package = self.search_record({"ID": package_id})
        if not package.empty:
            self.delete_record(package.iloc[0].to_dict())
            print(f"Paquete {package_id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró el paquete con ID {package_id}.")

    def search_package(self, search_criteria):
        """
        Busca paquetes basados en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print("NO_FOUND")
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

class InvoiceManager(Manager):
    def __init__(self):
        super().__init__("Invoices")
        self.prefix = "I"  # Prefijo para generar IDs de facturas

    def generate_invoice(self, user_id, shipment_id, cost, date):
        """
        Genera una nueva factura en el sistema.
        """
        invoice_id = self.id_generator()
        new_invoice = Invoice(invoice_id, user_id, shipment_id, cost, date)
        self.add_record(new_invoice.__dict__)
        print(f"Factura {invoice_id} generada con éxito.")

    def update_invoice(self, invoice_id, cost=None, date=None):
        """
        Actualiza los datos de una factura existente.
        """
        invoice = self.search_record({"ID": invoice_id})
        if not invoice.empty:
            if cost is not None:
                invoice["Cost"] = cost
            if date is not None:
                invoice["Date"] = date
            self.edit_record(invoice.iloc[0].to_dict())
            print(f"Factura {invoice_id} actualizada con éxito.")
        else:
            print(f"Error: No se encontró la factura con ID {invoice_id}.")

    def delete_invoice(self, invoice_id):
        """
        Elimina una factura del sistema.
        """
        invoice = self.search_record({"ID": invoice_id})
        if not invoice.empty:
            self.delete_record(invoice.iloc[0].to_dict())
            print(f"Factura {invoice_id} eliminada con éxito.")
        else:
            print(f"Error: No se encontró la factura con ID {invoice_id}.")

    def search_invoice(self, search_criteria):
        """
        Busca facturas basadas en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print("NO_FOUND")

class UserManager(Manager):
    def __init__(self):
        super().__init__("Users")
        self.prefix = "U"  # Prefijo para generar IDs de usuarios

    def update_user(self, user_id, username=None, password=None, name=None,
                    email=None, address=None, permissions=None):
        """
        Actualiza los datos de un usuario existente.
        """
        user = self.search_record({"ID": user_id})
        if not user.empty:
            if username is not None:
                user["Username"] = username
            if password is not None:
                user["Password"] = password
            if name is not None:
                user["Name"] = name
            if email is not None:
                user["Email"] = email
            if address is not None:
                user["Address"] = address
            if permissions is not None:
                user["Permissions"] = permissions
            self.edit_record(user.iloc[0].to_dict())
            print(f"Usuario {user_id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró el usuario con ID {user_id}.")

    def delete_user(self, user_id):
        """
        Elimina un usuario del sistema.
        """
        user = self.search_record({"ID": user_id})
        if not user.empty:
            self.delete_record(user.iloc[0].to_dict())
            print(f"Usuario {user_id} eliminado con éxito.")
        else:
            print(f"Error: No se encontró el usuario con ID {user_id}.")

    def search_user(self, search_criteria):
        """
        Busca usuarios basados en criterios específicos.
        """
        result = self.search_record(search_criteria)
        if not result.empty:
            print(result)
        else:
            print("NO_FOUND")