from tkinter import Tk, Label, Button, Frame, messagebox
from usuarios import usuario
from funciones import show_bank_name

def show_client_menu(cliente):
    ventana_cliente = Tk()
    ventana_cliente.title("Pacific Standart - Cliente")
    ventana_cliente.geometry("1500x800")
    ventana_cliente.configure(bg="black")
    
    show_bank_name(ventana_cliente)

    label_encabezado = Label(ventana_cliente, text="Menú de Cliente", font=("Arial", 18, "bold"), bg="black", fg="white")
    label_encabezado.place(x=650, y=200)

    saldo=str(usuario.clientes.checar_balance(cliente[0]))

    def checar_saldo():
        messagebox.showinfo("Checar Saldo", f"Tu saldo disponible es de $ {saldo}")
    
    def transferir_dinero():
        from ..action_transacciones.ventana_transferir_dinero import transferir_dinero
        transferir_dinero(cliente)
    
    def retirar_dinero():
        from ..action_transacciones.ventana_retirar_dinero import retirar_dinero
        retirar_dinero(cliente)
    
    def solicitar_prestamo():
        from ..action_transacciones.ventana_solicitar_prestamo import solicitar_prestamo
        solicitar_prestamo(cliente)
    
    def actualizar_datos():
        from ..action_transacciones.ventana_actualizar_datos import actualizar_datos
        actualizar_datos(cliente)
    
    def salir():
        ventana_cliente.destroy()

    # Botones del Menú de Cliente
    boton_checar_saldo = Button(ventana_cliente, text="Checar Saldo", font=("Arial", 12), command=checar_saldo)
    boton_checar_saldo.place(x=650, y=300, width=200)

    boton_transferir_dinero = Button(ventana_cliente, text="Transferir Dinero", font=("Arial", 12), command=transferir_dinero)
    boton_transferir_dinero.place(x=650, y=350, width=200)

    boton_retirar_dinero = Button(ventana_cliente, text="Retirar Dinero", font=("Arial", 12), command=retirar_dinero)
    boton_retirar_dinero.place(x=650, y=400, width=200)

    boton_solicitar_prestamo = Button(ventana_cliente, text="Solicitar Préstamo", font=("Arial", 12), command=solicitar_prestamo)
    boton_solicitar_prestamo.place(x=650, y=450, width=200)

    boton_actualizar_datos = Button(ventana_cliente, text="Actualizar Datos", font=("Arial", 12), command=actualizar_datos)
    boton_actualizar_datos.place(x=650, y=500, width=200)

    boton_salir = Button(ventana_cliente, text="Salir", font=("Arial", 12), command=salir)
    boton_salir.place(x=650, y=550, width=200)

    ventana_cliente.mainloop()

