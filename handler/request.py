from flask import jsonify
from dao.request import RequestDAO


class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        result['req_id'] = row[0]
        result['consumer_id'] = row[1]
        result['resource_id'] = row[2]
        result['req_need'] = row[3]
        result['created_at'] = row[4]
        return result


    def getAllRequest(self):
        dao = RequestDAO()
        request_list = dao.getAllRequest()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getRequestById(self, reqid):
        dao = RequestDAO()
        row = dao.getRequestById(reqid)
        if not row:
            return jsonify(Error="Reservation Not Found"), 404
        else:
            order = self.build_request_dict(row)
        return jsonify(Request=order)

    def getLatestRequest(self):
        dao = RequestDAO()
        row = dao.getLatestRequest()
        if not row:
            return jsonify(Error="Latest Request Not Found"), 404
        else:
            part = self.build_request_dict(row)
        return jsonify(LatestRequest=part)