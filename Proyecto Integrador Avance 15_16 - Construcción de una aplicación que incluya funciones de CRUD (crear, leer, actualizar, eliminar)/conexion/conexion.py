import os
import pg8000.dbapi


class CursorWrapper:
    def __init__(self, cursor, dictionary=False):
        self._cursor = cursor
        self.dictionary = dictionary

    def execute(self, *args, **kwargs):
        return self._cursor.execute(*args, **kwargs)

    def fetchone(self):
        row = self._cursor.fetchone()

        if row is None or not self.dictionary:
            return row

        columns = [desc[0] for desc in self._cursor.description]
        return dict(zip(columns, row))

    def fetchall(self):
        rows = self._cursor.fetchall()

        if not self.dictionary:
            return rows

        columns = [desc[0] for desc in self._cursor.description]
        return [dict(zip(columns, row)) for row in rows]

    def close(self):
        return self._cursor.close()


class ConnectionWrapper:
    def __init__(self, connection):
        self._connection = connection

    def cursor(self, dictionary=False):
        return CursorWrapper(
            self._connection.cursor(),
            dictionary=dictionary
        )

    def commit(self):
        return self._connection.commit()

    def rollback(self):
        return self._connection.rollback()

    def close(self):
        return self._connection.close()


def obtener_conexion():
    conexion = pg8000.dbapi.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=int(os.getenv("PGPORT", "5432")),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", "5432"),
        database=os.getenv("PGDATABASE", "smartpredict_ai")
    )

    return ConnectionWrapper(conexion)