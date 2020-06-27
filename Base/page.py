from selenium.webdriver.common.by import By


class PageElement:

    # ----设置页面-----
    # 搜索按钮
    search_but_id = (By.ID,'com.android.settings:id/search')

    # ----搜索界面----
    # 搜索输入框
    search_box_id = (By.ID, "android:id/search_src_text")
    # 搜索结果
    search_result_ids = (By.ID, "com.android.settings:id/title")
