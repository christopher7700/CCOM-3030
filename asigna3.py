#=================================================================
#   Programador: Christopher Rodriguez    CCOM 3030  Sección 002
#   Numero de estudiante: 801-16-7700     Primer Semestre 2020-21
#   Asigna3 Puntuaciones                  Prof. Rafael J. Colorado
#   Archivo: Asigna3.py                   Fecha: 02-09-2020
#
#=================================================================
#
#   Propósito:  Este programa, dado el nombre, número y las
#               últimas tres puntuaciones del estudiante,
#               calcula y despliega el nombre, número,
#               las últimas tres puntuaciones y el promedio
#               de las últimas tres puntuaciones del estudiante.
#
#=================================================================

# Desplegar el propósito del programa.

print('''\n\tEste programa, dado el nombre, número y las
\túltimas tres puntuaciones del estudiante,
\tcalcula y despliega el nombre, número,
\tlas últimas tres puntuaciones y el promedio
\tde las últimas tres puntuaciones del estudiante.\n''')

# Ingresar el nombre del estudiante.

Nombre = input("\tIngrese su nombre: ")

# Ingresar el número del estudiante.

Num_Estudiante = input("\tIngrese su número de estudiante (000-00-0000): ")

# Ingresar primera puntuación del estudiante, con input validation.

Puntuación1 = int(input("\tIngrese la puntuación #1 (Entre 0 y 100): "))
#Imput Validatio is below
while Puntuación1 < 0 or Puntuación1 > 100:
    print("\tERROR: La puntuación debe ser mayor de 0 y menor de 100.")
    Puntuación1 = int(input("\tIngrese la puntuación #1 (Entre 0 y 100): "))

# Ingresar segunda puntuación del estudiante, con input validation.

Puntuación2 = int(input("\tIngrese la puntuación #2 (Entre 0 y 100): "))
while Puntuación2 < 0 or Puntuación2 > 100:
    print("\tERROR: La puntuación debe estar entre 0 y 100.")
    Puntuación2 = int(input("\tIngrese la puntuación #2 (Entre 0 y 100): "))

# Ingresar tercera puntuación del estudiante, con input validation.

Puntuación3 = int(input("\tIngrese la puntuación #3 (Entre 0 y 100): "))
while Puntuación3 < 0 or Puntuación3 > 100:
    print("\tERROR: La puntuación debe estar entre 0 y 100.")
    Puntuación3 = int(input("\tIngrese la puntuación #3 (Entre 0 y 100): "))

# Calcular el promedio de las puntuaciones.

Promedio = (Puntuación1 + Puntuación2 + Puntuación3)/3.0

# Desplegar el el nombre, número, las últimas tres puntuaciones
# y el promedio de las últimas tres puntuaciones del estudiante.

print("\n\t<<< Información y Promedio del Estudiante >>>\n")
print("\tNombre ===========", format(Nombre))
print("\tNum. Estudiante.==", format(Num_Estudiante))
print("\tPuntuación #1 ====", format(Puntuación1))
print("\tPuntuación #2 ====", format(Puntuación2))
print("\tPuntuación #3 ====", format(Puntuación3))
print("\tPromedio =========", format(Promedio, '.2f'))

input("\n\tOprima ENTER para terminar el programa…")
