from models.usuario import Usuario
from utils.json_manager import JsonManager


class Profesor(Usuario):
    def __init__(self, nombre, apellido, cedula, correo, telefono, materia, departamento):
        super().__init__(nombre, apellido, cedula, correo, telefono, "profesor")
        self.materia = materia
        self.departamento = departamento

    # Polimorfismo: sobreescribe el método del padre
    # El profesor tiene 30 días para devolver un libro
    def dias_prestamo(self):
        return 30

    def estructura_json(self):
        datos = super().estructura_json()
        datos["materia"] = self.materia
        datos["departamento"] = self.departamento
        return datos

    def crear(self):
        manager = JsonManager("usuario")
        manager.write_json(self.estructura_json())
