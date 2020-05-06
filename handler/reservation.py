from flask import jsonify
from dao.reservation import ReservationDAO


class ReservationHandler:
    def build_reservation_dict(self, row):
        result = {}
        result['res_id'] = row[0]
        result['req_id'] = row[1]
        result['created_at'] = row[2]
        return result

    # resource_id, req_id, res_type, req_need
    def build_reservation_requested_dict(self, row):
        result = {}
        result['res_id'] = row[0]
        result['req_id'] = row[1]
        result['res_type'] = row[2]
        result['req_need'] = row[3]
        return result

    # resource_id, res_type, res_aval
    def build_reservation_available_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['res_type'] = row[1]
        result['res_aval'] = row[2]
        return result

    def getAllReservation(self):
        dao = ReservationDAO()
        reservation_list = dao.getAllReservation()
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getReservationAvailable(self):
        dao = ReservationDAO()
        reservation_list = dao.getReservationAvailable()
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_available_dict(row)
            result_list.append(result)
        return jsonify(ReservationAvailalbeSorted=result_list)

    def getReservationRequested(self):
        dao = ReservationDAO()
        reservation_list = dao.getReservationRequested()
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_requested_dict(row)
            result_list.append(result)
        return jsonify(ReservationRequestedSorted=result_list)

    def getReservationById(self, payid):
        dao = ReservationDAO()
        row = dao.getReservationById(payid)
        if not row:
            return jsonify(Error="Reservation Not Found"), 404
        else:
            order = self.build_reservation_dict(row)
        return jsonify(Reservation=order)

    def getLatestReservation(self):
        dao = ReservationDAO()
        row = dao.getLatestReservation()
        if not row:
            return jsonify(Error="Latest Reservation Not Found"), 404
        else:
            part = self.build_reservation_dict(row)
        return jsonify(LatestReservation=part)

