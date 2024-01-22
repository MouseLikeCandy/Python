# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/18 7:14
@Auth ： 异世の阿银
@File ：modules_install.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
第三方模块 PyInstaller

1. 从国内的镜像源中查找需要下载的模块, 速度快
pip install PyInstaller -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

2. 从国外的镜像源中查找需要下载的模块
pip install PyInstaller

3. 删除已经下载的第三方模块
pip uninstall PyInstaller

4. 列出所有已经下载的第三方模块
pip list 

5. 测试第三方模块是否安装成功
1) python 进入Python交互式界面
2) import PyInstaller 如果不报错,说明第三方模块安装成功
3) quit() 退出Python交互式界面
4) exit   退出cmd命令行窗口

需求: 将项目打包为一个可执行的exe文件. 这样的文件就可以在其他没有安装Python环境的计算机中运行了.
# pyinstaller -F E:\PythonProject\Day16\test04.py   需要打包的.py模块的文件路径
说明: -F 表示只生成一个.exe的可执行文件.

8577 INFO: Updating manifest in C:\Users\YiNing\dist\test04.exe.notanexecutable

有notanexecutable  但还是能执行.
'''



