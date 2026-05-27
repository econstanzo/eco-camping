print("Gestión Eco-Camping 'Bosque Vivo'")
capacidad_maxima = 15
sitios_ocupados = 0
ejecutando = True
while ejecutando:
    print("\n=== MENÚ DE CONTROL DE REGISTROS")
    print("1.-Ver sitios disponibles")
    print("2.-Registro de nuevos vehículos en el sitio (Entrada)")
    print("3.-Registro de Salida de vehículo (Salida)")
    print("4.-Estado actual del camping")
    print("5.-Salir")
    try:
        opcion = int(input("Seleccione una opción (1-5)"))
    except ValueError:
        print("Opción no válida, por favor selección entre 1 y 5")
        continue
    #Despliegue de opciones
    if opcion == 1
        disponibles = capacidad_maxima - sitios_ocupados
        print(f"\n[INFO] Sitios libres para recibir vehículos:  {disponibles}")
    elif opcion == 2
        sitios_libre = capacidad_maxima - sitios_ocupados
        if sitios_libre == 0:
            print("Lo sentimos, no quedan espacios en el camping")
        else:
            try:
                ingreso = int(input("Cuántos sitios o vehículos  van a ingresar "))
                if ingreso <= 0:
                    print("Error: La cantidad de ingresos debe ser mayor a 0")
                elif ingreso > sitios_libre:
                    print(f"Solo puede ingresar un máximo de {sitios_libre} sitios")
                else:
                    sitios_ocupados += ingreso
                    print(f"ingreso registrado, se han ocupado {ingreso} de sitios")
            except ValueError:
                print("Error: debe ingresar un número válido")
    else:
        print("Opción fuera de Rango")