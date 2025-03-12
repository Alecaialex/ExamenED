# Documentación Examen

> Esta documentación ha sido hecha para el código del examen de ED del 12 de Marzo de 2025.

<br>

## Índice

- [Buscar palabra](#buscar)
- [Imprimir lista inversa](#imprimirinversa)
- [Nombres y edades](#nombresedades)
- [Bucle principal](#bucle)

<br>

<div id="buscar">

## 1. Buscar palabra

Esta es la primera función del código, nos sirve para buscar si una palabra está contenida en un diccionario mediante el uso de bucles y condicionales, este es el código:

```py
def buscarPalabra(objetivo, palabras):
    for palabra in palabras:
        if palabra == objetivo: return True
    else: return False
```

Los pasos que sigue son los siguientes:

1. Comenzamos definiendo la función con el nombre **buscarPalabra** y los parámetros _**objetivo**_ y _**palabras**_.
2. Empezamos el bucle con un for recorriendo la lista _**palabras**_ (parámetro) usando el iterador _**palabra**_ (que se podía haber llamado de cualquier forma) que lo que hará será contener el valor en cada iteración de la lista.
3. Comprobamos si la palabra se encuentra en la lista, y en caso de ser así devolvemos **True**
4. Si terminan todas las iteraciones y no se ha encontrado, se devuelve **False**.

- [X] Uso de bucles
- [X] Uso de condicionales

<br>

<div id="imprimirinversa">

## 2. Imprimir lista inversa

En esta segunda función llamada **imprimirListaInversa** con el parámetro _**lista**_ nos servirá para obtener una lista mediante el parámetro, y imprimirla a la inversa, este es el código:

```py
def imprimirListaInversa(lista):
    for item in range(len(lista) -1, -1, -1):
        print(f"- {lista[item]}")
```

Los pasos que sigue son los siguientes:

1. Comenzamos definiendo la función con el nombre **imprimirListaInversa** y el parámetro _**lista**_.
2. Recorremos la lista con el iterador _**item**_ usando el rango `range(len(lista) -1, -1, -1)`
    
    1. A la longitud de la lista le restamos 1 ya que los valores empiezan desde 0.
    2. Ponemos como final el -1 para abarcar todos los items (ya que el final no se incluye, entonces llegará hasta 0).
    3. Definimos el avance en -1 para que vaya de mas a menos.

3. Imprimimos la cadena `f"- {lista[item]}"` la cual nos imprimirá un - seguido del item actual en cada iteración (De modo inverso).

<br>

<div id="nombresedades">

## 3. Nombres y edades
> Este código ha sido proporcionado totalmente por el profesor

En este apartado encontramos un código simple, definiendo las siguientes variables:

- **Nombres**: Que contendrá una lista o array con varios nombres.

---

- **Edades**: Que contendrá un diccionario con los nombres como clave y las edades de cada uno.

Este es el código:

```py
nombres = ["Mengano", "Fulano", "Zutano", "Perantano"]
edades = {
    "Mengano": 0,
    "Fulano": 25,
    "Zutano": 50,
    "Perantano": 75
}
```

<br>

<div id="bucle">

## 4. Bucle principal

En esta parte del código vamos a crear el código que se va a ejecutar constantemente, donde usaremos las funciones creadas anteriormente para hacer funcionar el programa, este es el código:

```py

```

1. Comenzamos llamando a la función [**imprimirListaInversa**](#imprimirinversa) para antes de entrar en el bucle imprimir una vez todos los nombres en orden inverso.

2. Empezamos con el [*bucle*](#bucle) definiéndolo con un **while True**, esto lo que hace es que el bucle sea infinito hasta que lo rompamos nosotros con un _break_.

3. Leemos el input del usuario mostrando `Buscar nombre:` por consola y lo guardamos en la variable _**nombre**_.

4. Nuestra primera verificación va a ser comprobar si lo introducido es = a `exit` ya que como indica el enunciado, aun que exit fuera un nombre tiene que comprobarse primero para salir del programa, ya que es nuestra palabra reservada, y si efecitvamente lo introducido es `exit`, imprimiremos `FIN DEL PROGRAMA` y luego haremos un *break* para salir del bucle y terminar la ejecución ya que no hay mas código.

5. Añadimos una condición elif para que si no es exit, use la función **buscarPalabra** con el nombre introducido sobre la lista nombres, y si devuelve _True_ entonces imprimirá la siguiente cadena `f"{nombre} tiene {edades[nombre]} años"` en la cual formateamos el nombre introducido, y usamos `edades[nombre]` para buscar su edad ya que la clave del diccionario son los nombres, y los valores son las edades.

6. :warning: En caso de que ninguna se cumpla, imprimiremos un mensaje informando de que el nombre no existe y el bucle volverá al principio para leer.