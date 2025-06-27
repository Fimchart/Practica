from funciones import menu, ingresar_pokemon,buscar_pokemon,eliminar_pokemon,listar_pokemons

pokemons = []

print("**** Bienvenido ****")
while True:
    menu()
    try:
        opcionI = int(input("Ingrese una opción: "))
    except ValueError:
        print(" Opción inválida. Debe ingresar un número.")
        continue

    if opcionI == 1: 
        ingresar_pokemon()
    elif opcionI == 2:
        buscar_pokemon()
    elif opcionI == 3:
        eliminar_pokemon()
    elif opcionI == 4:
        listar_pokemons()
    elif opcionI == 5:
        print("¡Gracias por usar el sistema!")
        print("**** Saliendo ****")
        break
    else:
        print("Opción no valida.")
        print("Por favor, seleccione una opción valida.")
