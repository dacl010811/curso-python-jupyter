from tkinter import *


def iniciarVentana():
    root = Tk()
    root.title("Text")
    root.iconbitmap('icono.ico')
    root.resizable(0, 0)

    text_area = Text(root)
    text_area.config(width=30, height=10, font=("Verdana", 45),
                     padx=10, pady=10, selectbackground="yellow")
    text_area.pack()

    root.mainloop()  # Metodo que hace visible la ventana


if __name__ == "__main__":
    iniciarVentana()
