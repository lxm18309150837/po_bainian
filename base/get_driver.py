from appium import webdriver


def get_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.125.101:5555'
    # APP包名
    desired_caps['appPackage'] = 'com.yunmall.lc'
    desired_caps['appActivity'] = 'com.yunmall.ymctoc.ui.activity.MainActivity'

    # 获取toast
    desired_caps['automationName'] = "uiautomator2"
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    # 声明driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)