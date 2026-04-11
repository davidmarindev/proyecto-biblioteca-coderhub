from models.libro import Libro
from services.biblioteca import Biblioteca

biblioteca = Biblioteca("Biblioteca Nacional")

while True:
    print("\n" + "═" * 35)
    print(f"   📚 {biblioteca.nombre}")
    print("═" * 35)
    print("  1. Agregar libro")
    print("  2. Listar libros")
    print("  3. Registrar usuario")
    print("  4. Listar usuarios")
    print("  5. Crear préstamo")
    print("  6. Devolver libro")
    print("  7. Ver préstamos activos")
    print("  8. Ver historial de usuario")
    print("  9. Salir")
    print("═" * 35)
    opcion = input("  Seleccione una opción: ")

    if opcion == "1":
        autor = input("Autor: ")
        titulo = input("Título: ")
        categoria = input("Categoría: ")
        anio = input("Año: ")
        codigo_isbn = input("ISBN: ")
        editorial = input("Editorial: ")
        nivel = input("Nivel (Primaria / Secundaria): ")
        libro = Libro(autor, titulo, categoria, anio, codigo_isbn, editorial, nivel)
        libro.crear()
        print("✅ Libro agregado al catálogo.")

    elif opcion == "2":
        libros = biblioteca.mostrar_catalogo()
        if not libros:
            print("El catálogo está vacío.")
        else:
            print("\n📖 Catálogo de libros:")
            for libro in libros:
                estado = "Disponible" if libro["disponible"] else "Prestado"
                print(f"  [{libro['codigo_isbn']}] {libro['titulo']} — {libro['autor']} | {estado}")

    elif opcion == "3":
        biblioteca.registrar_usuario()

    elif opcion == "4":
        usuarios = biblioteca.listar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados.")
        else:
            print("\n👤 Usuarios registrados:")
            for u in usuarios:
                bloqueo = f" 🔒 Bloqueado hasta {u['bloqueado_hasta']}" if u.get("bloqueado") else ""
                print(f"  [{u['cedula']}] {u['nombre']} {u['apellido']} | {u['tipo']}{bloqueo}")

    elif opcion == "5":
        biblioteca.crear_prestamo()

    elif opcion == "6":
        biblioteca.devolver_libro()

    elif opcion == "7":
        activos = biblioteca.listar_prestamos_activos()
        if not activos:
            print("No hay préstamos activos.")
        else:
            print("\n📋 Préstamos activos:")
            for p in activos:
                print(f"  ISBN: {p['codigo_libro']} | Cédula: {p['usuario_cedula']} | Límite: {p['fecha_limite']}")

    elif opcion == "8":
        historial = biblioteca.ver_historial_usuario()
        if not historial:
            print("No se encontraron préstamos para ese usuario.")
        else:
            print("\n📜 Historial de préstamos:")
            for p in historial:
                devolucion = p["fecha_devolucion"] if p["fecha_devolucion"] else "Pendiente"
                print(f"  ISBN: {p['codigo_libro']} | Estado: {p['estado']} | Prestado: {p['fecha_prestamo']} | Devuelto: {devolucion}")

    elif opcion == "9":
        print("👋 Hasta luego.")
        break

    else:
        print("❌ Opción inválida. Intente de nuevo.")
