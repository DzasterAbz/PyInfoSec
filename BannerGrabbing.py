import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Error Input! Usage: " +sys.argv[0]+ "<URL>")
    sys.exit(1)

webrequest = requests.get("https://"+sys.argv[1])
print("\n"+str(webrequest.headers))

gethostID_ = socket.gethostbyname(sys.argv[1])
print("\nIP Address of "+sys.argv[1]+" is: "+gethostID_)

requestAPI = requests.get("https://ipinfo.io/"+gethostID_+"/json")
responseAPI = json.loads(requestAPI.txt)

print("Location: "+responseAPI['loc'])
print("Region: "+responseAPI['region'])
print("City: "+responseAPI['city'])
print("Country: "+responseAPI['country'])