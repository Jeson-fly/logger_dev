# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/4/3
  Desc  ：
"""

import logging


def sample_logger() -> logging.Logger:
    """简单的日志"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger_ = logging.getLogger(__name__)
    return logger_


def write_logger() -> logging.Logger:
    """写文件的日志"""
    logger_ = logging.getLogger(__name__)
    logger_.setLevel(logging.INFO)
    handler = logging.FileHandler("test.log")
    handler.setLevel(logging.INFO)
    formate = logging.Formatter('%(asctime)s - %(process)d - %(thread)d - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formate)
    logger_.addHandler(handler)

    # 输出到屏幕
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    logger_.addHandler(console)
    return logger_


if __name__ == '__main__':
    logger = write_logger()
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")

# 写入日志文件
