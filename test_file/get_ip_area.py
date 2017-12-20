#-*- coding:utf-8 -*-
import json
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def get_ip_area(ip):
    """
    使用新浪云接口，查询用户登录的ip地址所在区域
    :param ip: 
    :return:  用户ip的国家省份地区
    """
    get_url = "http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=Json&ip=" + ip
    ip_area = ""
    try:
        requst = urllib2.urlopen(get_url)
        response = json.loads(requst.read())
        if response.has_key("country"):
            country = response["country"]
            province = response["province"]
            city = response["city"]
            ip_area = country + province + city
    except:
        logging.info("-----------------获取ip异常------------------------")
    finally:
        print ip_area
        return ip_area

if __name__ == "__main__":
    get_ip_area("153.125.232.243")