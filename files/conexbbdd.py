import mysql.connector
from mysql.connector import Error

class ConexBBDD():
    def add_reg(self, nombre_archivo, niv_azul, niv_ver, niv_roj):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='color_tracker',
                                                 user='root',
                                                 password='')
            cursor = connection.cursor()
            mySql_insert_query = """INSERT INTO trackingdata (Image, Histogram, BlueChannel, GreenChannel, RedChannel)
                                    VALUES (%s, %s, %s, %s, %s) """
            nombre = "{}.png".format(nombre_archivo)
            histograma = "{}-hst.png".format(nombre_archivo)
            print("[BBDD] Table trackingdata. {}-{}-{}-{}-{}".format(nombre, histograma, int(niv_azul[0]), int(niv_ver[0]), int(niv_roj[0])))
            recordTuple = (nombre, histograma, int(niv_azul[0]), int(niv_ver[0]), int(niv_roj[0]))
            cursor.execute(mySql_insert_query, recordTuple)
            connection.commit()


        except mysql.connector.Error as error:
            print("Error adding data in trackingdata {}".format(error))
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
