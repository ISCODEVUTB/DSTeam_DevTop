

class User:
    def __init__(self, user_id, username, password, name, email, address, permissions):
        """
        Representa un usuario con un ID, nombre de usuario, contraseña,
        nombre, email, dirección y permisos.
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.address = address
        self.permissions = permissions

    def __str__(self):
        """
        Devuelve una representación en cadena del usuario.
        """
        return (f"User {self.user_id}: {self.name} ({self.username}), "
                f"{self.email}, {self.address}, Permissions: {self.permissions}")
