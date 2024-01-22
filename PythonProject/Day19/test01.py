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
''''
pygame模块提供了一个Sprite 精灵这个父类, 主要的作用就是用来检测'精灵'间是否发生了碰撞.
思考: 自定义对象如何成为'精灵'对象?  答曰: 自定义类继承Sprite类.
'''
import pygame
import sys
import random
import pygame.freetype
# 导入精灵类
from pygame.sprite import Sprite

# 定义一个TankManager管理者
class TankManager(object):
    # 类数据
    size = width, height = (800, 500)  # 元组自动解包
    # 主窗口对象
    main_window = None
    # 定义一个我方坦克
    my_tank = None
    # Frames Per Second 每秒帧率参数
    fps = 100
    fclock = pygame.time.Clock()

    # 定义一个存储敌方坦克对象的列表
    enemy_tank_list = []

    # 定义一个font
    font = None
    # 定义一个存储我方坦克的子弹列表
    myTank_bullet_list = []


    # 展示界面
    @staticmethod
    def show_menu():
        # 1. 初始化pygame模块
        pygame.init()
        # 2. 设置主窗口显示模式 size = (宽, 高)
        TankManager.main_window = pygame.display.set_mode(TankManager.size)
        # 3. 设置游戏标题名称
        pygame.display.set_caption('pygame坦克大战')

        # 创建font对象
        TankManager.font = pygame.freetype.Font(r'C:\Windows\Fonts\msyh.ttc')

        # 在外面创建Tank, 在while True里面刷新窗口之前刷新
        # 创建我方坦克
        TankManager.my_tank = MyTank(350, 300)
        # 创建敌方坦克(5)
        for i in range(1, 6, 1):
            enemy_tank = EnemyTank(i * 130, 10)
            # 将创建的敌方坦克添加到敌方坦克列表中
            TankManager.enemy_tank_list.append(enemy_tank)

        # 4. 保证窗口不退出
        while True:
            # 5. 设置主窗口的填充色
            TankManager.main_window.fill(pygame.Color('black'))

            # 绘制窗口左上角文字
            TankManager.font.render_to(TankManager.main_window, (10, 10),
                                       f'剩余敌方坦克数量: {len(TankManager.enemy_tank_list)}', fgcolor='red', size=30)


            # 刷新我方坦克
            TankManager.my_tank.display_tank()
            # 判断我方坦克的移动开关状态
            # if TankManager.my_tank.stop == False:   # 不要停一直移动
            if not TankManager.my_tank.stop:
                # 调用move方法
                TankManager.my_tank.move()
                # 检测我方坦克是否与敌方坦克发生碰撞
                TankManager.my_tank.myTank_hit_enemyTank()

            # 刷新敌方坦克
            for enemy_tank in TankManager.enemy_tank_list:
                # 调用Tank类的display_tank 方法
                enemy_tank.display_tank()
                # 让敌方坦克实现移动
                enemy_tank.move()
                # 检测敌方坦克是否与我方坦克发生碰撞
                enemy_tank.enemyTank_hit_myTank()

            # 刷新我方坦克的子弹列表
            for my_Bullet in TankManager.myTank_bullet_list:
                # 判断我方坦克的子弹状态
                if my_Bullet.live:
                    # 存活状态, 需要展示子弹
                    my_Bullet.display_bullet()
                    # 调用子弹的移动方法
                    my_Bullet.move()
                else:
                    # 消亡状态, 需要将子弹从子弹列表中移除
                    TankManager.myTank_bullet_list.remove(my_Bullet)

            # 6. 刷新窗口
            pygame.display.update()
            # 控制屏幕每秒刷新的帧率
            TankManager.fclock.tick(TankManager.fps)
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
                    elif event.key == pygame.K_SPACE:
                        # 创建我方坦克的子弹, 然后将子弹加到我方坦克的子弹列表中
                        # 子弹数量控制
                        if len(TankManager.myTank_bullet_list) < 3:
                            my_Bullet = Bullet(TankManager.my_tank)
                            TankManager.myTank_bullet_list.append(my_Bullet)
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
class Tank(Sprite):
    # 初始化数据  left, top, images, direction, speed 不同坦克也不一样
    def __init__(self, left, top, images, direction, speed):
        # 保存加载的图片
        # 对象数据,可以由外部传入(left, top)还可以由内部自行定义.
        # 根据方法获取对应的坦克图片
        self.images = images
        self.direction = direction
        self.image = self.images[self.direction]
        # rect 区域, 碰撞检测
        # 根据当前图片对象, 获取对应的rect对象
        self.rect = self.image.get_rect()
        # 设置区域对象的left和top数据
        self.rect.left = left
        self.rect.top = top

        self.speed = speed
        # 控制坦克的移动开关(默认坦克不能移动)
        self.stop = True
        # 新增属性, 记录原来的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    # 移动  根据方向
    def move(self):
        # 每次移动时,我们需要更新坦克对象的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

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
    def __init__(self, left, top):
        # 图片数据
        images = {
            'U': pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif')
        }
        # 方向(默认向上)
        direction = 'U'
        # 设置我方坦克的移动速度
        speed = 5
        # 调用父类的初始化方法, 将数据传入到父类中实现数据的初始化
        super().__init__(left, top, images, direction, speed)

    # 检测我方坦克是否与敌方坦克发生碰撞
    def myTank_hit_enemyTank(self):
        # 遍历敌方坦克列表
        for enemy_tank in TankManager.enemy_tank_list:
            # 调用 sprite 碰撞检测的方法
            if pygame.sprite.collide_rect(self, enemy_tank):
                # 如果程序来到这里, 说明两个对象发生了碰撞
                # 让我方坦克回到原来的坐标
                self.rect.left = self.oldLeft
                self.rect.top = self.oldTop

