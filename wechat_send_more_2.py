import itchat
from itchat.content import *
import os
import time

rec_tmp_dir = os.path.join(os.getcwd(), 'tmp/')
if not os.path.exists(rec_tmp_dir):
    os.mkdir(rec_tmp_dir)

itchat.auto_login()
room_name_family = '体育锻炼'
room_id_family = itchat.search_chatrooms(name=room_name_family)[0].get('UserName')


@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO, SHARING, MAP], isFriendChat=True, isGroupChat=True)
def handle_friend_msg(msg):

    if msg['Type'] == 'Text':
        print('ok.......')
        itchat.send(msg['Content'], toUserName=room_id_family)
    elif msg['Type'] == 'Picture' \
            or msg['Type'] == 'Recording' \
            or msg['Type'] == 'Video' \
            or msg['Type'] == 'Attachment':
        msg['Text'](rec_tmp_dir + msg['FileName'])

    elif msg['Type'] == 'Sharing':
        print('a sharing......')
        itchat.send("%s:\n%s\n%s" % (msg['Type'], msg['FileName'], msg['Url']), toUserName=room_id_family)
        itchat.send(msg, toUserName=room_id_family)

    elif msg['Type'] == 'Map':
        print('a map......')
        itchat.send("%s:\n%s%s" % (msg['Type'],
                                   msg['Content'][:msg['Content'].index(':')] + '，' +
                                   msg['OriContent'][msg['OriContent'].index('poiname=\"')+9:msg['OriContent'].index('\" poiid=')],
                                   '\n' + msg['Url'] + '。'), toUserName=room_id_family)


itchat.run()
