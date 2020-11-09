

##=================================================================                                                 
#   Programador: Chritopher Rodriguez   CCOM 3030    Sección 002     
#   Numero de estudiante: 801-16-7700   Primer Semestre 2020-21       
#   Asignación  #8                      Prof. Rafael J. Colorado       
#   Archivo: asigna8                    Fecha: 11/1/2020
#    Media                                                               
#=================================================================
#                                                                    
#   Propósito: Este programa calcula la media aritmeica
#   de las puntuaciones
#                             
#=================================================================




#Proposito
print('''\n\tEste programa calcula la media aritmeica
\tde las puntuaciones''')

#Leer la cantidad de puntuaciones
cantidad = int(input("\n\tIndique la cantidad de puntuaciones: "))
while cantidad < 1:
    print("\tERROR. El numero a ingresar debe ser mayor que 1")
    cantidad = int(input("\n\tIndique la cantidad de puntuaciones: "))


#Leer cada una de las puntuaciones
suma = 0.0
for puntos in range(1,cantidad+1):
    dato = int(input("\n\tIngrese la puntuacion:"))
    suma += dato
    

#Calcular y desplegar la media aritmética
media = suma / cantidad


#Mensaje correspondiente de Media
if media >= 90:
    print("\n\tEl grupo salió muy bien")
elif media >= 80:
    print("\n\tEl grupo salió bien")
elif media >= 70 :
    print('\n\tEl grupo salio regular')
elif media >= 60 :
    print("\n\tEl grupo salio mal")
else:
    print("\n\tEl grupo salio muy mal")

#Desplegar promedio
print("\tPromedio: ",format(media,'.2f'))
    
