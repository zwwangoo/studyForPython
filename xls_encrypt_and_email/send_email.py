import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def create_email(
    email_from, email_to, email_subject, email_text,
    annex_path=None, annex_name=None,
):
    """
    :param @email_from 输入发件人昵称
    :param @email_to 收件人昵称
    :param @email_subject 邮件主题
    :param @email_text 正文
    :param @email_path 附件地址
    :param @email_name 附件名称
    :retuen 邮件信息
    """
    message = MIMEMultipart()
    message.attach(MIMEText(email_text, 'plain', 'utf-8'))

    message['From'] = email_from
    message['To'] = email_to
    message['Subject'] = Header(email_subject, 'utf-8')  # subject

    for path in annex_path:
        att1 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1.add_header(
            'Content-Disposition', 'attachment',
            filename=Header(path.split('/')[-1], 'utf-8').encode(),
        )
        message.attach(att1)
    return message


def send_email(sender, password, receiver, msg):
    """
    :param @sender 发件人邮箱, 这里使用163邮箱
    :param @password 发件人邮箱密码
    :param @receiver 收件人邮箱 收件人邮箱账号（是一个列表）
    :param @msg 邮件内容
    """
    try:
        server = smtplib.SMTP_SSL("smtp.163.com", 465)  # 发件人邮箱中的SMTP服务器
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功")
        server.quit()  # 关闭连接
    except Exception as e:
        print(e)
        print("邮件发送失败")
