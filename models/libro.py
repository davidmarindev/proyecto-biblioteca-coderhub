from utils.json_manager import JsonManager
class Libro():
  def __init__(self, autor, titulo, categoria, anio, codigo_isbn, editorial, nivel, disponible = True):
    self.autor = autor
    self.titulo = titulo
    self.categoria = categoria
    self.anio = anio
    self.codigo_isbn = codigo_isbn
    self.editorial = editorial
    self.nivel = nivel
    self.disponible = disponible

  def __str__(self):
    return f"{self.titulo}, {self.autor}, {self.anio}"

  def estructura_json(self):
    return {
      "autor": self.autor,
      "titulo": self.titulo,
      "categoria": self.categoria,
      "anio": self.anio,
      "codigo_isbn": self.codigo_isbn,
      "editorial": self.editorial,
      "nivel": self.nivel,
      "disponible": self.disponible
    }

  # Metodo de instancia
  def crear(self):
    manager = JsonManager("catalogo")
    manager.write_json(self.estructura_json())

  


  # @classmethod
  # def listar(cls):
  #   # managaer = JsonManager("catalogo")
  #   # return managaer.read_json()
  #   print("Listando libros...")


# Metodos de instacia

# Se aplican sobre la instacia que se esta creando o con la instancia actual en uso

# Metodos de clase

# Se aplican sobre la clase(Toda la clase, no sobre una instancia en particular)

# Metodos estaticos

# No se aplican ni sobre la clase ni sobre la instancia, se aplican sobre el metodo en si mismo

# libro = Libro("Gabriel Garcia Marquez", "Cien años de soledad", "Novela", "1967", "978-0307474728", "Sudamericana", "Secundaria", True)
# # libro.crear()
# Libro.listar()