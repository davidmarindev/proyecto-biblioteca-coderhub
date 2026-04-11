import json

BOOKS_FILE = "data/catalogo.json"
USERS_FILE = "data/usuarios.json"
LOANS_FILE = "data/prestamos.json"


class JsonManager:
    def __init__(self, entity):
        self.entity = entity
        self.file_path = self._get_file_path()

    def _get_file_path(self):
        if self.entity == "catalogo":
            return BOOKS_FILE
        elif self.entity == "usuario":
            return USERS_FILE
        elif self.entity == "prestamo":
            return LOANS_FILE
        else:
            raise ValueError(f"Entidad '{self.entity}' no reconocida.")

    def read_json(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def write_json(self, data):
        """Agrega un nuevo registro al archivo JSON."""
        registros = self.read_json()
        registros.append(data)
        self.guardar_todo(registros)

    def guardar_todo(self, datos):
        """Sobreescribe el archivo JSON con la lista completa de datos."""
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=2, ensure_ascii=False)