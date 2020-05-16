from config.dbconfig import pg_config
import psycopg2


class CompanyDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCompany(self):
        cursor = self.conn.cursor()
        query = "select * from company;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCompanyById(self, compid):
        cursor = self.conn.cursor()
        query = "select * from company where com_id = %s;"
        cursor.execute(query, (compid,))
        result = cursor.fetchone()
        return result

    def getCompanyByCompname(self, compname):
        cursor = self.conn.cursor()
        query = "select * from company where compname = %s;"
        cursor.execute(query, (compname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getConsumerByCompanyId(self, compid):
        cursor = self.conn.cursor()
        query = "select consid, consusername from consumer natural inner join company where compid = %s;"
        cursor.execute(query, (compid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCompanyId(self, compid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, ramount, rlocation from resources natural inner join company where compid = %s;"
        cursor.execute(query, (compid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByCompanyId(self, compid):
        cursor = self.conn.cursor()
        query = "select sid, susername, scompany from supplier natural inner join company where compid = %s;"
        cursor.execute(query, (compid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    ############ phase 3 ################################

    def insert(self, com_name, sup_id, com_phone):
        cursor = self.conn.cursor()
        query = "insert into company(com_name, sup_id, com_phone) values (%s, %s, %s) returning com_id;"
        cursor.execute(query, (com_name, sup_id, com_phone,))
        com_id = cursor.fetchone()[0]
        self.conn.commit()
        return com_id

    def update(self, compid, compname):
        cursor = self.conn.cursor()
        query = "update company set compname = %s where compid = %s;"
        cursor.execute(query, (compname, compid,))
        self.conn.commit()
        return compid

    def delete(self, compid):
        cursor = self.conn.cursor()
        query = "delete from company where compid = %s;"
        cursor.execute(query, (compid,))
        self.conn.commit()
        return compid
