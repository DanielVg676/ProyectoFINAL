from colorama import *
from conexionDB import *

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n \t \t Oprima cualquier tecla para continuar ...")
  input()  


def show_bank_name():
    print(Fore.RED+Style.BRIGHT+("██████╗░░█████╗░░█████╗░██╗███████╗██╗░█████╗░   ░██████╗████████╗░█████╗░███╗░░██╗██████╗░░█████╗░██████╗░████████╗"))
    print(Fore.BLUE+"██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║██╔══██╗   ██╔════╝╚══██╔══╝██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝")
    print(Fore.WHITE+"██████╔╝███████║██║░░╚═╝██║█████╗░░██║██║░░╚═╝   ╚█████╗░░░░██║░░░███████║██╔██╗██║██║░░██║███████║██████╔╝░░░██║░░░")
    print(Fore.RED+"██╔═══╝░██╔══██║██║░░██╗██║██╔══╝░░██║██║░░██╗   ░╚═══██╗░░░██║░░░██╔══██║██║╚████║██║░░██║██╔══██║██╔══██╗░░░██║░░░")
    print(Fore.BLUE+"██║░░░░░██║░░██║╚█████╔╝██║██║░░░░░██║╚█████╔╝   ██████╔╝░░░██║░░░██║░░██║██║░╚███║██████╔╝██║░░██║██║░░██║░░░██║░░░")
    print(Fore.WHITE+"╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░╚════╝░   ╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░")
    print()
    print(Style.RESET_ALL)

def show_complete():
    print()
    print(Fore.GREEN+Style.BRIGHT+"░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
    print(Fore.GREEN+Style.BRIGHT+"██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
    print(Fore.GREEN+Style.BRIGHT+"██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
    print(Fore.GREEN+Style.BRIGHT+"██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
    print(Fore.GREEN+Style.BRIGHT+"╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
    print(Fore.GREEN+Style.BRIGHT+" ╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
    print(Style.RESET_ALL)

def show_incomplete():
    print(Fore.RED+Style.BRIGHT+"██╗███╗░░██╗░█████╗░░█████╗░███╗░░░███╗██████╗░██╗░░░░░███████╗████████╗███████╗")
    print(Fore.RED+Style.BRIGHT+"██║████╗░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░░░░░██╔════╝╚══██╔══╝██╔════╝")
    print(Fore.RED+Style.BRIGHT+"██║██╔██╗██║██║░░╚═╝██║░░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░░░░██║░░░█████╗░░")
    print(Fore.RED+Style.BRIGHT+"██║██║╚████║██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░░░░██║░░░██╔══╝░░")
    print(Fore.RED+Style.BRIGHT+"██║██║░╚███║╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░███████╗███████╗░░░██║░░░███████╗")
    print(Fore.RED+Style.BRIGHT+"╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝░░░╚═╝░░░╚══════╝")
    print(Style.RESET_ALL)

def show_welcome():
    borrarPantalla()
    print(Fore.GREEN+Style.BRIGHT+"░██╗░░░░░░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗    ░░██╗██████╗░")
    print(Fore.GREEN+Style.BRIGHT+"░██║░░██╗░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝    ░██╔╝╚════██╗")
    print(Fore.GREEN+Style.BRIGHT+"░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░    ██╔╝░░█████╔╝")
    print(Fore.GREEN+Style.BRIGHT+"░░████╔═████║░██╔══╝░░██║░░░░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░    ╚██╗░░╚═══██╗")
    print(Fore.GREEN+Style.BRIGHT+"░░╚██╔╝░╚██╔╝░███████╗███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗    ░╚██╗██████╔╝")
    print(Fore.GREEN+Style.BRIGHT+"░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝    ░░╚═╝╚═════╝░")
    print(Style.RESET_ALL)

def show_warning():
    borrarPantalla()
    print(Fore.RED+Style.BRIGHT+"░██╗░░░░░░░██╗░█████╗░██████╗░███╗░░██╗██╗███╗░░██╗░██████╗░    ██╗██╗░░██╗")
    print(Fore.RED+Style.BRIGHT+"░██║░░██╗░░██║██╔══██╗██╔══██╗████╗░██║██║████╗░██║██╔════╝░    ╚═╝╚█║░██╔╝")
    print(Fore.RED+Style.BRIGHT+"░╚██╗████╗██╔╝███████║██████╔╝██╔██╗██║██║██╔██╗██║██║░░██╗░    ░░░░╚╝██╔╝░")
    print(Fore.RED+Style.BRIGHT+"░░████╔═████║░██╔══██║██╔══██╗██║╚████║██║██║╚████║██║░░╚██╗    ░░░░░░╚██╗░")
    print(Fore.RED+Style.BRIGHT+"░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║██║░╚███║██║██║░╚███║╚██████╔╝    ██╗░░░░╚██╗")
    print(Fore.RED+Style.BRIGHT+"░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░    ╚═╝░░░░░╚═╝")
    print(Style.RESET_ALL)

def show_exit_message():
    print()
    print(Fore.YELLOW+Style.BRIGHT+"██╗░░██╗░█████╗░██╗░░░██╗███████╗  ░█████╗░  ███╗░░██╗██╗░█████╗░███████╗  ██████╗░░█████╗░██╗░░░██╗")
    print(Fore.YELLOW+Style.BRIGHT+"██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔══██╗  ████╗░██║██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗╚██╗░██╔╝")
    print(Fore.YELLOW+Style.BRIGHT+"███████║███████║╚██╗░██╔╝█████╗░░  ███████║  ██╔██╗██║██║██║░░╚═╝█████╗░░  ██║░░██║███████║░╚████╔╝░")
    print(Fore.YELLOW+Style.BRIGHT+"██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══██║  ██║╚████║██║██║░░██╗██╔══╝░░  ██║░░██║██╔══██║░░╚██╔╝░░")
    print(Fore.YELLOW+Style.BRIGHT+"██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░██║  ██║░╚███║██║╚█████╔╝███████╗  ██████╔╝██║░░██║░░░██║░░░")
    print(Fore.YELLOW+Style.BRIGHT+"╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝  ╚═╝░░╚══╝╚═╝░╚════╝░╚══════╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░")
    print(Style.RESET_ALL)

def show_empleados():
    print("\n\t\t Selecciona la id del empleado")
    try:
        micursor = conexion.cursor()
        sql = "select * from empleados"
        micursor.execute(sql)
        resultado = micursor.fetchall()
    except:
        print("Ha ocurrido un error")
    else:
        for x in resultado:
            print(x)

def show_clientes():
    try:
        micursor = conexion.cursor()
        sql = "select * from clientes"
        micursor.execute(sql)
        resultado = micursor.fetchall()
    except:
        print("Ha ocurrido un error")
    else:
        for x in resultado:
            print(x)
