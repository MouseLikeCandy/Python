# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/14 21:21
@Auth ： 异世の阿银
@File ：test_JavaScript.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import re
'''
需求1: 匹配hi
需求2: 加入him,history,high 进行\b边界检测
需求3: 匹配hi jack 加入.*+?
需求4: 匹配三个字符的单词 加入[]{}
需求5: 匹配所有h/H开头的单词,或者a开头的单词.然后后面至少有一个字符的单词
需求6: 匹配字符中号码 加入\d
需求7: 匹配数字和字母 加入 \w
需求8: 匹配号码 加入 ^ $ 开始和结尾
'''

# 功能: 测试正则表达式
def testRegEx(regEx, str):
    # 参数:  regEx 正则字符串     str 源字符串数据
    # 1. 将正则字符串在底层编译为一个'正则对象'
    pattern = re.compile(regEx)
    # 2. 通过正则对象调用对象的字符串处理行为
    result_set = pattern.findall(str)
    # 3. 查看结果集
    for result in result_set:
        print(result)


if __name__ == '__main__':
    regEx = 'hi'
    # 边界检测 \b
    regEx = r'\bhi\b'   # 原生字符串
    str = 'hi jack how are you doing today? I ahim doing great, How about? hi Rose, Not bad, Thank you, bye! ' \
          'him,history,high'
    # 调用函数, 查看结果
    testRegEx(regEx, str)

    regEx = 'hi jack'
    str = 'hi jack how are you doing'
    testRegEx(regEx, str)

    regEx = 'hi.jack'
    str = 'hi爱jack how are you doing'
    # 点. 含义: 表示除了换行以外的任意单个字符
    testRegEx(regEx, str)
    # 量词 *+?  含义: 前面出现的字符可以出现  * (0个或多个)  + (1个或多个)  ? (0个或一个)
    regEx = 'hi.*jack'
    str = 'hi    jack how are you doing'
    testRegEx(regEx, str)

    regEx = 'hi.+jack'
    str = 'hijack how are you doing'
    testRegEx(regEx, str)

    regEx = 'hi.?jack'
    str = 'hijack how are you doing'
    testRegEx(regEx, str)

    # 匹配三个字符的单词
    # [] 范围     {m,n} 量词   限定前面范围的次数{开始,结束}
    regEx = r'\b[A-Za-z]{3,}\b'
    str = 'hi jack how are you doing today? I ahim doing great, How about? hi Rose, Not bad, Thank you, bye! ' \
          'him,history,high'
    testRegEx(regEx, str)

    regEx = r'\b[hHa][a-zA-Z]+\b'
    str = 'hi jack how are you doing today? I ahim doing great, How about? hi Rose, Not bad, Thank you, bye! ' \
          'him,history,high'
    testRegEx(regEx, str)

    regEx = '[0-9]+'
    regEx = r'\d'   # [0-9] 可以使用\d替换
    str = 'hi jack 666 how are you doing today? 999 I ahim doing great, How about? hi Rose, 888 Not bad, ' \
          'Thank you, bye! ' \
          'him,history,high'
    testRegEx(regEx, str)

    # 匹配数字和字母
    regEx = r'[0-9A-Za-z_]+'
    regEx = r'\w+'  # [0-9A-Za-z_] 可以使用\w替换  变量命名规则
    str = 'hi jack 666how are you doing today? 999I_ahim doing great, How about? hi Rose, 888 Not bad, ' \
          'Thank you, bye! ' \
          'him,history,high'
    testRegEx(regEx, str)

    # 匹配号码
    # ^ 开头
    # $ 结尾
    regEx = r'\d{11}'
    regEx = r'^\d{11}$'     # 中间全是数字
    str = '13366285946'
    testRegEx(regEx, str)