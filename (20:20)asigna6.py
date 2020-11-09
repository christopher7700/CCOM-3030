
#=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asigna  #6                          Prof. Rafael J. Colorado       
#   Archivo: Asigna6                    Fecha: 10/02/2020
#   Dimensiones de Triangulo                                                                 
#=================================================================
#                                                                    
#   Propósito: Este programa, dado el peso en libras de una persona
#   y la estatura en pulgadas, calcula y despliega el
#   Índice de Masa Corporal y la condición de la persona.
#                             
#=================================================================

#Desplegar Proposito
print("\nProposito: Este programa, dado el peso en libras de una persona\
y la estatura en pulgadas, calcula y despliega el\
Índice de Masa Corporal y la condición de la persona.")

#Ingresar nombre
nombre=input("\nIngrese su nombre: ")

#Ingresar peso en Lbs & input validation >0
pesoLBS = float(input("\nIngrese su peso en Lbs: "))
while pesoLBS <=0 :
    print("ERROR. Deben ingresar un valor mayor de 0.")
    pesoLBS = float(input("\nIngrese su peso en Lbs: "))
    

#Ingresar altura en pulgadas & input validation >0
altPULG = float(input("\nIngrese su altura en pulgadas: "))
while altPULG <= 0 :
    print("ERROR. Deben ingresar un valor mayor de 0.")
    altPULG = float(input("\nIngrese su altura en pulgadas: "))
    
#Convertir el peso en libras a peso en kilogramos
pesoKILO = pesoLBS * 0.4536
    
#Convertir la estatura en pulgadas a estatura en metros
altMETR = altPULG * 0.0254

#Calcular el IMC utilizando la fórmula de Quetelet.

IMC = pesoKILO/altMETR ** 2
#Desplegar un mensaje que incluya siguiente información sobre la persona
#Determinar Condicion

print ('\n\t<<<<<<<<Resultados del paciente>>>>>>>>')
print("\n\tNombre ==============>",format(nombre))
print("\tPeso en libras=========>",format(pesoLBS,'4.2f'))
print('\tPeso en kilogramos=====>',format(pesoKILO,'4.2f'))
print('\tEstatura en pulgadas===>',format(altPULG,'4.2f'))
print('\tEstatura en metros=====>',format(altMETR,'4.2f'))
print('\tIndiceDeMasaCorporal===>',format(IMC,'4.2f'))

if IMC < 18.5 :
    print("\n\tCondicion =======> Bajo Peso")
elif IMC < 25.0 :
    print("\n\tCondicion =======> Peso Normal")
elif IMC < 30.0 :
    print("\n\tCondicion =======> Sobre Normal")
else :
    print("\n\tCondicion =======> Obeso")

#Finalizar Programa...
input('\nOprimar ENTER para terminar el programa...')




