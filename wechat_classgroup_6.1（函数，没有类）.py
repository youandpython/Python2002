"""
这是6.0版本，新增功用有：定时往群里发送截止时间之前剩余的时间；
统计结果自动排序，发往群里；
分发内容给各个负责人。。。
"""

import itchat
import time
import datetime
import random
import threading
import re
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler

itchat.auto_login(True)
scheduler = BackgroundScheduler()  # 单独线程的定时任务要放在函数前面
itchat.get_chatrooms(update=True)

'''获取各个项目微信群的ID
room_name_list = [0'龙源双语五年级六班', 1'有家有爱', 2'体育锻炼', 3'练字图片', 4'英语视频', 5'反思', 
                  6'语文说作文', 7'英语说作文',- 8'每日读书', 9'英语语音', 10英语一起作业', 11'五年级六班下通知临时群']'''
room_name_list = ['龙源双语五年级六班', '有家有爱', '体育锻炼', '练字图片', '英语视频', '反思',
                  '语文说作文', '英语说作文', '每日读书', '英语语音', '英语一起作业', '五年级六班下通知临时群']


'''获取各个项目群id'''


def to_room_id(num):
    room = itchat.search_chatrooms(name=room_name_list[num])
    to_id = room[0].get('UserName')
    return to_id


room_id = to_room_id(0)  # 当天主体群id,下面很多函数有引用，重要

'''定时发送截止时间提醒信息，后续再完善'''


def usable_time(h, m, send_to_id):
    now_h = datetime.datetime.now().hour
    now_m = datetime.datetime.now().minute
    '''下面把具体到秒的语句去掉了'''
    # now_s = datetime.datetime.now().second
    # s = 60
    '''这里也可以用现成的日期数值转日期对象的方法，进行比较。下处我是为了练手。'''
    if now_h < h or (now_h == h and now_m < m):
        if now_m > m:
            m = m + 60
            h = h - 1
        usable_h = h - now_h
        usable_m = m - now_m
        # usable_s = s - now_s
        tim_now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

        itchat.send(f'{tim_now}\n🕗🕗🕗🕗🕗🕗\n👉距终评还剩{usable_h}小时{usable_m}分📢\n加油💪👊👊👊💪', toUserName=send_to_id)


'''190424'''


def print_dic():

    itchat.send(dic_to_str(dic_clean(dic_recording)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_recording)), toUserName=to_room_id(9))

    itchat.send(dic_to_str(dic_clean(dic_picture)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_picture)), toUserName=to_room_id(3))

    itchat.send(dic_to_str(dic_clean(dic_think)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_think)), toUserName=to_room_id(5))

    itchat.send(dic_to_str(dic_clean(dic_eng_text)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_eng_text)), toUserName=to_room_id(7))

    itchat.send(dic_to_str(dic_clean(dic_read)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_read)), toUserName=to_room_id(8))

    itchat.send(dic_to_str(dic_clean(dic_chi_text)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_chi_text)), toUserName=to_room_id(6))

    itchat.send(dic_to_str(dic_clean(dic_eng_video)), toUserName=to_room_id(11))
    itchat.send(dic_to_str(dic_clean(dic_eng_video)), toUserName=to_room_id(4))

    itchat.send(dic_to_str(dic_clean(dic_eng_exercise)), toUserName=to_room_id(11))

    itchat.send(dic_to_str(dic_clean(dic_sport)), toUserName=to_room_id(11))

    time_now_str = time.strftime('%y-%m-%d')  # 返回当前时间，类型为str，格式为年月日
    filename = time_now_str + '.txt'

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_recording)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_picture)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_think)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_eng_text)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_read)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_chi_text)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_eng_video)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_eng_exercise)) + '\n' * 2)

    with open(filename, 'a') as f:
            f.write(dic_to_str(dic_clean(dic_sport)) + '\n' * 2)

    dic_recording.clear()
    dic_picture.clear()
    dic_think.clear()
    dic_eng_text.clear()
    dic_read.clear()
    dic_chi_text.clear()
    dic_eng_video.clear()
    dic_eng_exercise.clear()
    dic_sport.clear()

    dic_recording['今天英语语音上传成绩如下：'] = 99999
    dic_picture['今天练字及作业图片成绩如下：'] = 99999
    dic_think['今天每日反思成绩如下：'] = 99999
    dic_eng_text['今天英语说作文成绩如下：'] = 99999
    dic_read['今天每日读书成绩如下：'] = 99999
    dic_chi_text['今天语文说作文成绩如下：'] = 99999
    dic_eng_video['今天英语视频展示成绩如下：'] = 99999
    dic_eng_exercise['今天英语一起作业成绩如下：'] = 99999
    dic_sport['今天体育锻炼成绩如下：'] = 99999


