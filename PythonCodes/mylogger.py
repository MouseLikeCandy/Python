# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/5 7:20
@Auth ： 异世の阿银
@File ：mylogger.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
日志推荐
pip install loguru
简单优雅永不过时
'''

from loguru import logger


logger.trace("堆栈信息")    # 等级低
logger.debug("调试信息")
logger.info('pip install loguru')
logger.warning("看不清可以打在这里吗?")
logger.error("错误信息")

