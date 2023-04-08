# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
  Author  ：lining
  Email  ：993811091@qq.com
  Time  ：2023/4/3
  Desc  ：
"""
import yaml
import logging.config
import os


def setup_logging(default_path="logger.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def func():
    logging.info("start func")

    logging.info("exec func")

    logging.info("end func")


if __name__ == "__main__":
    setup_logging(default_path="logger.yaml")
    func()


