from conexionDB import *

class Retiro:
    def __init__(self,id_cliente, monto,id_transaccion):
        self.__id_cliente=id_cliente
        self.__monto=monto
        self.__id_transaccion=id_transaccion
    
    def get_id_cliente(self):
        return self.__id_cliente

    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente

    def get_monto(self):
        return self.__monto

    def set_monto(self, monto):
        self.__monto = monto

    def get_id_transaccion(self):
        return self.__id_transaccion

    def set_id_transaccion(self, id_transaccion):
        self.__id_transaccion = id_transaccion

    def registrar_retiro(self):
            try:
                # Verificar saldo del cliente
                cursor.execute("SELECT saldo FROM clientes WHERE id = %s", (self.__id_cliente,))
                resultado = cursor.fetchone()
                
                if resultado is None:
                    print(f"El cliente con id {self.__id_cliente} no existe.")
                    return False
                
                saldo_cliente = resultado[0]

                if saldo_cliente >= self.__monto:
                    # Restar monto al saldo del cliente
                    nuevo_saldo = saldo_cliente - self.__monto
                    cursor.execute("UPDATE clientes SET saldo = %s WHERE id = %s", (nuevo_saldo, self.__id_cliente))
                    
                    # Registrar el retiro
                    cursor.execute(
                        "INSERT INTO retiros (id_retiro, id_cliente, monto, id_transaccion) VALUES (null, %s, %s, %s)",
                        (self.get_id_cliente(), self.get_monto(), self.get_id_transaccion())
                    )
                    conexion.commit()
                    return True
                else:
                    print("Saldo insuficiente para realizar el retiro.")
                    return False

            except Exception as e:
                print(f"Error al registrar el retiro: {e}")
                return False