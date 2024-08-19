from conexionDB import *
from tkinter import Label

def show_bank_name(ventana):
    texto0 = Label(ventana, text="",
                   fg="red", bg="black", font=("Courier", 12, "bold"))
    texto0.pack()

    texto1 = Label(ventana, text="██████╗░░█████╗░░█████╗░██╗███████╗██╗░█████╗░     ░██████╗████████╗░█████╗░███╗░░██╗██████╗░░█████╗░██████╗░████████╗",
                   fg="red", bg="black", font=("Courier", 12, "bold"))
    texto1.pack()

    texto2 = Label(ventana, text="██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║██╔══██╗     ██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝",
                   fg="blue", bg="black", font=("Courier", 12, "bold"))
    texto2.pack()

    texto3 = Label(ventana, text="██████╔╝███████║██║░░╚═╝██║█████╗░░██║██║░░╚═╝     ╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░██║███████║██████╔╝░░░██║░░░",
                   fg="white", bg="black", font=("Courier", 12, "bold"))
    texto3.pack()

    texto4 = Label(ventana, text="██╔═══╝░██╔══██║██║░░██╗██║██╔══╝░░██║██║░░██╗     ░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██║██╔══██║██╔══██╗░░░██║░░░",
                   fg="red", bg="black", font=("Courier", 12, "bold"))
    texto4.pack()

    texto5 = Label(ventana, text="██║░░░░░██║░░██║╚█████╔╝██║██║░░░░░██║╚█████╔╝     ██████╔╝░░░██║░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░░██║░░░██║░░░",
                   fg="blue", bg="black", font=("Courier", 12, "bold"))
    texto5.pack()

    texto6 = Label(ventana, text="╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░╚════╝░     ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░",
                   fg="white", bg="black", font=("Courier", 12, "bold"))
    texto6.pack()




def show_empleados():
    print("\n\t\t Selecciona la id del empleado")
    try:
        micursor = conexion.cursor()
        sql = "select * from empleados"
        micursor.execute(sql)
        resultado = micursor.fetchall()
    except:
        print("Ha ocurrido un error")
    else:
        for x in resultado:
            print(x)

def show_clientes():
    try:
        micursor = conexion.cursor()
        sql = "select * from clientes"
        micursor.execute(sql)
        resultado = micursor.fetchall()
    except:
        print("Ha ocurrido un error")
    else:
        for x in resultado:
            print(x)
