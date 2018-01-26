import sqlite3

class con():
    def __init__(self):
        """
        Construct of the class, create all table of brain
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()

        cursor.execute("drop table if exists pattern;")
        cursor.execute("drop table if exists response;")
        cursor.execute("""
        CREATE TABLE pattern(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            pattern text not NULL,
            section integer not NULL
        );
        """)
        cursor.execute("""
        CREATE TABLE response(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            response text not NULL,
            patternId integer not NULL
        );
        """)


        print("Brain iniciado com sucesso...")
        conn.close()

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

    def insertPattern(self,pattern,section):
        """
        Insert a new pattern in knowledge
        :param pattern: String
        :param section: Integer
        :return: Boolean
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pattern(pattern,section) VALUES('"+pattern+"',"+str(section)+");")
        conn.commit()
        conn.close()
        return True

    def insertResponse(self,response,patternId):
        """
        Insert a new response in knowledge
        :param pattern: String
        :param section: Integer
        :return: Boolean
        """
        conn = sqlite3.connect('brain.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO response(response,patternId) values('"+response+"',"+str(patternId)+");")
        conn.commit()
        conn.close()
        return True


c = con()
c.insertPattern("bom dia",1)
c.insertResponse("ola",1)