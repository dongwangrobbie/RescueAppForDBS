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

    ############## Phase 3 ######################

    def insertAdmin(self, uid, admin_name):
        cursor = self.conn.cursor()
        query = "insert into administrator(uid, admin_name) values (%s, %s) returning admin_id;"
        cursor.execute(query, (uid, admin_name,))
        admin_id = cursor.fetchone()[0]
        self.conn.commit()
        return admin_id

    def update(self, said, uid, sausername):
        cursor = self.conn.cursor()
        query = "update sys_adm set uid = %s, sausername = %s where said = %s;"
        cursor.execute(query, (uid, sausername, said,))
        self.conn.commit()
        return said

    def delete(self, said):
        cursor = self.conn.cursor()
        query = "delete from sys_adm where said = %s;"
        cursor.execute(query, (said,))
        self.conn.commit()
        return said

