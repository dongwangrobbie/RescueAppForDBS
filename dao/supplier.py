from config.dbconfig import pg_config
import psycopg2

# This is the way I can login to the database
# conn = psycopg2.connect("dbname=p1 user=DongWang password=wangdong host =127.0.0.1")

class SupplierDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByName(self, city):
        cursor = self.conn.cursor()
        query = "select * from supplier where sup_name = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, sid):
            cursor = self.conn.cursor()
            query = "select * from supplier where sup_id = %s;"
            cursor.execute(query, (sid,))
            result = cursor.fetchone()
            return result

    def getLatestSupplier(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM supplier ORDER BY created_at DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getPartsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select resource.resource_id, resource.res_type, resource.unit_price, resource.res_location, res_aval " \
                "from supplier join supplies on supplier.sup_id = supplies.sup_id " \
                "join resource on resource.resource_id = supplies.resource_id " \
                "where supplier.sup_id = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

