import os
import pytest
import allure

if __name__ == "__main__":
    # 运行测试并生成Allure报告数据
    import os

    # 定义报告目录路径
    result_dir = "./report/allure-results"
    report_dir = "./report/allure-report"

    # 检查并创建目录（exist_ok=True表示如果目录已存在也不会报错）
    os.makedirs(result_dir, exist_ok=True)

    # 生成报告数据到allure-results目录
    os.system(f"pytest --alluredir={result_dir}")

    # 先生成并保存到指定目录
    os.system(f"allure generate {result_dir} -o {report_dir} --clean")
    # 再临时预览（此时预览的是已保存的文件）
    os.system(f"allure serve ./report/allure-results")