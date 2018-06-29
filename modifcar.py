import sys
import MySQLdb

try:
    conn=MySQLdb.connect(host="localhost", user="root", passwd="1234", db="blockchain")
except MySQLdb.error:
    print ("error de conexion")
    sys.exit(1)
cursor=conn.cursor()

def agregar (self, nombre, clave):
    try:
        cursor.execute("""
        INSERT INTO usuarios(nombre, publicKey) 
        VALUES (%nombre, %clave)
        """ %(nombre,clave))
        cursor.execute("""
                INSERT INTO datos(nombre, archivo) 
                VALUES (%nombre, 0)
                """ % (nombre))
        conn.commit()
        print "añadido correctamente"
    except:
        conn.rollback()

    cursor.close()
    conn.close()

def agregar1 (self, nombre, archivo):
    try:
        cursor.execute("UPDATE datos set archivo='%archivo', WHERE nombre='%n'" %(archivo, nombre))
        conn.commit()
        print "añadido correctamente"
    except:
        conn.rollback()

    cursor.close()
    conn.close()

