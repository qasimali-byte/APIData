import requests
import json
import adresses



def UserInput():
    UserPassword=input('Enter the Password')
    UserPassword = int(UserPassword)
    load = {"UserPassword": UserPassword }
    print(load)
    # postingrequest
    print("Posting request")
    R_URL = adresses.logon
    data = json.dumps(load)
    headerJson = {"Content-Type": "application/json;charset=UTF-8",
                  "Accept": "*/*",
                  "Host":adresses.url,
                  "Connection": "keep-alive",
                  "User-Agent": "PostmanRuntime/7.32.0"}
    r = requests.post(R_URL, data=data, headers=headerJson)  # params=pload,
    a = json.loads(r.text)
    if (a.get('Sucess')):
        print('Return Success')
        print(a.get('UserId'))
        GetStatus(a.get('UserId'))

def GetStatus(data):
    data=int(data)
    load = {"UserId": data }
    print(load)
    print("Posting request")
    R_URL =adresses.getstatus
    data = json.dumps(load)
    headerJson = {"Content-Type": "application/json;charset=UTF-8",
                  "Accept": "*/*",
                  "Host":adresses.url,
                  "Connection": "keep-alive",
                  "User-Agent": "PostmanRuntime/7.32.0"}
    r = requests.post(R_URL, data=data, headers=headerJson)  # params=pload,
    a = json.loads(r.text)
    print("Extracting version")
    if (a.get('Sucess')):
        print('Hi')

def GetConfiguration(data):
    data=int(data)
    load = {"UserId": data }
    print(load)
    print("Posting request")
    R_URL =adresses.getconfiguration
    data = json.dumps(load)
    headerJson = {"Content-Type": "application/json;charset=UTF-8",
                  "Accept": "*/*",
                  "Host":adresses.url,
                  "Connection": "keep-alive",
                  "User-Agent": "PostmanRuntime/7.32.0"}
    r = requests.post(R_URL, data=data, headers=headerJson)  # params=pload,
    a = json.loads(r.text)
    print("Extracting version")
    if (a.get('Sucess')):
        print('Hi')
def SetConfiguration(data):
    data=int(data)
    load = {"UserId": data }
    print(load)
    print("Posting request")
    R_URL =adresses.setconfiguration
    data = json.dumps(load)
    headerJson = {"Content-Type": "application/json;charset=UTF-8",
                  "Accept": "*/*",
                  "Host":adresses.url,
                  "Connection": "keep-alive",
                  "User-Agent": "PostmanRuntime/7.32.0"}
    r = requests.post(R_URL, data=data, headers=headerJson)  # params=pload,
    a = json.loads(r.text)
    print("Extracting version")
    if (a.get('Sucess')):
        print('Hi')
def SetMaxPower(data):
    data=int(data)
    load = {"UserId": data }
    print(load)
    print("Posting request")
    R_URL =adresses.setmaxpower
    data = json.dumps(load)
    headerJson = {"Content-Type": "application/json;charset=UTF-8",
                  "Accept": "*/*",
                  "Host":adresses.url,
                  "Connection": "keep-alive",
                  "User-Agent": "PostmanRuntime/7.32.0"}
    r = requests.post(R_URL, data=data, headers=headerJson)  # params=pload,
    a = json.loads(r.text)
    print("Extracting version")
    if (a.get('Sucess')):
        print('Hi')
def SetSolarMode(data):
    data=int(data)
    load = {"UserId": data }
    print(load)
    print("Posting request")
    R_URL =adresses.setsolarmode
    data = json.dumps(load)
    headerJson = {"Content-Type": "application/json;charset=UTF-8",
                  "Accept": "*/*",
                  "Host":adresses.url,
                  "Connection": "keep-alive",
                  "User-Agent": "PostmanRuntime/7.32.0"}
    r = requests.post(R_URL, data=data, headers=headerJson)  # params=pload,
    a = json.loads(r.text)
    print("Extracting version")
    if (a.get('Sucess')):
        print('Hi')



def main():
    print('Test File for Local API')
    UserInput()

if __name__ == "__main__":
    main()