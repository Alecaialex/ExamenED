def buscarPalabra(objetivo, palabras):
    if objetivo in palabras: return True
    else: return False


def imprimirListaInversa(lista):
    for item in range(len(lista) -1, -1, -1):
        print(f"- {lista[item]}")
        
    print()

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

while True:
    imprimirListaInversa(nombres)
    nombre = input("\nBuscar nombre: ")
    if buscarPalabra(nombre, nombres): print("Existe\n")
    else: print("No existe\n")
