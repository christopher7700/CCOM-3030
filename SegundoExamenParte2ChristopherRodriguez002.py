#Encabezamiento

##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   EXAMEN 2                            Prof. Rafael J. Colorado       
#   Archivo: Examen2                    Fecha: 11/2/2020
#                                                                  
#=================================================================
#                                                                    
#   Propósito: Este programa calcula y despliega el costo de la matrícula
#        de un semestre de los estudiantes de Ciencias Naturales
#        y despliega el recaudo total de la UPR por esta matrícula y deermina
#           si el estudiante aplica para beca o no.
#                             
#=================================================================

#Desplegar el Proposito.

print ("""\n\tEste programa calcula y despliega el costo de la matrícula
        de un semestre de los estudiantes de Ciencias Naturales
        y despliega el recaudo total de la UPR por esta matrícula y determina
        si el estudiante aplica para beca o no.""")

#Constantes a utilizar.

Costo_cred = 115.00
Costo_lab = 75.00
Cuota_mant = 47.00
Cuota_tecn = 25.00

#Ingresar la cantidad de estudiantes and Input validation.
Cantidad = int(input("\n\tCantidad de estudiantes: "))

while Cantidad < 1:

    print("\n\tERROR. Ingrese una cantidad mayor de 0.")
    Cantidad = int(input("\tCantidad de estudiantes: "))
    
#Accumulador 
Recaudo_total = 0.0

for Counter in range (1, Cantidad + 1):
    
    #Ingresar Num. de Eatudiante.
    Numest = str(input("\n\tNumero de estudiante: ")) 

    #Ingresar la cantidad de creditos e Input validation.    

    Creditos = int(input("\tCantidad de creditos: "))

    while Creditos < 12 or Creditos > 21: 
        print("\n\tERROR. Ingrese una cantidad entre 12 y 21.")

        Creditos = int(input("\tCantidad de creditos: "))

    #Cantidad de Labs e Input Validation.
    Laboratorios = int(input("\tIngrese la Cantidad de laboratorios: "))

    while Laboratorios < 0 or Laboratorios > 3:
        print("\n\tERROR. Cantidad debe ser entre 0 y 3.")
        Laboratorios = int(input("\n\tIngrese la Cantidad de laboratorios a tomar."))

    #Costo de  la Matricula
    Costo_creds = float(Costo_cred * Creditos)
    Costo_labs = float(Costo_lab * Laboratorios)
    Costo_mat = float(Costo_creds + Costo_labs + Cuota_mant + Cuota_tecn)

    print("\n\tNumero de Estudiante: ",Numest)
    print("\tCreditos: ", Creditos, '\t', "Costo: $", format(Costo_creds,',.2f'))
    print("\tLaboratorios:",Laboratorios , '\t', "Costo: $",format(Costo_labs, ',.2f'))
    print("\ttCuota de Mantenimiento: $",format(Cuota_mant,',.2f'))
    print("\tCuota de Tecnologia: $", format(Cuota_tecn, ',.2f'))
    print("\tCosto Total de Matricula: $",format(Costo_mat, ',.2f'))

    if Costo_mat <= 1800:
        print("\n\tEl estudiante NO cualifica para la beca.")
    else:
        print("\n\tEl estudiante cualifica para la beca.")

    #Recaudo Total
    Recaudo_total += Costo_mat
    
print("\n\tRecaudo por concepto de matrícula: $",format(Recaudo_total,',.2f'))


    






