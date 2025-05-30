users = {"admin": "123"}
u = input("Usuario: ")
p = input("Contraseña: ")
print("Acceso" if users.get(u) == p else "Denegado")
