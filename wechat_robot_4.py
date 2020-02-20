# coding=utf-8
import itchat
import time
import os
import datetime
import random
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler

print('全体注意！机器人现在开始登录。。。。。。\n' + time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())))


def after_login():
    print('\n机器人已经登录。。。。。。\n' + time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())))


def after_logout():
    print('机器人已经退出。。。。。。\n' + time.strftime('%Y.%m.%d:%H:%M:%S', time.localtime(time.time())))


itchat.auto_login(loginCallback=after_login, exitCallback=after_logout, hotReload=True)
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
room_name_english = '6.2英语'
room_id_english = itchat.search_chatrooms(name=room_name_english)[0].get('UserName')

scheduler = BackgroundScheduler()
# m = str(datetime.datetime.now().month)
# d = str(datetime.datetime.now().day)
# timer = time.strftime("%m-%d %H:%M:%S", time.localtime())


def send_message_to_class():
    print('Class is ok.......')
    itchat.send('杨老师您好，没有新增情况。', toUserName=room_id_class)


def send_message_to_education():
    print('Education is ok.......')
    itchat.send('府前街小学{}月{}日无新增5类人员；无医学隔离和发热人员；《重点防控汇总-潍坊》数据无变化；《发热等特殊情况统计表》无新增人员。省外未归教职工已确定回诸日期，平台已修改。'
                .format(str(datetime.datetime.now().month), str(datetime.datetime.now().day)), toUserName=room_id_education)


def send_message_to_school():
    print('School is ok.......')
    path = 'E:\\school'
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) is True:
            new_name = file.replace(file, '{}月{}日图书电教实验共13人.rar'.format(str(datetime.datetime.now().month), str(datetime.datetime.now().day)))
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
    itchat.send_file(path+'\\'+os.listdir(path)[0], toUserName=room_id_school)
    itchat.send('{}月{}日电教组无新增情况，一切正常。'.format(str(datetime.datetime.now().month), str(datetime.datetime.now().day)), toUserName=room_id_school)


def send_message_to_computer():
    print('Computer is ok.......')
    itchat.send('早上好，又得麻烦大家:\n1.有无发热等新增情况？如果没有就不用上报了；\n2.健康台账不要忘了每天上午下午填写那个腾讯文档电子表格。', toUserName=room_id_computer)


scheduler.add_job(send_message_to_class, 'cron', hour=6, minute=50, second=0, args=())
scheduler.add_job(send_message_to_education, 'cron', hour=8, minute=30, second=0, args=())
scheduler.add_job(send_message_to_school, 'cron', hour=8, minute=0, second=0, args=())
scheduler.add_job(send_message_to_computer, 'cron', hour=7, minute=50, second=0, args=())

scheduler.start()


@itchat.msg_register([TEXT, MAP, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply(msg):
    if (msg.User['NickName'] == room_name_class) or (msg.User['NickName'] == room_name_english):
        if msg['ActualNickName'] == '数学老师' \
                or msg['ActualNickName'] == '英语周老师' \
                or msg['ActualNickName'] == '白兰鸽' \
                or ('语文' in msg['ActualNickName']) \
                or msg['ActualNickName'] == '美术老师' \
                or msg['ActualNickName'] == '音乐老师' \
                or msg['ActualNickName'] == '体育老师':
            timer = time.strftime("%m-%d %H:%M:%S", time.localtime())
            # li = '[呲牙][强][憨笑]😄[抱拳][鼓掌][偷笑]'
            if not (
                    (
                            ('[强]' in msg['Content'])
                            and ('@' in msg['Content'])
                            and (len(msg['Content']) < 15)
                    )
                    or (len(msg['Content']) < 5)
            ):
                if msg['Type'] == 'Recording':
                    msg['Text'](msg['FileName'])
                    time.sleep(random.random())
                    itchat.send(msg['ActualNickName']+'在'+timer + '发的语音：', toUserName=room_id_family)
                    itchat.send('@%s@%s' % ('fil', msg['FileName']), toUserName=room_id_family)
                if msg['Type'] == 'Picture':
                    msg['Text'](msg['FileName'])
                    time.sleep(random.random())
                    itchat.send(msg['ActualNickName']+'在'+timer + '发的图片：', toUserName=room_id_family)
                    itchat.send('@%s@%s' % ('img', msg['FileName']), toUserName=room_id_family)
                if msg['Type'] == 'Video':
                    msg['Text'](msg['FileName'])
                    time.sleep(random.random())
                    itchat.send(msg['ActualNickName']+'在'+timer + '发的视频：', toUserName=room_id_family)
                    itchat.send('@%s@%s' % ('vid', msg['FileName']), toUserName=room_id_family)
                if msg['Type'] == 'Attachment':
                    msg['Text'](msg['FileName'])
                    time.sleep(random.random())
                    itchat.send(msg['ActualNickName']+'在'+timer + '发的文件：', toUserName=room_id_family)
                    itchat.send('@%s@%s' % ('fil', msg['FileName']), toUserName=room_id_family)
                if msg['Type'] == 'Text':
                    if msg['FromUserName'] == itchat.get_friends(update=True)[0]['UserName']:
                        time.sleep(random.random())
                        itchat.send('我在'+timer+'说：\n' + msg['Content'], toUserName=room_id_family)
                    else:
                        time.sleep(random.uniform(0.1, 0.3))
                        itchat.send(msg['ActualNickName']+'在'+timer+'说：\n' + msg['Content'], toUserName=room_id_family)
                if '<mpurl>' in msg['Content']:
                    print('a video link......')
                    url = msg['Content'].split('<mpurl>')[1].split('</mpurl')[0]
                    time.sleep(random.random())
                    itchat.send("%s%s:\n%s\n%s" % (
                    msg['ActualNickName'] + '在' + timer + '分享的链接,', msg['Type'], msg['FileName'], url),
                                toUserName=room_id_family)
                elif msg['Type'] == 'Sharing':
                    print('a sharing......')
                    time.sleep(random.random())
                    itchat.send("%s%s:\n%s\n%s" % (msg['ActualNickName']+'在'+timer + '分享的链接,', msg['Type'], msg['FileName'],
                                                   msg['Url']), toUserName=room_id_family)
                if msg['Type'] == 'Map':
                    print('a map......')
                    time.sleep(random.random())
                    itchat.send("%s%s:\n%s%s" % (msg['ActualNickName']+'在'+timer + '发的位置，', msg['Type'],
                                               msg['Content'][:msg['Content'].index(':')] + '，' +
                                               msg['OriContent'][msg['OriContent'].index('poiname=\"')+9:msg['OriContent']
                                                 .index('\" poiid=')],
                                               '\n' + msg['Url'] + '。'), toUserName=room_id_family)


itchat.run()