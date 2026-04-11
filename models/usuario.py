from utils.json_manager import JsonManager


class Usuario:
    def __init__(self, nombre, apellido, cedula, correo, telefono, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.correo = correo
        self.telefono = telefono
        self.tipo = tipo  # "estudiante" o "profesor"
        self.bloqueado = False
        self.bloqueado_hasta = None  # Fecha en formato "YYYY-MM-DD"
        self.historial_prestamos = []  # Lista de IDs de préstamos

    def __str__(self):
        return f"{self.nombre} {self.apellido} | Cédula: {self.cedula} | Tipo: {self.tipo}"

    # Método base — será sobreescrito por Estudiante y Profesor (polimorfismo)
    def dias_prestamo(self):
        return 7

    def estructura_json(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "cedula": self.cedula,
            "correo": self.correo,
            "telefono": self.telefono,
            "tipo": self.tipo,
            "bloqueado": self.bloqueado,
            "bloqueado_hasta": self.bloqueado_hasta,
            "historial_prestamos": self.historial_prestamos
        }

    def crear(self):
        manager = JsonManager("usuario")
        manager.write_json(self.estructura_json())