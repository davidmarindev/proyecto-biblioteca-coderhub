from utils.json_manager import JsonManager

print("Hola mundo")

manager = JsonManager('usuario')
users = manager.read_json()["usuarios"]

print("Usuarios", users)

for usuario in users:
  print(f"Mi nombre es: {usuario['nombre']}")

uss = {"nombre": "Jose"}

manager.write_json(uss)