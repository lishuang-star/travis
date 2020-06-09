import requests
import time

web = "192.168.56.102" 

time.sleep(40)
 
# install
burp0_url = "http://"+web+"/install/index.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://"+web+"/install/not_installed.php", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
time.sleep(5)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/index.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"new_version": "2.2.2", "next": "  Install  "}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"action": "process", "step": "1", "new_version": "2.2.2", "submit": "I Agree"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)


burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"action": "process", "step": "2", "new_version": "2.2.2", "db_host": "mysql", "db_port": "3306", "db_login": "root", "db_password": "rootpwd", "db_name": "atutor", "tb_prefix": "AT_", "submit": "Next \xc2\xbb "}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"step": "3", "step2[new_version]": "2.2.2", "step2[db_host]": "mysql", "step2[db_port]": "3306", "step2[db_login]": "root", "step2[db_password]": "rootpwd", "step2[db_name]": "atutor", "step2[tb_prefix]": "AT_", "submit": "Next \xc2\xbb "}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"action": "process", "form_admin_password_hidden": "07bb1830e46cd22ff5c19e14b6c2acef77e47b40", "form_account_password_hidden": "7c4a8d09ca3762af61e59520943dc26494f8941b", "step": "3", "step2[new_version]": "2.2.2", "step2[db_host]": "mysql", "step2[db_port]": "3306", "step2[db_login]": "root", "step2[db_password]": "rootpwd", "step2[db_name]": "atutor", "step2[tb_prefix]": "AT_", "smtp": "false", "admin_username": "admin", "admin_password": '', "admin_email": "894597649@qq.com", "site_name": "Course Server", "email": "2237744542@qq.com", "just_social": "0", "home_url": '', "account_username": "liming", "account_password": '', "account_email": "894597649@qq.com", "account_fname": "Li", "account_lname": "ming", "submit": " Next \xc2\xbb"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"step": "4", "copy_from": '', "get_file": "TRUE", "step2[new_version]": "2.2.2", "step2[db_host]": "mysql", "step2[db_port]": "3306", "step2[db_login]": "root", "step2[db_password]": "rootpwd", "step2[db_name]": "atutor", "step2[tb_prefix]": "AT_", "step3[smtp]": "false", "step3[admin_password]": '', "step3[account_password]": '', "step3[account_fname]": "Li", "step3[account_lname]": "ming", "content_dir": "/var/www/html/content", "submit": " Next \xc2\xbb"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"step": "5", "step2[new_version]": "2.2.2", "step2[db_host]": "mysql", "step2[db_port]": "3306", "step2[db_login]": "root", "step2[db_password]": "rootpwd", "step2[db_name]": "atutor", "step2[tb_prefix]": "AT_", "step3[smtp]": "false", "step3[admin_password]": '', "step3[account_password]": '', "step3[account_fname]": "Li", "step3[account_lname]": "ming", "step4[copy_from]": '', "step4[get_file]": "TRUE", "step4[content_dir]": "%2Fvar%2Fwww%2Fhtml%2Fcontent%2F", "submit": " Next \xc2\xbb "}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/install/install.php"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://"+web, "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
burp0_data = {"step": "6", "log_upgrade": "0", "step2[new_version]": "2.2.2", "step2[db_host]": "mysql", "step2[db_port]": "3306", "step2[db_login]": "root", "step2[db_password]": "rootpwd", "step2[db_name]": "atutor", "step2[tb_prefix]": "AT_", "step3[smtp]": "false", "step3[admin_password]": '', "step3[account_password]": '', "step3[account_fname]": "Li", "step3[account_lname]": "ming", "step4[copy_from]": '', "step4[get_file]": "TRUE", "step4[content_dir]": "%2Fvar%2Fwww%2Fhtml%2Fcontent%2F", "log_os": "Linux 4.15.0-99-generic #100-Ubuntu SMP Wed Apr 22 20:32:56 UTC 2020 x86_64", "log_server": "Apache/2.4.10 (Debian)", "log_php": "5.6.30", "log_mysql": "5.6.48", "log_url": "http://"+web+"/", "log_url_yes": "1", "log_yes": "1", "submit": " Next \xc2\xbb "}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
time.sleep(3)

burp0_url = "http://"+web+"/login.php?submit=%C2%BB+Log-in%21"
burp0_cookies = {"PHPSESSID": "d5c264210ea3d8d98bb53cab26864ef5", "ATutorID": "99a8ec7f488074be2c18ad19390be848"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://"+web+"/install/install.php", "Upgrade-Insecure-Requests": "1"}
requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
time.sleep(3)

 print("Config success!")