from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_socketio import SocketIO
import os
import xmltodict
import debugmode
from json2xml import json2xml
app = Flask(__name__)
socketio = SocketIO(app)
api = Api(app)
Sucess=False
import json
def checkPostedDataEVC(postedData):#, functionName):
    global Sucess
    if "CurrentVersionEVC" not in postedData:
        Sucess=False
        return Sucess #Missing parameter
    else:
        Sucess=True
        return Sucess
def checkPostedDataMC(postedData):#, functionName):
    global Sucess
    if "CurrentVersionMC" not in postedData:
        Sucess=False
        return Sucess #Missing parameter
    else:
        Sucess=True
        return Sucess

def checkpostdataforheartbeat(postedData):
    global Sucess
    if "DeviceID" and 'Status' not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess
def checkpostdataforuserlogin(postedData):
    global Sucess
    if "DeviceID" and 'Status' not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess
def checkpostdataforEVModuleStatuschange(postedData):
    global Sucess
    if "DeviceID" and 'Status' not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess
def checkpostdataforChargingstatus(postedData):
    global Sucess
    if "DeviceID" and 'ChargerStatus' not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess
def checkpostdataforrequestbycloudplatform(postedData):
    global Sucess
    if "DeviceID" not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess

def CheckDataForRecieveConfigurationFromEVSE(postedData):
    global Sucess
    if "DeviceID" and "RequestedEVSEConfiguration" not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess
def CheckDataForChargerLock(postedData):
    global Sucess
    if "DeviceID" and "ChargerLock" not in postedData:
        Sucess=False
        return Sucess
    else:
        Sucess=True
        return Sucess

