# coding=utf-8
import itchat
import time


def after():
    user_info = itchat.search_friends(name='王金涛')
    if len(user_info) > 0:
        # 拿到用户名
        user_name = user_info[0]['UserName']
        # 发送文字信息
        itchat.send_msg('王书记你好啊！', user_name)
        # 发送图片
        time.sleep(1)
        itchat.send_image('math.png', user_name)
        # 发送文件
        time.sleep(1)
        itchat.send_file('pdf.py', user_name)
        # 发送视频
        time.sleep(1)
        itchat.send_video('wuhan.mp4', user_name)


itchat.auto_login(loginCallback=after)
itchat.run()

