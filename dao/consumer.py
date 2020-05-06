from config.dbconfig import pg_config
import psycopg2

# This is the way I can login to the database
# conn = psycopg2.connect("dbname=p1 user=DongWang password=wangdong host =127.0.0.1")

class ConsumerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllConsumers(self):
        cursor = self.conn.cursor()
        query = "select * from consumer;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, uid, category, first_name, last_name, payment_method, address, phone):
        cursor = self.conn.cursor()
        query = "insert into consumer(uid, category, first_name, last_name, payment_method, address, phone) values (%s, %s, %s, %s, %s, %s, %s) returning sid;"
        cursor.execute(query, (uid, category, first_name, last_name, payment_method, address, phone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

    def getConsumerByPhone(self, phone):
        cursor = self.conn.cursor()
        query = "select * from customer where phone = %s;"
        cursor.execute(query, (phone,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerById(self, cid):
        cursor = self.conn.cursor()
        query = "select * from consumer where consumer_id = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getLatestConsumer(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM consumer ORDER BY created_at DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

