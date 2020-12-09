from tkinter import *
from tkinter import filedialog as FileDialog
from io import open


ruta = ""


def abrir_archivo():
    global ruta
    ruta = FileDialog.askopenfilename(initialdir='.', filetypes=(
        ("Ficheros de Texto", "*.py")), title="Abrir archivos python")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        text_area.delete(1.0, 'end')
        text_area.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi Editor")


def saludo_evento():
    print("Hola Mundo desde Tkinter....!")


root = Tk()
root.title("Bloc Notas Python")
root.iconbitmap('icono.ico')

menubar_principal = Menu(root)
filemenu = Menu(menubar_principal, tearoff=0)
filemenu.add_command(label="Nuevo", command="")
filemenu.add_command(label="Abrir", command=abrir_archivo)
filemenu.add_command(label="Guardar", command="")
filemenu.add_command(label="Guardar Como", command="")
filemenu.add_separator()
filemenu.add_command(label="Salir", command="")

menubar_principal.add_cascade(menu=filemenu, label="Archivo")

text_area = Text(root)
text_area.pack(fill="both", expand=1)
text_area.config(bd=0, padx=10, pady=10, font=("Verdana", 50))


root.config(menu=menubar_principal)
root.mainloop()  # Metodo que hace visible la ventana
