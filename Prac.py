from funciones import menu

pokemons = []
tipos_validos = ["fuego","agua", "psiquico", "planta", "lucha", "veneno", "electrico", 
                 "roca", "dragon", "bicho", "tierra", "volador", "hielo", "fantasma"]

print("**** Bienvenido ****")
while True:
    menu()
    opcionI = int(input("Ingrese una opción: "))
    if opcionI == 1: 
        nombrePokemon = input("Ingrese el nombre del pokemon: ").lower()
        if nombrePokemon in pokemons:  
            print("El pokemon ingresado ya esta registrado.")
            continue
        tipoPokemon = input("Ingese de que tipo es el pokemon: ").lower()
        if tipoPokemon not in tipos_validos:
            print("Tipo invalido.")
            continue
        pokemons.append({
            "nombre": nombrePokemon,
            "tipo": tipoPokemon})
    elif opcionI == 2:
        buscar_pokemon = input("Ingrese el nombre del pokemon a buscar: ").lower()
        encontrado= False
        for i in pokemons:
            if i["nombre"] == buscar_pokemon:
                print("***Pokemon encontrado***\n")
                print(f"nombre: {i["nombre"]}")
                print(f"tipo: {i["tipo"]}\n")
                encontrado = True
                break
        if not encontrado:
            print("\nNo se ha encontrado al pokemon.")