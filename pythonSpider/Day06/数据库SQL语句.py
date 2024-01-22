# -*- coding: utf-8 -*-
"""
@Time ： 2022/10/27 19:29
@Auth ： 异世の阿银
@File ：数据库SQL语句.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
查询
'''

'''
# 创建数据库,表
CREATE DATABASE mydb3;
USE mydb3;
CREATE TABLE exam(
	id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(20) NOT NULL,
	chinese DOUBLE,
	math DOUBLE,
	english DOUBLE
);
INSERT INTO exam VALUES(NULL, '关羽', 85, 76, 60);
INSERT INTO exam VALUES(NULL, '张飞', 70, 75, 70);
INSERT INTO exam VALUES(NULL, '赵云', 90, 60, 95);
INSERT INTO exam VALUES(NULL, '刘备', 97, 50, 50);
INSERT INTO exam VALUES(NULL, '曹操', 90, 89, 80);
INSERT INTO exam VALUES(NULL, '司马懿', 90, 67, 65);
# sql语句中的注释
-- sql语句中的注释
-- 1.查看表中的所有数据  选中执行
SELECT * FROM exam; 
-- 指定列查询
-- 需求: 查询表中所有学生的姓名和对应的英语成绩
-- * 通配符, 查询表中所有列
SELECT NAME, english FROM exam;
-- 条件查询 关键字where
-- 需求: 查询姓名为赵云的学生成绩
SELECT * FROM exam WHERE NAME='赵云';
-- 需求: 查询姓名为赵云的英语成绩
SELECT NAME, english FROM exam WHERE NAME='赵云';

-- 运算符 比较运算符和逻辑运算符
-- 需求: 查询英语成绩大于90分的同学
SELECT * FROM exam WHERE english > 90;
-- 需求: 查询英语成绩不等于70分的同学
SELECT * FROM exam WHERE english <> 70;
SELECT * FROM exam WHERE english != 70;
-- 需求: 查询英语分数在80-90 之间的同学(包含80和90)
SELECT * FROM exam WHERE english >=80 AND english <= 90;
SELECT * FROM exam WHERE english 80 <= english <= 90; -- 写法错误
SELECT * FROM exam WHERE english BETWEEN 80 AND 90;
-- 不包含80和90
SELECT * FROM exam WHERE english >80 AND english < 90;
-- 需求: 查询数学分数为89, 75, 91 的同学
SELECT * FROM exam WHERE math IN (89, 75, 91);

-- 插入一条语句
INSERT INTO VALUES(NULL,'刘阿斗',86,NULL,83);
-- 需求: 查询所有姓刘的学生成绩
SELECT * FROM exam WHERE NAME LIKE '刘%'; -- '%'后面有0个或多个字符
-- 需求: 查询所有姓刘,姓名为两个字的学生成绩
SELECT * FROM exam WHERE NAME LIKE '刘_'; -- '_'后面有且仅有1个字符
-- 需求: 查询姓名中包含'刘'的学生成绩
SELECT * FROM exam WHERE NAME LIKE '%刘%'; -- '%'后面有0个或多个字符

-- 需求: 查询数学成绩不为null的学生
SELECT * FROM exam WHERE math != NULL;  -- 语法没错, 执行结果错误
SELECT * FROM exam WHERE math IS NOT NULL;
-- 需求: 查询数学成绩为NULL的学生
SELECT * FROM exam WHERE math IS NULL;

-- 需求: 查询数学和语文成绩都大于80 的学生
SELECT * FROM exam WHERE math>80 AND chinese>80; 
-- 需求: 查询数学或语文成绩都大于80 的学生
SELECT * FROM exam WHERE math>80 OR chinese>80; 

-- 查询英语分数不大于60的学生
SELECT * FROM exam WHERE english <= 60;
SELECT * FROM exam WHERE NOT english >60;

-- 虑重
-- 需求: 查询所有的语文成绩
SELECT chinese FROM exam;
-- 需求: 过滤掉重复的语文成绩
SELECT DISTINCT chinese FROM exam;

-- 别名 -- as 不建议省略, 别名不建议加引号
SELECT id AS '编号', NAME AS '姓名', chinese AS '语文' , math AS '数学', english AS '英语' FROM exam;
SELECT id '编号', NAME  '姓名', chinese '语文' , math '数学', english '英语' FROM exam;
SELECT id 编号, NAME  姓名, chinese 语文, math 数学, english 英语 FROM exam;
-- 需求: 查询姓名和对应的英语成绩
SELECT NAME, english FROM exam;
SELECT NAME english FROM exam;  -- 把name重命名为english

-- 需求: 查询每个学生的总分
SELECT id, NAME, chinese+math+english AS '总分' FROM exam; 
SELECT *, chinese+math+english AS '总分' FROM exam; 

-- 排序 order by 
-- asc ascending 升序
-- desc descending 降序

-- 需求: 对语文成绩升序排序后输出
SELECT * FROM exam;
SELECT * FROM exam ORDER BY chinese ASC;
-- 需求: 对语文升序排序, 如果语文成绩一样, 按数学成绩降序排序.
SELECT * FROM exam ORDER BY chinese ASC, math DESC;
-- 需求: 对总分排序, 从高到低
SELECT *, chinese+math+english AS '总分' FROM exam ORDER BY '总分' DESC; -- 加单引号不排序
SELECT *, chinese+math+english AS 总分 FROM exam ORDER BY 总分 DESC;

-- null的处理 IFNULL
SELECT NAME, IFNULL(chinese,0)+IFNULL(math,0)+IFNULL(english,0) AS 总分 FROM exam ORDER BY 总分 DESC;

-- 需求: 对姓刘的学生成绩总分进行降序排序
SELECT NAME, IFNULL(chinese,0)+IFNULL(math,0)+IFNULL(english,0) AS 总分 FROM exam;
	WHERE NAME LIKE '刘%' 
		ORDER BY 总分 DESC;
	
-- 聚合函数
-- 需求: 统计参加数学考试的有多少人
SELECT COUNT(math) FROM exam; -- 去除null
SELECT COUNT(id) FROM exam; -- 总数
SELECT COUNT(*) FROM exam; -- 除非所有行中数据都为null

-- 需求: 统计语文成绩大于等于90的学生数
SELECT COUNT(*) FROM exam WHERE chinese >= 90;
-- 需求: 统计总分大于250的人数有多少
SELECT *, IFNULL(chinese,0)+IFNULL(math,0)+IFNULL(english,0) AS 总分 FROM exam;

SELECT COUNT(*) FROM exam
	WHERE IFNULL(chinese,0)+IFNULL(math,0)+IFNULL(english,0) > 250;

-- 需求: 统计一个班级数学总成绩
SELECT SUM(math) FROM exam;   -- 自动排除null

-- 需求: 分别显示一个班级语文, 英文, 数学各科的总成绩
SELECT SUM(chinese), SUM(math), SUM(english) FROM exam;

-- 需求: 统计一个班级全部学生的语文, 英文, 数学各科的成绩总和
SELECT SUM(chinese+math+english) AS 三科总成绩 FROM exam;               -- 2186 -- 先按行统计 -- 86+null+83 = null
SELECT SUM(IFNULL(chinese,0) + IFNULL(math,0) + IFNULL(english,0)) AS 三科总成绩 FROM exam; -- 2355

SELECT SUM(chinese) + SUM(math) + SUM(english) AS 三科总成绩 FROM exam; -- 2355 -- 按列统计


-- 需求: 统计班级的语文平均分
SELECT SUM(chinese)/COUNT(*) FROM exam;

SELECT ROUND(SUM(chinese)/COUNT(*),2) AS 语文平均分 FROM exam; -- ROUND(值, 小数位数) 四舍五入, 保留两位小数

-- 需求: 数学平均分
SELECT AVG(math) FROM exam;           -- 78.22
SELECT SUM(math)/COUNT(*) FROM exam;  -- 70.4
SELECT AVG(IFNULL(math,0)) FROM exam; 

-- 需求: 求一个班级总成绩平均分
-- 1. 总成绩 SUM(chinese) + SUM(math) + SUM(english)
-- 2. 平均分 AVG()
SELECT AVG(SUM(chinese) + SUM(math) + SUM(english)) AS 总分平均分 FROM exam; -- Invalid use of group function 
-- 聚合函数不能嵌套
-- AVG(参数为某一列), 里面直接放入总和显然也是不正确的
SELECT AVG(IFNULL(chinese,0) + IFNULL(math,0) + IFNULL(english,0)) AS 总分平均分 FROM exam; -- 235.5
SELECT (SUM(chinese) + SUM(math) + SUM(english))/COUNT(*) AS 总分平均分 FROM exam;	    -- 235.5

-- 需求: 统计英语最低分最高分
SELECT MAX(english), MIN(english) FROM exam;

-- 需求: 统计总分的最高分和最低分
SELECT MAX(IFNULL(chinese,0) + IFNULL(math,0) + IFNULL(english,0)) AS 最高分,
 MIN(IFNULL(chinese,0) + IFNULL(math,0) + IFNULL(english,0)) AS 最低分 FROM exam;


-- ----------------------------------------------------------------------------------
CREATE TABLE orders(
	id INT,
	product VARCHAR(20),
	price FLOAT
);

INSERT INTO orders(id, product, price) VALUES(1, '纸巾', 16);
INSERT INTO orders(id, product, price) VALUES(2, '纸巾', 16);
INSERT INTO orders(id, product, price) VALUES(3, '红牛', 5);
INSERT INTO orders(id, product, price) VALUES(4, '洗衣粉', 60);
INSERT INTO orders(id, product, price) VALUES(5, '苹果', 8);
INSERT INTO orders(id, product, price) VALUES(6, '洗衣粉', 60);

-- 需求: 查询购买每种商品的总价
-- 说明: 一旦实现了分组, select显示语句中, 只应该显示被分组的列和聚合函数
SELECT product, SUM(price) FROM orders GROUP BY product;
SELECT id, product, SUM(price) FROM orders GROUP BY product; -- id 只有一个显示

-- 需求: 查询每一种商品的总价大于30的商品, 并显示总价.
SELECT product, SUM(price) FROM orders GROUP BY product WHERE SUM(price)>30; -- You have an error in your SQL syntax;
SELECT product, SUM(price) FROM orders WHERE SUM(price)>30 GROUP BY product ;-- Invalid use of group function
-- group by 分组之后如果要实现过滤, 必须与having连用
SELECT product, SUM(price) FROM orders 
	GROUP BY product HAVING SUM(price)>30;

-- where 分组之前实现过滤
-- having 分组之后实现过滤


-- select 语句的执行顺序
SELECT product, SUM(price) AS 总分 FROM orders 
	WHERE price > 6
		GROUP BY product HAVING 总价>30
			ORDER BY 总价 DESC;

-- 1. FROM 表, 列名
-- 2. WHERE 实现第一次过滤
-- 3. GROUP BY 分组
-- 4. SELECT 确定最终返回结果的列名, 但是会在所有语句执行完毕后才能返回.
-- 5. HAVING 实现分组过滤
-- 6. ORDER BY 最后排序 

-- 数据库备份
-- 语法: mysqldump -u 用户名 -p 数据库名 > 磁盘SQL文件绝对路径
-- 命令行: mysqldump -u root -p mydb3 > D:\backup\mydb3
-- 数据库恢复方式一
-- 新建一个空数据库,不需要进入到数据库中,直接使用指令实现导入.
-- 语法: mysql -u 用户名 -p 导入数据库名 < 磁盘SQL文件绝对路径
CREATE DATABASE mydb4;
-- 命令行: mysql -u root -p mydb4 > D:\backup\mydb3

-- 数据库恢复方式二
-- 说明: 新建一个空数据库, 然后在命令行中先进入到数据库中, 然后执行以下指令.
-- mysql> source 硬盘SQL文件绝对路径

'''