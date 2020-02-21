# coding=utf-8
import itchat
from itchat.content import *
import time

itchat.auto_login()

room_name_family = '有家有爱二'
room_id_family = itchat.search_chatrooms(name=room_name_family)[0].get('UserName')


@itchat.msg_register([TEXT, MAP, SHARING, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def text_reply(msg):
    if msg.User['NickName'] == room_name_family:

    # if msg['Content'] in li:
    #     print('in')
        print(len(msg['Content']))
    # print(msg['Content'])
    # itchat.send('[强]', toUserName=room_id_family)
    # itchat.send('😄😄😀 😁 😂 😃 😅 😆 😇 😈 😉 😊 😋 😌 😍 😎 😏😐 😑 😒 😓 😔 😕 😖 😗 😘 😙 😚 😛 😜 😝 😞 😟 😠 😡 😢 😣 😤 😥 😦 😧 😨 😩 😪 😫 😬 😭 😮 😯 😰 😱 😲 😳 😴 😵 😶 😷 😸 😹 😺 😻 😼 😽 😾 😿 🙀 🙁 🙂 🙃 🙄 🙅 🙆 🙇 🙈 🙉 🙊 🙋 🙌 🙍 🙎 🙏 😅 😆 😇 😈 😉 😊 😋 😌 😍 😎 😏😐 😑 😒 😓 😔 😕 😖 😗 😘 😙 😚 😛 😜 😝 😞 😟 😠 😡 😢 😣 😤 😥 😦 😧 😨 😩 😪 😫 😬 😭 😮 😯 😰 😱 😲 😳 😴 😵 😶 😷 😸 😹 😺 😻 😼 😽 😾 😿 🙀 🙁 🙂 🙃 🙄 🙅 🙆 🙇 🙈 🙉 🙊 🙋 🙌 🙍 🙎 🙏😀😁😂😃😄😅😆😉😊😋😎😍😘😗😙😚☺😇😐😑😶😏😣😥😮😯😪😫😴😌😛😜😝😒😓😔😕😲😷😖😞😟😤😢😭😦😧😨😬😰😱😳😵😡😠', toUserName=room_id_family)
    # print(msg['Content'])

    # if msg.User['NickName'] == room_name_family:
        # # print(msg)
        # for k, v in msg.items()://*[@id="catalog-list"]/li[2]/div[1]/div[1]/a/text()
        #     print(k, ':', v)承办县级综合性运动会统计信息
        # timer = time.strftime("%m-%d %H:%M:%S", time.localtime())
        #
        # if '<mpurl>' in msg['Content']:承办县级综合性运动会统计信息<a class="album-title line-1 lg bold _Ht" title="有书·热文快报" href="/toutiao/15159281/"><span class="v-m _Ht">有书·热文快报</span></a>
        #     print('a video link......')
        #     url = msg['Content'].split('<mpurl>')[1].split('</mpurl')[0]
        #     itchat.send("%s%s:\n%s\n%s" % (msg['ActualNickName'] + '在' + timer + '分享的链接,', msg['Type'], msg['FileName'], url), toUserName=room_id_family)
#<a class="album-title line-1 lg bold _Ht" title="有书·热文快报" href="/toutiao/15159281/"><span class="v-m _Ht">有书·热文快报</span></a>

itchat.run()