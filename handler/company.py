from flask import jsonify
from dao.company import CompanyDAO

class CompanyHandler:
    def build_company_dict(self, row):
        result = {}
        result['com_id'] = row[0]
        result['com_name'] = row[1]
        result['sup_id'] = row[2]
        result['com_phone'] = row[3]
        return result

    def build_consumer_dict(self, row):
        result = {}
        result['consid'] = row[0]
        result['consusername'] = row[1]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rprice'] = row[2]
        result['rlocation'] = row[3]
        result['ramount'] = row[4]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['susername'] = row[1]
        result['sccompany'] = row[2]
        return result

    def build_company_attributes(self, compid, compname):
        result = {}
        result['compid'] = compid
        result['compname'] = compname
        return result

    def getAllCompany(self):
        dao = CompanyDAO()
        company_list = dao.getAllCompany()
        result_list = []
        for row in company_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Company=result_list)

    def getCompanyById(self, comid):
        dao = CompanyDAO()
        row = dao.getCompanyById(comid)
        if not row:
            return jsonify(Error="Company Not Found"), 404
        else:
            company = self.build_company_dict(row)
        return jsonify(Company=company)

    def searchCompanies(self, args):
        compname = args.get('compname')
        dao = CompanyDAO()
        company_list = []
        if (len(args) == 1) and compname:
            company_list = dao.getCompanyByCompname(compname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in company_list:
            result = self.build_company_dict(row)
            result_list.append(result)
        return jsonify(Company=result_list)

    def getCompanyByCompname(self, compname):
        dao = CompanyDAO()
        row = dao.getCompanyByCompname(compname)
        if not row:
            return jsonify(Error="Company Not Found"), 404
        else:
            company = self.build_company_dict(row)
            return jsonify(Company=company)

    def getConsumerByCompanyId(self, compid):
        dao = CompanyDAO()
        if not dao.getCompanyById(compid):
            return jsonify(Error="Company Not Found"), 404
        consumers_list = dao.getConsumerByCompanyId(compid)
        result_list = []
        for row in consumers_list:
            result = self.build_consumer_dict(row)
            result_list.append(result)
        return jsonify(Company=result_list)

    def getResourcesByCompanyId(self, compid):
        dao = CompanyDAO()
        if not dao.getCompanyById(compid):
            return jsonify(Error="Company Not Found"), 404
        resources_list = dao.getResourcesByCompanyId(compid)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Company=result_list)

    def getSupplierByCompanyId(self, compid):
        dao = CompanyDAO()
        if not dao.getCompanyById(compid):
            return jsonify(Error="Company Not Found"), 404
        suppliers_list = dao.getSupplierByCompanyId(compid)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Company=result_list)

    def insertCompanyJson(self, json):
        compname = json['compname']
        if compname:
            dao = CompanyDAO()
            compid = dao.insert(compname)
            result = self.build_company_attributes(compid, compname)
            return jsonify(Company=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateCompany(self, compid, form):
        dao = CompanyDAO()
        if not dao.getCompanyById(compid):
            return jsonify(Error="Company not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                compname = form['compname']
                if compname:
                    dao.update(compid, compname)
                    result = self.build_company_attributes(compid, compname)
                    return jsonify(Company=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def deleteCompany(self, compid):
        dao = CompanyDAO()
        if not dao.getCompanyById(compid):
            return jsonify(Error="Company not found."), 404
        else:
            dao.delete(compid)
            return jsonify(DeleteStatus="OK"), 200
