from tkinter import Tk, Label, Button
from funciones import show_bank_name

def ir_ventana_login():
    global ventana
    from .ventana_login import mostrar_ventana_iniciar_sesion
    ventana.withdraw()
    mostrar_ventana_iniciar_sesion()

def ir_ventana_registro():
    global ventana
    from .ventana_registrar import mostrar_ventana_registro
    ventana.withdraw()
    mostrar_ventana_registro()

def show_welcome_and_options():
    global ventana
    ventana = Tk()
    ventana.title("Pacific Standart - Menu principal")
    ventana.geometry("1500x800")
    ventana.configure(bg="black")

    # Mostrar el nombre del banco o algún encabezado
    show_bank_name(ventana)

    # Etiqueta de bienvenida
    label_bienvenida = Label(ventana, text="Bienvenido a Pacific Standart", fg="white", bg="black", font=("Arial", 18, "bold"))
    label_bienvenida.place(relx=0.5, y=200, anchor="center")

    # Botones
    boton_iniciar = Button(ventana, text="Iniciar Sesión", font=("Arial", 12), command=ir_ventana_login)
    boton_iniciar.place(relx=0.4, y=300, anchor="center")

    boton_registrar = Button(ventana, text="Registrar", font=("Arial", 12), command=ir_ventana_registro)
    boton_registrar.place(relx=0.5, y=300, anchor="center")

    boton_salir = Button(ventana, text="Salir", font=("Arial", 12), command=ventana.quit)
    boton_salir.place(relx=0.6, y=300, anchor="center")

    ventana.mainloop()
