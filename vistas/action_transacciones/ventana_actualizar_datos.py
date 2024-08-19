from tkinter import Tk, Label, Button, Entry, messagebox

def actualizar_datos(cliente):
    ventana_actualizar = Tk()
    ventana_actualizar.title("Actualizar Datos")
    ventana_actualizar.geometry("500x500")
    ventana_actualizar.configure(bg="black")

    Label(ventana_actualizar, text="Nuevo Usuario:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
    entry_usuario = Entry(ventana_actualizar, font=("Arial", 12))
    entry_usuario.place(x=250, y=50, width=200)

    Label(ventana_actualizar, text="Nueva Contraseña:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=100)
    entry_contrasena = Entry(ventana_actualizar, font=("Arial", 12), show="*")
    entry_contrasena.place(x=250, y=100, width=200)

    Label(ventana_actualizar, text="Nuevo Nombre:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=150)
    entry_nombre = Entry(ventana_actualizar, font=("Arial", 12))
    entry_nombre.place(x=250, y=150, width=200)

    Label(ventana_actualizar, text="Nueva Dirección:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=200)
    entry_direccion = Entry(ventana_actualizar, font=("Arial", 12))
    entry_direccion.place(x=250, y=200, width=200)

    Label(ventana_actualizar, text="Nuevo Teléfono:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=250)
    entry_telefono = Entry(ventana_actualizar, font=("Arial", 12))
    entry_telefono.place(x=250, y=250, width=200)

    Label(ventana_actualizar, text="Nuevo Email:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=300)
    entry_email = Entry(ventana_actualizar, font=("Arial", 12))
    entry_email.place(x=250, y=300, width=200)

    def procesar_actualizacion():
        nuevo_usuario = entry_usuario.get()
        nueva_contrasena = entry_contrasena.get()
        nuevo_nombre = entry_nombre.get()
        nueva_direccion = entry_direccion.get()
        nuevo_telefono = entry_telefono.get()
        nuevo_email = entry_email.get()
        id_cliente= cliente[0]

        # Creación del objeto cliente y actualización de datos
        from usuarios import usuario

        obj_cliente = usuario.clientes(nuevo_usuario, nueva_contrasena, nuevo_nombre, nueva_direccion, nuevo_telefono, nuevo_email, None, None, None, None, id_cliente)
        resultado = obj_cliente.actualizar_datos()

        if resultado:
            messagebox.showinfo("Éxito", "Los datos se han actualizado y guardado correctamente.")
        else:
            messagebox.showerror("Error", "No fue posible actualizar los datos. Inténtalo de nuevo.")

    boton_actualizar = Button(ventana_actualizar, text="Actualizar", font=("Arial", 12), command=procesar_actualizacion)
    boton_actualizar.place(x=200, y=350, width=100)

    ventana_actualizar.mainloop()