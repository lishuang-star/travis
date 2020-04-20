import requests
import os

def configyouphptube():
    burp0_url = "http://web/install/checkConfiguration.php"
    burp0_data = {"webSiteRootURL": "http://web", "systemRootPath": "/var/www/html/", "webSiteTitle": "YouPHPTube", "databaseHost": "mysql", "databasePort": "3306", "databaseUser": "root", "databasePass": "password", "databaseName": "youPHPTube", "mainLanguage": "en", "systemAdminPass": "cuccs123", "contactEmail": "894597649@qq.com", "createTables": "2"}
    requests.post(burp0_url, data=burp0_data)

def configencoder():
    burp0_url = "http://web/login"
    burp0_data = {"user": "admin", "pass": "cuccs123", "siteURL": "http://web"}
    requests.post(burp0_url,data=burp0_data)

    burp0_url = "http://encoder:8889/install/checkConfiguration.php"
    burp0_cookies = {"PHPSESSID": "aa899c83e57d809e8cf33bd2af173277"}
    burp0_data = {"webSiteRootURL": "http://encoder:8889/", "systemRootPath": "/var/www/html/", "databaseHost": "mysql", "databaseUser": "root", "databasePass": "password", "databaseName": "youPHPTube-Encoder", "createTables": "2", "siteURL": "http://web", "inputUser": "admin", "inputPassword": "cuccs123", "allowedStreamers": "http://web", "defaultPriority": "1"}
    requests.post(burp0_url, cookies=burp0_cookies, data=burp0_data)

    
def login(host):
    burp0_data = {"user": "admin", "pass": "cuccs123", "siteURL": "http://web", "encodedPass": "false"}
    burp0_cookies = {"_ga": "GA1.1.500274602.1586273581", "PHPSESSID": "5ef3964b63d26a2097b462daafdbd034",
                     "_gid": "GA1.1.1691531968.1586788006"}
    res = requests.post(host, cookies=burp0_cookies,data=burp0_data)
    print(res)

def queue(host):
    burp0_cookies = {"_ga": "GA1.1.500274602.1586273581", "PHPSESSID": "5ef3964b63d26a2097b462daafdbd034",
                     "_gid": "GA1.1.1691531968.1586788006"}
    data = {"current": "1", "rowCount": "10", "sort[created]": "desc", "searchPhrase": ''}
    res = requests.post(host, cookies=burp0_cookies, data=data)
    print(res)

def admin(host):
    burp0_cookies = {"_ga": "GA1.1.500274602.1586273581", "PHPSESSID": "5ef3964b63d26a2097b462daafdbd034", "_gid": "GA1.1.1691531968.1586788006", "_gat_youPHPTube": "1"}
    burp0_data = {"user": "admin", "pass": "cuccs123"}
    requests.post(host, cookies=burp0_cookies, data=burp0_data)

def upload(filePath,filename):
    url = 'http://encoder:8889/upload'
    files = {'upl': open(filePath + '/' + filename, 'rb')}
    res = requests.post(url, files=files)
    print(res)


if __name__ == '__main__':
    a = 'http://encoder:8889/login'
    aa = 'http://encoder:8889/queue.json'
    aaa = 'http://web/login'
    Path = './vedio'
     
    configyouphptube()
    configencoder()
    login(a)
    queue(aa)
    admin(aaa)
    r = os.listdir(Path)
    for index in range(len(r)):
        upload(Path, r[index])
    print('Config success!')
    
