import os
import sys

import allure

sys.path.append(os.getcwd())

from base.read_data import ReadData

sys.path.append(os.getcwd())

import pytest

from page.page_in import PageIn

# 固定值
# def get_data():
#     return [("itheima","123456","itheima")]

# 传入yaml数据
def get_data():
    list=[]
    for data in ReadData("login_data.yaml").read_data().values():
        list.append((data.get("username"),data.get("password"),data.get("expect_result"),data.get("expect_toast")))
    return list


class TestLogin():

    def setup_class(self):
        self.login=PageIn().page_get_pagelogin()
        # 点击我
        self.login.page_click_me()
        # 点击已有账号
        self.login.page_click_username_link()


    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("username,password,expect_result,expect_toast",get_data())
    # @pytest.mark.parametrize("expect_result",["itheima"])
    @allure.step("开始执行登录测试")
    def test_login(self,username,password,expect_result,expect_toast):
        login = self.login
        if expect_result:
            try:
                # 输入用户名
                login.page_input_username(username)
                # 输入密码
                login.page_input_pwd(password)
                # 点击登录
                login.page_click_btn()
                # 获取昵称+断言
                assert expect_result in login.page_get_nickname()
                # 点击设置
                login.page_click_setting()
                # 退出
                login.page_logout()
                # 点击我
                login.page_click_me()
                # 点击已有账号去登录
                login.page_click_username_link()
            except AssertionError:
                # 截图
                login.base_get_image()
        else:
            try:
                # 输入用户名
                login.page_input_username(username)
                # 输入密码
                login.page_input_pwd(password)
                # 点击登录
                login.page_click_btn()

                # print(login.base_get_toast(expect_toast))

                # 断言
                assert "expect_toast" in login.base_get_toast(expect_toast)
            except AssertionError:
                # 截图
                login.base_get_image()
                # 打开图片
                with open("./image/faild.png","rb")as f:
                    # 写入报告
                    allure.attach("失败原因",f.read(),allure.attach_type.PNG)

