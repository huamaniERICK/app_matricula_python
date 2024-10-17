
# - registrar alumnos.
# - generar fichas de matricula
# - mostrar la lista de todos los matriculados
# - filtrar matriculados por programa de estudio

lista_alumnos=[]


def mensaje_menu():
    menu_opciones="""
      -----Bienvenido al sistema--------
      -----Registra tu alumno----------
    1.ingrese (s) si deseas agregar nuevo alumno
    2. ingrese (n) si deseas salir del programa
    Escribe la opcion que deseas realizar:"""
    return menu_opciones

def ingrese_datos_alumno():
    id=len(lista_alumnos)+1
    cui=int(input(" ingrese el numero de su dni: "))
    nombre=input("ingrese el nombre del alumno: ")
    apellido=input("ingrese el apellido del alumno: ")
    numero_celular=int(input("ingrese su numero de celular: "))
    programa_estudio=input("ingrese el programa de estudio: ")
    ciclo_academico=input("ingrese el ciclo academico: ")
    email=input("ingrese su correo electronico: ")
    guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumno={
          "id":id,
          "cui":cui,
          "nombre":nombre,
          "apellido":apellido,
          "numero_celular":numero_celular,
          "programa_estudio":programa_estudio,
          "ciclo_academico":ciclo_academico,
          "email":email
        }
    lista_alumnos.append(alumno)

while True:
    menu_opciones=input(mensaje_menu())
    if menu_opciones.lower() == "n":
        print("saliendo del sistema ")
        break
    elif menu_opciones.lower() == "s":
      
      ingrese_datos_alumno()
    else:
        print("opcion erronea")

print (lista_alumnos)

# CREAR UN MODULO POR CADA FUNCION
    
    




