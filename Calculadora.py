from tkinter import *

def main():
    #Datos
    global pantalla, memoria, root, ventana, operacion, borrar
    root = Tk()
    root.title("Calculadora")

    ventana = Frame(root)
    ventana.config(bg="#D6EAF8")
    root.config(bg="#D6EAF8")

    pantalla = StringVar()
    operacion = ""
    memoria = ""
    borrar = False

    #Interfaz de calculadora
    Label(ventana, textvariable = pantalla, width=16, height=2, bg="black", fg="#2ECC71", anchor="e", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    Button(ventana, text="C", width=20, bg = "#58D68D", font=("Arial", 10, ""), command=clear).grid(row=1, column=0, padx=5, pady=5, columnspan=4)    

    Button(ventana, text="7", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("7")).grid(row=2, column=0, padx=5, pady=5)
    Button(ventana, text="8", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("8")).grid(row=2, column=1, padx=5, pady=5)
    Button(ventana, text="9", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("9")).grid(row=2, column=2, padx=5, pady=5)
    Button(ventana, text="/", width=3, font=("Arial", 10, ""), command=lambda:botonOperacion("/")).grid(row=2, column=3, padx=5, pady=5) 

    Button(ventana, text="4", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("4")).grid(row=3, column=0, padx=5, pady=5)
    Button(ventana, text="5", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("5")).grid(row=3, column=1, padx=5, pady=5)
    Button(ventana, text="6", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("6")).grid(row=3, column=2, padx=5, pady=5)
    Button(ventana, text="x", width=3, font=("Arial", 10, ""), command=lambda:botonOperacion("x")).grid(row=3, column=3, padx=5, pady=5)

    Button(ventana, text="1", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("1")).grid(row=4, column=0, padx=5, pady=5)
    Button(ventana, text="2", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("2")).grid(row=4, column=1, padx=5, pady=5)
    Button(ventana, text="3", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("3")).grid(row=4, column=2, padx=5, pady=5)
    Button(ventana, text="+", width=3, font=("Arial", 10, ""), command=lambda:botonOperacion("+")).grid(row=4, column=3, padx=5, pady=5)

    Button(ventana, text="0", width=3, font=("Arial", 10, ""), command=lambda:numeroPresionado("0")).grid(row=5, column=0, padx=5, pady=5)
    Button(ventana, text=".", width=3, font=("Arial", 10, "bold"), command=lambda:numeroPresionado(".")).grid(row=5, column=1, padx=5, pady=5)
    Button(ventana, text="=", width=3, font=("Arial", 10, ""), command=lambda:botonOperacion("=")).grid(row=5, column=2, padx=5, pady=5)
    Button(ventana, text="-", width=3, font=("Arial", 10, ""), command=lambda:botonOperacion("-")).grid(row=5, column=3, padx=5, pady=5)

    ventana.pack(fill="both", expand="True", pady=10, padx=10)
    root.mainloop()


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


def clear():
    global memoria, operacion, pantalla, borrar
    memoria = ""
    operacion = ""
    pantalla.set("")
    borrar = False


if __name__ == "__main__":
    main()