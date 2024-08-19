from tkinter import Tk, Label, Button, Entry, messagebox

def solicitar_prestamo(cliente):
    ventana_prestamo = Tk()
    ventana_prestamo.title("Solicitar Préstamo")
    ventana_prestamo.geometry("500x300")
    ventana_prestamo.configure(bg="black")

    Label(ventana_prestamo, text="Monto del Préstamo:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
    entry_monto = Entry(ventana_prestamo, font=("Arial", 12))
    entry_monto.place(x=250, y=50, width=200)

    Label(ventana_prestamo, text="Razón del Préstamo:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=100)
    entry_descripcion = Entry(ventana_prestamo, font=("Arial", 12))
    entry_descripcion.place(x=250, y=100, width=200)

    def procesar_prestamo():
        try:
            monto = float(entry_monto.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida en Monto. Por favor ingrese un número.")
            return
        
        descripcion = entry_descripcion.get()
        tipo = "PRESTAMO"
        permiso_prestamo = False

        # Procesar la transacción y el préstamo
        from transacciones import transaccion, prestamo

        id_cliente= cliente[0]

        registrar_transaccion = transaccion.crear_transaccion(descripcion, monto, id_cliente, tipo)
        
        # Verifica si la transacción fue creada correctamente
        if not registrar_transaccion:
            messagebox.showerror("Error", "Error al registrar la transacción.")
            return
        
        crear_prestamo = prestamo.Prestamo(id_cliente, permiso_prestamo, registrar_transaccion)
        registrar_prestamo = crear_prestamo.registrar_prestamo()

        if registrar_prestamo:
            messagebox.showinfo("Éxito", "Préstamo registrado con éxito.")
        else:
            messagebox.showerror("Error", "Error al registrar el préstamo.")

    boton_prestamo = Button(ventana_prestamo, text="Solicitar Préstamo", font=("Arial", 12), command=procesar_prestamo)
    boton_prestamo.place(x=200, y=200, width=150)

    ventana_prestamo.mainloop()