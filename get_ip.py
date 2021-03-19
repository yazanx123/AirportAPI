import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("Insert URL :")
IP = socket.gethostbyname(url)
response=DbIpCity.get(IP,api_key='free')
print('IP:',IP)
print("City:" ,response.city)
print("Region:",response.region)
print("Country:",response.country)
