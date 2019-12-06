# encoding=utf-8
import smtplib

from email.mime.text import MIMEText
from email.utils import formataddr

SMTP_SERVER = {
    '163.com': ('smtp.163.com', 465),
    'qq.com': ('smtp.qq.com', 465),
    'ilabservice.com': ('smtp.qiye.aliyun.com', 465)
}


def send(sender, sender_passwd, sender_name,
         receivers,
         content, subject, content_type='plain'):

    msg = MIMEText(content, content_type, 'utf-8')
    msg['From'] = formataddr([sender_name, sender])
    msg['To'] = ','.join(receivers) if isinstance(receivers, list) \
        else receivers
    msg['Subject'] = subject
    smtp_host, smtp_port = SMTP_SERVER.get(sender.split('@')[-1])
    server = smtplib.SMTP_SSL(smtp_host, smtp_port)
    try:
        server.login(sender, sender_passwd)
        server.sendmail(sender, receivers, msg.as_string())
        server.quit()
        print('ok.')
    except Exception as e:
        print('error!', e)


send(sender='zw.wang@ilabservice.com',
     sender_passwd='',
     sender_name='混蛋',
     receivers=['w_angzhiwen@163.com', '1205352402@qq.com'],
     content='<p>你好<a href="https://www.baidu.com">百度</a></p>',
     content_type='html',
     subject='这是测试邮件'
     )
