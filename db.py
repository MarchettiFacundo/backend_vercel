from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
import logging

logging.basicConfig(level=logging.DEBUG)

Base = declarative_base()

class Database:
    def __init__(self, database_url: str, echo: bool = False, pool_size: int = 5, timeout: int = 120000):
        try:
            self.engine = create_engine(
                database_url,
                echo=echo,
                pool_size=pool_size,
                connect_args={"connect_timeout": int(timeout/1000)}  # en segundos
            )
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            logging.info("✅ Conexión establecida con la base de datos")
        except SQLAlchemyError as e:
            logging.error(f"❌ Error conectando a la base de datos: {e}")
            raise

    def __execute(self, sql, params=None, fetch=False):
        try:
            with self.engine.connect() as conn:
                sql = text(sql)
                trans = conn.begin()
                logging.debug(f"Ejecutando SQL: {sql}")
                if params:
                    if isinstance(params, dict) or (isinstance(params, list) and all(isinstance(item, dict) for item in params)):
                        logging.debug(f"Con parámetros: {params}")
                        result = conn.execute(sql, params)
                    else:
                        raise ValueError("Params must be dict or list of dicts")
                else:
                    result = conn.execute(sql)

                if fetch:
                    df = pd.DataFrame(result.mappings().all())
                    trans.commit()
                    return df  

                trans.commit()
                logging.debug(f"Filas afectadas: {result.rowcount}")
                return result.rowcount
        except Exception as e:
            if 'trans' in locals() and trans.is_active:
                trans.rollback()
            error_message = f"{str(e)}"
            logging.error(f"❌ Error en query: {error_message}")
            raise Exception(f"[DB][execute], message: {error_message}")

    def insert(self, sql, params=None):
        return self.__execute(sql, params)

    def update(self, sql, params=None):
        return self.__execute(sql, params)

    def delete(self, sql, params=None):
        return self.__execute(sql, params)

    def select(self, sql, params=None):
        return self.__execute(sql, params, fetch=True)