# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
# import re
import traceback
import csv


def getHtmlText(url):
    try:
        hd = {'user-agent': 'Chrome/10'}
        r = requests.get(url, timeout=30, headers=hd)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as err:
        print(err)
        return ""


def getJobDeatileList(jobList, html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        newlist_deatil_newlist = soup.find_all('div', attrs={'class':'newlist_detail newlist'})
        length = len(newlist_deatil_newlist)
        for index, newlist_deatil in enumerate(newlist_deatil_newlist):
            job_deatil = {}

            job_deatil["index"] = newlist_deatil.find("input").attrs['value'].split("_")[0][:-3]

            newlist_deatil_one = newlist_deatil.find('ul').find_all('a')
            job_deatil["title"] = newlist_deatil_one[0].get_text()
            job_deatil["href"] = newlist_deatil_one[0].attrs['href']
            job_deatil["company"] = newlist_deatil_one[1].string

            newlist_deatil_two = newlist_deatil.find(attrs={"class":"newlist_deatil_two"}).find_all("span")
            job_deatil["city"] = newlist_deatil_two[0].string
            job_deatil["salary"] = newlist_deatil_two[-1].string
            job_deatil["content"] = newlist_deatil.find(attrs={"class":"newlist_deatil_last"}).get_text()

            jobList.append(job_deatil)

            print("\r{:.2f}".format(float(index/length)), end="")  # 打印进度条
    except:
        traceback.print_exc()


def saveJobDataToFile(jobList):
    with open("./job.csv", "a") as cvsfile:
        writer = csv.writer(cvsfile)
        writer.writerow(["索引", "职位", "公司", "薪酬", "城市", "链接", "职位要求"])
        for job in jobList:
            job_deatil = [job["index"], job["title"], job["company"], job["salary"], job["city"], job["href"], job["content"]]
            writer.writerow(job_deatil)


def main():
    jobList = []
    base = "http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&sj=044%3B045%3B079&in=160400%3B160000&jl=%E6%9D%AD%E5%B7%9E&kw=python&sm=1"
    url = base + "&p=1"
    html = getHtmlText(url)
    getJobDeatileList(jobList, html)
    saveJobDataToFile(jobList)

    print("")


if __name__ == '__main__':
    main()
