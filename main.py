from models.libro import Libro
from services.biblioteca import Biblioteca

biblioteca = Biblioteca("Biblioteca Escolar")

while True:
  print("1. Agregar libro")
  print("2. Listar libros")
  print("3. Crear prestamo")
  print("4. Salir")
  opcion = input("Seleccione una opcion: ")

  if opcion == "1":
    autor = input("Ingrese el autor: ")
    titulo = input("Ingrese el titulo: ")
    categoria = input("Ingrese la categoria: ")
    anio = input("Ingrese el año: ")
    codigo_isbn = input("Ingrese el codigo ISBN: ")
    editorial = input("Ingrese la editorial: ")
    nivel = input("Ingrese el nivel: ")
    libro = Libro(autor, titulo, categoria, anio, codigo_isbn, editorial, nivel)
    libro.crear()
  elif opcion == "2":
    libros = biblioteca.mostrar_catalogo()
    for libro in libros:
      print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Nivel: {libro['nivel']}, Disponible: {libro['disponible']}")
  elif opcion == "3":
    biblioteca.crear_prestamo()
  elif opcion == "4":
    break
  else:
    print("Opcion invalida")
