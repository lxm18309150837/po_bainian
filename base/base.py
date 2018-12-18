from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver
    # 封装查找方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
        # 显示等待
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 封装输入方法
    def base_input(self,loc,value):
        ele=self.base_find_element(loc)
        ele.clear()
        ele.send_keys(value)

    # 封装点击
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 获取昵称
    def base_get_text(self,loc):
        return self.base_find_element(loc).text
    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("./image/faild.png")

    # 拖拽
    def base_drag_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)

    # 获取toast
    def base_get_toast(self,msg):
        loc=By.XPATH,"//*[contains(@text,'"+msg+"')]"
        return self.base_find_element(loc,timeout=3,poll=0.1).text
