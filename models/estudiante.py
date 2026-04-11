from models.usuario import Usuario
from utils.json_manager import JsonManager


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, cedula, correo, telefono, carnet, grado, seccion):
        super().__init__(nombre, apellido, cedula, correo, telefono, "estudiante")
        self.carnet = carnet
        self.grado = grado
        self.seccion = seccion

    # Polimorfismo: sobreescribe el método del padre
    # El estudiante tiene 7 días para devolver un libro
    def dias_prestamo(self):
        return 7

    def estructura_json(self):
        datos = super().estructura_json()
        datos["carnet"] = self.carnet
        datos["grado"] = self.grado
        datos["seccion"] = self.seccion
        return datos

    def crear(self):
        manager = JsonManager("usuario")
        manager.write_json(self.estructura_json())