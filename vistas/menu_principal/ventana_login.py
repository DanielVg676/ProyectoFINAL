from funciones import show_bank_name
from tkinter import Tk, Label, Entry, Button, Frame, messagebox
from usuarios import usuario
import hashlib

def regresar():
    from .ventana_menu_principal import show_welcome_and_options
    ventana.withdraw()
    show_welcome_and_options()

def mostrar_ventana_iniciar_sesion():
    global ventana
    ventana = Tk()
    ventana.title("Pacific Standart - login")
    ventana.geometry("1500x800")
    ventana.configure(bg="black")  # Fondo negro para resaltar el texto

    label_encabezado = Label(ventana, text="Iniciar sesion", font=("Arial", 18, "bold"), bg="black", fg="white")
    label_encabezado.place(x=680, y=200)

    show_bank_name(ventana)

    # Entrada de Usuario
    etiqueta_usuario = Label(ventana, text="Usuario", font=("Arial", 12), bg="black", fg="white")
    etiqueta_usuario.place(x=650, y=300)

    usuario_entry = Entry(ventana, bg="white", font=("Arial", 12))
    usuario_entry.place(x=650, y=330, width=200)

    # Entrada de Contraseña
    etiqueta_contrasena = Label(ventana, text="Contraseña", font=("Arial", 12), bg="black", fg="white")
    etiqueta_contrasena.place(x=650, y=370)

    contrasena_entry = Entry(ventana, bg="white", font=("Arial", 12), show="*")
    contrasena_entry.place(x=650, y=400, width=200)

    def iniciar_sesion():
        user = usuario_entry.get()
        user = int(user)
        contrasena = contrasena_entry.get()
        contrasena = str(contrasena)

        registro, tipo_usuario = usuario.Usuario.iniciar_sesion(user, contrasena)

        print(registro, tipo_usuario)

        if registro:
            ventana.withdraw()
            if tipo_usuario == 'cliente':
                from ..action_menues.ventana_menu_cliente import show_client_menu
                show_client_menu(registro)
                
            elif "gerente" in registro:
                from ..action_menues.ventana_menu_gerente import mostrar_menu_gerente
                mostrar_menu_gerente(registro)

            elif tipo_usuario == 'empleado':
                from ..action_menues.ventana_menu_empleado import mostrar_menu_empleado
                mostrar_menu_empleado(registro)
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")


    boton_salir = Button(ventana, text="Regresar", font=("Arial", 12), command=regresar)
    boton_salir.place(x=650, y=450)

    boton_iniciar = Button(ventana, text="Iniciar Sesión", font=("Arial", 12), command=iniciar_sesion)
    boton_iniciar.place(x=750, y=450)

    ventana.mainloop()
