from psycopg2 import sql, extras
import psycopg2
import os


configs = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}


class DatabaseConnector:
    @classmethod
    def get_connection(cls):
        cls.conn = psycopg2.connect(**configs)
        cls.cur = cls.conn.cursor(cursor_factory=extras.RealDictCursor)

    @classmethod
    def commit_and_close(cls):
        cls.conn.commit()
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def insert_into(cls, payload: dict, table_name: str):
        cls.get_connection()

        sql_table_name = sql.Identifier(table_name)
        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]

        query = sql.SQL(
            """
                INSERT INTO {table}
                    ({columns})
                VALUES
                    ({values})
                RETURNING *
            """
        ).format(
            table=sql_table_name,
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
        )

        cls.cur.execute(query)

        result = cls.cur.fetchone()

        cls.commit_and_close()

        return result

    @classmethod
    def select_all(cls, table_name: str):
        cls.get_connection()

        sql_table_name = sql.Identifier(table_name)

        query = sql.SQL(
            """
                SELECT * FROM {table}
            """
        ).format(table=sql_table_name)

        cls.cur.execute(query)

        result = cls.cur.fetchall()

        cls.commit_and_close()

        return result

    @classmethod
    def serialize(cls, values: tuple, columns: list[str]):
        return dict(zip(columns, values))
