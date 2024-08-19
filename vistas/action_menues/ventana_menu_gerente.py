from tkinter import Tk, Label, Button, Entry, messagebox
from usuarios import usuario
from funciones import show_bank_name

def mostrar_menu_gerente(gerente):
    ventana_gerente = Tk()
    ventana_gerente.title("Pacific Standart - Gerente")
    ventana_gerente.geometry("1500x800")
    ventana_gerente.configure(bg="black")
    
    show_bank_name(ventana_gerente)

    label_encabezado = Label(ventana_gerente, text="Menú de Gerente", font=("Arial", 18, "bold"), bg="black", fg="white")
    label_encabezado.place(x=650, y=200)

    def eliminar_empleado():
        ventana_eliminar = Tk()
        ventana_eliminar.title("Eliminar Empleado")
        ventana_eliminar.geometry("500x400")
        ventana_eliminar.configure(bg="black")
        
        Label(ventana_eliminar, text="ID Empleado:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
        entry_id_empleado = Entry(ventana_eliminar, font=("Arial", 12))
        entry_id_empleado.place(x=200, y=50, width=200)

        Label(ventana_eliminar, text="Contraseña:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=100)
        entry_contrasena = Entry(ventana_eliminar, font=("Arial", 12), show="*")
        entry_contrasena.place(x=200, y=100, width=200)

        def confirmar_eliminacion():
            id_empleado = entry_id_empleado.get()
            contrasena = entry_contrasena.get()
            print(contrasena)
            print(id_empleado)
            print(gerente)
            
            if contrasena == gerente[2]:  # Suponiendo que la contraseña del gerente está en la posición 1
                obj_empleado = usuario.Usuario(None, None, None, None, None, None, id_empleado)
                resultado = obj_empleado.eliminar_empleado()

                if resultado:
                    messagebox.showinfo("Éxito", f"El empleado con ID {id_empleado} se ha eliminado correctamente.")
                else:
                    messagebox.showerror("Error", "No fue posible eliminar el empleado. Inténtalo de nuevo.")
            else:
                messagebox.showerror("Error", "Contraseña incorrecta.")

        boton_confirmar = Button(ventana_eliminar, text="Eliminar", font=("Arial", 12), command=confirmar_eliminacion)
        boton_confirmar.place(x=200, y=200, width=100)

        ventana_eliminar.mainloop()

    def registrar_empleado():
        ventana_registrar = Tk()
        ventana_registrar.title("Registrar Empleado")
        ventana_registrar.geometry("500x600")
        ventana_registrar.configure(bg="black")

        Label(ventana_registrar, text="Usuario:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
        entry_usuario = Entry(ventana_registrar, font=("Arial", 12))
        entry_usuario.place(x=200, y=50, width=200)

        Label(ventana_registrar, text="Contraseña:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=100)
        entry_contrasena = Entry(ventana_registrar, font=("Arial", 12), show="*")
        entry_contrasena.place(x=200, y=100, width=200)

        Label(ventana_registrar, text="Nombre:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=150)
        entry_nombre = Entry(ventana_registrar, font=("Arial", 12))
        entry_nombre.place(x=200, y=150, width=200)

        Label(ventana_registrar, text="Dirección:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=200)
        entry_direccion = Entry(ventana_registrar, font=("Arial", 12))
        entry_direccion.place(x=200, y=200, width=200)

        Label(ventana_registrar, text="Teléfono:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=250)
        entry_telefono = Entry(ventana_registrar, font=("Arial", 12))
        entry_telefono.place(x=200, y=250, width=200)

        Label(ventana_registrar, text="Email:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=300)
        entry_email = Entry(ventana_registrar, font=("Arial", 12))
        entry_email.place(x=200, y=300, width=200)

        Label(ventana_registrar, text="Salario:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=350)
        entry_salario = Entry(ventana_registrar, font=("Arial", 12))
        entry_salario.place(x=200, y=350, width=200)

        Label(ventana_registrar, text="Puesto:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=400)
        entry_puesto = Entry(ventana_registrar, font=("Arial", 12))
        entry_puesto.place(x=200, y=400, width=200)

        Label(ventana_registrar, text="ID Banco:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=450)
        entry_id_banco = Entry(ventana_registrar, font=("Arial", 12))
        entry_id_banco.place(x=200, y=450, width=200)

        def confirmar_registro():
            user = entry_usuario.get()
            contrasena = entry_contrasena.get()
            nombre = entry_nombre.get()
            direccion = entry_direccion.get()
            telefono = entry_telefono.get()
            email = entry_email.get()
            salario = entry_salario.get()
            puesto = entry_puesto.get()
            id_banco = entry_id_banco.get()

            obj_empleado = usuario.empleado(user, contrasena, nombre, direccion, telefono, email, salario, puesto, id_banco)
            resultado = usuario.empleado.registrar_Empleado(obj_empleado)

            if resultado:
                messagebox.showinfo("Éxito", f"El empleado {nombre} se ha registrado correctamente.")
            else:
                messagebox.showerror("Error", "No fue posible registrar el empleado. Inténtalo de nuevo.")

        boton_registrar = Button(ventana_registrar, text="Registrar", font=("Arial", 12), command=confirmar_registro)
        boton_registrar.place(x=200, y=500, width=100)

        ventana_registrar.mainloop()

    def actualizar_salario():
        ventana_actualizar_salario = Tk()
        ventana_actualizar_salario.title("Actualizar Salario")
        ventana_actualizar_salario.geometry("500x300")
        ventana_actualizar_salario.configure(bg="black")

        Label(ventana_actualizar_salario, text="ID Empleado:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
        entry_id_empleado = Entry(ventana_actualizar_salario, font=("Arial", 12))
        entry_id_empleado.place(x=200, y=50, width=200)

        Label(ventana_actualizar_salario, text="Nuevo Salario:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=100)
        entry_nuevo_salario = Entry(ventana_actualizar_salario, font=("Arial", 12))
        entry_nuevo_salario.place(x=200, y=100, width=200)

        def confirmar_actualizacion():
            id_empleado = entry_id_empleado.get()
            nuevo_salario = entry_nuevo_salario.get()

            print(id_empleado)
            print(nuevo_salario)

            try:
                nuevo_salario = float(nuevo_salario)
            except ValueError:
                messagebox.showerror("Error", "El salario debe ser un número.")
                return

            obj_empleado = usuario.empleado(None, None, None, None, None, None, nuevo_salario, None, None, id_empleado)
            resultado = obj_empleado.actualizar_salario()

            if resultado:
                messagebox.showinfo("Éxito", "El salario se ha actualizado correctamente.")
            else:
                messagebox.showerror("Error", "No fue posible actualizar el salario. Inténtalo de nuevo.")

        boton_actualizar = Button(ventana_actualizar_salario, text="Actualizar", font=("Arial", 12), command=confirmar_actualizacion)
        boton_actualizar.place(x=200, y=150, width=100)

        ventana_actualizar_salario.mainloop()

    def salir():
        ventana_gerente.destroy()

    # Botones del Menú de Gerente
    boton_eliminar_empleado = Button(ventana_gerente, text="Eliminar Empleado", font=("Arial", 12), command=eliminar_empleado)
    boton_eliminar_empleado.place(x=650, y=300, width=200)

    boton_registrar_empleado = Button(ventana_gerente, text="Registrar Empleado", font=("Arial", 12), command=registrar_empleado)
    boton_registrar_empleado.place(x=650, y=350, width=200)

    boton_actualizar_salario = Button(ventana_gerente, text="Actualizar Salario", font=("Arial", 12), command=actualizar_salario)
    boton_actualizar_salario.place(x=650, y=400, width=200)

    boton_salir = Button(ventana_gerente, text="Salir", font=("Arial", 12), command=salir)
    boton_salir.place(x=650, y=450, width=200)

    ventana_gerente.mainloop()


    