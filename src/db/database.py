import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.create_tables()

    def create_tables(self):
        user_table_sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                full_name TEXT,
                email TEXT
            )
        """
        self.conn.execute(user_table_sql)

    def create_user(self, username, password, full_name, email):
        sql = "INSERT INTO users (username, password, full_name, email) VALUES (?, ?, ?, ?)"
        self.conn.execute(sql, (username, password, full_name, email))
        self.conn.commit()

    def get_user_by_id(self, user_id):
        sql = "SELECT id, username, password, full_name, email FROM users WHERE id = ?"
        cursor = self.conn.execute(sql, (user_id,))
        row = cursor.fetchone()
        if row is None:
            return None
        return {'id': row[0], 'username': row[1], 'password': row[2], 'full_name': row[3], 'email': row[4]}

    def get_user_by_username(self, username):
        sql = "SELECT id, username, password, full_name, email FROM users WHERE username = ?"
        cursor = self.conn.execute(sql, (username,))
        row = cursor.fetchone()
        if row is None:
            return None
        return {'id': row[0], 'username': row[1], 'password': row[2], 'full_name': row[3], 'email': row[4]}

    def authenticate_user(self, username, password):
        user = self.get_user_by_username(username)
        if user is None:
            return False
        return user['password'] == password

    def close(self):
        self.conn.close()