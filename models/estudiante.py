class Estudiante(Usuario): 
  def __init__(self, nombre, apellido, cedula, correo, telefono, carnet, grado, seccion):
    super().__init__(nombre, apellido, cedula, correo, telefono, "estudiante")
    self.carnet = carnet
    self.grado = grado
    self.seccion = seccion

  

  