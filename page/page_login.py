import allure

import page
from base.base import Base


class PageLogin(Base):
    # 点击我的
    @allure.step("点击我的")
    def page_click_me(self):
        self.base_click(page.login_me)
    # 点击已有账号去登录
    @allure.step("点击已有账号")
    def page_click_username_link(self):
        self.base_click(page.login_text_link)
    # 输入账号
    @allure.step("输入账号")
    def page_input_username(self,username):
        self.base_input(page.login_username,username)
    # 输入密码
    @allure.step("输入密码")
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)
    # 点击登录按钮
    @allure.step("点击登录按钮")
    def page_click_btn(self):
        self.base_click(page.login_btn)
    # 获取昵称
    @allure.step("获取昵称")
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)
    # 点击设置
    @allure.step("点击设置")
    def page_click_setting(self):
        self.base_click(page.login_click_setting)
    # 拖拽
    @allure.step("拖拽")
    def page_drag_and_drop(self):
        el1 = self.base_find_element(page.login_text_send)
        el2 = self.base_find_element(page.login_updata_pwd)
        self.base_drag_and_drop(el1,el2)
    # 点击退出
    @allure.step("点击退出")
    def page_click_logout(self):
        self.base_click(page.login_click_logout)
    # 确认退出
    @allure.step("确认退出")
    def page_login_click_ok_btn(self):
        self.base_click(page.login_click_ok_btn)

    # 封装整体退出
    def page_logout(self):
        # 拖拽
        self.page_drag_and_drop()
        # 点击退出
        self.page_click_logout()
        # 确认退出
        self.page_login_click_ok_btn()
    # 获取toast
    # def page_get_toast(self,msg):
    #     return self.base_get_toast(msg)