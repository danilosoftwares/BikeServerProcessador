import sqlite3

def Create():
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico (
                hash varchar(100) not null,
                data DATE NOT NULL,
                hora varchar(10) not null,
                ambiente INTEGER,
                salao_id INTEGER,
                tipo     VARCHAR(30),
                responsavel  VARCHAR(200) ,  
                PRIMARY KEY (hash)      
        );
        """)
        conn.close()

def Set(comando):
        retorno = {"status":0}
        conn = sqlite3.connect('banco.db')
        try:
                cursor = conn.cursor()
                cursor.execute(comando)
                conn.commit()
        except Exception as e:                
                conn.rollback()
                retorno = {"status":999,"error":str(e)}
        conn.close()
        return retorno

def Get(comando):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute(comando)
        retorno = []
        for linha in cursor.fetchall():
                retorno.append(linha)         
        conn.close()
        return retorno