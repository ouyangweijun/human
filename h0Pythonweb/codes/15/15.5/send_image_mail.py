# coding: utf-8
#########################################################################
# 网站: <a href="http://www.crazyit.org">疯狂Java联盟</a>               #
# author yeeku.H.lee kongyeeku@163.com                                  #
#                                                                       #
# version 1.0                                                           #
#                                                                       #
# Copyright (C), 2001-2018, yeeku.H.Lee                                 #
#                                                                       #
# This program is protected by copyright laws.                          #
#                                                                       #
# Program Name:                                                         #
#                                                                       #
# <br>Date:                                                             #
#########################################################################
import smtplib, email.utils
from email.message import EmailMessage

# 定义SMTP服务器地址:
smtp_server = 'smtp.qq.com'
# 定义发件人地址
from_addr = 'kongyeeku@qq.com'
# 定义登录邮箱的密码
password = '123456'
# 定义收件人地址:
to_addr = 'kongyeeku@163.com'

# 创建SMTP连接
#conn = smtplib.SMTP(smtp_server, 25)
conn = smtplib.SMTP_SSL(smtp_server,465)
conn.set_debuglevel(1)
conn.login(from_addr, password)            #①
# 创建邮件对象
msg = EmailMessage()
# 随机生成两个图片id
first_id, second_id = email.utils.make_msgid(), email.utils.make_msgid()
# 设置邮件内容，指定邮件内容为HTML
msg.set_content('<h2>邮件内容</h2>' +
    '<p>您好，这是一封来自Python的邮件' +
    '<img src="cid:' + second_id[1:-1] +'"><p>' +
    '来自<a href="http://www.crazyit.org">疯狂联盟</a>' +
    '<img src="cid:' + first_id[1:-1] +'">', 'html', 'utf-8')
msg['subject'] = '一封HTML邮件'
msg['from'] = '李刚 <%s>' % from_addr
msg['to'] = '新用户 <%s>' % to_addr
with open('E:/logo.jpg', 'rb') as f:
    # 添加第一个附件
    msg.add_attachment(f.read(), maintype='image',
        subtype='jpeg', filename='test.png', cid=first_id)
with open('E:/fklogo.gif', 'rb') as f:
    # 添加第二个附件
    msg.add_attachment(f.read(), maintype='image',
        subtype='gif', filename='test.gif', cid=second_id)
with open('E:/fkit.pdf', 'rb') as f:
    # 添加第三个附件，邮件正文不需引用该附件，因此不指定cid
    msg.add_attachment(f.read(), maintype='application',
        subtype='pdf', filename='test.pdf',)
# 发送邮件
conn.sendmail(from_addr, [to_addr], msg.as_string())
# 退出连接
conn.quit()