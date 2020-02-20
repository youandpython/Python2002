# coding=utf-8
import itchat
import time
import random
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler

itchat.auto_login(True)
room_name_class = '府小六年级二班'
room_id_class = itchat.search_chatrooms(name=room_name_class)[0].get('UserName')
room_name_family = '有家有爱'
room_id_family = itchat.search_chatrooms(name=room_name_family)[0].get('UserName')


scheduler = BackgroundScheduler()


def send_message_to_room():
    print('ok.......')
    itchat.send('杨老师您好，没有新增情况。', toUserName=room_id_class)


scheduler.add_job(send_message_to_room, 'cron', hour=7, minute=0, second=0, args=())
scheduler.start()


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply(msg):
    if msg.User['NickName'] == room_name_class:
        if msg['ActualNickName'] == '数学老师' or msg['ActualNickName'] == '英语周老师' or msg['ActualNickName'] == '白兰鸽' or ('语文' in msg['ActualNickName']):
            if msg['Type'] == 'Video' or msg['Type'] == 'Picture' or msg['Type'] == 'Recording' or msg['Type'] == 'Attachment':
                msg['Text'](msg['FileName'])
                itchat.send(msg['ActualNickName'] + '老师发布的：', toUserName=room_id_family)
                itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), toUserName=room_id_family)

            if msg['Type'] == 'Text':
                time.sleep(random.uniform(0.1, 2.5))
                # itchat.send(msg['ActualNickName'] + '老师说的：', toUserName=room_id_family)
                itchat.send(msg['ActualNickName'] + '说：\n' + msg['Content'], toUserName=room_id_family)


itchat.run()
