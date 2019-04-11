
# coding: utf-8
# author@zyh

# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


#下面的地址是在docs.seleniumhq.org/download/ 下载了火狐浏览器的webdriver之后解压存放exe的地址
#我想你也可以使用chrome浏览器,即使用chromewebdriver（然后"稍微"debug一下下）
#稍等一下window自动解析宽带或连到WiFi
time.sleep(3)
#.log文件是不考虑自启动python运行调通一次后生成在.py同目录的文件
driver = webdriver.Firefox(executable_path = 'I:\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe',log_path=r"E:\geckodriver.log")
driver.get("http://172.19.1.9:8080/")
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("2017111111111")#学号
driver.find_element_by_id("pwd_hk_posi").click()
driver.find_element_by_id("pwd").clear()
driver.find_element_by_id("pwd").send_keys("233333")#密码
driver.find_element_by_id("selectDisname").click()
driver.find_element_by_id("_service_0").click()
driver.find_element_by_id("loginLink_div").click()
#sleep是为了好玩(?) 你完全可以我觉得完全可以删掉
time.sleep(1)
driver.close()
#调通之后，设置开机自启,如下两步走
'''(1）首先，需要新建一个.bat文件（用来运行脚本），格式如下，红色部分为python脚本的位置（写完之后保存）：

python f:\project_cx\wanggong\httpRoute.py

pause

（2）点击开始--所有程序--启动--右击--打开，将已经保存的.bat文件复制到该目录（C:\用户\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup）下，可能杀毒软件会阻止，选择允许，然后重启电脑即可。
这里的Administrator可以是你的账户。如果不想要pause也许可以删掉这行(反正我最后是删掉了的)
注：开机自启以后会打开一个cmd窗口，关闭窗口，python程序将停止运行。
'''