'''190511,晚上休息时间截止提醒'''


def remind_rest(send_to_id):
    tim_now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    itchat.send(f'{tim_now}\n🕗🕗🕗🕗🕗🕗\n👉休息时间快要到了📢\n🌜🌜🌜🌜🌜🌜', toUserName=send_to_id)


'''发送定时器，h代表截止的小时数，m代表分钟数'''


def timer(h, m):
    # scheduler.add_job(usable_time, 'cron', hour='17-19', args=(19, 49))
    # scheduler.add_job(usable_time, 'interval', seconds=5, args=(19, 49, room_id))
    # scheduler.add_job(usable_time, 'cron', second='50', args=(14, 18, room_id))
    # 手动输入每天统计的截止时间
    # h, m = 19, 50
    # 190424
    scheduler.add_job(print_dic, 'cron', hour=h, minute=m, second=0, args=())
    scheduler.add_job(remind_rest, 'cron', hour=21, minute=20, second=0, args=(room_id,))

    # scheduler.add_job(usable_time, 'cron', day_of_week='sat,sun', hour='6-17', minute='30', second=0, args=(h, m, room_id))

    # scheduler.add_job(usable_time, 'cron', day_of_week='sat,sun', hour=19, minute=20, second=0, args=(h, m, room_id))

    scheduler.add_job(usable_time, 'cron', hour=6, minute=30, second=0, args=(h, m, room_id))
    # scheduler.add_job(usable_time, 'cron', day_of_week='1-5', hour=12, minute=30, second=0, args=(h, m, room_id))
    # scheduler.add_job(usable_time, 'cron', day_of_week='1-5', hour=17, minute=30, second=0, args=(h, m, room_id))
    scheduler.add_job(usable_time, 'cron', hour=18, minute=00, second=0, args=(h, m, room_id))
    # scheduler.add_job(usable_time, 'cron', day_of_week='1-7', hour=18, minute=30, second=0, args=(h, m, room_id))
    scheduler.add_job(usable_time, 'cron', hour=19, minute=00, second=0, args=(h, m, room_id))
    scheduler.add_job(usable_time, 'cron', hour=19, minute=50, second=0, args=(h, m, room_id))
    # scheduler.add_job(usable_time, 'cron', day_of_week='1-5', hour=19, minute=40, second='1', args=(h, m, room_id))


    scheduler.start()


timer(20, 00)  # 将截止小时数和分钟数置入函数中

'''统计英文或汉字数量'''


def get_word_nums(text):
    if len(text) == 1:  # 防止输入一个字符
        ch = text[0]
    else:
        ch = text[1]
    if ord(ch) in range(97, 123) or ord(ch) in range(65, 91):  # 判断是否是英文大小写字母
        error_list = ['.', ',', '?', '？', ':', '\'', '  ']  # 英文文章检索
        for err in error_list:
            text = text.replace(err, '')
        i = 0
        for space in text:
            if space == ' ':
                i += 1
        i = i + 1
        return '英语说作文共计', i, '个单词', '坚持下去，你就是英语专家！'
    '''汉字部分的检索,包括读书时间、反思、说作文'''
    if ('分钟' and '读' in text) and len(text) < 25:
        for r in text:
            if not r.isdigit():
                text = text.replace(r, '')
        return '每日读书共计', text, '分钟', '下一个故事大王就是你！'
    if '反思' in text:
        num = 0
        for word in text:
            if word not in '\n!"#$%&()*+,-./，。:;？<=>?@[\\]^_`{|}~':
                num += 1
        return '每日反思共计', num, '个汉字', '懂得反思和总结的同学，心灵是最美的！'

    if ('一起作业' in text) and len(text) < 15:
        pass
        return '英语一起作业', '坚持得', '很好', '持之以恒的精神最可贵！'

    if '体育锻炼' in text:
        pass
        return '体育锻炼', '很精彩', '，文明其精神，野蛮其体魄', '你的身体一定会很健康！'

    if (len(text) < 200) and ('英语学习机器人' not in text):
        pass
        return '未知信息', '已', '收到', '机器人正在眩晕中。。。'

    if len(text) > 200:
        number = 0
        for chi in text:
            if chi not in '\n!"#$%&()*+,-./，。:;？<=>?@[\\]^_`{|}~':
                number += 1
        return '语文说作文共计', number, '个汉字', '快成演讲家了，恭喜你！'


