import requests
import time
 
web = "web"

time.sleep(30)

burp0_url = "http://" +web+ "/install.php?m=Home&c=Index&a=step1"
burp0_cookies = {"_ga": "GA1.1.115988577.1589305154", "think_template": "default", "think_language": "zh-CN", "PHPSESSID": "4t8jvhepr7dk3oeoedbfm2q5n6"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/web+p,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://" +web+ "/install.php", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

burp0_url = "http://" +web+ "/install.php?m=Home&c=Index&a=step2"
burp0_cookies = {"_ga": "GA1.1.115988577.1589305154", "think_template": "default", "think_language": "zh-CN", "PHPSESSID": "4t8jvhepr7dk3oeoedbfm2q5n6"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; aWin64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/web+p,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://" +web+ "/install.php?m=Home&c=Index&a=step1", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)


burp0_url = "http://" +web+ "/install.php?m=Home&c=index&a=detection_db"
burp0_cookies = {"_ga": "GA1.1.115988577.1589305154", "think_template": "default", "think_language": "zh-CN", "PHPSESSID": "4t8jvhepr7dk3oeoedbfm2q5n6"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "http://" +web+ "", "Connection": "close", "Referer": "http://" +web+ "/install.php?m=Home&c=Index&a=step2"}
burp0_data = {"dbhost": "127.0.0.1", "dbuser": "root", "dbpass": "root", "dbname": "mysql", "pre": "qs_", "dbport": "3306", "dbport": "\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82", "default_district": "35", "admin_name": "admin", "admin_pwd": "admin123", "admin_pwd1": "admin123", "admin_email": "admin@qq.com", "detection": "0"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

burp0_url = "http://" +web+ "/install.php?m=Home&c=Index&a=step3"
burp0_cookies = {"_ga": "GA1.1.115988577.1589305154", "think_template": "default", "think_language": "zh-CN", "PHPSESSID": "4t8jvhepr7dk3oeoedbfm2q5n6"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/web+p,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://" +web+ "", "Connection": "close", "Referer": "http://" +web+ "/install.php?m=Home&c=Index&a=step2", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"dbhost": "127.0.0.1", "dbuser": "root", "dbpass": "root", "dbname": "mysql", "pre": "qs_", "dbport": "3306", "dbport": "\xe5\x8c\x97\xe4\xba\xac\xe5\xb8\x82", "default_district": "35", "admin_name": "admin", "admin_pwd": "admin123", "admin_pwd1": "admin123", "admin_email": "admin@qq.com", "detection": "0"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

burp0_url = "http://www.74cms.com/plus/getinstall.php?domaindir=http://" +web+ "/&domain=http://" +web+ "&email=admin@qq.com&v=5.0.1&t52&i=376"
burp0_cookies = {"UM_distinctid": "173004cbc9b397-075994bb66b47f8-4c302c7d-fa000-173004cbc9c445", "CNZZDATA2338778": "cnzz_eid%3D2000169776-1593436516-http%253A%252F%252F" +web+ "%252F%26ntime%3D1593569246", "__root_domain_v": ".74cms.com", "_qddaz": "QD.71tgnb.k8a4tu.kc0js5k9"}
burp0_headers = {"GET /plus/getinstall.php?domaindir=http": "/" +web+ "/&domain=http://" +web+ "&email=admin@qq.com&v=5.0.1&t52&i=376 HTTP/1.1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0", "Accept": "*/*", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://" +web+ "/install.php?m=Home&c=Index&a=step3"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

print("Config success!")