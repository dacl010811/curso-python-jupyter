from tkinter import *


def iniciarVentana():
    root = Tk()
    root.title("Hola Mundo Tk")
    root.iconbitmap('icono.ico')
    root.resizable(0, 0)  # Para no redimensionar la ventana principal

    root.config(width=1200, height=1000)
    root.mainloop()  # Metodo que hace visible la ventana


if __name__ == "__main__":
    iniciarVentana()
