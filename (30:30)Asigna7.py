
##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #7                      Prof. Rafael J. Colorado       
#   Archivo: asigna7                    Fecha: 10/18/2020
#    Desv&MEdi                                                               
#=================================================================
#                                                                    
#   Propósito:  Este Programa, dado un conjunto de datos calcula y despliega
#   la media aritmetica y la desviacion estandar de los datos
#                             
#=================================================================


#Desplegar Proposito
print("\n\tEste Programa, dado un conjunto de datos calcula y despliega\
\n\tla media aritmetica y la desviacion estandar de los datos.")

# Import Sqrt from math
from math import sqrt

#Increse cantidad de datos (n). + (n > 1 )  input validation.

N = int(input("\n\tIngrese el Numero de datos: "))
while N < 2:
    print("\tError. La cantidad debe ser mayor que 1.")
    N = int(input("\n\tIngrese el Numero de datos: "))


'''#Incluir dos variables que representen acumuladores'''
#Variable SumD
SumaD = 0.0

#Variable SumC
SumaC = 0.0

#Ciclo FOR
for a in range (0, N, 1) :
    Dato = float (input ("\tIngrese dato: "))
    SumaD = SumaD + Dato
    SumaC = SumaC + Dato ** 2

#Calcular Promedio y Desviacion
Medi = SumaD / N

Desv = sqrt ((N * SumaC - SumaD ** 2) / (N * (N - 1)))

#Desplegrar Promedio y Desviacion
print ("\n\tPromedio ====", format (Medi, '.2f'))
print ("\tDesviacion ==", format (Desv, '.2f'))
