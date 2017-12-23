# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import time
import csv


def getHtmlText(url):
    try:
        r = requests.get(url, headers={'user-agent': 'Chrome/10'})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getJobUrlList(urlList, html):
    urlList += re.compile(r'http://jobs.zhaopin.com/\w+?\.htm').findall(html)
    print("成功获取当前页面中职位链接。")


def getJobDeatileList(jobList, html):
    time.sleep(1)  # 这里暂停一秒
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("div", attrs={"class": "inner-left fl"})
    name = title.find("h1").string.strip()
    company = title.find("h2").get_text().strip()

    job_deatil_html = soup.find("div", attrs={"class": "terminalpage-left"})
    job_li = job_deatil_html.find("ul").find_all("li")

    salary = job_li[0].find("strong").get_text().strip()
    city =  job_li[1].find("strong").get_text().strip()
    date =  job_li[2].find("strong").get_text().strip()

    job_cont = soup.find("div", attrs={"class": "tab-inner-cont"})  # class="tab-inner-cont"的在界面中多次出现，但是第一次出现的却一直是需要的数据。
    deatil = job_cont.get_text().strip().replace("\n", "")
    job =  [name, company, salary, city, date, deatil]
    jobList.append(job)
    return ""


def saveJobDataToFile(jobList):
    path = "../data/"
    filename = path + "job0.9-1.csv"
    with open(filename, "w") as cvsfile:
        writer = csv.writer(cvsfile)
        writer.writerow([ "职位", "公司", "薪酬", "城市", "发布日期", "职位要求"])
        for job in jobList:
            writer.writerow(job)
    return ""


def isExistsInData(job):
    return ""


def main():
    base = "http://sou.zhaopin.com/jobs/searchresult.ashx?"

    urlList = []
    jobList = []

    # 参数设置
    page = 1
    city = "杭州"
    keyword = "python"

    url = base + "&jl=" + city + "&kw=" + keyword + "&p=1"
    urllist_html = getHtmlText(url)
    getJobUrlList(urlList, urllist_html)

    length = len(urlList)
    for index, job_url in enumerate(urlList):
        html = getHtmlText(job_url)
        getJobDeatileList(jobList, html)
        print("\r--------------{:.0f}%---------------------".format(float(index/length) * 100), end="")  # 打印进度条
    print("\r-----------------获取数据完成，数据存储中----------------", end="")
    saveJobDataToFile(jobList)
    print("\r-------------------存储完成----------------------", end="")

    print("")


if __name__ == '__main__':
    main()
