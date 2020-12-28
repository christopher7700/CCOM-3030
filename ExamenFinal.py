#=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Examen  #3                          Prof. Rafael J. Colorado       
#   Archivo: Examen3                    Fecha: 12/18/2020
#   Examen Final                                                                 
#=================================================================
#                                                                    
#   Propósito: Este programa: Calcua el salario semanal de una lista de
#           empleados y la nómina total de la empresa Brisas del Caribe.
#                             
#=================================================================

def main():
    #Desplegar proposito
    Desplegar_Proposito()
    
    
    #Leer los datos
    Cantidad,Numero,Salario,Horas = Leer_Datos()

    #Calcular los salarios
    SalarioTotal = Calcular_Salario(Salario,Horas)

     #Desplegar resultados
    Desplegar_Resultados(Cantidad,Numero,Salario,Horas,SalarioTotal)


######################################
#nombre:Desplegar_Proposito()
#Proceso: Despliega el proposito del programa
#Input:nada
#output:nada
######################################
def Desplegar_Proposito():
    print("""\n\tEste programa: Calcua el salario semanal de una lista de
    \templeados y la nómina total de la empresa Brisas del Caribe.""")




######################################
#nombre:Leer_Datos()
#Proceso: 
#Input: nada
#output: La lista con el número de empleado de cada empleado,
#        La lista con el salario por hora de cada empleado,
#        La lista con las horas semanales trabajadas por cada empleado

######################################

def Leer_Datos():

    #Leer cantidad de empleados
    Cantidad_empleados = int(input("\n\tIngrese la cantidad de empleados > 0: "))
    while Cantidad_empleados <= 0:
        print("\tError. cantidad de empleados > 0")
        Cantidad_empleados = int(input("\n\tIngrese la cantidad de empleados > 0: "))

    #Iniciar la lista a Nula o Vacia.
    Numero_ID = []
    Salario = []
    Horas_worked = []

    #Ingresar y anadir los datos

    for k in range(1,Cantidad_empleados+1):

        #Leer num del empleado

        print("\n\tIngrese Numero del empleado (4 digitos)",k,": ",end='')
        Dato = str(input())
        while len (Dato) != 4 or not Dato.isdigit ():
            print("\tError. EL numero debe ser de cuatro digitos.")
            print("\n\tIngrese Numero del empleado (4 digitos)",k,": ",end='')
            Dato = str(input())
          

        #Anadir el dato a la lista de Numero_ID
        Numero_ID.append(Dato)

        #Leer Salario de Empleados
        print("\n\tIngrese el salario por hora del empleado",k,"(>0): ",end='')
        pay = float(input())
        while pay <= 0:
            print("\tError. El salario del empleado debe ser mayor de creo(>0)")
            print("\n\tIngrese el salario por hora del empleado",k,"(>0): ",end='')
            pay = float(input())

        #Anadir el pay a la lista de Salario
        Salario.append(pay)


        #Leer horas trabajadas
        print("\n\tIngrese las horas tabajadas del empleado",k,"(entre 0 y 40): ",end='')
        Time = float(input())
        while Time < 0 or Time > 40:
            print("\tError. Las horas de trabajo semanal deben ser entre(0-40)")
            print("\n\tIngrese las horas tabajadas del empleado",k,"(entre 0 y 40): ",end='')
            Time = float(input())
        #Anadir las horas trabajadas a la lista
        Horas_worked.append(Time)

    
    #Devolver
    return Cantidad_empleados, Numero_ID, Salario, Horas_worked
            
    
######################################
#nombre: Calcular_Salario
#Proceso: Calcula el salario semanal de cada empleado.
#Input: lista de salarios y lista de horas trabajadas
#output:lista de salarios semanales de los empleados.

######################################
def Calcular_Salario(Salario,Horas_worked):

    #Inicia contador a 0
    Salario_semanal = []

    #cotejar en la lista
    for i in range(0,len(Salario)):
        Salario_semanal.append(Salario[i]*Horas_worked[i])
        
    return Salario_semanal 
    
########################################
#nombre: Desplegar_Resultados
#Proceso: Desplega los resultados de la lista
#Input:Cantidad,Numero,Salario,Horas,SalarioTotal
#output:No devuelve nada

########################################
def Desplegar_Resultados(Cantidad,Numero,Salario,Horas,SalarioTotal):
   print("\n\t\t\t<<< Resultado de la empresa Brisas del Caribe>>>")
   print("\n\t\t\tNumero\t\tSal/hora\t\tHoras\t\tSalario/semana")

   for resultado in range (len(SalarioTotal)):
       print("\t\t    ", resultado+1, ")",Numero[resultado],"\t\t$",Salario[resultado],
         "\t\t$",Horas[resultado],"\t\t$",SalarioTotal[resultado])
       
   print("\n\tNomina Total: $",format(sum(SalarioTotal),'4,.2f'))
             
        

####################################################################
main()
