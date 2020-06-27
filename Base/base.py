from selenium.webdriver.support.wait import WebDriverWait
from Base.driver import DriverBase


class Base:
    # 初始化 实例化driver对象
    def __init__(self):
        self.driver = DriverBase.get_driver()

    # 定位元素  单个元素
    def place_ele(self,by_methon,timeout=5,poll_frequency=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*by_methon))

    # 定位元素  单个元素
    def place_eles(self, by_methon, timeout=5, poll_frequency=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*by_methon))
    # 点击操作
    def click_but(self,by_methon,timeout=5,poll_frequency=0.5):
        self.place_ele(by_methon,timeout,poll_frequency).click()
    # 输入内容
    def input_text(self,by_methon,text,timeout=5,poll_frequency=0.5):
        # 清空
        self.place_ele(by_methon,timeout,poll_frequency).clear()
        # 输入内容
        self.place_ele(by_methon,timeout,poll_frequency).send_keys(text)
