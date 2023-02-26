# -*- coding: utf-8 -*- 
"""          
# @Time   : 2023/2/25 19:15
#  :TGW
"""
import logging


def test_log():
    # 创建日志器  这个日志器就写入了日志信息
    logger = logging.getLogger()
    # 设置级别  从哪个级别开始
    logger.setLevel(logging.INFO)
    if not logger.handlers:  # 不加这句可能打印两次

        # 指定日志信息显示在哪里 控制台
        # 创建控制台处理器
        sh = logging.StreamHandler()
        # 把日志信息添加到控制台
        logger.addHandler(sh)

        # 把日志信息显示到文本文件
        # 创建文本处理器  文件放在哪  文件地址
        fh = logging.FileHandler('log1.txt', encoding='utf-8')
        # 日志信息显示在文本文件中    日志信息保存在哪
        logger.addHandler(fh)

        # 格式器  创建格式器  设置自定义格式
        fmt1 = '%(asctime)s %(filename)s %(funcName)s %(message)s'
        formatter = logging.Formatter(fmt1)

        # 给控制台设置格式
        sh.setFormatter(formatter)
        # 给文本文件设置格式
        fh.setFormatter(formatter)
    return logger
