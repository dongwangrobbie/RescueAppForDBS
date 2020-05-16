from config.dbconfig import pg_config
import psycopg2


class OrderDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllOrder(self):
        cursor = self.conn.cursor()
        query = "select * from ordermake;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOrderById(self, ordid):
        cursor = self.conn.cursor()
        query = "select * from ordermake where ord_id = %s;"
        cursor.execute(query, (ordid,))
        result = cursor.fetchone()
        return result

    def getLatestOrder(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM ordermake ORDER BY created_at DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getOrderByNumber(self, odnumber):
        cursor = self.conn.cursor()
        query = "select * from orders where odnumber = %s;"
        cursor.execute(query, (odnumber,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByOrderId(self, odid):
        cursor = self.conn.cursor()
        query = "select consid, consusername from consumer natural inner join orders where odid = %s;"
        cursor.execute(query, (odid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationByOrderId(self, odid):
        cursor = self.conn.cursor()
        query = "select resid, restime from reservation natural inner join orders where odid = %s;"
        cursor.execute(query, (odid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByOrderId(self, odid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany from supplier natural inner join orders where odid = %s;"
        cursor.execute(query, (odid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, req_id, ord_amount):
        cursor = self.conn.cursor()
        query = "insert into ordermake(req_id, ord_amount) values (%s, %s) returning ord_id;"
        cursor.execute(query, (req_id, ord_amount,))
        ord_id = cursor.fetchone()[0]
        self.conn.commit()
        return ord_id

    def update(self, odid, odnumber):
        cursor = self.conn.cursor()
        query = "update orders set odnumber = %s where odid = %s;"
        cursor.execute(query, (odnumber, odid,))
        self.conn.commit()
        return odid

    def delete(self, odid):
        cursor = self.conn.cursor()
        query = "delete from orders where odid = %s;"
        cursor.execute(query, (odid,))
        self.conn.commit()
        return odid
