import redis
import re

def getOnOff():
    r = redis.Redis(host='', port=6379, password='', decode_responses=True, db='0')

    cWvalue = r.get('config:order:orderhttpflag:cw')
    print('cWvalue:'+cWvalue)
    krestecValue = r.get('config:order:orderhttpflag:krestec')
    print('krestecValue:'+krestecValue)
    motorValue = r.get('config:order:orderhttpflag:motor')
    print('cWvalue:'+motorValue)
    alist = [cWvalue, krestecValue, motorValue]
    return alist

# list = re.findall(r"'(.+?)'", list)
# list = "".join(list)  #atypical list -> str
# list = list.replace(' ', '')  #remove all spaces in str
# list = list.split(",")  #str -> normal list
