import qrcode


def gen_qrcode_img(string):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=5, border=1)
    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image()
    img = img.convert("RGBA")
    img.save('qrcode.png')


gen_qrcode_img('http://baidu.com')

