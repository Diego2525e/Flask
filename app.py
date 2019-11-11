from flask import Flask
from flask_restplus import Api, Resource, fields
import json

app = Flask(__name__)                  
api = Api(app) 

resource_fields = api.model('Resource', {
    'elements': fields.List(fields.String)
})

@api.route('/')

class Sort(Resource):
    @api.doc(body=resource_fields)
    def post(self):
        objList = api.payload['elements']
        strList = [str(i) for i in objList]
        try:
            strList.sort()
        except:
            responseError = {}
            responseError["status"]="error"
            responseError["message"]="The method add(Object, String) in the type ArrayList<String> is not applicable for the arguments (object)"
            return {"Error":"-1"}
        response = {}
        response["status"]="success"
        response["message"]="ok"
        data = {}
        data["sorted"]=strList
        response["data"]=data
        return response

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')  