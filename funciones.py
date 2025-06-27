tipos_validos = ["fuego","agua", "psiquico", "planta", "lucha", "veneno", "electrico", 
                 "roca", "dragon", "bicho", "tierra", "volador", "hielo", "fantasma"]

def menu():
    print("\n1. Ingresar pokemon")
    print("2. Buscar pokemon")
    print("3. Eliminar pokemon")
    print("4. Listar pokemons")
    print("5. Salir\n")


def ingresar_pokemon(pokemons):
    id_pokemon = input("Ingrese el id del pokemon: ")
    nombrePokemon = input("Ingrese el nombre del pokemon: ").lower()
    for p in pokemons:
        if p["nombre"] == nombrePokemon:
            print("El pokemon ya esta registrado.")
            return
    tipoPokemon = input("Ingese de que tipo es el pokemon: ").lower()
    if tipoPokemon not in tipos_validos:
        print("Tipo invalido.")
        return
    pokemons.append({
        "id": id_pokemon,
        "nombre": nombrePokemon,
        "tipo": tipoPokemon})
    print("¡Pokemon ingresado exitosamente!")


def buscar_pokemon(pokemons):
    buscar_pokemon = input("Ingrese el nombre del pokemon a buscar: ").lower()
    encontrado= False
    for i in pokemons:
        if i["nombre"] == buscar_pokemon:
            print("\n***Pokemon encontrado***\n")
            print(f"ID: {i['id']}")
            print(f"nombre: {i["nombre"]}")
            print(f"tipo: {i["tipo"]}\n")
            encontrado = True
            return
        if not encontrado:
            print("\nNo se ha encontrado al pokemon.")
        

def eliminar_pokemon(pokemons):
    eliminar_pokemon = input("Ingrese el pokemon a eliminar: ").lower()
    eliminado = False
    for r in pokemons:
        if r["nombre"] == eliminar_pokemon:
            print(f"\nEl pokemon '{eliminar_pokemon}' ha sido eliminado.")
            print(f"Buen viaje {eliminar_pokemon}....")
            pokemons.remove(r)
            eliminado = True
            return
        if not eliminado:
            print("\nNo se ha podido eliminar pokemon!")


def listar_pokemons(pokemons):
    if not pokemons:
            print("\nNo hay pokemons registrados.")
            return
    for p in pokemons:
        print(f"\nID: {p["id"]}")
        print(f"Nombre: {p["nombre"]}")
        print(f"Tipo: {p["tipo"]}\n")