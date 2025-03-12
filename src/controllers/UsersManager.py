from src.controllers.Manager import Manager


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
