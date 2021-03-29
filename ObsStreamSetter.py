import sys
from obswebsocket import obsws, requests, exceptions

# get arguments
argument = sys.argv

# connect to local websocket plugin
wsclient = obsws("localhost", 4444, "1234")
try:
    wsclient.connect()
except ConnectionRefusedError as e:
    print(e)
    print("websocket password를 확인해주세요.")
    exit()
except exceptions.ConnectionFailure as e:
    print(e)
    print("OBS를 먼저 켜주세요. 또는 port를 확인해주세요")
    exit()

# change key and save to disk
streamsettings = {'server': argument[1], 'key': argument[2]}
print("- Stream Url : {0}\n- Stream Key : {1}\n위와 같이 OBS Stream Setting을 변경하시겠습니까? (y/n)".format(streamsettings['server'], streamsettings['key']))
confirm = input()
if confirm != 'y':
    print('cancelled')
    exit()

wsclient.call(requests.SetStreamSettings("rtmp_custom", streamsettings, True))

# double check
streamsettings = wsclient.call(requests.GetStreamSettings()).getSettings()
print("\n다음과 같이 OBS Stream Setting이 설정되었습니다.")
print("- Stream Url : " + streamsettings["server"])
print("- Stream Key : " + streamsettings["key"])

wsclient.disconnect()
