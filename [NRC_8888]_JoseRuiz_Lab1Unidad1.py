""" 
    Universidad de las Fuerzas Armadas ESPE Sede Santo Domingo de los Colorados
    Departamento Ciencias de la Computación
    Ingeniería en Tecnologías de la Información
    
    Autor: José Andres Ruiz Sarauz
    ID: L00380361
    Materia: Inteligencia Artificial

    Programación del Agente
    Agente: Robot Bibliotecario

""" 
#Se define la función que pertence al área de libros.
def Area_Libros():
    #Se inicializa el objetivo_area_1
    #Se indica que 0 es las estanterías de libros vacias y 1 las estanterías libros llenas.
    objetivo_area_1 = {'A': '1'}
    costo = 0
    #Nombre del area.
    print("\nArea de Libros\n")
    #Variable del area de libros que permitira ingresar por consola al usuario.
    localizacion_A = input("Digite el estado que se encuentra las estanterías del area de libros: ") 
    #Objetivo alcanzar del área de libros.
    print("Objetivo del area de libros:" + str(objetivo_area_1))
    #Se usa una condición para el funcionamiento del robot
    if localizacion_A == '0':
            #La estantería se encuentra vacia.
            print("La estanteria del area de libros esta vacio.")
            # Llena la estanteria de libro marcando completa.
            objetivo_area_1['A'] = '1'
            costo += 1 #Aumenta el costo del robot bibliotecario.
            print("La estanteria esta ya llena con libros respectivos.")
            print("Costo actual: " + str(costo))
            
    else:
        #La estantería se encuentra llena. Por lo tanto no se realiza ninguna acción
        print("La estanteria del area de libros se encuentra llena ninguna accion a realizar.")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado del área seleccionado, alcanzo el objetivo con el costo.    
    print("Estado del objetivo del area: ")
    print(objetivo_area_1)
    print("Medición del rendimiento: " + str(costo))

#******************************************************************************************************************
    
#Se define la función que pertence al área de bodega.
def Area_Bodega():
    #Se inicializa el objetivo_area_2
    #Se indica que 0 es las estanterías de libros vacias y 1 las estanterías libros llenas.
    objetivo_area_2 = {'B': '1'}
    costo= 0
    #Nombre del area.
    print("\nArea de Bodega\n")
    #Variable del área de bodega que permitira ingresar por consola al usuario.
    localizacion_B = input("Digite el estado que se encuentra las estanterías del area de bodega: ") 
    #Objetivo alcanzar del área de bodega.
    print("Objetivo del area de bodega:" + str(objetivo_area_2))
    #Se usa una condición para el funcionamiento del robot.
    if localizacion_B == '0':
            #La estantería se encuentra vacia.
            print("La estanteria del area de bodega esta vacio.")
            # Llena la estanteria de libro marcando completa.
            objetivo_area_2['B'] = '1'
            costo += 1 #Aumenta el costo del robot bibliotecario
            print("La estanteria esta ya llena con libros respectivos.")
            print("Costo actual: " + str(costo))
    else:
        #La estantería se encuentra llena. Por lo tanto no se realiza ninguna acción
        print("La estanteria del area de bodega se encuentra llena ninguna accion a realizar")
        print("Costo actual: " "("+ str(costo)+")")   
    #Se imprimira el resultado del área seleccionado, alcanzo el objetivo con el costo.  
    print("Estado del objetivo del area: ")
    print(objetivo_area_2)
    print("Medición del rendimiento: " + str(costo))  

#******************************************************************************************************************

#Se define la función que pertence al área de lectura.     
def Area_Lectura():
    #Se inicializa el objetivo_area_3
    #Se indica que 0 es las estanterías de libros vacias y 1 las estanterías libros llenas.
    objetivo_area_3 = {'C': '1'}
    costo = 0
     #Nombre del area.
    print("Area de Lectura\n")
    #Variable del área de lectura que permitira ingresar por consola al usuario.
    localizacion_C = input("Digite el estado que se encuentra las estanterías del area de libros: ") 
     #Objetivo alcanzar del área de lectura.
    print("Objetivo del area de libros:" + str(objetivo_area_3))
    #Se usa una condición para el funcionamiento del robot.
    if localizacion_C == '0':
            #La estantería se encuentra vacia.
            print("La estanteria del area de libros esta vacio.")
            # Llena la estanteria de libro marcando completa.
            objetivo_area_3['C'] = '1'
            costo += 1 #Aumenta el costo del robot bibliotecario
            print("La estanteria esta ya llena con libros respectivos")
            print("Costo actual: " + str(costo))
    else:
        #La estantería se encuentra llena. Por lo tanto no se realiza ninguna acción
        print("La estanteria del area de libros se encuentra llena ninguna accion a realizar")
        print("Costo actual: " "("+ str(costo)+")")
    #Se imprimira el resultado del área seleccionado, alcanzo el objetivo con el costo. 
    print("Estado del objetivo del area: ")
    print(objetivo_area_3)
    print("Medición del rendimiento: " + str(costo)) 
    
#******************************************************************************************************************
   
#Definiendo el programa con un menu estableciendo las opciones con las 3 áreas de la biblioteca
#Se inicializa en una variable llamada opcion la que permitira interactuar el usuario con el menu del robot
opcion=1
#Se utiliza el bucle while para cuando sea diferente de 4 para que interactue con las opciones
while opcion != 4:
    print("\n\t**** ROBOT BIBLIOTECARIO ****\n")
    #Se muestra las opciones
    print('1.Area de Libros\n2.Area de Bodega\n3.Area de Lectura\n4.Salir')
    #El usuario ingresa la opción
    opcion = int(input('\nIngresa el area que va supervisar: '))
    if opcion == 1:
        #Llama a las funciones ya determinadas
        Area_Libros()
    elif opcion == 2:
        Area_Bodega()
    elif opcion == 3:
        Area_Lectura()
    elif opcion == 4:
        #Opción para salir del programa del robot bibliotecario
        print('\nAPAGANDO ROBOT BIBLIOTECARIO.....ADIOS!\n')
    else:
        #Mensaje de error al escoger un número erroneo que no se encuentra en el menu
        print("\nINGRESE UNA DE LAS AREAS QUE SE ENCUENTRA EN LAS OPCIONES DEL ROBOT")
       