# coding=utf-8
import itchat
import time
import datetime
import random
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler

print('全体注意！机器人现在开始登录。。。。。。\n' + time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())))


def after_login():
    print('\n全体注意！机器人已经登录。。。。。。\n' + time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())))


def after_logout():
    print('全体注意！机器人已经退出。。。。。。\n' + time.strftime('%Y.%m.%d:%H:%M:%S', time.localtime(time.time())))


itchat.auto_login(hotReload=True, loginCallback=after_login, exitCallback=after_logout)
room_name_class = '府小六年级二班'
room_id_class = itchat.search_chatrooms(name=room_name_class)[0].get('UserName')
room_name_family = '有家有爱'
room_id_family = itchat.search_chatrooms(name=room_name_family)[0].get('UserName')
room_name_education = '教体局教职工统计群'
room_id_education = itchat.search_chatrooms(name=room_name_education)[0].get('UserName')
room_name_school = '府小级部主任群'
room_id_school = itchat.search_chatrooms(name=room_name_school)[0].get('UserName')
room_name_computer = '府小信息实验图书团队'
room_id_computer = itchat.search_chatrooms(name=room_name_computer)[0].get('UserName')

scheduler = BackgroundScheduler()
m = str(datetime.datetime.now().month)
d = str(datetime.datetime.now().day)
timer = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def send_message_to_class():
    print('Class is ok.......')
    itchat.send('杨老师您好，没有新增情况。', toUserName=room_id_class)


def send_message_to_education():
    print('Education is ok.......')
    itchat.send('府前街小学{}月{}日无新增5类人员、无发热人员。《重点防控汇总-潍坊》已在平台修改。'.format(m, d), toUserName=room_id_education)


def send_message_to_school():
    print('School is ok.......')
    itchat.send('{}月{}日电教组无新增情况，一切正常。'.format(m, d), toUserName=room_id_school)


def send_message_to_computer():
    print('Computer is ok.......')
    itchat.send('1.居家照片；\n2.有无发热等新增情况；\n3.问卷。', toUserName=room_id_computer)


scheduler.add_job(send_message_to_class, 'cron', hour=7, minute=0, second=0, args=())
scheduler.add_job(send_message_to_education, 'cron', hour=8, minute=30, second=0, args=())
scheduler.add_job(send_message_to_school, 'cron', hour=8, minute=0, second=0, args=())
scheduler.add_job(send_message_to_computer, 'cron', hour=7, minute=30, second=0, args=())

scheduler.start()


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply(msg):
    if msg.User['NickName'] == room_name_class:
        if msg['ActualNickName'] == '数学老师' \
                or msg['ActualNickName'] == '英语周老师' \
                or msg['ActualNickName'] == '白兰鸽' \
                or ('语文' in msg['ActualNickName']) \
                or msg['ActualNickName'] == '美术老师' \
                or msg['ActualNickName'] == '音乐老师' \
                or msg['ActualNickName'] == '体育老师':
            if msg['Type'] == 'Video' or msg['Type'] == 'Picture' or msg['Type'] == 'Recording' or msg['Type'] == 'Attachment':
                # msg.download(msg['FileName'])   #这个同样是下载文件的方式
                #  注意：下载的文件存储在指定的文件中，直接将路径与FileName连接即可，如msg["Text"]('/tmp/wei_chat' + msg['FileName'])
                msg['Text'](msg['FileName'])
                itchat.send(msg['ActualNickName'] + '老师发布的：', toUserName=room_id_family)
                # itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg["FileName"]), msg["FromUserName"])
                itchat.send('@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName']), toUserName=room_id_family)
            if msg['Type'] == 'Text':
                time.sleep(random.random())
                itchat.send(msg['ActualNickName'] + '说'+timer+'：\n' + msg['Content'], toUserName=room_id_family)

            if msg['Type'] == 'Sharing':
                print('a sharing......')
                itchat.send("%s:\n%s\n%s" % (msg['Type'], msg['FileName'], msg['Url']), toUserName=room_id_family)

            if msg['Type'] == 'Map':
                print('a map......')
                itchat.send("%s:\n%s%s" % (msg['Type'],
                                           msg['Content'][:msg['Content'].index(':')] + '，' +
                                           msg['OriContent'][msg['OriContent'].index('poiname=\"')+9:msg['OriContent'].index('\" poiid=')],
                                           '\n' + msg['Url'] + '。'), toUserName=room_id_family)


itchat.run()
