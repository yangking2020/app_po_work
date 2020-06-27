import pytest
from Base.driver import DriverBase
from Base.entrance_page import EntrancePage


class TestSearch:
    # 退出driver
    def teardown_class(self):
        DriverBase.quit_driver()
    # 测试用例
    @pytest.mark.parametrize('search_text,search_result',[('1','休眠'),('i','IP地址'),('m','MAC地址')])
    def test_search_01(self,search_text,search_result):
        # 点击搜索按钮
        EntrancePage.get_setting_class().click_search_but()
        # 输入内容
        EntrancePage.get_search_calss().send_text(search_text)
        # 断言
        assert search_result in EntrancePage.get_search_calss().result_text()