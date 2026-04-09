from utils.json_manager import JsonManager
from models.prestamo import Prestamo

class Biblioteca:
  def __init__(self, nombre):
    self.nombre = nombre

  def mostrar_catalogo(self):
    manager = JsonManager("catalogo")
    return manager.read_json()

  def crear_prestamo(self):
    codigo_libro = input("Ingrese el codigo del libro: ")
    usuario_id = input("Ingrese el id del usuario: ")
    fecha_prestamo = input("Ingrese la fecha de prestamo: ")
    prestamo = Prestamo(codigo_libro, usuario_id, fecha_prestamo)
    prestamo.crear()
    