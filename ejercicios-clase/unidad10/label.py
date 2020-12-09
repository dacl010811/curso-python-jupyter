from tkinter import *


def mostrar_ventana():
    root = Tk()  # Ventana Principal
    root.title("Label")
    root.iconbitmap('icono.ico')

    Label(root, text="Hola mundo Etiqueta1").pack(anchor=NW)
    Label(root, text="Hola mundo Etiqueta2").pack(anchor=CENTER)
    Label(root, text="Hola mundo Etiqueta3").pack(anchor=CENTER)

    label = Label(root, text="Label Constructor")
    label.pack(anchor=CENTER)

    label.config(fg="blue", bg="green", font=('Verdana', 24))
    label.config(cursor="pirate")

    var_texto = StringVar()
    label.config(textvariable=var_texto)

    foto = PhotoImage(file="Linux-icon.png")
    label_foto = Label(root, image=foto, bd=1, ).pack(side="left")

    root.mainloop()


if __name__ == "__main__":
    mostrar_ventana()
