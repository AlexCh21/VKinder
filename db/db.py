
import psycopg2 as pg

from db.db_config import CONNSTR


def create_db():
    with pg.connect(CONNSTR) as conn:
        with conn.cursor() as cur:
            cur.execute()


def add_candidate(candidate, cursor):
    cursor.execute(candidate['id'], candidate['first_name'],
             candidate['last_name'], candidate['domain'])
    candidate_id = cursor.fetchone()[0]
    return candidate_id




if __name__ == '__main__':
    create_db()
    add_candidate()
