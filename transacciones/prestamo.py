from conexionDB import *

class Prestamo:
    def __init__(self,id_cliente, permiso_prestamo,id_transaccion):
        self.__id_cliente=id_cliente
        self.__permiso_prestamo=permiso_prestamo
        self.__id_transaccion=id_transaccion
    
    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_permiso_prestamo(self):
        return self.__permiso_prestamo

    def set_permiso_prestamo(self, permiso_prestamo):
        self.__permiso_prestamo = permiso_prestamo

    def get_id_transaccion(self):
        return self.__id_transaccion

    def set_id_transaccion(self, id_transaccion):
        self.__id_transaccion = id_transaccion


    def registrar_prestamo(self):
        try:
            cursor.execute(
                "INSERT INTO prestamos (id_prestamo, id_cliente, permiso_prestamo, id_transaccion) VALUES (null, %s,%s, %s)",
                (self.get_id_cliente(), self.get_permiso_prestamo(), self.get_id_transaccion())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar el prestamo: {e}")
            return False