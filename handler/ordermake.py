from flask import jsonify
from dao.ordermake import OrderDAO

class OrderHandler:
    def build_order_dict(self, row):
        result = {}
        result['ord_id'] = row[0]
        result['req_id'] = row[1]
        result['created_at'] = row[2]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['consusername'] = row[1]
        return result

    def build_reservation_dict(self, row):
        result = {}
        result['resid'] = row[0]
        result['restime'] = row[1]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['susername'] = row[1]
        result['sccompany'] = row[2]
        return result

    def build_order_attributes(self, odid, odnumber):
        result = {}
        result['odid'] = odid
        result['odnumber'] = odnumber
        return result

    def getAllOrder(self):
        dao = OrderDAO()
        order_list = dao.getAllOrder()
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getOrderById(self, ordid):
        dao = OrderDAO()
        row = dao.getOrderById(ordid)
        if not row:
            return jsonify(Error="Order Not Found"), 404
        else:
            order = self.build_order_dict(row)
        return jsonify(Order=order)

    def getLatestOrder(self):
        dao = OrderDAO()
        row = dao.getLatestOrder()
        if not row:
            return jsonify(Error="Latest Order Not Found"), 404
        else:
            part = self.build_order_dict(row)
        return jsonify(LatestOrder=part)

    def searchOrder(self, args):
        odnumber = args.get('odnumber')
        dao = OrderDAO()
        order_list = []
        if (len(args) == 1) and odnumber:
            order_list = dao.getOrderByNumber(odnumber)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in order_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getConsumerByOrderId(self, odid):
        dao = OrderDAO()
        if not dao.getOrderById(odid):
            return jsonify(Error="Order Not Found"), 404
        consumer_list = dao.getConsumerByOrderId(odid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getReservationByOrderId(self, odid):
        dao = OrderDAO()
        if not dao.getOrderById(odid):
            return jsonify(Error="Order Not Found"), 404
        reservation_list = dao.getReservationByOrderId(odid)
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def getSupplierByOrderId(self, odid):
        dao = OrderDAO()
        if not dao.getOrderById(odid):
            return jsonify(Error="Order Not Found"), 404
        supplier_list = dao.getSupplierByOrderId(odid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Order=result_list)

    def insertOrderJson(self, json):
        odnumber = json['odnumber']
        if odnumber:
            dao = OrderDAO()
            odid = dao.insert(odnumber)
            result = self.build_order_attributes(odid, odnumber)
            return jsonify(Order=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateOrder(self, odid, form):
        dao = OrderDAO()
        if not dao.getOrderById(odid):
            return jsonify(Error="Order not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                odnumber = form['odnumber']
                if odnumber:
                    dao.update(odid, odnumber)
                    result = self.build_order_attributes(odid, odnumber)
                    return jsonify(Order=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteOrder(self, odid):
        dao = OrderDAO()
        if not dao.getOrderById(odid):
            return jsonify(Error="Order not found."), 404
        else:
            dao.delete(odid)
            return jsonify(DeleteStatus="OK"), 200
