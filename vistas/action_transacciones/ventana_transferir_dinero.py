from tkinter import Tk, Label, Button, Entry, Frame, messagebox

def transferir_dinero(cliente):
    ventana_transferencia = Tk()
    ventana_transferencia.title("Transferir Dinero")
    ventana_transferencia.geometry("600x400")
    ventana_transferencia.configure(bg="black")

    Label(ventana_transferencia, text="Descripción:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
    entry_descripcion = Entry(ventana_transferencia, font=("Arial", 12))
    entry_descripcion.place(x=250, y=50, width=300)

    Label(ventana_transferencia, text="Monto:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=100)
    entry_monto = Entry(ventana_transferencia, font=("Arial", 12))
    entry_monto.place(x=250, y=100, width=300)

    Label(ventana_transferencia, text="Usuario Destino:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=150)
    entry_usuario_destino = Entry(ventana_transferencia, font=("Arial", 12))
    entry_usuario_destino.place(x=250, y=150, width=300)

    Label(ventana_transferencia, text="Banco Destino:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=200)
    entry_banco_destino = Entry(ventana_transferencia, font=("Arial", 12))
    entry_banco_destino.place(x=250, y=200, width=300)

    def procesar_transferencia():
        descripcion = str(entry_descripcion.get())

        try:
            monto = float(entry_monto.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida en Monto. Por favor ingrese un número.")
            return
        
        try:
            usuario_destino = int(entry_usuario_destino.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida en Usuario Destino. Por favor ingrese un número.")
            return
        
        try:
            banco_destino = int(entry_banco_destino.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida en Banco Destino. Por favor ingrese un número.")
            return

        impuesto = monto * 0.015
        
        id_emisor = cliente[0]
        print(id_emisor)

        # Procesar la transacción y la transferencia
        from transacciones import transaccion,transferencia

        registrar_transaccion = transaccion.crear_transaccion(descripcion, monto, id_emisor, "TRANSFERENCIA")
        crear_transferencia = transferencia.Transferencia(id_emisor, usuario_destino, banco_destino, impuesto, registrar_transaccion, monto)
        registrar_transferencia = crear_transferencia.registrar_transferencia()

        if registrar_transferencia:
            messagebox.showinfo("Éxito", "Transferencia registrada con éxito.")
        else:
            messagebox.showerror("Error", "Error al realizar la transferencia.")

    boton_transferir = Button(ventana_transferencia, text="Transferir", font=("Arial", 12), command=procesar_transferencia)
    boton_transferir.place(x=250, y=300, width=100)

    ventana_transferencia.mainloop()