'''构造阿拉伯数字基数词变为英语序数词函数'''


def num_to_eng(num):
    eng_list = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                'eleventh', 'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth',
                'eighteenth', 'nineteenth', 'twentieth', 'thirtieth', 'thirty-first', 'thirty-second',
                'thirty-third', 'thirty-fourth', 'thirty-fifth', 'thirty-sixth', 'thirty-seventh',
                'thirty-eighth', 'thirty-ninth', 'fortieth', 'forty-first', 'forty-second', 'forty-third',
                'forty-fourth', 'forty-fifth', 'forty-sixth', 'forty-seventh', 'forty-eighth', 'forty-ninth',
                'fiftieth', 'fifty-first', 'fifty-second', 'fifty-third', 'fifty-fourth', 'fifty-fifth',
                'fifty-sixth', 'fifty-seventh', 'fifty-eighth', 'fifty-ninth', 'sixtieth', 'sixty-first',
                'sixty-second', 'sixty-third', 'sixty-fourth', 'sixty-fifth', 'sixty-sixth', 'sixty-seventh',
                'sixty-eighth', 'sixty-ninth', 'seventieth', 'seventy-first', 'seventy-second', 'seventy-third',
                'seventy-fourth', 'seventy-fifth', 'seventy-sixth', 'seventy-seventh', 'seventy-eighth',
                'seventy-ninth', 'eightieth', 'eighty-first', 'eighty-second', 'eighty-third', 'eighty-fourth',
                'eighty-fifth', 'eighty-sixth', 'eighty-seventh', 'eighty-eighth', 'eighty-ninth', 'ninetieth',
                'ninety-first', 'ninety-second', 'ninety-third', 'ninety-fourth', 'ninety-fifth', 'ninety-sixth',
                'ninety-seventh', 'ninety-eighth', 'ninety-ninth', 'one', 'hundredth']

    str_num = eng_list[num-1]
    return str_num


'''遍历字典并打印出键值对'''


def print_all_dic(dic):  # 参数为字典类型
    for key, val in dic.items():
        print(key + ':' + str(val))


'''遍历取出群内所有成员昵称，放到字典中'''


def get_chatroom_members():
    '''get all members of chatroom'''
    chat_room = itchat.search_chatrooms(name=room_name_list[1])[0]
    wechat_name_uuid = chat_room.get('UserName')
    chatroom = itchat.update_chatroom(wechat_name_uuid, detailedMember=True)
    group_members_dic = {}
    for member in chatroom['MemberList']:
        group_members_dic_key = member['DisplayName']
        group_members_dic[group_members_dic_key] = 0
    return group_members_dic  # 以上代码块是获取当前微信群内全部成员昵称的字典，没有NickName键值，这个需要在群消息互动过程中 动态添加


'''以下，将放置语音等项目成绩单的字典初始化为空'''

dic_recording = {'今天英语语音上传成绩如下：': 99999}
dic_picture = {'今天练字及作业图片成绩如下：': 99999}
dic_think = {'今天每日反思成绩如下：': 99999}
dic_eng_text = {'今天英语说作文成绩如下：': 99999}
dic_read = {'今天每日读书成绩如下：': 99999}
dic_chi_text = {'今天语文说作文成绩如下：': 99999}
dic_eng_video = {'今天英语视频展示成绩如下：': 99999}
dic_eng_exercise = {'今天英语一起作业成绩如下：': 99999}
dic_sport = {'今天体育锻炼成绩如下：': 99999}


'''上面还要添加其它分支用到的字典copy语句'''

'''对字符串进行非法字符的清洗'''


