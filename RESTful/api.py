from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

class getFlow(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('proto_name', type=str)
        parser.add_argument('src', type=str)
        parser.add_argument('sport', type=int)
        parser.add_argument('dst', type=str)
        parser.add_argument('dport', type=int)
        parser.add_argument('proto', type=int)
        parser.add_argument('push_flag_ratio', type=float)
        parser.add_argument('avrg_len', type=float)
        parser.add_argument('avrg_payload_len', type=float)
        parser.add_argument('pkt_count', type=int)
        parser.add_argument('avrg_inter_arrival_time', type=float)
        args = parser.parse_args()

        return args
    def get(self):
        print('get')

api.add_resource(getFlow, '/flow')

if __name__ == '__main__':
    app.run()
