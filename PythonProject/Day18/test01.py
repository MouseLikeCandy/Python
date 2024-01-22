# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/18 19:32
@Auth ： 异世の阿银
@File ：test01.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
'''
内置模块
第三方模块 : 自己的官网, 说明文档 py : python
https://www.pygame.org/news

pip install pygame
'''

'''
类:  数据 / 行为
坦克: Tank
    我方坦克
    敌方坦克
子弹: Bullet
墙: Wall
爆炸: Explode
音乐: Music

管理者: TankManager
1.数据: 坦克数据,子弹数据,墙壁数据...
2.行为(展示界面)

标题文字: 游戏名
游戏文字
'''
'''
pygame 最小开发模块

屏幕刷新: 100次/秒   坦克位置 子弹位置  -> 动画
获取时间并逐类响应  <--> 屏幕刷新

步骤:
# 1. 初始化pygame模块
# 2. 设置主窗口显示模式
# 3. 设置游戏标题名称
# 4. 保证窗口不退出
# 5. 设置主窗口的填充色
# 6. 刷新窗口
# 7. 获取所有事件,并响应
# 8. 如果用户点击了窗体的'关闭'按钮, 则实现程序的退出.
'''

'''
图片: Surface对象(载入的图片对象)  Rect对象(覆盖图像的矩形Rect对象)
blit(图片对象, rect对象)   块传输, 展示图片 
'''
import pygame
import sys

# 定义一个TankManager管理者
class TankManager(object):
    # 类数据
    size = width, height = (800, 500)  # 元组自动解包
    # 主窗口对象
    main_window = None
    # 定义一个我方坦克
    my_tank = None


    # 展示界面
    @staticmethod
    def show_menu():
        # 1. 初始化pygame模块
        pygame.init()
        # 2. 设置主窗口显示模式 size = (宽, 高)
        TankManager.main_window = pygame.display.set_mode(TankManager.size)
        # 3. 设置游戏标题名称
        pygame.display.set_caption('pygame坦克大战')

        # 在外面创建Tank, 在while True里面刷新窗口之前刷新
        TankManager.my_tank = Tank(350, 300)


        # 4. 保证窗口不退出
        while True:
            # 5. 设置主窗口的填充色
            TankManager.main_window.fill(pygame.Color('black'))

            # 刷新我方坦克
            TankManager.my_tank.display_tank()
            # 判断我方坦克的移动开关状态
            # if TankManager.my_tank.stop == False:   # 不要停一直移动
            if not TankManager.my_tank.stop:
                # 调用move方法
                TankManager.my_tank.move()


            # 6. 刷新窗口
            pygame.display.update()
            # 7. 获取所有事件,并响应
            for event in pygame.event.get():
                # 8. 如果用户点击了窗体的'关闭'按钮, 则实现程序的退出.
                if event.type == pygame.QUIT:
                    # print('关闭按钮被点击了...')
                    # break 不能结束程序, 只能跳出for循环
                    sys.exit()
                    # pygame.quit() # 以报错形式退出
                # 键盘按下事件
                elif event.type == pygame.KEYDOWN:
                    # 控制上下左右键
                    # 修改坦克移动的开关
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        TankManager.my_tank.stop = False
                    if event.key == pygame.K_UP:
                        # 切换方向, 调用坦克移动的方法
                        TankManager.my_tank.direction = 'U'
                        TankManager.my_tank.move()
                    elif event.key == pygame.K_DOWN:
                        TankManager.my_tank.direction = 'D'
                        TankManager.my_tank.move()
                    elif event.key == pygame.K_LEFT:
                        TankManager.my_tank.direction = 'L'
                        TankManager.my_tank.move()
                    elif event.key == pygame.K_RIGHT:
                        TankManager.my_tank.direction = 'R'
                        TankManager.my_tank.move()
                # 键盘松开事件
                elif event.type == pygame.KEYUP:
                    # 修改坦克移动的开关
                    if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                        TankManager.my_tank.stop = True
'''
1. 定义一个Tank类, 实现初始化方法, 移动坦克的方法, 展示坦克的方法
2. 在定义两个Tank的子类, MyTank(Tank) 和 EnemyTank(Tank)
3. 在TankManager类中定义一个我方坦克的类属性, 然后实现创建我方坦克, 并实现刷新我方坦克的功能.
'''

# 定义一个Tank类
class Tank(object):
    # 初始化数据
    def __init__(self, left, top):
        # 保存加载的图片
        # 对象数据,可以由外部传入(left, top)还可以由内部自行定义.
        self.images = {
            'U':pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        # 方向(默认向上)
        self.direction = 'U'
        # 根据方法获取对应的坦克图片
        self.image = self.images[self.direction]
        # rect 区域, 碰撞检测
        # 根据当前图片对象, 获取对应的rect对象
        self.rect = self.image.get_rect()
        # 设置区域对象的left和top数据
        self.rect.left = left
        self.rect.top = top
        # 设置我方坦克的移动速度
        self.speed = 5
        # 控制坦克的移动开关(默认坦克不能移动)
        self.stop = True

    # 移动  根据方向
    def move(self):
        # 判断坦克的方向,并实现移动  原点(0,0)  不能越界
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < TankManager.width:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < TankManager.height:
                self.rect.top += self.speed

    # 展示坦克
    def display_tank(self):
        # 根据方向获取对应的图片
        self.image = self.images[self.direction]
        # 主窗口中展示 (块传输)
        TankManager.main_window.blit(self.image, self.rect)




# 定义一个MyTank类
class MyTank(Tank):
    pass
# 定义一个EnemyTank类
class EnemyTank(Tank):
    pass

if __name__ == '__main__':
    # 游戏测试入口
    TankManager.show_menu()


# 如何控制坦克的移动速度呢?
# 使用speed不合理
# 屏幕的帧率控制 fps = frames per second
# 视频中每次展示的静态图像称为帧
# tick 摇摆, 钟摆
