# coding: utf-8
from qqweibo import APIClient
qq = APIClient("801058005", "31cc09205420a004f3575467387145a7", redirect_uri="callback_uri")
qq.set_access_token("83d36ac2caa900ab53374903183cba06", "5FD49B7E7A810115834085C835A0B42E", "1593764748")
#print qq.post.t__add(content="test", clientip="202.22.251.18")
print qq.post.t__add_pic_url(content="test", clientip="real ip", pic_url="/home/pi/img/capture.jpg")
