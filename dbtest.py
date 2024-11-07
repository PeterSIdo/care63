# db_test.py
import sys
from os.path import abspath, dirname


# Add 'app' directory to the sys.path
# Add the path to the db_connection module
sys.path.append(dirname(abspath(__file__)) + '/app')

from app.db_connection.conn import get_connection


def test_db():
    conn = get_connection()
    if conn is None:
        raise Exception('Database connection is not established.')

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Connected to -", db_version)


# Execute DELETE query
    delete_query = """
            DELETE FROM resident_list
            WHERE resident_firstname = 'empty'
        """
        
    cursor.execute(delete_query)
    conn.commit()
    print("Record deleted successfully")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    test_db()