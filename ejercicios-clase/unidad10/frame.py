from tkinter import *


def mostrar_ventana():
    root = Tk()  # Ventana Principal
    root.title("Ventana Principal")
    root.iconbitmap('icono.ico')
    #root.resizable(0, 0)  # Para no redimensionar la ventana principal

    frame = Frame(root)
    frame.pack(fill="both", expand=1)
    frame.config(cursor="pirate")
    frame.config(bg="green")
    frame.config(bd=25)
    frame.config(relief="sunken")
    
    frame.config(width=1200, height=1000)
    
    """frame.pack(side=RIGHT)  # Redistribuir los componentes
    frame.pack(anchor=SE)
    frame.pack(fill="x")
    frame.pack(fill="y")
    frame.pack(fill="both")"""
    

    root.mainloop()  # Ejecutor o hace visible la ventana principal


if __name__ == "__main__":
    mostrar_ventana()
