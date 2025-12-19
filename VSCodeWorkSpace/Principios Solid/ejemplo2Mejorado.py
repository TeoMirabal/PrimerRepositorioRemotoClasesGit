class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email


class GestorCorreo:
    def enviar_correo(self, destinatario, asunto, mensaje):
        print(
            f"Enviando correo a { destinatario} con asunto: {asunto} y mensaje: {mensaje}"
        )


class RegistroAcciones:
    def guardar_registro(self, accion):
        print(f"Guardando registro de acción: {accion}")


class GestorUsuarios:
    def __init__(self, gestor_correo, registro_accion):
        self.usuarios = []
        self.gestor_correo = gestor_correo
        self.registro_accion = registro_accion

    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)
        self.gestor_correo.enviar_correo(
            usuario.email, "Asunto : registro #34", "Gracias por registrarte"
        )
        self.registro_accion.guardar_registro(f"Registro de usuario: {usuario.nombre}")


gestor_correo = GestorCorreo()
registro_accion = RegistroAcciones()
gestor_usuarios = GestorUsuarios(gestor_correo, registro_accion)
gestor_usuarios.agregar_usuario("Juan", "juan@example.com")
