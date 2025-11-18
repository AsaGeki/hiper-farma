from config import get_db_connection

class WorkerModel:

    @staticmethod
    def create(first_name, last_name, cpf):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO worker (first_name, last_name, cpf, hiring_date, operation, worker_role, gender) "
            "VALUES (%s, %s, %s, CURRENT_DATE, 'ativo', 'operador de caixa', 'masculino')",
            (first_name, last_name, cpf)
        )
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def list_all():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name, cpf FROM worker ORDER BY first_name")
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
