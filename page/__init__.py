from selenium.webdriver.common.by import By

# 点击我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 点击已有账号
login_text_link = By.ID, "com.yunmall.lc:id/textView1"
# 输入账号
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 点击登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.XPATH, "//*[contains(@text,'itheima')]"
# 设置
login_click_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 消息推送
login_text_send = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
login_updata_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 退出
login_click_logout = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认退出
login_click_ok_btn = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
