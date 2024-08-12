from conexionDB import *
import datetime

class Transaccion:
    def __init__(self, descripcion, monto, id_cliente, tipo):
        self.__descripcion = descripcion
        self.fecha = datetime.datetime.now()
        self.__monto = monto
        self.__id_cliente = id_cliente
        self.__tipo = tipo
    
    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def get_monto(self):
        return self.__monto

    def set_monto(self, monto):
        self.__monto = monto

    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, tipo):
        self.__tipo = tipo

    def registrar_transaccion(self):
        try:
            cursor.execute(
                "INSERT INTO transacciones (id_transaccion, descripcion, fecha, monto, id_cliente, tipo) VALUES (null, %s, %s, %s, %s, %s)",
                (self.get_descripcion(), self.fecha, self.get_monto(), self.get_id_cliente(), self.get_tipo())
            )
            conexion.commit()
            id_transaccion = cursor.lastrowid
            return id_transaccion

        except Exception as e:
            print(f"Error al registrar la transacción: {e}")
            return False
    

def crear_transaccion(descripcion, monto, id_cliente, tipo):
    # Crear una instancia 
    nueva_transaccion = Transaccion(descripcion, monto, id_cliente, tipo)
    # Registrar la transacción en la base de datos
    id_transaccion = nueva_transaccion.registrar_transaccion()
    return id_transaccion



def show_historial_transacciones(id_cliente):
    try:
        micursor = conexion.cursor()
        sql = f"select * from transacciones WHERE id_cliente={id_cliente}"
        micursor.execute(sql)
        resultado = micursor.fetchall()
        if not resultado:
                print("...::: No se ha encontrado informacion en el historial :::...")
    except:
        print("Ha ocurrido un error")
    else:
        for x in resultado:
            print(x)


def show_transaccion(self, id_transaccion):
    try:
        micursor = conexion.cursor()
        sql = "select * from transacciones WHERE id=%s"
        (self.get_id_cliente())
        micursor.execute(sql)
        resultado = micursor.fetchall()
        if not resultado:
                print("...::: No se ha encontrado la transaccion :::...")
    except:
        print("Ha ocurrido un error")
    else:
        for x in resultado:
            print(x)
