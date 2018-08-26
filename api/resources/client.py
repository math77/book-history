from flask import jsonify, request
from flask_restful import Resource
from api.models import Client


class ClientResource(Resource):

    def post(self):
        args = request.get_json()
        username = args['username']
        email = args['email']
        password = args['password']
        client = Client(username=username, email=email, password=password)
        client.save()
        return jsonify({'message': 'Saved', 'code':'200'})

    def get(self, id_client=None):
        if id_client is None:
            data = Client.query.all()
            return jsonify([client.to_dict() for client in data])
        data = Client.query.filter_by(id=id_client).first()
        return jsonify(data.to_dict())
