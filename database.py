import mysql.connector


def conectar():

    conexion = mysql.connector.connect(

        host="localhost",

        user="root",

        password="TU_CONTRASEÑA",

        database="ejercicios_python"

    )

    return conexion