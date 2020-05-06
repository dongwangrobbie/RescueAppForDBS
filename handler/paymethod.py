from flask import jsonify
from dao.paymethod import PayMethodDAO

class PayMethodHandler:
    def build_pay_dict(self, row):
        result = {}
        result['pay_id'] = row[0]
        result['card_no'] = row[1]
        result['first_name'] = row[2]
        result['last_name'] = row[3]
        result['exp_date'] = row[4]
        result['consumer_id'] = row[5]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['consusername'] = row[1]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['susername'] = row[1]
        result['sccompany'] = row[2]
        return result

    def build_payment_attributes(self, pmid, pmname):
        result = {}
        result['pmid'] = pmid
        result['pmname'] = pmname
        return result

    def getAllPayMethod(self):
        dao = PayMethodDAO()
        payment_list = dao.getAllPayMethod()
        result_list = []
        for row in payment_list:
            result = self.build_pay_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def getPayMethodById(self, payid):
        dao = PayMethodDAO()
        row = dao.getPayMethodById(payid)
        if not row:
            return jsonify(Error="Payment Not Found"), 404
        else:
            order = self.build_pay_dict(row)
        return jsonify(PayMethod=order)

    def searchPayMethod(self, args):
        pmname = args.get('pmname')
        dao = PayMethodDAO()
        payment_list = []
        if (len(args) == 1) and pmname:
            payment_list = dao.getPayMethodByName(pmname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def getConsumerByPayMethodId(self, pmid):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment Not Found"), 404
        consumer_list = dao.getConsumerByPayMethodId(pmid)
        result_list = []
        for row in consumer_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def getSupplierByPayMethodId(self, pmid):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment Not Found"), 404
        supplier_list = dao.getSupplierByPayMethodId(pmid)
        result_list = []
        for row in supplier_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(PayMethod=result_list)

    def insertPayMethodJson(self, json):
        pmname = json['pmname']
        if pmname:
            dao = PayMethodDAO()
            pmid = dao.insert(pmname)
            result = self.build_payment_attributes(pmid, pmname)
            return jsonify(PayMethod=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updatePayMethod(self, pmid, form):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                pmname = form['pmname']
                if pmname:
                    dao.update(pmid, pmname)
                    result = self.build_payment_attributes(pmid, pmname)
                    return jsonify(PayMethod=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deletePayMethod(self, pmid):
        dao = PayMethodDAO()
        if not dao.getPayMethodById(pmid):
            return jsonify(Error="Payment not found."), 404
        else:
            dao.delete(pmid)
            return jsonify(DeleteStatus="OK"), 200
