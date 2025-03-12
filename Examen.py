def buscarPalabra(objetivo, palabras):
    for palabra in palabras:
        if palabra == objetivo: return True
    else: return False


def imprimirListaInversa(lista):
    for item in range(len(lista) -1, -1, -1):
        print(f"- {lista[item]}")

nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}

imprimirListaInversa(nombres)
while True:
    nombre = input("\nBuscar nombre: ")
    if nombre == "exit":
        print("\nFIN DEL PROGRAMA")
        break
    elif buscarPalabra(nombre, nombres): print(f"{nombre} tiene {edades[nombre]} años")
    else: print("El nombre no existe...")
