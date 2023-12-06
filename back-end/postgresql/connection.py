import psycopg
import traceback

from types import TracebackType

DB_NAME = "ACEI_Test"
DB_HOST = "127.0.0.1"
DB_PASSWD = "Test18Ets!"
DB_PORT = "5432"

class Connection:
    def __init__(self) -> None:
        self.__conn = None
        self.__curs = None

    def __enter__(self):
        self.__connection_bd()
        return self

    def __exit__(self, exc_type: BaseException, exc_value: BaseException, exc_tb: TracebackType) -> bool:
        self.__close_db()
        if isinstance(exc_value, Exception):
            trace = traceback.format_exception(exc_type, exc_value, exc_tb)
            print(''.join(trace))
            return False
        return True
    
    @property
    def connection(self):
        return self.__conn

    @property
    def cursor(self):
        return self._curs
    
    def __connection_bd(self):
        self.__conn = psycopg.connect(f"dbname={DB_NAME} user=postgres host={DB_HOST} port={DB_PORT} password={DB_PASSWD}")
        self.__curs = self.__conn.cursor()

    def __close_db(self):
        self.__curs.close()
        self.__conn.close()