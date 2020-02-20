import itchat
from itchat.content import *
import time

itchat.auto_login()

room_name_family = '有家有爱二'
room_id_family = itchat.search_chatrooms(name=room_name_family)[0].get('UserName')


@itchat.msg_register([TEXT, MAP, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply(msg):

    if msg.User['NickName'] == room_name_family:
        # # print(msg)
        for k, v in msg.items():
            print(k, ':', v)
        timer = time.strftime("%m-%d %H:%M:%S", time.localtime())

        if '<mpurl>' in msg['Content']:
            print('a video link......')
            url = msg['Content'].split('<mpurl>')[1].split('</mpurl')[0]
            itchat.send("%s%s:\n%s\n%s" % (msg['ActualNickName'] + '在' + timer + '分享的链接,', msg['Type'], msg['FileName'], url), toUserName=room_id_family)


itchat.run()
