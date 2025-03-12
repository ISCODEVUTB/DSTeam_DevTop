from src.utils.utils import generate_id
import pandas as pd
import os
from src.utils.constants import NO_FOUND


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
