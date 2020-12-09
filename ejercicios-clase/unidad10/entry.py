from tkinter import *


def iniciarVentana():
    root = Tk()
    root.title("Entry")
    root.iconbitmap('icono.ico')
    root.resizable(0, 0)

    label_nombre = Label(root, text="Nombres:")
    label_nombre.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    txt_nombre = Entry(root)
    txt_nombre.grid(row=0, column=1, padx=5, pady=5)

    label_apellido = Label(root, text="Apellidos:")
    label_apellido.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    txt_apellido = Entry(root)
    txt_apellido.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()  # Metodo que hace visible la ventana


if __name__ == "__main__":
    iniciarVentana()
