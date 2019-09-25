from flask_restful import Resource
from Model import Users, UsersSchema
from convert import ConvertData


class UsersResource(Resource):

    def post(self):
        populate = ConvertData()
        populate.populate_users_data()
        return {'status': 'success', 'message': 'Successfully added to the database'}, 201

    def get(self):
        users = Users.query.all()
        usere = UsersSchema(many=True).dump(users).data
        return {'status': 'success', 'data': usere}, 200
