from flask import jsonify
from dao.administrator import AdministratorDAO


class AdministratorHandler:
    def build_administrator_dict(self, row):
        result = {}
        result['admin_id'] = row[0]
        result['uid'] = row[1]
        result['created_at'] = row[2]
        return result


    def getAllAdministrators(self):
        dao = AdministratorDAO()
        administrators_list = dao.getAllAdministrators()
        result_list = []
        for row in administrators_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        return jsonify(Administrators=result_list)

    def getAdministratorById(self, cid):
        dao = AdministratorDAO()
        row = dao.getAdministratorById(cid)
        if not row:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            part = self.build_administrator_dict(row)
        return jsonify(Administrator_id=part)

    def getLatestAdministrator(self):
        dao = AdministratorDAO()
        row = dao.getLatestAdministrator()
        if not row:
            return jsonify(Error="Latest Administrator Not Found"), 404
        else:
            part = self.build_administrator_dict(row)
        return jsonify(LatestAdministrator=part)


    def insertAdministrator(self, form):
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
                dao = AdministratorDAO()
                sid = dao.insertAdministrator(uid, category, first_name, last_name
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
                return jsonify(Customers=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def searchAdministrator(self, args):
        return -1
    #     if len(args) > 1:
    #         return jsonify(Error="Malformed search string."), 400
    #     else:
    #         # phone = args.get("phone")
    #         if phone:
    #             dao = AdministratorDAO()
    #             # customer_list = dao.getustomerByPhone(phone)
    #             result_list = []
    #         else:
    #             return jsonify(Error="Malformed search string."), 400

