
class Usuarios:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def mostrar_info(self):
        return f"Usuario: {self.name }, Email: { self.email}"
    
userUno = Usuarios("Pepe", "pepe@gmail.com")
userDos = Usuarios("PepeDos", "pepedos@gmail.com")

numer_uno: int = 10

numer_dos = '20'
numer_dos = 20

print(userUno.mostrar_info())
print(userDos.mostrar_info())
