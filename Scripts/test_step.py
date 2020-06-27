import allure

class Teststep:
    @allure.step('描述信息')
    def test_001(self):
        '''手动啊'''
        allure.attach('这是登陆测试用例1.输入手机号....','用例描述')

    @allure.severity(allure.severity_level.BLOCKER)
    def test_002(self):
        assert True

    @allure.severity(allure.severity_level.CRITICAL)
    def test_003(self):
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_004(self):
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_005(self):
        assert True