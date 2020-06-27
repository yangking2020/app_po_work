from Base.base import Base
from Base.page import PageElement

# 搜索页面类
class SearchPage(Base):
    def __init__(self):
        super().__init__()

    # 输入搜索内容
    def send_text(self, text):
        self.input_text(PageElement.search_box_id, text)

    # 获取搜索结果
    def result_text(self):
        result = self.place_eles(PageElement.search_result_ids)
        return [i.text for i in result]