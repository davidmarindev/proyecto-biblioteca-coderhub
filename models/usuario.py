class Usuario: 
  def __init__(self, nombre, apellido, cedula, correo, telefono):
    self.nombre = nombre
    self.apellido = apellido
    self.cedula = cedula
    self.correo = correo
    self.telefono = telefono

  def __str__(self):
    return f"{self.nombre} {self.apellido}, {self.cedula}, {self.correo}, {self.telefono}"

  def estructura_json(self):
    return {
      "nombre": self.nombre,
      "apellido": self.apellido,
      "cedula": self.cedula,
      "correo": self.correo,
      "telefono": self.telefono
    }

  def crear(self):
    manager = JsonManager("usuario")
    manager.write_json(self.estructura_json())