# 定义一个EnemyTank类
class EnemyTank(Tank):
    def __init__(self, left, top):
        # 图片数据
        images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }
        # 方向随机
        # direction_list = ['U', 'D', 'L', 'R']
        # direction_index = random.randint(0, 3)
        # direction = direction_list[direction_index]
        direction = EnemyTank.__get_random_direction()
        # 设置移动速度随机
        speed = random.randint(3, 6)
        # 调用父类的初始化方法, 将数据传入到父类中实现数据的初始化
        super().__init__(left, top, images, direction, speed)
        # 给敌方坦克增加'step'数据属性
        self.step = 50

    # 子类的move方法与父类的move方法不一致, 实现随机移动
    def move(self):
        if self.step <= 0:
            # 随机切换方向, 尽量不要相同功能出现两次
            # direction_list = ['U', 'D', 'L', 'R']
            # direction_index = random.randint(0, 3)
            # direction = direction_list[direction_index]
            self.direction = EnemyTank.__get_random_direction()
            # 让移动步数复原
            self.step = 50
        else:
            # 敌方坦克可以移动, 父类方法已经实现了移动方法
            super().move()
            # 让移动步数递减
            self.step -= 1
    # 定义一个私有方法, 本类内部自己使用, 不让其它类调用.(双下划线开头)
    @staticmethod
    def __get_random_direction():
        direction_list = ['U', 'D', 'L', 'R']
        direction_index = random.randint(0, 3)
        direction = direction_list[direction_index]
        return direction

    # 检测敌方坦克是否与我方坦克发生碰撞
    def enemyTank_hit_myTank(self):
        # 直接检测
        if pygame.sprite.collide_rect(self, TankManager.my_tank):
            # 敌方与我方坦克发生了碰撞, 让敌方坦克不移动
            self.rect.left = self.oldLeft
            self.rect.top = self.oldTop



# 定义一个子弹类
class Bullet(Sprite):
    # 初始化数据
    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load('img/enemymissile.gif')
        # 坦克方向决定子弹方向, 坦克坐标决定子弹坐标
        self.direction = tank.direction
        # 根据图片对象获取rect区域对象
        self.rect = self.image.get_rect()
        # 子弹的坐标(left, top) direction
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.height / 2
        # 设置子弹的速度
        self.speed = 8
        # 设置子弹状态(默认状态为存活)
        self.live = True

    # 子弹的移动方法
    def move(self):
        # 子弹的移动也是根据方向实现的
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 子弹碰到了边界, 需要修改子弹的状态
                self.live = False
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < TankManager.height:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left + self.rect.width < TankManager.width:
                self.rect.left += self.speed
            else:
                self.live = False
    # 展示子弹
    def display_bullet(self):
        # 将子弹图片加载到主窗口中
        TankManager.main_window.blit(self.image, self.rect)


if __name__ == '__main__':
    # 游戏测试入口
    TankManager.show_menu()


# 如何控制坦克的移动速度呢?
# 使用speed不合理
# 屏幕的帧率控制 fps = frames per second
# 视频中每次展示的静态图像称为帧
# tick 摇摆, 钟摆
