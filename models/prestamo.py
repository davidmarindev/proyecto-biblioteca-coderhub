from utils.json_manager import JsonManager

class Prestamo(): 
  def __init__(self, codigo_libro, usuario_id, fecha_prestamo, fecha_devolucion=None):
    self.codigo_libro = codigo_libro
    self.usuario_id = usuario_id
    self.fecha_prestamo = fecha_prestamo
    self.fecha_devolucion = fecha_devolucion

  def __str__(self):
    return f"Libro: {self.codigo_libro}, Usuario: {self.usuario_id}, Fecha de prestamo: {self.fecha_prestamo}, Fecha de devolucion: {self.fecha_devolucion}"

  def estructura_json(self):
    return {
      "codigo_libro": self.codigo_libro,
      "usuario_id": self.usuario_id,
      "fecha_prestamo": self.fecha_prestamo,
      "fecha_devolucion": self.fecha_devolucion
    }

  def crear(self):
    manager = JsonManager("prestamo")
    manager.write_json(self.estructura_json())