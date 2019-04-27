import datetime
from encrypt_xls import encrypt
from get_data_to_xls import make_xls
from send_email import create_email, send_email


def main():
    files = make_xls()
    encrypt(files, '123654')

    email_from = ''  # 发件人邮箱
    email_password = ''  # 发件人邮箱密码
    email_to = ['w_angzhiwen@163.com', '']  # 收件人邮箱，可以是多个
    msg = create_email(
        email_from, email_to,
        datetime.date.today().strftime('%Y%m%d') + '日报',
        '每日维修和安装商户工单完成情况报表',
        files,
    )
    send_email(email_from, email_password, email_to, msg)


if __name__ == '__main__':
    main()
