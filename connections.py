import sqlite3

class con():
    def __init__(self):
        """
        Construct of the class, create all table of brain
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()

        cursor.execute("""
        drop table if exists pattern;
        drop table if exists response;
        CREATE TABLE pattern(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                pattern text not NULL,
                section integer not NULL
        );
        CREATE TABLE response(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                response text not NULL,
                patternId integer not NULL
        );
        """)

        print("Brain iniciado com sucesso...")
        conn.colse()

    def query(self,sql):
        """
        Execute a query in sqlite
        :param sql: String
        :return: Boolean
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.close()
        return True

    def insertPattern(self,pattern):
        
