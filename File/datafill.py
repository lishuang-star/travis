import requests
import os

def login(host):
    burp0_data = {"user": "admin", "pass": "cuccs123", "siteURL": "http://192.168.1.3:8888/", "encodedPass": "false"}
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
    url = 'http://192.168.1.3:8889/upload'
    files = {'upl': open(filePath + '/' + filename, 'rb')}
    res = requests.post(url, files=files)
    print(res)


if __name__ == '__main__':
    a = 'http://192.168.1.3:8889/login'
    aa = 'http://192.168.1.3:8889/queue.json'
    aaa = "http://192.168.1.3:8888/login"
    Path = './vedio'

    login(a)
    queue(aa)
    admin(aaa)
    r = os.listdir(Path)
    for index in range(len(r)):
        upload(Path, r[index])
    print('Config success!')
    
