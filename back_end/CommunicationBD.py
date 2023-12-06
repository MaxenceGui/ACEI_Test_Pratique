import psycopg

DB_NAME = "ACEI_Test"
DB_HOST = "127.0.0.1"
DB_PASSWD = "Test18Ets!"
DB_PORT = "5432"

CREATE_TABLE = """
    CREATE TABLE players(
        id serial PRIMARY KEY,
        name text,
        gp integer,
        g integer,
        a integer,
        pts integer,
        pim integer,
        diff integer
    )
"""

class CommunicationBD:
    def __init__(self) -> None:
        self.__conn = None
        self.__curs = None
    
    def connection_bd(self):
        self.__conn = psycopg.connect(f"dbname={DB_NAME} user=postgres host={DB_HOST} port={DB_PORT} password={DB_PASSWD}")
        self.__curs = self.__conn.cursor()

    def close_db(self):
        self.__curs.close()
        self.__conn.close()

    def create_table(self):
        self.__curs.execute(CREATE_TABLE)
        self.__conn.commit()

    def drop_table(self, table_name: str):
        self.__curs.execute("DROP TABLE IF EXISTS %s", table_name)
        self.__conn.commit()

    def insert(self, info: list):
        self.__curs.execute("INSERT INTO players (name, gp, g, a, pts, pim, diff) VALUES(%s,%s,%s,%s,%s,%s, %s)", info)
        self.__conn.commit()
