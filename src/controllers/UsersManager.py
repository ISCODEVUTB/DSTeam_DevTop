from controllers.Manager import Manager


class UserManager(Manager):
    def __init__(self):
        super().__init__("Users")
        self.prefix = "U"  # Prefijo para generar IDs de usuarios

    def update_user(self, user_id, **kwargs):
        """
        Actualiza los datos de un usuario existente.
        """
        user = self.search_record({"ID": user_id})
        if not user.empty:
            for key, value in kwargs.items():
                if value is not None:
                    user[key] = value
            record = user.iloc[0].to_dict()
            if "ID" not in record:
                record["ID"] = user_id
            self.edit_record(record)
            print(f"Usuario {user_id} actualizado con éxito.")
        else:
            print(f"Error: No se encontró el usuario con ID {user_id}.")

    def delete_user(self, user_id):
        """
        Elimina un usuario del sistema.
        """
        user = self.search_record({"ID": user_id})
        if not user.empty:
            record = user.iloc[0].to_dict()
            if "ID" not in record:
                record["ID"] = user_id
            self.delete_record(record)
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
