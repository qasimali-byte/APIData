from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO
app = Flask(__name__)
socketio = SocketIO(app)
api = Api(app)
Sucess=False

def checkPostedDatalogon(postedData):#, functionName):
    global Sucess
    if "UserId" not in postedData:
        Sucess=False
        return Sucess #Missing parameter
    else:
        Sucess=True
        return Sucess

        return Sucess


class Logon(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedDatalogon(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)

            #Step 2: Add the posted data
        else:
            data = postedData['UserId']
            print(data)
            if(int(data)>1):
                Userdata=Authenticate_Custom_User(data)
                print(Userdata)

            retMap = {
                'Sucess': True
            }

            return jsonify(retMap)



api.add_resource(Logon, "/logon")
# api.add_resource(Logoff, "/logoff")
# api.add_resource(Getsession, "/getsession")
# api.add_resource(Getstatusdefaultuser, "/getstatusdefaultuser")
# api.add_resource(Getconfiguration, "/getconfiguration")
# api.add_resource(Setconfiguration, "/setconfiguration")
# api.add_resource(Getschedules, "/getschedules")
# api.add_resource(Createschedule, "/createschedule")
# api.add_resource(Setmaxpower, "/setmaxpower")
# api.add_resource(Setsolarmode, "/setsolarmode")
# api.add_resource(Getstatusnormaluser, "/getstatusnormaluser")

@app.route('/')
def hello_world():
    return "Welcome to the LocalRestAPI!"


if __name__=="__main__":
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
    app.run(debug=True)