def name_clean(name):
    '''清洗非法字符'''
    error_name_list = ['爸爸', '妈妈', '的', '。', ' ', '(', ')', '（', '）']  # 群内家长的昵称中含有的非法字符列表集
    emoji_list = [chr(value) for value in range(0x1f300, 0x1f6ff)]  # 表情集，也可和上面列表连成一个列表
    msg_name = name  # 将当前发言者的昵称赋值给一个变量
    '''清洗'''
    for err in error_name_list:  # 清洗个别字符
        msg_name = msg_name.replace(err, '')
    for err2 in emoji_list:  # 清洗表情符号
        msg_name = msg_name.replace(err2, '')

    return msg_name


'''对字典进行大范围非法字符串的清洗，并排序输出，需要调用上面的字符串清洗函数'''


def dic_clean(dic_name):  # 形参为字典类型
    ok_dic = {}
    for key, val in dic_name.items():
        ok_dic[name_clean(key)] = val  # 这里引用了上面的对单个字符串进行清洗的函数
    # ok_dic = sorted(ok_dic.items(), key=lambda d: d[1], reverse=True)#返回函数值之前对字典进行基于键值的排序
    return ok_dic


'''清洗后放入此函数，进行排序并按照按行格式输出，返回值为字符串类型'''


def dic_to_str(dic):  # 形参为字典类型
    error_word = ['[', ']', '(', ')', '\'', ' ']

    lis = sorted(dic.items(), key=lambda d: d[1], reverse=True)  # 返回函数值之前对字典进行基于键值的排序
    str_lis = str(lis)
    str_lis = str_lis.replace(')]', '分')
    for num in range(1, len(lis) + 1):
        str_lis = str_lis.replace('),', f'分\n第{num}名：', 1)

    str_lis = str_lis.replace(', 99999分', '')

    for word in error_word:
        str_lis = str_lis.replace(word, '')
    str_lis = str_lis.replace(',', '~~')
    return str_lis


'''表扬用语列表'''
reply_list = ['\n你发了{}个科目的练字和作业图片，写字好，才够优秀！',
              '\n你进行了{}次视频展示，你是最棒的！继续努力！',
              '\nThis is the {} voice you uploaded today, you are the best！',
              '\n你的{}{}{}，{}',
              '\n您的点评很到位，孩子们因您更精彩！',
              '\n你的{}坚持的很好,持之以恒的精神最可贵！',
              '\n文明其精神，野蛮其体魄.坚持{}的同学身体最健康！']

'''构造自动回复内容的框架函数'''


def send_content(name, type_reply, id_of_room):  # 函数参数用的时候调用最上面的表扬用语列表
    time_now = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    top_words = f'{time_now}\n—————————————\n'
    end_words = '\n—————————————\n机器人助理为您服务。'

    itchat.send(f'{top_words}{name}:{type_reply}{end_words}', toUserName=id_of_room)


"""0506"""


def get_chinese(text):  # 从字符串取出中文
    """"取出字符串中的中文"""
    word = re.sub(r'[A-Za-z0-9]|\(|\)|\’|\-|\?|\？|\（|\）', '', text)
    word = word.strip()
    return word


"""0506"""


def get_english(text):  # 从字符串取出英语单词
    word = re.findall(r'[^(\u4E00-\u9FA5)\（\）\,\，\.\、\；\？\?\……]', text)
    word = ''.join(word)
    word = word.strip()
    return word


"""0506"""


def get_room_member_dic():  # 获取当前群内所有成员的昵称、ID字典
    chat_room = itchat.search_chatrooms(name='龙源双语五年级六班')[0]
    name_uuid = chat_room.get('UserName')
    chat_room = itchat.update_chatroom(name_uuid, detailedMember=True)
    group_members = {}
    for member in chat_room['MemberList']:
        group_members_dic_value = member['UserName']
        group_members_dic_key = member['DisplayName']
        group_members[group_members_dic_key] = group_members_dic_value

    return group_members


"""0506"""


