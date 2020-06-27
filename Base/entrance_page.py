from Page.search_page import SearchPage
from Page.setting_page import SettingPage


class EntrancePage:
    # ----设置页面类对象----
    @classmethod
    def get_setting_class(cls):
        return SettingPage()
    # ----搜索页面对象----
    @classmethod
    def get_search_calss(cls):
        return SearchPage()