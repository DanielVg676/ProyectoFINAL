from tkinter import Tk, Label, Button, Entry, messagebox

def retirar_dinero(id_cliente):
    ventana_retiro = Tk()
    ventana_retiro.title("Retirar Dinero")
    ventana_retiro.geometry("400x300")
    ventana_retiro.configure(bg="black")

    Label(ventana_retiro, text="Monto a Retirar:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
    entry_monto = Entry(ventana_retiro, font=("Arial", 12))
    entry_monto.place(x=200, y=50, width=150)

    def procesar_retiro():
        try:
            monto = float(entry_monto.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida en Monto. Por favor ingrese un número.")
            return
        
        descripcion = ""  # Descripción vacía como en el ejemplo
        tipo = "RETIRO"

        cliente=id_cliente[0]

        from transacciones import transaccion, retiro

        registrar_transaccion = transaccion.crear_transaccion(descripcion, monto, cliente, tipo)
        
        if not registrar_transaccion:
            messagebox.showerror("Error", "Error al registrar la transacción.")
            return
        
        crear_retiro = retiro.Retiro(cliente, monto, registrar_transaccion)
        registrar_retiro = crear_retiro.registrar_retiro()

        if registrar_retiro:
            messagebox.showinfo("Éxito", "Retiro registrado con éxito.")
        else:
            messagebox.showerror("Error", "Error al realizar el retiro.")

    boton_retirar = Button(ventana_retiro, text="Retirar", font=("Arial", 12), command=procesar_retiro)
    boton_retirar.place(x=150, y=150, width=100)

    ventana_retiro.mainloop()