class UpdateEVC(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedDataEVC(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
#-------------------------------------------------------------------------------Checking The Files--------------------------------------------------------------------------
        print("Creating and checking directries")
        pidatafolder = debugmode.dpath + "APIData"
        pd = os.path.isdir(pidatafolder)
        if (pd == False):
            os.makedirs(pidatafolder, mode=0o777)
        detailsfile = debugmode.dpath + "APIData/EVCversion.txt"
        vfile = os.path.isfile(detailsfile)
        if (vfile == False):
            file1 = open(detailsfile, 'w+')
            file1.write("")
            file1.close()
        efile = os.path.getsize(detailsfile)
        if (efile == 0):
            file1 = open(detailsfile, 'w+')
            file1.write("2;https://devomech.com/wp-content/uploads/2020/09/download.zip;1")
            file1.close()
        # reading Current version
        print("Reading Available version")
        file = open(detailsfile, 'r')
        for line in file:
            fields = line.split(";")
            Available_Version= fields[0]
            url=fields[1]
            print('Available_Version',Available_Version)
            #Step 2: Add the posted data
        retMap = {
            'Sucess': True,
            'Available_VersionEVC': Available_Version,
            'url':url
        }

        return jsonify(retMap)

#-----------------------------Update The Microcontroller Software--------------------------------

class UpdateMC(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkPostedDataMC(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
#-----------------------------Checking The Files---------------------------------
        print("Creating and checking directries")
        pidatafolder = debugmode.dpath + "APIData"
        pd = os.path.isdir(pidatafolder)
        if (pd == False):
            os.makedirs(pidatafolder, mode=0o777)
        detailsfile = debugmode.dpath + "APIData/MCversion.txt"
        vfile = os.path.isfile(detailsfile)
        if (vfile == False):
            file1 = open(detailsfile, 'w+')
            file1.write("")
            file1.close()
        efile = os.path.getsize(detailsfile)
        if (efile == 0):
            file1 = open(detailsfile, 'w+')
            file1.write("2;https://devomech.com/wp-content/uploads/2020/09/download.zip;1")
            file1.close()
        # reading Current version
        print("Reading Available version")
        file = open(detailsfile, 'r')
        for line in file:
            fields = line.split(";")
            Available_Version= fields[0]
            url=fields[1]
            print('Available_Version',Available_Version)
            #Step 2: Add the posted data
        retMap = {
            'Sucess': True,
            'Available_VersionMC': Available_Version,
            'url':url
        }

        return jsonify(retMap)
#---------------------------------------HeartBeat Class------------------------------
class HeartBeat(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkpostdataforheartbeat(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
        DeviceID=postedData['DeviceID']
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID
        }

        return jsonify(retMap)
class UserLogin(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkpostdataforheartbeat(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
        DeviceID = postedData['DeviceID']
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID
        }

        return jsonify(retMap)
class EVModuleStatuschange(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkpostdataforEVModuleStatuschange(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
        DeviceID = postedData['DeviceID']
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID
        }

        return jsonify(retMap)
class Chargingstatus(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkpostdataforChargingstatus(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
        DeviceID = postedData['DeviceID']
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID
        }

        return jsonify(retMap)

class ChargerLock(Resource):
    def post(self):
        postedData = request.get_json()
        status_code=CheckDataForChargerLock(postedData)
        ChargerStatus=postedData['ChargerLock']
        DeviceID=postedData['DeviceID']
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID,
            'ChargerStatus':ChargerStatus
        }

        return jsonify(retMap)

#----------------------------------------Here we are request to the EVC send me the following data--------------
class RequestbyCloudPlatfrom(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = checkpostdataforrequestbycloudplatform(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)

            #Step 2: Add the posted data
            with open("Recivedconfigurationfromevc.xml") as xml_file:
                data_dict = xmltodict.parse(xml_file.read())
                xml_file.close()
                currentconfiguration = json.dumps(data_dict)
        DeviceID = postedData['DeviceID']
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID,
            'Request':"SendConfiguration"      #To get the information from the client
            # 'UserValues':{'NAME':"Custom4",'USER_ID':"5",\
            #               'EMAIL':"Custom4@email.com",'PASSWORD':"5555"}, #in case when Create the user
            # 'DeleteUserID':"5",
            # 'NAME':"Custom2",
            # 'EMAIL':"Custom12@email.com",
            # 'PASSWORD':"5555",
            # 'Configuration':currentconfiguration,
            # 'UserId':"2" #change the Name or password of Given Id Users


        }

        return jsonify(retMap)

class RecieveConfigurationFromEVC(Resource):
    def post(self):
        postedData = request.get_json()
        status_code = CheckDataForRecieveConfigurationFromEVSE(postedData)
        if (status_code!=True):
            retJson = {
                "Sucess": False,
                "Message": "An error happened"
                }
            return jsonify(retJson)
        data=postedData['RequestedEVSEConfiguration']
        print(data)
        print(type(data))
        # final_dictionary = json.loads(data)
        # data = json2xml.Json2xml(final_dictionary , wrapper="all", pretty=True, attr_type=False).to_xml()
        # myfile = open("Recivedconfigurationfromevc.xml", "w")
        # myfile.write(data)
        # myfile.close()
        # FormattheXmlFile()
        DeviceID = postedData['DeviceID']
            #Step 2: Add the posted data
        retMap = {
            'Sucess': True,
            'DeviceID': DeviceID,
        }

        return jsonify(retMap)
#---------------------------------Format the XML File for Read------------------------------------
def FormattheXmlFile():
    f = open('Recivedconfigurationfromevc.xml', 'r')
    lines = f.readlines()
    lineslength = len(lines)
    f.close()
    print(lineslength)
    f = open('Recivedconfigurationfromevc.xml', 'w')
    f.write('\n'.join(lines[2:lineslength - 1]))
    f.close()


api.add_resource(UpdateEVC, "/updateevc")
api.add_resource(UpdateMC, "/updatemc")
api.add_resource(ChargerLock,'/chargerlock')
api.add_resource(HeartBeat,"/heartbeat")
api.add_resource(UserLogin,"/userlogin")
api.add_resource(EVModuleStatuschange,"/evmodulestatuschange")
api.add_resource(Chargingstatus,"/chargingstatus")
api.add_resource(RequestbyCloudPlatfrom, "/requestbycloudplatform")
api.add_resource(RecieveConfigurationFromEVC,"/sendevseconfigurationtocloud")  #recieveronfigurationfromevc

@app.route('/')
def hello_world():
    return "Welcome to the RestAPI!"

if __name__=="__main__":
    socketio.run(app, host='127.0.0.1', port=5000, debug=True,use_reloader=False)
    app.run(debug=True)
