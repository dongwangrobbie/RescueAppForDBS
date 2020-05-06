from flask import jsonify
from dao.user import UserDAO


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['appuser_id'] = row[0]
        result['appuser_type'] = row[1]
        result['appuser_name'] = row[2]
        result['appuser_password'] = row[3]
        return result

    def getAllUsers(self):
        dao = UserDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, cid):
        dao = UserDAO()
        row = dao.getUserById(cid)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            part = self.build_user_dict(row)
        return jsonify(User_id=part)

    def searchUsers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            user_id = args.get("user_id")
            if user_id:
                dao = UserDAO()
                users_list = dao.getUserById(user_id)
                result_list = []
                for row in users_list:
                    result = self.build_user_dict(row)
                    result_list.append(row)
                return jsonify(User=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400