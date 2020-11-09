'''
Encabezamiento
Proposito
Import from Math
Input longitud de los lados; anadir input validation
calcular semiperimetro
calcular perimetro
calcular area
Desplegar Dimensiones del triangulo
Terminar Programa
 '''


#Encabezamiento

#=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Examen  #1                          Prof. Rafael J. Colorado       
#   Archivo: Examen1                    Fecha: 09/21/2020
#   Dimensiones de Triangulo                                                                 
#=================================================================
#                                                                    
#   Propósito: Dadas las longitudes de los lados de un triángulo,
#   este programa calcula y despliega el área del
#   triángulo utilizando la fórmula de Herón.
#                             
#=================================================================

# Proposito

print('''\n\tDadas las longitudes de los lados de un triángulo,
\teste programa calcula y despliega el área del
\ttriángulo utilizando la fórmula de Herón.''')

# Import from Math
import math

# Input longitud de los lados; anadir input validation

long_A = float(input("\tIngrese Longuitud del primer lado: "))
while long_A <=0 :
    print("\tERROR. El valor a entrar debe ser mayor que 0.")
    long_A = float(input("\tIngrese Longuitud del primer lado: "))
    

long_B = float(input("\tIngrese Longuitud del segundo lado: "))
while long_B <=0 :
    print("\tERROR. El valor a entrar debe ser mayor que 0.")
    long_B = float(input("\tIngrese Longuitud del segundo lado: "))

long_C = float(input("\tIngrese Longuitud del tercer lado: "))
while long_C <=0 :
    print("\tERROR. El valor a entrar debe ser mayor que 0.")
    long_C = float(input("\tIngrese Longuitud del tercer lado: "))

# calcular semiperimetro
S = (long_A + long_B + long_C)/2

# calcular perimetro
P = S*2

# calcular area
A = math.sqrt(S*(S-long_A)*(S-long_B)*(S-long_C))

# Desplegar Dimensiones del triangulo
print("\n\t<<< Dimensiones del Triangulo >>>\n")

print("\tLongitud del primer lado ==", format(long_A, '.2f'))
print("\tLongitud del segundo lado =", format(long_B, '.2f'))
print("\tLongitud del tercer lado ==", format(long_C, '.2f'))

print("\tSemiperímetro =============", format(S, '.2f'))
print("\tPerímetro =================", format(P, '.2f'))
print("\tÁrea ======================", format(A, '.2f'))

#Terminar Programa
input("\nOprima ENTER para terminar el programa...")


