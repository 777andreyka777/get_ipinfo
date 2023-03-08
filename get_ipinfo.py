import ipinfo
import sys

#target
try:
    ip_adress = sys.argv[1] 
except IndexError:
    ip_adress = None

TOKEN = 'e4145508b44c3d' #ipinfo.io auth token

handler = ipinfo.getHandler(TOKEN)

details = handler.getDetails(ip_adress)

for key,value in details.all.items():
    print(f'{key}:{value}')

