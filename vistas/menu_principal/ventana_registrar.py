from tkinter import Tk, Label, Entry, Button, messagebox
from usuarios import usuario
from funciones import show_bank_name

def regresar():
    from .ventana_menu_principal import show_welcome_and_options
    ventana.withdraw()
    show_welcome_and_options()

def mostrar_ventana_registro():
    global ventana
    ventana = Tk()
    ventana.title("Pacific Standart - Registro")
    ventana.geometry("1500x800")
    ventana.configure(bg="black")

    show_bank_name(ventana)
    label_encabezado = Label(ventana, text="Registro de Nuevo Cliente", font=("Arial", 18, "bold"), bg="black", fg="white")
    label_encabezado.place(x=620, y=180)

 
    etiqueta_usuario = Label(ventana, text="Usuario", font=("Arial", 12), bg="black", fg="white")
    etiqueta_usuario.place(x=600, y=250)
    campo_usuario = Entry(ventana, bg="white", font=("Arial", 12))
    campo_usuario.place(x=800, y=250, width=200)

    etiqueta_contrasena = Label(ventana, text="Contraseña", font=("Arial", 12), bg="black", fg="white")
    etiqueta_contrasena.place(x=600, y=300)
    campo_contrasena = Entry(ventana, bg="white", font=("Arial", 12), show="*")
    campo_contrasena.place(x=800, y=300, width=200)

    etiqueta_confirmar_contrasena = Label(ventana, text="Confirmar Contraseña", font=("Arial", 12), bg="black", fg="white")
    etiqueta_confirmar_contrasena.place(x=600, y=350)
    campo_confirmar_contrasena = Entry(ventana, bg="white", font=("Arial", 12), show="*")
    campo_confirmar_contrasena.place(x=800, y=350, width=200)

    etiqueta_nombre = Label(ventana, text="Nombre", font=("Arial", 12), bg="black", fg="white")
    etiqueta_nombre.place(x=600, y=400)
    campo_nombre = Entry(ventana, bg="white", font=("Arial", 12))
    campo_nombre.place(x=800, y=400, width=200)

    etiqueta_direccion = Label(ventana, text="Dirección", font=("Arial", 12), bg="black", fg="white")
    etiqueta_direccion.place(x=600, y=450)
    campo_direccion = Entry(ventana, bg="white", font=("Arial", 12))
    campo_direccion.place(x=800, y=450, width=200)

    etiqueta_telefono = Label(ventana, text="Teléfono", font=("Arial", 12), bg="black", fg="white")
    etiqueta_telefono.place(x=600, y=500)
    campo_telefono = Entry(ventana, bg="white", font=("Arial", 12))
    campo_telefono.place(x=800, y=500, width=200)

    etiqueta_email = Label(ventana, text="Email", font=("Arial", 12), bg="black", fg="white")
    etiqueta_email.place(x=600, y=550)
    campo_email = Entry(ventana, bg="white", font=("Arial", 12))
    campo_email.place(x=800, y=550, width=200)

    etiqueta_ocupacion = Label(ventana, text="Ocupación", font=("Arial", 12), bg="black", fg="white")
    etiqueta_ocupacion.place(x=600, y=600)
    campo_ocupacion = Entry(ventana, bg="white", font=("Arial", 12))
    campo_ocupacion.place(x=800, y=600, width=200)

    etiqueta_saldo = Label(ventana, text="Saldo Inicial", font=("Arial", 12), bg="black", fg="white")
    etiqueta_saldo.place(x=600, y=650)
    campo_saldo = Entry(ventana, bg="white", font=("Arial", 12))
    campo_saldo.place(x=800, y=650, width=200)

    def registrar_cliente():
        user = campo_usuario.get()
        contrasena = campo_contrasena.get()
        confirmar_contrasena = campo_confirmar_contrasena.get()
        nombre = campo_nombre.get()
        direccion = campo_direccion.get()
        telefono = campo_telefono.get()
        email = campo_email.get()
        ocupacion = campo_ocupacion.get()
        saldo = campo_saldo.get()

        if contrasena != confirmar_contrasena:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        try:
            saldo = float(saldo)
        except ValueError:
            messagebox.showerror("Error", "El saldo debe ser un número válido.")
            return

        from usuarios import usuario
        nuevo_cliente = usuario.clientes(user, contrasena, nombre, direccion, telefono, email, ocupacion, "", saldo)
        resultado = nuevo_cliente.registrar_Cliente(nuevo_cliente)
        
        if resultado:
            messagebox.showinfo("Éxito", "Cliente registrado exitosamente.")
            ventana.quit()
            regresar()
        else:
            messagebox.showerror("Error", "No se pudo registrar al cliente.")


    boton_salir = Button(ventana, text="Regresar", font=("Arial", 12), command=regresar)
    boton_salir.place(x=700, y=700)

    boton_registrar = Button(ventana, text="Registrar", font=("Arial", 12), command=registrar_cliente)
    boton_registrar.place(x=800, y=700)

    ventana.mainloop()