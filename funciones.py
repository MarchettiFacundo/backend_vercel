import pandas as pd
from db import Database
#Datos para conexion
DB_USER = "devuser"
DB_PASS = "devpass"
DB_HOST = "localhost"  
DB_PORT = "5432"
DB_NAME = "devdb"

# URL de conexión
DATABASE_URL = "postgresql://neondb_owner:npg_2fdtB6URYonQ@ep-nameless-dream-adds7rjb-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require"

db = Database(DATABASE_URL)

# ____________SELECT____________
def get_materias():
    select_sql = "SELECT * FROM materia"
    params = None
    materias = db.select(select_sql,params)
    return materias.to_json()