from funciones import menu

pokemons = []

print("**** Bienvenido ****")
while True:
    menu()
    opcionI = int(input("Ingrese una opción: "))
    if opcionI == 1: 
        nombrePokemon = input("Ingrese el nombre del pokemon: ")
        if nombrePokemon in pokemons:  
            print("El pokemon ingresado ya esta registrado.")
            continue
        else:
            pokemons.append(nombrePokemon)
        tipoPokemonn = input("Ingese de que tipo es el pokemon: ")
        if tipoPokemonn != "fuego":
            pass
    elif opcionI == 2:
        for buscar in pokemons:
            buscar_pokemon = input("Ingrese el nombre del pokemon a buscar: ")
            if buscar_pokemon in pokemons:
                print(pokemons)
            else:
                print("El pokemon no se encuentra registrado.")