def word_to_group_mini(to_id, path='words_result.txt'):  # 将单词和对应翻译发给指定ID的微信好友（或群）
        word_list = []
        with open(path) as f:
            for i in f.readlines():
                word_list.append(i)

        n = 10
        lis3 = [word_list[j:j + n] for j in range(0, len(word_list), n)]

        for m in lis3:
            str_eng = ''
            for n in m:
                str_eng += get_english(n) + ', '
            str_eng = str_eng[:-2]
            # print(str_eng)
            time.sleep(random.random())
            itchat.send(str_eng, to_id)
            time.sleep(random.randint(20, 25))

            str_chi = ''
            for p in m:
                str_chi += get_chinese(p) + ', '
            str_chi = str_chi[:-2]
            # print(str_chi)
            time.sleep(random.random())
            itchat.send(str_chi, to_id)
            time.sleep(random.randint(10, 15))


'''主体代码块'''


@itchat.msg_register([PICTURE, TEXT, VIDEO, RECORDING], isGroupChat=True)
def text_reply(msg):

    if msg.User['NickName'] == room_name_list[0]:
        # print(msg['ActualNickName'] + '在群里说道：')

        msg_name = name_clean(msg['ActualNickName'])  # 将当前发言者放入昵称清洗函数
        msg_name = msg_name + '同学'

        '''下面是针对特定老师和发言的同学的特定回复'''
        if msg['ActualNickName'] == '刘老师':
            pass
            # send_content(msg_name, reply_list[4], room_id)
        elif '语文' in msg['ActualNickName']:
            pass
            # send_content(msg_name, reply_list[4], room_id)
        elif msg['ActualNickName'] == '数学老师':
            pass
            # send_content(msg_name, reply_list[4], room_id)
        # elif msg['ActualNickName'] == '张博华':
        elif msg['ActualNickName'] == '班主任~张博华':

            if '统计' in msg['Content']:
                # time.sleep(random.random())
                itchat.send(dic_to_str(dic_clean(dic_recording)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_recording)), toUserName=to_room_id(9))

                itchat.send(dic_to_str(dic_clean(dic_picture)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_picture)), toUserName=to_room_id(3))

                itchat.send(dic_to_str(dic_clean(dic_think)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_think)), toUserName=to_room_id(5))

                itchat.send(dic_to_str(dic_clean(dic_eng_text)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_eng_text)), toUserName=to_room_id(7))

                itchat.send(dic_to_str(dic_clean(dic_read)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_read)), toUserName=to_room_id(8))

                itchat.send(dic_to_str(dic_clean(dic_chi_text)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_chi_text)), toUserName=to_room_id(6))

                itchat.send(dic_to_str(dic_clean(dic_eng_video)), toUserName=to_room_id(11))
                itchat.send(dic_to_str(dic_clean(dic_eng_video)), toUserName=to_room_id(4))

                itchat.send(dic_to_str(dic_clean(dic_eng_exercise)), toUserName=to_room_id(11))
                '''还没创建聊天群'''
                # itchat.send(dic_to_str(dic_clean(dic_eng_exercise)), toUserName=to_room_id(10))

            else:
                pass

        elif msg['Type'] == 'Picture':
            time.sleep(random.random())
            print('一张图片。')
            time.sleep(random.random())

            msg['Text'](msg['FileName'])
            send_object = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
            itchat.send(name_clean(msg['ActualNickName']) + '同学的练字图片：', toUserName=to_room_id(3))  # 这里清洗了昵称
            itchat.send(send_object, toUserName=to_room_id(3))

            time.sleep(random.random())
            time.sleep(random.random())

            if msg['ActualNickName'] not in dic_picture:
                dic_picture[msg['ActualNickName']] = 0
            dic_picture[msg['ActualNickName']] += 10

            send_content(msg_name, reply_list[0].format(int(dic_picture[msg['ActualNickName']] / 10)), room_id)

        elif msg['Type'] == 'Video':
            time.sleep(random.random())
            time.sleep(random.random())

            print('一个视频。')

            msg['Text'](msg['FileName'])
            send_object = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
            itchat.send(name_clean(msg['ActualNickName']) + '同学的英语视频：', toUserName=to_room_id(4))
            itchat.send(send_object, toUserName=to_room_id(4))
            time.sleep(random.random())
            time.sleep(random.random())

            if msg['ActualNickName'] not in dic_eng_video:
                dic_eng_video[msg['ActualNickName']] = 0
            dic_eng_video[msg['ActualNickName']] += 20

            send_content(msg_name, reply_list[1].format(int(dic_eng_video[msg['ActualNickName']] / 20)), room_id)

        elif msg['Type'] == 'Recording':
            time.sleep(random.random())
            time.sleep(random.random())

            print('一段语音。')

            if msg['ActualNickName'] not in dic_recording:
                dic_recording[msg['ActualNickName']] = 0
            dic_recording[msg['ActualNickName']] += 1

            time.sleep(random.random())
            time.sleep(random.random())


            send_content(msg_name, reply_list[2].format(num_to_eng(dic_recording[msg['ActualNickName']])), room_id)

        elif msg['Type'] == 'Text':
            time.sleep(random.random())
            time.sleep(random.random())

            print(msg['Content'])

            if '英语学习机器人' in msg['Content']:
                time.sleep(random.random())
                time.sleep(random.random())

                t = threading.Thread(target=word_to_group_mini,
                                     args=(get_room_member_dic().get(msg['ActualNickName']),))
                t.start()

            elif get_word_nums(msg['Content'])[0] == '英语说作文共计':
                time.sleep(random.random())
                time.sleep(random.random())

                itchat.send('这是' + name_clean(msg['ActualNickName']) + '同学的英语说作文：\n' + msg['Content'], toUserName=to_room_id(7))

                if msg['ActualNickName'] not in dic_eng_text:
                    dic_eng_text[msg['ActualNickName']] = 0
                dic_eng_text[msg['ActualNickName']] += round(int(get_word_nums(msg['Content'])[1]) // 10)

            elif get_word_nums(msg['Content'])[0] == '每日反思共计':
                time.sleep(random.random())
                time.sleep(random.random())

                itchat.send('这是' + name_clean(msg['ActualNickName']) + '同学的反思：\n' + msg['Content'], toUserName=to_room_id(5))

                if msg['ActualNickName'] not in dic_think:
                    dic_think[msg['ActualNickName']] = 0
                dic_think[msg['ActualNickName']] += round(int(get_word_nums(msg['Content'])[1]) // 10)

            elif get_word_nums(msg['Content'])[0] == '每日读书共计':
                time.sleep(random.random())
                time.sleep(random.random())

                itchat.send('这是' + name_clean(msg['ActualNickName']) + '同学的每日读书：\n' + msg['Content'], toUserName=to_room_id(8))

                if msg['ActualNickName'] not in dic_read:
                    dic_read[msg['ActualNickName']] = 0
                dic_read[msg['ActualNickName']] += round(int(get_word_nums(msg['Content'])[1]) // 6)

            elif get_word_nums(msg['Content'])[0] == '语文说作文共计':
                time.sleep(random.random())
                time.sleep(random.random())

                itchat.send('这是' + name_clean(msg['ActualNickName']) + '同学的语文说作文：\n' + msg['Content'], toUserName=to_room_id(6))

                if msg['ActualNickName'] not in dic_chi_text:
                    dic_chi_text[msg['ActualNickName']] = 0
                dic_chi_text[msg['ActualNickName']] += round(int(get_word_nums(msg['Content'])[1]) // 50)

            elif get_word_nums(msg['Content'])[0] == '英语一起作业':
                time.sleep(random.random())
                time.sleep(random.random())

                '''还没创建聊天群'''
                # itchat.send('这是' + msg['ActualNickName'] + '同学的英语一起作业：\n' + msg['Content'], toUserName=to_room_id(10))
                if msg['ActualNickName'] not in dic_eng_exercise:
                    dic_eng_exercise[msg['ActualNickName']] = 0
                dic_eng_exercise[msg['ActualNickName']] += 20

            elif get_word_nums(msg['Content'])[0] == '体育锻炼':
                time.sleep(random.random())
                time.sleep(random.random())

                if msg['ActualNickName'] not in dic_sport:
                    dic_sport[msg['ActualNickName']] = 0
                dic_sport[msg['ActualNickName']] += 20

            if get_word_nums(msg['Content'])[0] != '未知信息':
                # pass
                time.sleep(random.random())
                time.sleep(random.random())

                send_content(msg_name, reply_list[3].format(get_word_nums(msg['Content'])[0],
                                                            get_word_nums(msg['Content'])[1],
                                                            get_word_nums(msg['Content'])[2],
                                                            get_word_nums(msg['Content'])[3]), room_id)


itchat.run()
