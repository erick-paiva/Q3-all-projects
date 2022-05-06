from app.models import DatabaseConnector
from psycopg2 import sql

class Anime(DatabaseConnector):

    
    def __init__(self, data:dict) -> None:
        
        self.anime = data["anime"].title()
        self.released_date = data["released_date"]
        self.seasons = data["seasons"]
     
    @classmethod
    def create_table_if_not_exists(self):
        
        self.get_connection()
        
        query = """
            CREATE TABLE IF NOT EXISTS animes(
                id 				BIGSERIAL 		PRIMARY KEY,
                anime 			VARCHAR(100) 	NOT NULL UNIQUE,
                released_date 	DATE 			NOT NULL,
                seasons 		INTEGER 		NOT NULL
                );
        """
        
        self.cur.execute(query)
        
        self.commit_and_close()
        
        
        
    def adcionar_anime(self):
        self.create_table_if_not_exists()
        result = self.insert_into(self.__dict__, "animes")
        
        return dict(result)
    
    @classmethod
    def obter_todos_animes(self):
        self.create_table_if_not_exists()
        result = self.select_all("animes")
        return result
    
    @classmethod
    def obter_anime_por_id(self, anime_id):
        
        self.create_table_if_not_exists()
        
        self.get_connection()
        query = sql.SQL(
            """
                SELECT * FROM animes
                WHERE id = {anime_id}
            """
        ).format(
            anime_id=sql.Literal(anime_id),
        )
        
        self.cur.execute(query)
        
        
        result = self.cur.fetchone()
        
        self.commit_and_close()
        
        return result
    
    @classmethod
    def atualizar_anime_por_id(self, data, anime_id):
        self.create_table_if_not_exists()
        self.get_connection()

        columns = [sql.Identifier(key) for key in data.keys()]
        values = [sql.Literal(value) for value in data.values()]
        id_serie = sql.Literal(anime_id)

        query = sql.SQL(
            """
            UPDATE
                animes
            SET
                ({columns}) = ROW({values})
            WHERE
                id = {anime_id}
            RETURNING *;
            """
        ).format(
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
            anime_id=id_serie
        )

        self.cur.execute(query)
        
        result = self.cur.fetchone()
        
        self.commit_and_close()

        return result
    
    @classmethod
    def deletar_anime_por_id(self, anime_id):
        self.create_table_if_not_exists()
        self.get_connection()
        
        id_serie = sql.Literal(anime_id)

        query = sql.SQL(
            """
            DELETE FROM
                animes
            WHERE
                id = {anime_id}
            RETURNING *;
            """
        ).format(
            anime_id=id_serie
        )

        self.cur.execute(query)
        
        result = self.cur.fetchone()
        
        self.commit_and_close()

        return result
       
