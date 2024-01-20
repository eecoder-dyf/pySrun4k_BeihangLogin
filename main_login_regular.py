import os, time
from Login import *

user = os.environ['user']
pwd = os.environ['pwd']

# t = 0.25 # hour

while True:
    ret = check_online(gatewayUrl)
    # print(ret)
    #ret['online']  ret['ip']
    if not ret['online']:
        print(ret)
        retlogin = do_login(gatewayUrl, user, pwd)
        print("try login:")
        print(retlogin)
    else:
        with open("aliyun.py", 'r') as f:
            exec(f.read())
    time.sleep(30)

    # os.system("python Login.py login {} {}".format(user, pwd))
    # time.sleep(t*3600)