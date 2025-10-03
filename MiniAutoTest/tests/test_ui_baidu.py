from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu_search():
    service = Service(r"D:\测试\MiniAutoTest\drivers\msedgedriver.exe")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    driver = webdriver.Edge(service=service, options=options)

    driver.get("http://www.baidu.com")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "kw"))
    )

    # 输入 + 提交
    driver.execute_script("arguments[0].value = '毛毛信息技术';", search_box)
    driver.execute_script("arguments[0].form.submit();", search_box)

    # 等待搜索结果
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.result"))
    )

    print("当前标题：", driver.title)  # 调试用
    assert "毛毛信息技术" in driver.title or "百度" in driver.title
    driver.quit()
