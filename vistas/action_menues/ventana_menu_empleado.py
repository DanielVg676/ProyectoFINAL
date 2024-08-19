from tkinter import Tk, Label, Button, Entry, messagebox
from usuarios import usuario
from funciones import show_bank_name
from conexionDB import conexion

def mostrar_menu_empleado(empleado):
    ventana_empleado = Tk()
    ventana_empleado.title("Pacific Standart - Empleado")
    ventana_empleado.geometry("1500x800")
    ventana_empleado.configure(bg="black")
    
    show_bank_name(ventana_empleado)

    label_encabezado = Label(ventana_empleado, text="Menú de Empleado", font=("Arial", 18, "bold"), bg="black", fg="white")
    label_encabezado.place(x=650, y=200)







    def consultar_transaccion():
        ventana_transaccion = Tk()
        ventana_transaccion.title("Consultar Transacción")
        ventana_transaccion.geometry("500x300")
        ventana_transaccion.configure(bg="black")
        
        Label(ventana_transaccion, text="ID Transacción:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
        entry_id_transaccion = Entry(ventana_transaccion, font=("Arial", 12))
        entry_id_transaccion.place(x=200, y=50, width=200)

        def buscar_transaccion():
            id_transaccion = entry_id_transaccion.get()
            try:
                micursor = conexion.cursor()
                sql = f"SELECT * FROM transacciones WHERE id_transaccion={id_transaccion}"
                micursor.execute(sql)
                resultado = micursor.fetchall()
                if not resultado:
                    messagebox.showinfo("Resultado", "No se ha encontrado información en el historial.")
                else:
                    transaccion_info = "\n".join([str(x) for x in resultado])
                    messagebox.showinfo("Resultado", transaccion_info)
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
            finally:
                micursor.close()

        boton_buscar = Button(ventana_transaccion, text="Buscar", font=("Arial", 12), command=buscar_transaccion)
        boton_buscar.place(x=200, y=150, width=100)

        ventana_transaccion.mainloop()







    def consultar_historial():
        ventana_historial = Tk()
        ventana_historial.title("Consultar Historial")
        ventana_historial.geometry("500x300")
        ventana_historial.configure(bg="black")

        Label(ventana_historial, text="ID Cliente:", font=("Arial", 12), bg="black", fg="white").place(x=50, y=50)
        entry_id_cliente = Entry(ventana_historial, font=("Arial", 12))
        entry_id_cliente.place(x=200, y=50, width=200)

        def buscar_historial():
            id_cliente = entry_id_cliente.get()
            try:
                micursor = conexion.cursor()
                sql = f"SELECT * FROM transacciones WHERE id_cliente={id_cliente}"
                micursor.execute(sql)
                resultado = micursor.fetchall()
                if not resultado:
                    messagebox.showinfo("Resultado", "No se ha encontrado información en el historial.")
                else:
                    historial_info = "\n".join([str(x) for x in resultado])
                    messagebox.showinfo("Resultado", historial_info)
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
            finally:
                micursor.close()

        boton_buscar = Button(ventana_historial, text="Buscar", font=("Arial", 12), command=buscar_historial)
        boton_buscar.place(x=200, y=150, width=100)

        ventana_historial.mainloop()




    def salir():
        ventana_empleado.destroy()






    boton_consultar_transaccion = Button(ventana_empleado, text="Consultar Transacción", font=("Arial", 12), command=consultar_transaccion)
    boton_consultar_transaccion.place(x=650, y=300, width=200)

    boton_consultar_historial = Button(ventana_empleado, text="Consultar Historial", font=("Arial", 12), command=consultar_historial)
    boton_consultar_historial.place(x=650, y=350, width=200)

    boton_salir = Button(ventana_empleado, text="Salir", font=("Arial", 12), command=salir)
    boton_salir.place(x=650, y=400, width=200)

    ventana_empleado.mainloop()
