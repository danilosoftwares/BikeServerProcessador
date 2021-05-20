import mysql.connector

def Create():
        cnx = mysql.connector.connect(user="dms@bikeserverproc", password='', host="bikeserverproc.mysql.database.azure.com", port=3306, database='bike', ssl_verify_cert=True)
        print(cnx)

# def Set(comando):
#         retorno = {"status":0}
#         conn = sqlite3.connect('banco.db')
#         try:
#                 cursor = conn.cursor()
#                 cursor.execute(comando)
#                 conn.commit()
#         except Exception as e:                
#                 conn.rollback()
#                 retorno = {"status":999,"error":str(e)}
#         conn.close()
#         return retorno

# def Get(comando):
#         conn = sqlite3.connect('banco.db')
#         cursor = conn.cursor()
#         cursor.execute(comando)
#         retorno = []
#         for linha in cursor.fetchall():
#                 retorno.append(linha)         
#         conn.close()
#         return retorno