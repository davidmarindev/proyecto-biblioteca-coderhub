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
      raise ValueError("Entity not found")

  def read_json(self):
    with open(self.file_path, "r") as file:
      return json.load(file)

  def write_json(self, data):
    current_data = self.read_json()
    current_data.append(data)

    with open(self.file_path, "w") as file:
      json.dump(current_data, file, indent=2)