class Paquete:
    def __init__(self,id_paquete, nombre, peso, destino):
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.peso = peso
        self.destino = destino


class Usuario:
    def __init__(self, id_Usuario,nombre, correo, contraseña, direccion):
        self.id_Usuario = id_Usuario
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.direccion = direccion

class Envio:
    def __init__(self, id_envio, usuario, paquete, costo, fecha):
        self.id_envio = id_envio
        self.usuario = usuario
        self.paquete = paquete
        self.costo = costo
        self.fecha = fecha

class factura:
    def __init__(self, id_factura, usuario, envio, costo, fecha):
        self.id_factura = id_factura
        self.usuario = usuario
        self.envio = envio
        self.costo = costo
        self.fecha = fecha
    