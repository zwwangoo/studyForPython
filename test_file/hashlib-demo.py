import hashlib


def str2sha256(value):
    return hashlib.sha256(value).hexdigest()

if __name__ == "__main__":
    print(str2sha256('1234'.encode()))
