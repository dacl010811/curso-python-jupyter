from tkinter import *


def funcion_sumar():
    resultado.set(float(n1.get()) + float(n2.get()))
    limpiar()


def funcion_restar():
    resultado.set(float(n1.get()) - float(n2.get()))
    limpiar()


def funcion_multiplicar():
    resultado.set(float(n1.get()) * float(n2.get()))
    limpiar()


def funcion_dividir():
    resultado.set(float(n1.get()) / float(n2.get()))
    limpiar()


def limpiar():
    n1.set('')
    n2.set('')


root = Tk()
root.title("Suma")
root.iconbitmap('icono.ico')

# Button(root, text="Enviar", command=saludo_evento).pack()

# Nombre de variables de los Widgets
n1 = StringVar()
n2 = StringVar()
resultado = StringVar()

Label(root, text="Numero 1").pack()
Entry(root, textvariable=n1).pack()

Label(root, text="Numero 2").pack()
Entry(root, textvariable=n2).pack()

Label(root, text="Resultado").pack()
Entry(root, textvariable=resultado, state=DISABLED).pack()

Label(root).pack()

Button(root, text="Sumar", command=funcion_sumar).pack(side="left")
Button(root, text="Restar", command=funcion_restar).pack(side="left")
Button(root, text="Multiplicar", command=funcion_multiplicar).pack(side="left")
Button(root, text="Dividir", command=funcion_dividir).pack(side="left")

root.mainloop()  # Metodo que hace visible la ventana
