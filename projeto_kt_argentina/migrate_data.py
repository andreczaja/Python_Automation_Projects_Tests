import sqlite3
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def migrate_kt_data():
    print("Iniciando migração dos dados...")
    
    # Conectar ao SQLite antigo
    sqlite_conn = sqlite3.connect('db_kt_argentina.db')
    
    # Conectar ao PostgreSQL novo
    pg_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    pg_cursor = pg_conn.cursor()
    
    # Criar tabela no PostgreSQL
    pg_cursor.execute('''CREATE TABLE IF NOT EXISTS table_kt (
        input_id SERIAL PRIMARY KEY,
        data DATE,
        task_name TEXT,
        status_kt TEXT,
        status_dtp TEXT
    )''')
    
    # Buscar dados do SQLite
    df_sqlite = pd.read_sql_query("SELECT * FROM table_kt", sqlite_conn)
    print(f"Encontrados {len(df_sqlite)} registros no SQLite")
    
    # Inserir dados no PostgreSQL
    for _, row in df_sqlite.iterrows():
        pg_cursor.execute("""
            INSERT INTO table_kt (data, task_name, status_kt, status_dtp) 
            VALUES (%s, %s, %s, %s)
        """, (row['data'], row['task_name'], row['status_kt'], row['status_dtp']))
    
    pg_conn.commit()
    print("Migração concluída com sucesso!")
    
    # Verificar migração
    pg_cursor.execute("SELECT COUNT(*) FROM table_kt")
    count = pg_cursor.fetchone()[0]
    print(f"Total de registros no PostgreSQL: {count}")
    
    sqlite_conn.close()
    pg_conn.close()

if __name__ == "__main__":
    migrate_kt_data()