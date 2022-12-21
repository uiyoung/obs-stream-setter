import obsws_python as obs
import sys
import logging
logging.basicConfig(level=logging.INFO)

# get arguments
argument = sys.argv


def setStream(server_url, stream_key):
    stream_type = "rtmp_custom"
    stream_settings = {
        'server': server_url,
        'key': stream_key,
        'bwtest': False,
        'use_auth': False
    }

    # pass conn info
    cl = obs.ReqClient(host='localhost', port=4455, password='123456')
    # set stream settings
    resp = cl.set_stream_service_settings(stream_type, stream_settings)
    # get stream settings info
    resp = cl.get_stream_service_settings()

    print('--- Stream Settings ---')
    print('- Server URL :', resp.stream_service_settings["server"])
    print('- Stream Key :', resp.stream_service_settings["key"])
    confirm = input("start stream with this setting? [y/n]")

    if confirm != 'y':
        print('cancelled')
        exit()

    # start stream
    cl.start_stream()


if __name__ == '__main__':
    # setStream('test', 'hi')
    setStream(argument[1], argument[2])
