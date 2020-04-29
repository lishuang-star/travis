import requests
import os
import time

cookies = {"PHPSESSID": "0acab05af285106e154184a65c8ae0a6"}


def configyouphptube():
    burp0_url = "http://web:8000/install/checkConfiguration.php"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "Origin": "http://web:8000/", "Connection": "close",
                     "Referer": "http://web:8000/install/index.php"}
    burp0_data = {"webSiteRootURL": "http://web:8000/", "systemRootPath": "/var/www/html/",
                  "webSiteTitle": "YouPHPTube", "databaseHost": "mysql", "databasePort": "3306", "databaseUser": "root",
                  "databasePass": "password", "databaseName": "youPHPTube", "mainLanguage": "en",
                  "systemAdminPass": "cuccs123", "contactEmail": "894597649@qq.com", "createTables": "2"}
    res = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)


def configencoder():
    burp0_url = "http://web:8000/login"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "Origin": "http://encoder:8000", "Connection": "close",
                     "Referer": "http://encoder:8000/install/index.php"}
    burp0_data = {"user": "admin", "pass": "cuccs123", "siteURL": "http://web:8000/"}
    requests.post(burp0_url, headers=burp0_headers, data=burp0_data)

    burp0_url = "http://encoder:8000/install/checkConfiguration.php"
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "Origin": "http://encoder:8000",
                     "Connection": "close", "Referer": "http://encoder:8000/install/index.php"}
    burp0_data = {"webSiteRootURL": "http://encoder:8000/", "systemRootPath": "/var/www/html/",
                  "databaseHost": "mysql", "databaseUser": "root", "databasePass": "password",
                  "databaseName": "youPHPTube-Encoder", "createTables": "2", "siteURL": "http://web:8000/",
                  "inputUser": "admin", "inputPassword": "cuccs123", "allowedStreamers": "http://web:8000/",
                  "defaultPriority": "1"}
    res = requests.post(burp0_url, headers=burp0_headers, cookies=cookies, data=burp0_data)


def login(hostip):
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "Origin": "http://encoder:8000",
                     "Connection": "close", "Referer": "http://encoder:8000/"}
    burp0_data = {"user": "admin", "pass": "cuccs123", "siteURL": "http://web:8000/", "encodedPass": "false"}
    res = requests.post(hostip, headers=burp0_headers, cookies=cookies, data=burp0_data)


def queue(hostip):
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
                     "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate",
                     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                     "X-Requested-With": "XMLHttpRequest", "Origin": "http://encoder:8000/",
                     "Connection": "close", "Referer": "http://encoder:8000/"}
    data = {"current": "1", "rowCount": "10", "sort[created]": "desc", "searchPhrase": ''}
    res = requests.post(hostip, headers=burp0_headers, cookies=cookies, data=data)



def upload(filePath, filename):
    url = 'http://encoder:8000/upload'
    files = {'upl': open(filePath + '/' + filename, 'rb')}
    res = requests.post(url, cookies=cookies, files=files)



if __name__ == '__main__':
    a = 'http://encoder:8000/login'
    aa = 'http://encoder:8000/queue.json'
    Path = '/video'

    time.sleep(60)

    configyouphptube()
    time.sleep(5)

    configencoder()
    time.sleep(5)

    login(a)
    queue(aa)
    time.sleep(5)

    r = os.listdir(Path)
    for index in range(len(r)):
        upload(Path, r[index])
    
    login(a)
    queue(aa)
    time.sleep(60)
    print('Config success!')

