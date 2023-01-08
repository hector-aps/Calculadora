# Calculadora
![](https://github.com/hector-aps/Calculadora/blob/main/Imagen.png?raw=true)


Una calculadora simple, muy útil para hacer cálculos.
El codigo es muy corto y funciona unicamente con **3 funciones** ayudandose de 3 variables de control, las cuales son las siguientes:

- **operacion:** Guarda la operacion que esta en curso.
- **memoria:** Guarda el numero escrito anteriormente si se desea hacer una operacion.
- **borrar:** Controla cuando al precionar un numero se borra lo que hay en pantalla.

### Funciones


La primera funcion permite recibir la informacion de los numeros precionados, los cuales actuaran de cierta manera dependiendo del contexto, por ejemplo, si se tiene un numero en memoria o se ha precionado una operacion antes:
```python
def numeroPresionado(numero):
    global borrar, memoria, pantalla
    if numero == "0" and pantalla.get() != "":
        pantalla.set(pantalla.get() + numero)
    elif numero != "0":
        if borrar:
            pantalla.set("")
            borrar=False
        if numero != ".":
            pantalla.set(pantalla.get()+numero)

        if pantalla.get() != "" and "." not in pantalla.get() and numero == ".":
            pantalla.set(pantalla.get()+".")
        elif "." not in pantalla.get() and pantalla.get() == "":
            pantalla.set("0.")

```

La segunda funcion maneja las acciones de los botones de operaciones:
```python
def botonOperacion(op):
    global borrar, memoria, operacion

    if memoria != "" and op != "":
        match operacion:
            case "+":
                pantalla.set(str(float(memoria) + float(pantalla.get())))
            case "-":
                pantalla.set(str(float(memoria) - float(pantalla.get())))
            case "/":
                pantalla.set(str(float(memoria) / float(pantalla.get())))
            case "x":
                pantalla.set(str(float(memoria) * float(pantalla.get())))
        operacion = op
        memoria = pantalla.get()
        borrar=True
    
    elif op != "=" and memoria == "" and pantalla.get() != "" and not borrar:
        memoria = pantalla.get()
        operacion = op
        borrar = True
```

La tercera funcion reestablece los valores de las variables de control y borra lo que hay en pantalla:

```python
def clear():
    global memoria, operacion, pantalla, borrar
    memoria = ""
    operacion = ""
    pantalla.set("")
    borrar = False
```
