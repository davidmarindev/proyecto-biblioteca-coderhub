from utils.json_manager import JsonManager
from models.prestamo import Prestamo
from models.estudiante import Estudiante
from models.profesor import Profesor
from datetime import date, timedelta


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre

    # ── LIBROS ──────────────────────────────────────────────

    def mostrar_catalogo(self):
        manager = JsonManager("catalogo")
        return manager.read_json()

    # ── USUARIOS ─────────────────────────────────────────────

    def registrar_usuario(self):
        print("\n¿Qué tipo de usuario deseas registrar?")
        print("  1. Estudiante")
        print("  2. Profesor")
        tipo = input("Seleccione una opción: ")

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        cedula = input("Cédula: ")
        correo = input("Correo: ")
        telefono = input("Teléfono: ")

        if tipo == "1":
            carnet = input("Carnet: ")
            grado = input("Grado: ")
            seccion = input("Sección: ")
            usuario = Estudiante(nombre, apellido, cedula, correo, telefono, carnet, grado, seccion)
        elif tipo == "2":
            materia = input("Materia: ")
            departamento = input("Departamento: ")
            usuario = Profesor(nombre, apellido, cedula, correo, telefono, materia, departamento)
        else:
            print("Opción inválida.")
            return

        usuario.crear()
        print(f"\n✅ Usuario '{nombre} {apellido}' registrado correctamente.")

    def listar_usuarios(self):
        manager = JsonManager("usuario")
        return manager.read_json()

    def _buscar_usuario(self, cedula):
        """Busca un usuario por cédula y lo retorna como diccionario."""
        usuarios = self.listar_usuarios()
        for usuario in usuarios:
            if usuario["cedula"] == cedula:
                return usuario
        return None

    def _buscar_libro(self, isbn):
        """Busca un libro por código ISBN y lo retorna como diccionario."""
        libros = self.mostrar_catalogo()
        for libro in libros:
            if libro["codigo_isbn"] == isbn:
                return libro
        return None

    # ── PRÉSTAMOS ────────────────────────────────────────────

    def crear_prestamo(self):
        cedula = input("Ingrese la cédula del usuario: ")
        usuario = self._buscar_usuario(cedula)

        if usuario is None: # is None es igual a == None, pero es mas rapido
            print("❌ Usuario no encontrado.")
            return

        # Verificar si el usuario está bloqueado
        if usuario.get("bloqueado"):
            print(f"❌ El usuario {usuario['nombre']} está bloqueado hasta {usuario['bloqueado_hasta']}.")
            return

        isbn = input("Ingrese el ISBN del libro: ")
        libro = self._buscar_libro(isbn)

        if libro is None:
            print("❌ Libro no encontrado.")
            return

        if libro["disponible"] == False: # otra opcion: if not libro.get("disponible", True)
            print(f"❌ El libro '{libro['titulo']}' no está disponible.")
            return

        # Calcular días según el tipo de usuario (polimorfismo)
        if usuario["tipo"] == "estudiante":
            dias = 7
        else:
            dias = 30

        prestamo = Prestamo(isbn, cedula, usuario["tipo"], dias)
        prestamo.crear()

        # Marcar libro como no disponible
        self._actualizar_disponibilidad_libro(isbn, False)

        print(f"\n✅ Préstamo creado. Fecha límite de devolución: {prestamo.fecha_limite}")

    def devolver_libro(self):
        cedula = input("Ingrese la cédula del usuario: ")
        isbn = input("Ingrese el ISBN del libro a devolver: ")

        manager = JsonManager("prestamo")
        prestamos = manager.read_json()

        prestamo_encontrado = False

        for prestamo in prestamos:
            if prestamo["usuario_cedula"] == cedula and prestamo["codigo_libro"] == isbn and prestamo["estado"] == "activo":
                prestamo["estado"] = "devuelto"
                prestamo["fecha_devolucion"] = str(date.today())
                prestamo_encontrado = True

                # Verificar si la devolución fue tardía
                try:
                    fecha_limite = date.fromisoformat(prestamo["fecha_limite"])
                    fue_tardio = date.today() > fecha_limite
                except ValueError:
                    print("⚠️ Error al leer la fecha límite del préstamo.")
                    fue_tardio = False

                # Solo se bloquea al estudiante por devolución tardía
                if fue_tardio and prestamo["tipo_usuario"] == "estudiante":
                    fecha_bloqueo = str(date.today() + timedelta(days=30))
                    self._bloquear_usuario(cedula, fecha_bloqueo)
                    print(f"⚠️ Devolución tardía. El estudiante queda bloqueado hasta {fecha_bloqueo}.")
                elif fue_tardio:
                    print("⚠️ La devolución fue tardía, pero los profesores no son bloqueados.")

                break

        if not prestamo_encontrado:
            print("❌ No se encontró un préstamo activo con esos datos.")
            return

        # Guardar cambios en prestamos.json
        manager.guardar_todo(prestamos)

        # Marcar libro como disponible nuevamente
        self._actualizar_disponibilidad_libro(isbn, True)

        print("✅ Libro devuelto correctamente.")

    def listar_prestamos_activos(self):
        manager = JsonManager("prestamo")
        prestamos = manager.read_json()
        return [p for p in prestamos if p["estado"] == "activo"]

    def ver_historial_usuario(self):
        cedula = input("Ingrese la cédula del usuario: ")
        manager = JsonManager("prestamo")
        prestamos = manager.read_json()
        historial = [p for p in prestamos if p["usuario_cedula"] == cedula]
        return historial

    # ── HELPERS INTERNOS ─────────────────────────────────────

    def _actualizar_disponibilidad_libro(self, isbn, disponible):
        """Actualiza el campo 'disponible' de un libro en el JSON."""
        manager = JsonManager("catalogo")
        libros = manager.read_json()
        for libro in libros:
            if libro["codigo_isbn"] == isbn:
                libro["disponible"] = disponible
                break
        manager.guardar_todo(libros)

    def _bloquear_usuario(self, cedula, fecha_bloqueo):
        """Marca un usuario como bloqueado en el JSON."""
        manager = JsonManager("usuario")
        usuarios = manager.read_json()
        for usuario in usuarios:
            if usuario["cedula"] == cedula:
                usuario["bloqueado"] = True
                usuario["bloqueado_hasta"] = fecha_bloqueo
                break
        manager.guardar_todo(usuarios)