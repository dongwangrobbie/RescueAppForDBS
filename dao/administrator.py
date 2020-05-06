from config.dbconfig import pg_config
import psycopg2

# This is the way I can login to the database
# conn = psycopg2.connect("dbname=p1 user=DongWang password=wangdong host =127.0.0.1")

class AdministratorDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAdministrators(self):
        cursor = self.conn.cursor()
        query = "select * from administrator;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertAdministrator(self, uid, category, first_name, last_name, payment_method, address, phone):
        cursor = self.conn.cursor()
        query = "insert into consumer(uid, category, first_name, last_name, payment_method, address, phone) values (%s, %s, %s, %s, %s, %s, %s) returning sid;"
        cursor.execute(query, (uid, category, first_name, last_name, payment_method, address, phone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid



    def getAdministratorById(self, adid):
        cursor = self.conn.cursor()
        query = "select * from administrator where admin_id = %s;"
        cursor.execute(query, (adid,))
        result = cursor.fetchone()
        return result

    def getLatestAdministrator(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM administrator ORDER BY created_at DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        return result
