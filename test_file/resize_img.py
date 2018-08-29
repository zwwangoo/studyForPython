import time
import string
import random
from PIL import Image


def get_random_string(index):
    return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(index))


def get_random_file_name(suffix):
    mills = str(round(time.time() * 1000))
    filename = '{}{}'.format(get_random_string(6), '{}.{}'.format(mills, suffix))
    return filename


def resize_img(path, dist_w, dist_h):
    origin = Image.open(path)
    ori_w, ori_h = origin.size
    width_ratio = height_ratio = None
    ratio = 1
    if (ori_w and ori_w > dist_w) or (ori_h and ori_h > dist_h):
        if dist_w and ori_w > dist_w:
            width_ratio = float(dist_w / ori_w)
        if dist_h and ori_h > dist_h:
            height_ratio = float(dist_h / ori_h)
        if width_ratio and height_ratio:
            if width_ratio < height_ratio:
                ratio = width_ratio
            else:
                ratio = height_ratio
        new_w = int(ori_w * ratio)
        new_h = int(ori_h * ratio)
    else:
        new_h = ori_h
        new_w = ori_w
    new_path = get_random_file_name('png')
    origin.resize((new_w, new_h), Image.ANTIALIAS).save(new_path, quality=75)
    return new_path


resize_img('./darkness-622932-unsplash.jpg', 700, 700)
