from flask import jsonify
from dao.resource import ResourceDAO
from google_map import google_map

class ResourceHandler:
    def build_resource_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['res_type'] = row[1]
        result['res_price'] = row[2]
        result['res_loc'] = row[3]
        result['res_aval'] = row[4]
        result['res_info'] = row[5]
        result['res_free'] = row[6]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sup_id'] = row[0]
        result['sup_name'] = row[1]
        result['phone'] = row[2]
        return result

    # req_id, resource_id, res_type, req_need
    def build_resource_requested_dict(self, row):
        result = {}
        result['req_id'] = row[0]
        result['resource_id'] = row[1]
        result['res_type'] = row[2]
        result['res_need'] = row[3]
        return result




    # def build_part_attributes(self, res_id, res_type, unit_price):
    #     result = {}
    #     result['resource_id'] = res_id
    #     result['res_type'] = res_type
    #     result['unit_price'] = unit_price
    #     return result

    def getAllResource(self):
        dao = ResourceDAO()
        parts_list = dao.getAllResource()
        result_list = []
        for row in parts_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resource_Types=result_list)

    def getAllResourceRequested(self):
        dao = ResourceDAO()
        parts_list = dao.getAllResourceRequested()
        result_list = []
        for row in parts_list:
            result = self.build_resource_requested_dict(row)
            result_list.append(result)
        return jsonify(Resource_Requested=result_list)

    def getResourceById(self, pid):
        dao = ResourceDAO()
        row = dao.getResourceById(pid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            part = self.build_resource_dict(row)
            return jsonify(Resource=part)

    def getResourceByIdCity(self, pid):
        dao = ResourceDAO()
        row = dao.getResourceById(pid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            part = self.build_resource_dict(row)
            location = part['res_loc']
            gm = google_map()
            gm.map_city(location)
            return jsonify(Resource=part)

    def getResourceByIdRegion(self, pid):
        dao = ResourceDAO()
        row = dao.getResourceById(pid)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            part = self.build_resource_dict(row)
            location = part['res_loc']
            gm = google_map()
            gm.map_region(location)
            return jsonify(Resource=part)

    # def searchParts(self, args):
    #     dao = PartsDAO

    def deletePart(self, pid):
        dao = ResourceDAO()
        if not dao.getResourceById(pid):
            return jsonify(Error="Part Not Found."), 404
        else:
            dao.delete(pid)
            return jsonify(DeleteStatus="OK"), 200

    def updatePart(self, pid, form):
        dao = ResourceDAO()
        if not dao.getResourceById(pid):
            return jsonify(Error="Part Not Found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Column Amount in Malform."), 400
            else:
                res_type = form['res_type']
                unit_price = form['unit_price']
                if res_type and unit_price:
                    dao.update(pid, res_type, unit_price)
                    # result = self.build_part_attributes(pid, res_type, unit_price)
                    # return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected Attributes for Update Request."), 400

    def getSuppliersByResourceId(self, pid):
        dao = ResourceDAO()
        if not dao.getResourceById(pid):
            return jsonify(Error="Part Not Found"), 404
        suppliers_list = dao.getSuppliersByResourceId(pid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)



