from Base.base import Base
from Base.page import PageElement

# 设置页面类
class SettingPage(Base):
    # 重写初始化
    def __init__(self):
        super().__init__()
    # 点击搜索按钮
    def click_search_but(self):
        self.click_but(PageElement.search_but_id)
