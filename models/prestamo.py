from utils.json_manager import JsonManager
from datetime import date, timedelta


class Prestamo:
    def __init__(self, codigo_libro, usuario_cedula, tipo_usuario, dias):
        self.id = str(date.today()) + "_" + usuario_cedula + "_" + codigo_libro
        self.codigo_libro = codigo_libro
        self.usuario_cedula = usuario_cedula
        self.tipo_usuario = tipo_usuario  # "estudiante" o "profesor"
        self.fecha_prestamo = str(date.today())
        self.fecha_limite = str(date.today() + timedelta(days=dias))
        self.fecha_devolucion = None
        self.estado = "activo"  # "activo" o "devuelto"

    def __str__(self):
        return (
            f"Préstamo ID: {self.id}\n"
            f"  Libro: {self.codigo_libro}\n"
            f"  Usuario: {self.usuario_cedula} ({self.tipo_usuario})\n"
            f"  Prestado: {self.fecha_prestamo} | Límite: {self.fecha_limite}\n"
            f"  Estado: {self.estado}"
        )

    def esta_vencido(self):
        try:
            limite = date.fromisoformat(self.fecha_limite)
            return date.today() > limite
        except ValueError:
            print("Error: formato de fecha inválido.")
            return False

    def estructura_json(self):
        return {
            "id": self.id,
            "codigo_libro": self.codigo_libro,
            "usuario_cedula": self.usuario_cedula,
            "tipo_usuario": self.tipo_usuario,
            "fecha_prestamo": self.fecha_prestamo,
            "fecha_limite": self.fecha_limite,
            "fecha_devolucion": self.fecha_devolucion,
            "estado": self.estado
        }

    def crear(self):
        manager = JsonManager("prestamo")
        manager.write_json(self.estructura_json())