def menu():
  print("----------------------------------")
  print("-----Bienvenido al sistema-----")
  print("-----Registra tu alumno-----")
  print("1. Ingrese (s) si deseas agregar nuevo alumno")
  print("2. Ingrese (n) si deseas salir del programa")
  print("Escribe la opción que deseas realizar: ")
  print("----------------------------------")
  return input()

def ingresar_datos():
  id = len(alumnos) + 1
  cui = int(input("Ingrese el número de su dni: "))
  nombre = input("Ingrese el nombre del alumno: ")
  apellido = input("Ingrese el apellido del alumno: ")
  celular = int(input("Ingrese su número de celular: "))
  programa = input("Ingrese el programa de estudio: ")
  ciclo = input("Ingrese el ciclo académico: ")
  email = input("Ingrese su correo electrónico: ")
  alumnos.append({"id": id, "cui": cui, "nombre": nombre, "apellido": apellido, "celular": celular, "programa": programa, "ciclo": ciclo, "email": email})

alumnos = []

while True:
  opcion = menu()
  if opcion.lower() == "n":
    print("Saliendo del sistema")
    break
  elif opcion.lower() == "s":
    ingresar_datos()
  else:
    print("Opción errónea")

print(alumnos)