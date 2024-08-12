from colorama import *
from transacciones import transaccion, transferencia, prestamo, retiro
from usuarios import usuario
from funciones import *

def main1():
    borrarPantalla()
    # Mostrar logo banco
    show_bank_name()

    # Mostrar opciones usuario
    mostrar_menu2()

def mostrar_menu2():
    while True:
        print("\n\t..::: BIENVENIDO A PACIFIC STANDART :::..")

        while True:
            try:
                opcion = int(input("\n\t Seleccione una opción:\n\t1.-Login\n\t2.-Registrar\n\t3.-Salir\n\n\t---->"))
                if opcion in [1, 2, 3]:
                    break
                else:
                    print("Opción incorrecta, ingrese un número válido.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

        if opcion == 1:
            borrarPantalla()
            print("\n\t..::: INICIA SESION :::..")
            user = input("\n\t Ingresa tu usuario: ")
            contrasena = input("\n\t Ingresa tu contraseña: ")
            registro, tipo_usuario = usuario.Usuario.iniciar_sesion(user, contrasena)
            
            if registro:
                borrarPantalla()
                if tipo_usuario == 'cliente':
                    actions_menu(registro[0])
                elif tipo_usuario == 'empleado':
                    actions_menu_empleado(registro[0:2])
                elif tipo_usuario == "gerente":
                    actions_menu_gerente(registro[0:2])
            else:
                print("Error al iniciar sesión.")
                
        elif opcion == 2:
            print("\n\t..:: REGISTRO ::..")
            user = input("Ingrese número de usuario (*tarjeta): ")
            contrasena = input("Ingrese su contraseña: ")
            nombre = input("Ingrese su nombre: ")
            direccion = input("Ingrese su dirección: ")
            telefono = input("Ingrese número telefónico: ")
            email = input("Ingrese su email: ")
            ocupacion = input("Ingrese su ocupación: ")
            historial = ""
            
            while True:
                try:
                    saldo = float(input("Ingrese saldo inicial: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número.")

            objeto_cliente = usuario.clientes(user, contrasena, nombre, direccion, telefono, email, ocupacion, historial, saldo)
            registrado = usuario.clientes.registrar_Cliente(objeto_cliente)

            if registrado:
                borrarPantalla()
                show_welcome()
                esperarTecla()
            else:
                borrarPantalla()
                show_warning()
                print("\n\t Error al registrarse ")
                esperarTecla()
        elif opcion == 3:
            break
        
        else:
            print("Opción incorrecta, ingrese un número válido.")

def actions_menu(id):
    while True:
        print('---------------------------------')
        print()
        print(Fore.CYAN+Style.BRIGHT+"YOU CAN PERFORM THE NEXT ACTIONS")
        print(Fore.CYAN+Style.BRIGHT+"* Type only the number* \n\t1. Check balance\n\t2. Deposit to other accounts\n\t3. Withdraw money\n\t4. Realizar solicitud para un préstamo\n\t5. Actualizar datos\n\t6. Exit")
        print(Style.RESET_ALL)

        while True:
            try:
                opcion = int(input("\n\t Seleccione una opción: "))
                if opcion in [1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("Opción incorrecta, ingrese un número válido.")
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")

        if opcion == 1:
            borrarPantalla()
            print(".:: CHECAR BALANCE ::.")
            check = usuario.clientes.checar_balance(id)
            esperarTecla()
            borrarPantalla()
        elif opcion == 2:
            borrarPantalla()
            print(".:: Transferir dinero ::.")

            while True:
                try:
                    monto = float(input("\n\t Ingrese la cantidad a depositar: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número.")

            while True:
                try:
                    usuario_destino = int(input("\n\t Introduce el número de usuario receptor: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número.")

            while True:
                try:
                    banco_destino = int(input("Ingrese el ID del banco destino: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número.")

            descripcion = input("\n\t Introduce la descripción de la transferencia: ")
            tipo = "TRANSFERENCIA"
            impuesto = monto * .015
            id_emisor = id

            # Procesar la transacción y la transferencia
            registrar_transaccion = transaccion.crear_transaccion(descripcion, monto, id, tipo)
            crear_transferencia = transferencia.Transferencia(id_emisor, usuario_destino, banco_destino, impuesto, registrar_transaccion, monto)
            registrar_transferencia = crear_transferencia.registrar_transferencia()

            if registrar_transferencia:
                print("Transferencia registrada con éxito.")
            else:
                print("Error al realizar la transferencia.")
            esperarTecla()
            borrarPantalla()

        elif opcion == 3:
            borrarPantalla()
            print(".:: Retirar dinero ::.")

            while True:
                try:
                    monto = float(input("\n\t Ingrese la cantidad a retirar: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número.")

            descripcion = ""
            tipo = "RETIRO"

            # PROCESO PARA REGISTRAR TRANSACCIÓN
            registrar_transaccion = transaccion.crear_transaccion(descripcion, monto, id, tipo)

            # PROCESO PARA REGISTRAR RETIRO
            crear_retiro = retiro.Retiro(id, monto, registrar_transaccion)
            registrar_retiro = retiro.Retiro.registrar_retiro(crear_retiro)
            if registrar_retiro:
                print("Retiro registrado.")
            esperarTecla()
            borrarPantalla()

        elif opcion == 4:
            borrarPantalla()
            print(".:: Préstamos ::.")

            while True:
                try:
                    monto = float(input("\n\t Ingrese la cantidad del préstamo: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor ingrese un número.")

            descripcion = input("\n\t Ingrese la razón de este préstamo: ")
            tipo = "PRESTAMO"
            permiso_prestamo = False

            # PROCESO PARA REGISTRAR TRANSACCIÓN
            registrar_transaccion = transaccion.crear_transaccion(descripcion, monto, id, tipo)

            # PROCESO PARA REGISTRAR PRÉSTAMO
            crear_prestamo = prestamo.Prestamo(id, permiso_prestamo, registrar_transaccion)
            registrar_retiro = prestamo.Prestamo.registrar_prestamo(crear_prestamo)
            if registrar_retiro:
                print("Préstamo registrado.")
            esperarTecla()
            borrarPantalla()

        elif opcion == 5:
            borrarPantalla()
            print("\n\t..::: ACTUALIZA TUS DATOS :::..")
            nuevo_usuario = input("Ingrese su nuevo usuario: ")
            nueva_contrasena = input("Ingrese su nueva contraseña: ")
            nuevo_nombre = input("Ingrese su nuevo nombre: ")
            nueva_direccion = input("Ingrese su nueva dirección: ")
            nuevo_telefono = input("Ingrese su nuevo teléfono: ")
            nuevo_email = input("Ingrese su nuevo email: ")
            obj_cliente = usuario.clientes(nuevo_usuario, nueva_contrasena, nuevo_nombre, nueva_direccion, nuevo_telefono, nuevo_email, None, None, None, None, id)
            resultado = obj_cliente.actualizar_datos()

            if resultado:
                print(f"\n\t Los datos se han actualizado y guardado correctamente.")
                esperarTecla()
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
                esperarTecla()

        elif opcion == 6:
            borrarPantalla()
            break
        else:
            pass


#PARTE DEL MENU EMPLEADO -------


def actions_menu_empleado(id_empleado):
    show_welcome()
    esperarTecla()
    while True:
        borrarPantalla()
        show_bank_name()

        print("\n\t..::: BIENVENIDO A PACIFIC STANDART :::..")
        print("\n\t Menu de empleado regular")
        opcion = input("\n\t Seleccione una opción:\n\t1.-Consultar transaccion\n\t2.-Consultar historial\n\t3.-salir\n\n\t---->")

        if opcion == "1":
            borrarPantalla()
            print("..:: CONSULTAR TRANSACCION ::..")
            id_transaccion = input("\n\t Ingresa el id de la transaccion: ")

            try:
                micursor = conexion.cursor()
                sql = f"select * from transacciones WHERE id_transaccion={id_transaccion}"
                micursor.execute(sql)
                resultado = micursor.fetchall()
                if not resultado:
                        print("...::: No se ha encontrado informacion en el historial :::...")
            except:
                print("Ha ocurrido un error")
            else:
                for x in resultado:
                    print(x)
            finally:        
                esperarTecla()
            

        elif opcion == "2":
            borrarPantalla()
            print("\n\t\t..:: CONSULTAR HISTORIAL ::..")
            id_cliente = input("\n\t Ingresa el id del cliente: ")
            print("\n\t PARA CONFIRMAR SU IDENTIDAD INGRESE SU CONTRASEÑA")
            contrasena = str(input("\n\t contrasena: "))
            if contrasena == str(id_empleado[1]):
                print("\n\t\t..:: ACCESO AUTORIZADO ::..")
                print("\n\t\t..:: HISTORIAL ::..")
                try:
                    micursor = conexion.cursor()
                    sql = f"select * from transacciones WHERE id_cliente={id_cliente}"
                    micursor.execute(sql)
                    resultado = micursor.fetchall()
                    if not resultado:
                            print("\n\t...::: No se ha encontrado informacion en el historial :::...")
                except:
                    print("Ha ocurrido un error")
                else:
                    for x in resultado:
                        print(x)
                finally:        
                    esperarTecla()
            else:
                print("Contrasena incorrecta")
                esperarTecla()

        elif opcion == "3":
            break

        else:
            print("Opción incorrecta, ingrese un número válido")

def actions_menu_gerente(id_gerente):
    show_welcome()
    esperarTecla()
    while True:
        borrarPantalla()
        show_bank_name()

        print("\n\t..::: BIENVENIDO A PACIFIC STANDART :::..")
        print("\n\t\t\t MENU DE GERENTE")
        opcion = input("\n\t Seleccione una opción:\n\t1.-eliminar empleado\n\t2.-Registrar empleado\n\t3.-Actualizar salario\n\t4.-salir\n\n\t---->")

        if opcion == "1":
            borrarPantalla()
            print("..:: ELIMINAR EMPLEADO ::..")
            show_empleados()
            id_empleado = input("\n\t Ingresa el id del empleado: ")
            print("\n\t PARA CONFIRMAR SU IDENTIDAD INGRESE SU CONTRASEÑA")
            contrasena = str(input("\n\t contrasena: "))
            if contrasena == str(id_gerente[1]):
                print("\n\t\t..:: ACCESO AUTORIZADO ::..")
                obj_empleado= usuario.Usuario(None, None, None, None, None, None, id_empleado)
                resultado=obj_empleado.eliminar_empleado()

            else:
                print("Contrasena incorrecta")
                esperarTecla()

            print(f"{id_gerente}")
                
            if resultado:
                print(f"\n\t El empleado con id {id_empleado} se ha eliminado correctamente")
                esperarTecla()
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
                esperarTecla()
            
            

        elif opcion == "2":
            borrarPantalla()
            print("..:: REGISTRAR EMPLEADO ::..")
            user=input("ingrese numero de usuario (*tarjeta): ")
            contrasena=input("ingrese su contraseña: ")
            nombre=input("ingresa tu nombre: ")
            direccion=input("ingrese su dirección: ")
            telefono=input("ingrese numero telefonico: ")
            email=input("ingrese su email: ")
            salario=input("ingrese salario: ")
            puesto= input("ingreser puesto del empleado: ")
            id_banco=input("ingrese el id del banco correspondiente: ")

            objeto_cliente=usuario.empleado(user, contrasena, nombre, direccion, telefono, email, salario, puesto, id_banco)
            resultado=usuario.empleado.registrar_Empleado(objeto_cliente)

            if resultado:
                print(f"\n\t El empleado {nombre} se ha registrado correctamente")
                esperarTecla()
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
                esperarTecla()

        elif opcion == "3":
            borrarPantalla()
            print("\n\t ..:: ACTUALIZAR SALARIO ::..")
            show_empleados()
            id_empleado=input("\n\tIngrese la id de la persona: ")
            nuevo_salario=float(input("\n\tIngrese el nuevo salario: $"))
            obj_empleado= usuario.empleado(None, None, None, None, None, None, nuevo_salario, None, None, id_empleado)
            resultado=obj_empleado.actualizar_salario()

            if resultado:
                print(f"\n\t El salario se ha actualizado correctamente")
                esperarTecla()
            else:
                print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
                esperarTecla()
        
        elif opcion == "4":
            break

        else:
            print("Opción incorrecta, ingrese un número válido")


main1()
