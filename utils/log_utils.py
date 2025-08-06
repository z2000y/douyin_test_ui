import logging
from datetime import datetime
import os

class logUtils:
    @staticmethod
    def get_logger(name):
        #创建日志器
        logger=logging.getLogger(name)
        logger.setLevel(logging.INFO)

        #避免日志重复输出
        if logger.handlers:
            return logger

        #创建日志目录
        log_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 日志文件名（按日期）
        log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        # 创建文件处理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 定义日志格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 添加处理器到日志器
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        return logger