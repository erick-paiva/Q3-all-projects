import psycopg2

# Criando a conexão com o banco de dados.
# Para conectar ao banco de dados postgres é preciso passar
# as seguintes informações:

conn = psycopg2.connect(host="localhost", database="psycopg2",
                        user="erick", password="8844")


cur = conn.cursor()


# Agora podemos executar as nossas queries, vamos criar uma nova tabela 
# caso ela não exista:

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS times (
	  id BIGSERIAL PRIMARY KEY,
	  nome_do_time VARCHAR NOT NULL,
	  divisao VARCHAR(128) NOT NULL 
    );
    """
)


# Inserindo dados na nossa tabela:
cur.execute("""
    INSERT INTO times 
        (nome_do_time, divisao)
    VALUES
        ('Zé do Leite FC', '1ª divisão'),
        ('Esporte Clube Estoura Dedo', '1ª divisão'),
        ('Atlético da esquina FC', '2ª divisão');
""")

# Pegando os dados que inserimos:
cur.execute("""
    SELECT * FROM times;
""")

# Para pegar a saída desses dados, rodamos o seguinte comando:
registros = cur.fetchall()
print(registros)

# Depois que executarmos nossos comandos, precisamos persistir as mudanças:
conn.commit()

# E por fim, não podemos esquecer de fechar nossa comunicação:
cur.close()
conn.close()
