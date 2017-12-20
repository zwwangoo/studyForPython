# -*- coding: utf-8 -*-
from Crypto.Cipher import AES

class CryptoTools():
    """ 加密解密类 """
    def __init__(self, key):
        self.key = key
        # 设置加解密模式为AES的CBC模式
        self.mode = AES.MODE_CBC
        self.padding = "\0"

    def encrypto(self, text):
        """ 对明文加密 """
        cryptor = AES.new(self.key, self.mode, self.key[:16])
        length = 16
        count = text.count("")
        if count < length:
            add = (length - count) + 1
            text += (self.pdding * add)
        elif count > length:
            add = (length - (count % length)) + 1
            text += (self.padding * add)
        self.ciphertext = cryptor.encrypt(text)
        return self.ciphertext

    def decrypt(self, text):
        """ 解密 """
        cryptor = AES.new(self.key, self.mode, self.key[:16])
        plain_text = cryptor.decrypt(text)
        return plain_text.rstrip("\0")





if __name__ == "__main__":
    key = '0123456789abcdef'
    data = "{'a':'123中文', sss}"
    ec = CryptoTools(key)
    encrypt_data = ec.encrypto(data)
    decrypt_data = ec.decrypt(encrypt_data)
    print encrypt_data, decrypt_data, decrypt_data == data

    from base64 import b64decode, b64encode
    print b64encode(encrypt_data)
