from conexionDB import *

class Transferencia:
    def __init__(self, id_emisor, usuario_destino, banco_destino, impuesto, id_transaccion, monto):
        self.__id_emisor=id_emisor
        self.__usuario_destino=usuario_destino
        self.__banco_destino=banco_destino
        self.__impuesto=impuesto
        self.__id_transaccion=id_transaccion
        self.__monto = monto
    
    def get_id_emisor(self):
        return self.__id_emisor

    def set_id_emisor(self, id_emisor):
        self.__id_emisor = id_emisor

    
    def get_usuario_destino(self):
        return self.__usuario_destino

    def set_usuario_destino(self, usuario_destino):
        self.__usuario_destino = usuario_destino

    def get_banco_destino(self):
        return self.__banco_destino

    def set_banco_destino(self, banco_destino):
        self.__banco_destino = banco_destino

    def get_impuesto(self):
        return self.__impuesto

    def set_impuesto(self, impuesto):
        self.__impuesto = impuesto

    def get_id_transaccion(self):
        return self.__id_transaccion
    
    def set_id_transaccion(self,id_transaccion):
        self.__id_transaccion = id_transaccion
    
    def get_id_monto(self):
        return self.__id_monto

    def set_id_monto(self, id_monto):
        self.__id_monto = id_monto

    

    def registrar_transferencia(self):
        try:
            # Verificar saldo del emisor
            cursor.execute("SELECT saldo FROM clientes WHERE id = %s", (self.__id_emisor,))
            resultado = cursor.fetchone()
            
            if resultado is None:
                print(f"El cliente con id {self.__id_emisor} no existe.")
                return False
            
            saldo_emisor = resultado[0]

            if saldo_emisor >= (self.__monto + self.__impuesto):
                # Restar monto al saldo del emisor
                nuevo_saldo_emisor = saldo_emisor - (self.__monto + self.__impuesto)
                cursor.execute("UPDATE clientes SET saldo = %s WHERE id = %s", (nuevo_saldo_emisor, self.__id_emisor))
                
                # Sumar monto al saldo del receptor
                cursor.execute("SELECT saldo FROM clientes WHERE usuario = %s", (self.__usuario_destino,))
                resultado = cursor.fetchone()
                
                if resultado is None:
                    print(f"El cliente destino con id {self.__usuario_destino} no existe.")
                    return False
                
                saldo_receptor = resultado[0]
                nuevo_saldo_receptor = saldo_receptor + self.__monto
                cursor.execute("UPDATE clientes SET saldo = %s WHERE usuario = %s", (nuevo_saldo_receptor, self.__usuario_destino))
                
                # Registrar la transferencia
                cursor.execute(
                    "INSERT INTO transferencias (id_transferencia, id_emisor, usuario_destino, banco_destino, impuesto, id_transaccion) VALUES (null, %s, %s, %s, %s, %s)",
                    (self.__id_emisor, self.__usuario_destino, self.__banco_destino, self.__impuesto, self.__id_transaccion)
                )
                conexion.commit()
                return True
            else:
                print("Saldo insuficiente para realizar la transferencia.")
                return False

        except Exception as e:
            print(f"Error al registrar la transferencia: {e}")
            return False