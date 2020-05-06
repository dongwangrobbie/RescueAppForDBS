from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sup_id'] = row[0]
        result['sup_name'] = row[1]
        result['sup_phone'] = row[2]
        result['uid'] = row[3]
        result['created_at'] = row[4]
        return result

    def build_part_dict(self, row):
        result = {}
        result['resource_id'] = row[0]
        result['res_type'] = row[1]
        result['unit_price'] = row[2]
        result['res_location'] = row[3]
        result['res_aval'] = row[4]
        return result


    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            sup_name = args.get("sup_name")
            if sup_name:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByName(sup_name)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(row)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def getPartsBySupplierId(self, sid):
        dao = SupplierDAO()
        if not dao.getSupplierById(sid):
            return jsonify(Error="Supplier Not Found"), 404
        parts_list = dao.getPartsBySupplierId(sid)
        result_list = []
        for row in parts_list:
            result = self.build_part_dict(row)
            result_list.append(result)
        return jsonify(ResourceSupply=result_list)

    def getSupplierById(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            part = self.build_supplier_dict(row)
        return jsonify(Supplier=part)

    def getLatestSupplier(self):
        dao = SupplierDAO()
        row = dao.getLatestSupplier()
        if not row:
            return jsonify(Error="Latest Supplier Not Found"), 404
        else:
            part = self.build_supplier_dict(row)
        return jsonify(LatestSupplier=part)