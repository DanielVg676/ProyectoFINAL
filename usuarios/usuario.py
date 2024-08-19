from conexionDB import *
import hashlib
from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, usuario=None, contrasena=None, nombre=None, direccion=None, telefono=None, email=None, id_empleado=None, id_cliente=None):
        self.__usuario = usuario
        self.__contrasena = contrasena               #hash_password(contrasena) if contrasena else None
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__id_empleado = id_empleado
        self.__id_cliente = id_cliente


    # Método para encriptar la contraseña
    def hash_password(self, contrasena):
        if contrasena is None:
            return None
        return hashlib.sha256(contrasena.encode()).hexdigest()

    # Getters y Setters
    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_contrasena(self):
        return self.__contrasena

    def set_contrasena(self, contrasena):
        self.__contrasena = self.hash_password(contrasena)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_id_empleado(self):
        return self.__id_empleado


    def get_id_cliente(self):
        return self.__id_cliente


    # Método para registrar un usuario
    def registrar(self):
        pass

    
    # Método para iniciar sesión    /// AQUI CAMBIE LA VARIABLE USUARIO POR CLIENTE Y EMPLEADO PARA PODER DIFERENCIAR Y NO TENER PROBLEMAS CUANDO SE ASIGNE UNA U OTRA
    @staticmethod
    def iniciar_sesion(usuario, contrasena):
        print(contrasena)
        try:
            # Verifica si es un cliente
            cursor.execute(
                "SELECT * FROM clientes WHERE usuario=%s AND contrasena=%s",
                (usuario, contrasena)
            )
            cliente = cursor.fetchone()
            if cliente:
                return cliente, "cliente"
            
            # Verifica si es un gerente o empleado
            cursor.execute(
                "SELECT * FROM empleados WHERE usuario=%s AND contrasena=%s",
                (usuario, contrasena)
            )
            empleado = cursor.fetchone()
            if empleado:
                if usuario == "987" and contrasena == "987":
                    return empleado, "gerente"
                else:
                    return empleado, "empleado"
            else:
                return None, None
        except Exception as e:
            print(f"Error al iniciar sesión: {e}")
            return None, None

    def eliminar_empleado(self):
        
        if conexion is None:
            return False

        try:
            print("Se llego al sql")
            cursor.execute(
                "DELETE FROM empleados WHERE id = %s",
                (self.get_id_empleado(),)
            )
            conexion.commit()
            return True

        except Exception as e:
            print(f"Error al eliminar el empleado: {e}")
            conexion.rollback()
            return False

        pass

class clientes(Usuario):
    def __init__(self, usuario, contrasena, nombre, direccion, telefono, email, ocupacion, historial, saldo, id_empleado=None, id_cliente=None):
        super().__init__(usuario, contrasena, nombre, direccion, telefono, email, id_empleado, id_cliente)
        self.__ocupacion = ocupacion
        self.__historial = historial
        self.__saldo = saldo

    # Métodos getter y setter
    def get_ocupacion(self):
        return self.__ocupacion

    def set_ocupacion(self, ocupacion):
        self.__ocupacion = ocupacion

    def get_historial(self):
        return self.__historial

    def set_historial(self, historial):
        self.__historial = historial

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        self.__saldo = saldo
    

    @staticmethod
    def registrar_Cliente(self):
        try:
            self.get_id_cliente()
            cursor.execute(
                "INSERT INTO clientes (id,usuario, contrasena, nombre, direccion, telefono, email, ocupacion, historial, saldo) VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (self.get_usuario(), self.get_contrasena(), self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_email(), self.get_ocupacion(), self.get_historial(), self.get_saldo())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar el usuario: {e}")
            return False
    
    @staticmethod
    def checar_balance(id):
        try:
            cursor.execute(
                "SELECT saldo FROM clientes where id=%s",
                ((id,))
            )
            resultado=cursor.fetchall()
            print(f"Tu saldo disponible es de {resultado}")
            return resultado
        except Exception as e:
            print(f"Error al registrar el usuario: {e}")
            return False
    
    def actualizar_datos(self):
        if conexion is None:
            return False
        cursor = conexion.cursor()
        try:
            consulta = """ UPDATE clientes SET usuario=%s, contrasena=%s, nombre=%s, direccion=%s, telefono=%s, email=%s WHERE id = %s """
            cursor.execute(consulta, (self.get_usuario(), self.get_contrasena(), self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_email(), self.get_id_cliente()))
            conexion.commit()
            print(f"Informacion de la persona con ID {self.get_id_cliente()} actualizados correctamente.")
            return True
        except Exception as e:
            print(f"Error al actualizar los datos: {e}")
            conexion.rollback()
            return False
        
class empleado(Usuario):
    def __init__(self, usuario, contrasena, nombre, direccion, telefono, email, salario, puesto, id_banco, id_empleado=None):
        super().__init__(usuario, contrasena, nombre, direccion, telefono, email, id_empleado)
        self.__salario = salario
        self.__puesto = puesto
        self.__id_banco = id_banco

    # Métodos getter y setter
    def get_salario(self):
        return self.__salario

    def set_ocupacion(self, salario):
        self.__salario = salario

    def get_puesto(self):
        return self.__puesto

    def set_puesto(self, puesto):
        self.__puesto = puesto

    def get_id_banco(self):
        return self.__id_banco

    def set_saldo(self, id_banco):
        self.__id_banco = id_banco
    

    @staticmethod
    def registrar_Empleado(self):
        try:
            cursor.execute(
                "INSERT INTO empleados (id,usuario, contrasena, nombre, direccion, telefono, email, salario, puesto, id_banco) VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (self.get_usuario(), self.get_contrasena(), self.get_nombre(), self.get_direccion(), self.get_telefono(), self.get_email(), self.get_salario(), self.get_puesto(), self.get_id_banco())
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar el usuario: {e}")
            return False
    
    def actualizar_salario(self):
        if conexion is None:
            return False
        cursor = conexion.cursor()
        try:
            consulta = """ UPDATE empleados SET salario=%s WHERE id = %s """
            cursor.execute(consulta, (self.get_salario(), self.get_id_empleado()))
            conexion.commit()
            print(f"Salario de la persona con ID {self.get_id_empleado()} actualizados correctamente.")
            return True
        except Exception as e:
            print(f"Error al actualizar los datos: {e}")
            conexion.rollback()
            return False
    
        

