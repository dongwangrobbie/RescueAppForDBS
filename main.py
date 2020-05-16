from flask import Flask, jsonify, request, render_template
from handler.resource import ResourceHandler
from handler.supplier import SupplierHandler
from handler.consumer import ConsumerHandler
from handler.company import CompanyHandler
from handler.user import UserHandler
from handler.paymethod import PayMethodHandler
from handler.administrator import AdministratorHandler
from handler.reservation import ReservationHandler
from handler.ordermake import OrderHandler
from handler.request import RequestHandler
# Import Cross-Origin Resource Sharing to enable
# services on other ports on this machine or on other
# machines to access this app
from flask_cors import CORS, cross_origin

# Activate
app = Flask(__name__)
# Apply CORS to this app
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
    # return 'This will be located homepage!'

# 1.1 Resource -- Get

@app.route('/RescueApp/resource', methods=['GET', 'POST'])
def getAllResource():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ResourceHandler().insertResource(request.json)
    else:
        if not request.args:
            return ResourceHandler().getAllResource()
        else:
            return ResourceHandler().searchResource(request.args)

@app.route('/RescueApp/resource/requested', methods=['GET'])
def getAllResourceRequested():
    return ResourceHandler().getAllResourceRequested()


@app.route('/RescueApp/resource/<int:pid>', methods=['GET', 'PUT', 'DELETE'])
def getResourceById(pid):
    if request.method == 'GET':
        return ResourceHandler().getResourceById(pid)
    elif request.metod == 'PUT':
        return ResourceHandler().updatePart(pid, request.form)
    elif request.method == 'DELETE':
        return ResourceHandler().deletePart(pid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/RescueApp/resource/<int:pid>/city', methods=['GET'])
def getResourceByIdCity(pid):
    if request.method == 'GET':
        return ResourceHandler().getResourceByIdCity(pid)

@app.route('/RescueApp/resource/<int:pid>/region', methods=['GET'])
def getResourceByIdRegion(pid):
    if request.method == 'GET':
        return ResourceHandler().getResourceByIdRegion(pid)



# -----------------------------------------------------------------------#

# 2.1 Supplier -- Get

@app.route('/RescueApp/supplier', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        print("Request: ", request.json)
        return SupplierHandler().insertSupplier(request.json)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.json)

@app.route('/RescueApp/supplier/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SupplierHandler().getSupplierById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/RescueApp/supplier/latest', methods=['GET'])
def getLatestSupplier():
    return SupplierHandler().getLatestSupplier()

# -----------------------------------------------------------------------#

# 3.1 Resource and Supplier -- Get
@app.route('/RescueApp/resource/<int:pid>/suppliers', methods=['GET', 'POST'])
def getSupplierByResourceId(pid):
    return ResourceHandler().getSuppliersByResourceId(pid)

@app.route('/RescueApp/suppliers/<int:sid>/resource')
def getResourceBySuplierId(sid):
    return SupplierHandler().getPartsBySupplierId(sid)

# -----------------------------------------------------------------------#



# 4.1 Consumer -- Get
@app.route('/RescueApp/consumer', methods=['GET', 'POST'])
def getALLConsumers():
    if request.method == 'POST':
        return ConsumerHandler().insertConsumer(request.json)
    else:
        if not request.json:
            return ConsumerHandler().getAllConsumers()
        else:
            return ConsumerHandler().searchConsumers(request.json)

@app.route('/RescueApp/consumer/<int:cid>', methods=['GET', 'PUT', 'DELETE'])
def getConsumerById(cid):
    if request.method == 'GET':
        return ConsumerHandler().getConsumerById(cid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error = "Method not allowed"), 405

@app.route('/RescueApp/consumer/latest', methods=['GET'])
def getLatestConsumer():
    return ConsumerHandler().getLatestConsumer()

# -----------------------------------------------------------------------#

# 5.1 Administrator -- Get
@app.route('/RescueApp/administrator', methods=['GET', 'POST'])
def getALLAdministrator():
    if request.method == 'POST':
        print("Request: ", request.json)
        return AdministratorHandler().insertAdministrator(request.json)
    else:
        if not request.args:
            return AdministratorHandler().getAllAdministrators()
        else:
            return AdministratorHandler().searchAdministrator(request.json)

@app.route('/RescueApp/administrator/<int:adid>', methods=['GET', 'PUT', 'DELETE'])
def getAdministratorById(adid):
    if request.method == 'GET':
        return AdministratorHandler().getAdministratorById(adid)
    elif request.method == 'PUT':
        return AdministratorHandler().updateAdministrator(adid, request.form)
    elif request.method == 'DELETE':
        return UserHandler().deleteAdministrator(adid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/RescueApp/administrator/latest', methods=['GET'])
def getLatestAdministrator():
    return AdministratorHandler().getLatestAdministrator()


# -----------------------------------------------------------------------#

# 6.1 user -- get
@app.route('/RescueApp/appuser', methods=['GET', 'POST'])
def getAllUser():
    if request.method == 'POST':
        # return print("REQUEST: ", request.json)
        # return UserHandler().insertUserJson(request.json)
        return
    else:
        if not request.args:
            return UserHandler().getAllUsers()
        else:
            return UserHandler().searchUsers(request.args)


@app.route('/RescueApp/appuser/<int:uid>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(uid):
    if request.method == 'GET':
        return UserHandler().getUserById(uid)
    elif request.method == 'PUT':
        return UserHandler().updateUser(uid, request.form)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(uid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/RescueApp/user/<int:uid>/consumer')
def getConsumerByUserId(uid):
    return jsonify('UserHandler().getConsumerByUserId(uid)'), 200

@app.route('/RescueApp/user/<int:uid>/supplier')
def getSupplierByUserId(uid):
    return jsonify('UserHandler().getSupplierByUserId(uid)'), 200

@app.route('/RescueApp/user/<int:uid>/SysAdm')
def getSysAdmByUserId(uid):
    return jsonify('UserHandler().getSysAdmByUserId(uid)'), 200

# -----------------------------------------------------------------------#

# 7.1 company -- Get
@app.route('/RescueApp/company', methods=['GET', 'POST'])
def getAllCompany():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return CompanyHandler().insertCompanyJson(request.json)
    else:
        if not request.args:
            return CompanyHandler().getAllCompany()
        else:
            return CompanyHandler().searchCompanies(request.args)

@app.route('/RescueApp/company/<int:comid>', methods=['GET', 'PUT', 'DELETE'])
def getCompanyById(comid):
    if request.method == 'GET':
        return CompanyHandler().getCompanyById(comid)
    elif request.method == 'PUT':
        return CompanyHandler().updateCompany(comid, request.json)
    elif request.method == 'DELETE':
        return CompanyHandler().deleteCompany(comid)
    else:
        return jsonify(Error="Method not allowed."), 405

#
# @app.route('/RescueApp/company/<int:compid>/consumer')
# def getConsumerByCompanyId(compid):
#     return CompanyHandler().getConsumerByCompanyId(compid)
#
# @app.route('/RescueApp/company/<int:compid>/resources')
# def getResourcesByCompanyId(compid):
#     return CompanyHandler().getResourcesByCompanyId(compid)
#
#
# @app.route('/RescueApp/company/<int:compid>/supplier')
# def getSupplierByCompanyId(compid):
#     return CompanyHandler().getSupplierByCompanyId(compid)

# -----------------------------------------------------------------------#

# 8.1 paymethod -- Get

@app.route('/RescueApp/paymethod', methods=['GET', 'POST'])
def getAllPayMethod():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PayMethodHandler().insertPayMethodJson(request.json)
    else:
        if not request.args:
            return PayMethodHandler().getAllPayMethod()
        else:
            return PayMethodHandler().searchPayMethod(request.args)


@app.route('/RescueApp/paymethod/<int:payid>', methods=['GET', 'PUT', 'DELETE'])
def getPayMethodById(payid):
    if request.method == 'GET':
        return PayMethodHandler().getPayMethodById(payid)
    elif request.method == 'PUT':
        return PayMethodHandler().updatePayMethod(payid, request.form)
    elif request.method == 'DELETE':
        return PayMethodHandler().deletePayMethod(payid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/RescueApp/paymethod/<int:pmid>/consumer')
def getConsumerByPayMethodId(pmid):
    return PayMethodHandler().getConsumerByPayMethodId(pmid)


@app.route('/RescueApp/paymethod/<int:pmid>/supplier')
def getSupplierByPayMethodId(pmid):
    return PayMethodHandler().getSupplierByPayMethodId(pmid)

# 9.1 Reservation -- Get

@app.route('/RescueApp/reservation', methods=['GET', 'POST'])
def getAllReservations():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReservationHandler().insertReservation(request.json)
    else:
        if not request.args:
            return ReservationHandler().getAllReservation()
        else:
            return ReservationHandler().searchReservation(request.args)


@app.route('/RescueApp/reservation/<int:resid>', methods=['GET', 'PUT', 'DELETE'])
def getReservationsById(resid):
    if request.method == 'GET':
        return ReservationHandler().getReservationById(resid)
    elif request.method == 'PUT':
        return ReservationHandler().updateReservation(resid, request.form)
    elif request.method == 'DELETE':
        return ReservationHandler().deleteReservation(resid)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/RescueApp/reservation/<int:resid>/resources')
def getResourcesByReservationId(resid):
    return jsonify('ReservationsHandler().getResourcesByReservationId(resid)'), 200

@app.route('/RescueApp/reservation/latest', methods=['GET'])
def getLatestReservation():
    return ReservationHandler().getLatestReservation()

@app.route('/RescueApp/reservation/requested', methods=['GET'])
def getReservationRequest():
    return ReservationHandler().getReservationRequested()

@app.route('/RescueApp/reservation/available', methods=['GET'])
def getReservationAvailable():
    return ReservationHandler().getReservationAvailable()



# -----------------------------------------------------------------------#

# 10. ordermake -- Get

@app.route('/RescueApp/order', methods=['GET', 'POST'])
def getAllOrder():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return OrderHandler().insertOrder(request.json)
    else:
        if not request.args:
            return OrderHandler().getAllOrder()
        else:
            return OrderHandler().searchOrder(request.args)


@app.route('/RescueApp/order/<int:ordid>', methods=['GET', 'PUT', 'DELETE'])
def getOrderById(ordid):
    if request.method == 'GET':
        return OrderHandler().getOrderById(ordid)
    elif request.method == 'PUT':
        return OrderHandler().updateOrder(ordid, request.form)
    elif request.method == 'DELETE':
        return OrderHandler().deleteOrder(ordid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/RescueApp/order/latest', methods=['GET'])
def getLatestOrder():
    return OrderHandler().getLatestOrder()


# @app.route('/RescueApp/order/<int:odid>/consumer')
# def getConsumerByOrderId(odid):
#     return OrderHandler().getConsumerByOrderId(odid)
#
#
# @app.route('/RescueApp/order/<int:odid>/reservation')
# def getReservationByOrderId(odid):
#     return OrderHandler().getReservationByOrderId(odid)
#
#
# @app.route('/RescueApp/order/<int:odid>/supplier')
# def getSupplierByOrderId(odid):
#     return OrderHandler().getSupplierByOrderId(odid)

# 11. Request -- Get
@app.route('/RescueApp/request', methods=['GET', 'POST'])
def getAllRequest():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return RequestHandler().insertRequestJson(request.json)
    else:
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchRequest(request.args)

@app.route('/RescueApp/request/<int:reqid>', methods=['GET', 'PUT', 'DELETE'])
def getRequestById(reqid):
    if request.method == 'GET':
        return RequestHandler().getRequestById(reqid)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(reqid, request.form)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequest(reqid)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/RescueApp/request/latest', methods=['GET'])
def getLatestRequest():
    return RequestHandler().getLatestRequest()




if __name__ == '__main__':
    app.run(debug=True)