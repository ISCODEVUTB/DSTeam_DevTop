class Paquete:
    def __init__(self, nombre, peso, destino):
        self.nombre = nombre
        self.peso = peso
        self.destino = destino


class Usuario:
    def __init__(self, nombre, correo, contraseña, direccion):
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.direccion = direccion

class Envio:
    def __init__(self, usuario, paquete, costo, fecha):
        self.usuario = usuario
        self.paquete = paquete
        self.costo = costo
        self.fecha = fecha

class factura:
    def __init__(self, usuario, envio, costo, fecha):
        self.usuario = usuario
        self.envio = envio
        self.costo = costo
        self.fecha = fecha
    