from tkinter import *


def saludo_evento():
    print("Hola Mundo desde Tkinter....!")


root = Tk()
root.title("Bloc Notas Python")
root.iconbitmap('icono.ico')

menubar_principal = Menu(root)
filemenu = Menu(menubar_principal, tearoff=0)
filemenu.add_command(label="Nuevo", command="")
filemenu.add_command(label="Abrir", command="")
filemenu.add_command(label="Guardar", command="")
filemenu.add_command(label="Guardar Como", command="")
filemenu.add_separator()
filemenu.add_command(label="Salir", command="")

menubar_principal.add_cascade(menu=filemenu, label="Archivo")

root.config(menu=menubar_principal)
root.mainloop()  # Metodo que hace visible la ventana
