from flask import jsonify
from dao.consumer import ConsumerDAO


class ConsumerHandler:
    def build_consumer_dict(self, row):
        result = {}
        result['consumer_id'] = row[0]
        result['uid'] = row[1]
        result['consumer_firstname'] = row[2]
        result['consumer_lastname'] = row[3]
        result['address'] = row[4]
        result['phone'] = row[5]
        result['created_at'] = row[6]
        return result


    def getAllConsumers(self):
        dao = ConsumerDAO()
        customers_list = dao.getAllConsumers()
        result_list = []
        for row in customers_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Consuemrs=result_list)

    def getConsumerById(self, cid):
        dao = ConsumerDAO()
        row = dao.getConsumerById(cid)
        if not row:
            return jsonify(Error="Customer Not Found"), 404
        else:
            part = self.build_consumer_dict(row)
        return jsonify(Consumer_id=part)

    def getLatestConsumer(self):
        dao = ConsumerDAO()
        row = dao.getLatestConsumer()
        if not row:
            return jsonify(Error="Latest Consumer Not Found"), 404
        else:
            part = self.build_consumer_dict(row)
        return jsonify(LatestConsumer=part)

    def insertConsumer(self, form):
        if form and len(form) == 7:
            uid = form['uid']
            category = form['category']
            first_name = form['first_name']
            last_name = form['last_name']
            payment_method = form['payment_method']
            address = form['address']
            phone = form['phone']
            if uid and category and first_name and last_name\
                    and payment_method and address and phone:
                dao = ConsumerDAO()
                sid = dao.insert(uid, category, first_name, last_name
                                 /payment_method, address, phone)
                result = {}
                result['sid'] = sid
                result['uid'] = uid
                result['category'] = category
                result['first_name'] = first_name
                result['last_name'] = last_name
                result['payment_method'] = payment_method
                result['address'] = address
                result['phone'] = phone
                return jsonify(Consumers=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def searchConsumers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            phone = args.get("phone")
            if phone:
                dao = ConsumerDAO()
                customer_list = dao.getConsumerByPhone(phone)
                result_list = []
                for row in customer_list:
                    result = self.build_consumer_dict(row)
                    result_list.append(row)
                return jsonify(Consumers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400