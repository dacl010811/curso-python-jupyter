from tkinter import *



def  saludo_evento():
    print("Hola Mundo desde Tkinter....!")



def iniciarVentana():
    root = Tk()
    root.title("Text")
    root.iconbitmap('icono.ico')


    Button(root, text="Enviar", command=saludo_evento).pack()

    root.mainloop()  # Metodo que hace visible la ventana


if __name__ == "__main__":
    iniciarVentana()
