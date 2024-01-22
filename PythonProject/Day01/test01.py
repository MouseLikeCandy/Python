# -*- coding: utf-8 -*-
"""
@Time ： 2023/4/24 6:52
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# 1——Python语言介绍
'''
PYPL 可以查看计算机编程语言排行榜   PYPL PopularitY of Programming Language index

python3.0

Python发展方向

人生苦短，我用Python

学习方法--讨论   实践练习   向他人教授/立即使用

编程语言不仅仅是程序员的事情

全民学Python, 学校已经开课, Python二级

办公自动化  人工智能  自动化运维  爬虫   科学计算  数据分析  机器学习  数据挖掘  搜索算法 推荐算法  深度学习

所有学科的交叉 
'''
# 2——编程的学习方法
'''
实践练习         多敲
向其他人教授

不理解也要敲吗？对   在敲代码的过程中，就是在不断的思考，写完代码后，运行程序就可以看到代码的逻辑，这种过程不断的帮助自己理解
'''
# 3——什么是计算机语言
'''
计算机只认识0和1
内存中的单位使用字节表示（集成电路）

int(4字节）  在内存中开辟32bit的空间

机器语言：01010101001101
汇编语言：特殊符号，奇怪的字符，代替了01
高级语言：模拟人的思维
'''
# 4——基础课程案例展示
'''
PyCharm

设置字体  外观

案例展示

石头剪刀布
斗地主
学生管理系统
坦克大战
'''
# 5——第一个Python程序
'''
New - Project
New - Python Package  
New - Python File

print("Hello World!")

搜狗输入法 ---中文时使用英文标点

解释器的位置
编辑器尽量不要汉化-积累基础的单词
'''
# 6——注释的说明
'''
# shift 3
注释快捷键  Ctrl + /
'''
'''
多行注释
作用：
1.给人看的
2.不会被解释器执行的，解释器会忽略
3.注释是程序员间的交流文字
注意：
1.注释不能相互嵌套
2.养成注释习惯
3.注释与功能相同
'''
# 7——关键字和标识符

# 导入系统库（关键字）
import keyword
# 输出查看关键字列表
print(keyword.kwlist)
print (len(keyword.kwlist))
'''
有些单词被Python语言赋予了 ‘’特殊含义‘’，也称作保留字

自己定义名称，如何定义？
名称：变量 函数 类名 对象名 。。。  统称为 ‘’标识符‘’
1.数字不能开头
2.只能使用a-z,A-Z,0-9,_(下划线）
3.不能使用系统关键字
4.严格区分大小写

命名规则：                            函数名 （坦克碰撞墙壁）
1.小驼峰 tankHitWall
2.大驼峰 TankHitWall
3.下划线 tank_hit_wall
'''
# 8——变量和数据类型
'''
变量中的数据有覆盖的概念，后面的数据会覆盖原先的数据。
赋值运算符 =  从右向左
将数据存储到变量名的内存空间中

数据类型
1.Number 数值  int float
2.String     字符串
3.集合   list dict tuple

查看数据类型
内置函数：type(变量)
'''
# 9——数据类型演示

'''
格式：变量名 = 变量值
'''
num1 = 10  # 将数值10赋值给了num1名称的内存空间
print(num1)

print(f"num1={num1}，type(num1)={type(num1)}")   # f-》format格式化  {}表示占位符，大括号放变量名称

num2 = 6.66  # 前面不加类型
print(f"num2={num2}，type(num2)={type(num2)}")

# bool ->boolean    真假True/False
is_visited = True
print(f"is_visited={is_visited}，type(is_visited)={type(is_visited)}")

s1 = 'Hello World.'
s2 = "Hello World."
s3 = '''Hello World.'''
print(f"s={s1}，type(s)={type(s1)}")
print(f"s={s2}，type(s)={type(s2)}")
print(f"s={s3}，type(s)={type(s3)}")
# 字符串：单引号   双引号  三引号

# 列表类型  有序，可重复
stu_list = ['张三', '李四', '王五', '李四', '张三']
print(f"stu_list={stu_list}，type(stu_list)={type(stu_list)}")

# 元组类型  长度固定，不可更改
stu_tuple = ('张三', '李四', '王五', '李四', '张三')
print(f"stu_tuple={stu_tuple}，type(stu_tuple)={type(stu_tuple)}")

# 集合    无序 ，不重复
stu_set = {'张三', '李四', '王五', '李四', '张三'}
print(f"stu_set={stu_set}，type(stu_set)={type(stu_set)}")

# 字典类型     键值对，键不能重复
stu_dict = {'张三': 18, '李四': 20, '王五': 30}
print(f"stu_dict={stu_dict}，type(stu_dict)={type(stu_dict)}")


# 10——字符串格式化占位符

'''
1.定义一个变量name，输出 “我的名字叫小明,请多多关照”
'''
name = '小明'
age = 18
# 占位符： %s 字符串   %d 整型占位符  %f 浮点型
print('我的名字叫%s,今年%d岁,请多多关照！' % (name, age))

# f (format)的写法
print(f'我的名字叫{name},今年{age}岁,请多多关照！')
