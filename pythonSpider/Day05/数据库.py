# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/7 20:01
@Auth ： 异世の阿银
@File ：数据库.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


'''
数据库: Database 是按照数据结构来组织,存储和管理数据的仓库
数据结构

网状数据库
关系数据库
图灵奖
oracle access mysql

文件存储---垃圾场
数据库-----仓库

结构化
共享
独立

关系型数据库/键值存储数据库
MySQL瑞典
速度快.成熟稳定,免费,适合中小企业和个人(90%)
数据库排行榜 https://db-engines.com/en/ranking

运行 services.msc   查找MySql服务

数据库的下载,安装,卸载

www.mysql.com
1.卸载
默认安装路径数据会存储在ProgramData文件夹中.
说明: ProgramData文件夹是一个隐藏的文件夹,因此要设置'显示隐藏文件夹'才能看到.
2.安装

3.检查环境变量
windows + R键 cmd
mysql -u root -p
'mysql' 不是内部或外部命令，也不是可运行的程序
或批处理文件。
找不到mysql.exe文件 - > 配置环境变量
计算机-属性-高级系统设置-环境变量-系统变量-path-编辑-新建-将mysql.exe所在目录放在里面

mysql(mysql指令) -u (用户名->) root -p(回车输入密码) 
4.检查环境是否启动
windows + R键 services.msc 查看MySQL服务是否启动

5.检查是否登录成功
-u user 用户名
-p password 密码
-h host 主机
-P 端口


可视化工具:
1.SQLyog工具
主机地址: 127.0.0.1 localhost
root 123456 3306

mysql数据库的存储结构

# 连接不成功问题
# mysql 8.0之后密码验证发生了变化
解决: 进入mysql, 修改加密规则
修改:
ALTER USER 'root'@'localhost'IDENTIFED BY'123456'PASSWORD EXPIRE NEVER;
ALTER USER 'root'@'localhost'IDENTIFIED WITH mysql_native_password BY'123456'
刷新:
FLUSH PRIVILEGES

默认有四个数据库

'''
# 步骤
# 1.操作数据库
# SQL语句
# 结构化查询语言(Structured Query Language)
# information_schema数据库
# 其中保存着关于MySQL服务器所维护的所有其他数据库的信息.如数据库名,数据库的表,表栏的数据类型与访问权限等.
# performance_schema数据库
# 存储引擎: 命名PERFORMANCE_SCHEMA,主要用于收集数据库服务器性能参数.
# mysql数据库:
# mysql库是系统库,里面保存有账户信息,权限信息,存储过程,event,时区等信息.
# sys数据库: 顾名思义,应该是与系统相关配置的信息.

# 客户端连接数据库①命令行②图形化界面③Python程序...
# 命令行 mysql -u root -p
'''
1.查询mysql服务软件的所有数据仓库
show databases;
drop database mydb3;
drop database mydb5;
2.查看mysql数据仓库的编码
show create database mysql;
3.创建数据库
create database mydb1; CREATE DATABASE mydb1;
默认编码方式:UTF8
create database mydb2 character set utf8;
4.删除数据库
drop database mydb3;
drop database mydb5;
drop database mydb4;
5.修改数据库编码集
alter database mydb2 character set gbk;
6.切换数据库和查看正在使用的数据库.
查看正在使用的数据库: select database();
切换数据库: use mydb2;
'''
# 2.操作数据表
'''
数据表结构的sql语句
[示例]
需求: 创建一个员工表,员工表有工号/姓名/年龄/性别/生日
class Employee(0bject):
    def init(self,emp_id, name, age, gender, birthday):
    self.emp_id = emp_id
字段I类型
字符串有两种类型:
①char(固定长度)
②varchar(可变长度)
整型:int
浮点型: 
float单精度(4个字节)
double双精度(8个字节)

如果一个数据不是用于运算, 我们就应该将这个数据定义为字符串类型的数据.
create table employee(
    emp_id int,
    name varchar(16),
    age int,
    gender varchar(8),
    birthday date             # 最后一条语句不能写逗号
);


查看表
1.查看该数据库的所有表    show tables;
2.查看建表语句以及字符集  show create table employee;
3.查看表的列信息(查看表结构) desc(description) employee;

约束
意义: 保证数据的有效性和完整性,可以确保数据库满足业务规则.
需求: 创建一个员工表,员工表有工号/姓名/年龄/性别/生日/住址
1.要求工号是主键并且设置自增长    primary key  auto_increment 当前列名设置为主键实现自增长, 主键特点:唯一, 非空
2.姓名必须是唯一的      unique 
3.年龄必须是非空的      not null
4.地址必须是唯一的,并且非空     unique not null

空表示没有信息,不是重复

create table employee(
    emp_id int primary key auto_increment,
    name varchar(16) unique,
    age int not null,
    gender varchar(8),
    birthday date
    address varchar(30) unique not null             
);

数据表的删除
需求: 删除employee
drop table employee;

alter 修改
'''
# 3.操作数据表中的数据
'''
数据记录的增删改查
insert, delete, update, select
查询
select * from user;

insert插入语句:
所有列/部分列/省略列名,值需要全部提供
insert into user (id, name, age, gender, birthday, address) values(null, '张三', 20, '男', '2008-08-08', '天安门1号')
emp_id 是自增长的, 可以不写, 要用null占位
insert into user (id, name, age, address) values(null, '李四', 20, '天安门2号')
insert into user values(null, '王五', 25, '男', '2020-02-02', '天安门3号')


update 修改语句
格式: update 表名 set 列名 = 值 [where 条件];
需求: 将所有人的年龄修改为22岁.
update user set age = 22;
需求: 将姓名为张三的人的年龄改为18岁.
update user set age = 30 where name = '张三';
需求: 将姓名为李四的人的年龄改为30, 地址改为天安门666号.
update user set age = 30, address = '天安门666号' where name = '李四';
需求: 将王五的年龄在原基础上增加2岁.
update user set age = age + 2 where id = 3;


delete 删除语句
格式: delete from 表名 [where 条件]
需求: 删除表中名称为'王五'的记录.
delete from user where name = '王五';
需求: 删除年龄是30岁的员工.
delete from user where age = 30;
需求: 删除表中所有记录.
delete from user;



'''
