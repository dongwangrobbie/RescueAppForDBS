# -*- coding: utf-8 -*-
from config.dbconfig import pg_config
import psycopg2


class ReservationDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservation(self):
        cursor = self.conn.cursor()
        query = "select * from reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationAvailable(self):
        cursor = self.conn.cursor()
        query = "select resource_id, res_type, res_aval " \
                "from resource where res_aval > 0 order by res_type;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

# resource_id, req_id, res_type, req_need
    def getReservationRequested(self):
        cursor = self.conn.cursor()
        query = "select resource_id, req_id, res_type, req_need " \
                "from request natural inner join resource " \
                "where request.resource_id = resource.resource_id order by res_type;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, resid):
        cursor = self.conn.cursor()
        query = "select * from reservation where res_id = %s;"
        cursor.execute(query, (resid,))
        result = cursor.fetchone()
        return result

    def getLatestReservation(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM reservation ORDER BY created_at DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        return result


    def getResourcesByReservationId(self, resid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rprice, ramount, rlocation from resources natural inner join reservations where resid = %s;"
        cursor.execute(query, (resid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, req_id, res_amount):
        cursor = self.conn.cursor()
        query = "insert into reservation(req_id, res_amount) values (%s, %s) returning res_id;"
        cursor.execute(query, (req_id, res_amount,))
        res_id = cursor.fetchone()[0]
        self.conn.commit()
        return res_id
