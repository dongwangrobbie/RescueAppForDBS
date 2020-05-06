from config.dbconfig import pg_config
import psycopg2

# This is the way I can login to the database
# conn = psycopg2.connect("dbname=p1 user=DongWang password=wangdong host =127.0.0.1")

class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResource(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from resource where resource_id = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getAllResourceRequested(self):
        cursor = self.conn.cursor()
        query = "select req_id, resource_id, res_type, req_need " \
                "from request natural inner join resource " \
                "where request.resource_id = resource.resource_id;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def delete(self, pid):
        cursor = self.conn.cursor()
        query = "delete from resource where resource_id = %s;"
        cursor.execute(query, (pid,))
        self.conn.commit()
        return pid

    def update(self, resource_id, res_type, unit_price):
        cursor = self.conn.cursor()
        query = "update resource set resource_id = %s, res_type = %s, unit_price = %s where resource_id = %s;"
        cursor.execute(query, (resource_id, res_type, unit_price,))
        self.conn.commit()
        return resource_id

    def getSuppliersByResourceId(self, pid):
        cursor = self.conn.cursor()
        query = "select supplier.sup_id, supplier.sup_name, supplier.phone from " \
                "supplier join supplies on supplier.sup_id = supplies.sup_id " \
                "join resource on resource.resource_id = supplies.resource_id where resource.resource_id = %s;"
        cursor.execute(query, (pid,))
        result = []
        for row in cursor:
            result.append(row)
        return result



