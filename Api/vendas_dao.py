import psycopg2

db_config = {
    "host": "localhost",
    "database": "",
    "user": "postgres",
    "password": ""
}

def select_vendas():
    try:
        with psycopg2.connect(**db_config) as conexao:
            with conexao.cursor() as cursor:
                comando = f'SELECT * FROM vendas'
                cursor.execute(comando)
                resultado  = cursor.fetchall() # lendo o bd
                return resultado
    except psycopg2.Error as er:
        print("Ocorreu um erro consultar os dados: ", er)
        return None


def select_venda_por_id(id):
    try:
        with psycopg2.connect(**db_config) as conexao:
            with conexao.cursor() as cursor:
                comando = f'SELECT * FROM vendas WHERE id_vendas = {id}'
                cursor.execute(comando)
                resultado = cursor.fetchone()
                return resultado
    except psycopg2.Error as er:
        print("Id não encontrado", er)
        return None


def insert_venda(nome_produto, valor):
    try:
        with psycopg2.connect(**db_config) as conexao:
            with conexao.cursor() as cursor:
                comando = f"INSERT INTO vendas (nome_produto, valor) VALUES ('{nome_produto}',{valor})"
                cursor.execute(comando)
                conexao.commit()
                print("Dados inseridos com sucesso no banco de dados!")
    except psycopg2.Error as er:
        print("Ocorreu um erro ao inserir o produto:", er)
        return None

def update_venda(id, nome_produto, valor):
    try:
        with psycopg2.connect(**db_config) as conexao:
            with conexao.cursor() as cursor:
                comando = f"UPDATE vendas SET nome_produto = '{nome_produto}', valor = '{valor}' WHERE id_vendas = {id}"
                cursor.execute(comando)    
                conexao.commit()
                print("Dados alterados com sucesso no banco de dados!")
    except psycopg2.Error as er:
        print("Ocorreu um erro consultar os dados: ", er)
        return None

def delete_venda(nome_produto):
    try:
        with psycopg2.connect(**db_config) as conexao:
            with conexao.cursor() as cursor:
                comando = f"DELETE FROM vendas WHERE nome_produto = '{nome_produto}'"
                cursor.execute(comando)
                conexao.commit()
                print("Dados deletados com sucesso!")
    except psycopg2.Error as er:
        print("Ocorreu um erro consultar os dados: ", er)
        return None