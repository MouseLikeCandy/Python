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
Pycharm 忽略大小写提示  code Completion代码补全  Macth case 去掉勾选
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
    # 定义一个存储敌方坦克的子弹列表
    enemyTank_bullet_list = []
    # 定义一个存储爆炸效果的列表
    explode_list = []
    # 定义一个存储墙壁的列表
    wall_list = []

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
        # 播放音乐
        Music.play_music('img/start.wav')
        # 创建敌方坦克(5)
        for i in range(1, 6, 1):
            enemy_tank = EnemyTank(i * 130, 10)
            # 将创建的敌方坦克添加到敌方坦克列表中
            TankManager.enemy_tank_list.append(enemy_tank)

        # 创建墙壁列表
        for i in range(6):
            # 初始化墙壁
            wall = Wall(i * 148, 220)
            # 将创建的wall对象添加到墙壁列表中
            TankManager.wall_list.append(wall)

        # 4. 保证窗口不退出
        while True:
            # 5. 设置主窗口的填充色
            TankManager.main_window.fill(pygame.Color('black'))

            # 绘制窗口左上角文字
            TankManager.font.render_to(TankManager.main_window, (10, 10),
                                       f'剩余敌方坦克数量: {len(TankManager.enemy_tank_list)}', fgcolor='red', size=30)

            # 判断我方坦克是否为存活状态
            if TankManager.my_tank and TankManager.my_tank.live:
                # 存活, 刷新我方坦克
                TankManager.my_tank.display_tank()
            else:
                # 消亡状态, 需要删除掉我方坦克对象
                del TankManager.my_tank
                # 将我方坦克置空(保险起见)
                TankManager.my_tank = None  # 空对象, 不能调用任何数据与方法

            # 判断my_tank 不为None, 为存活状态
            if TankManager.my_tank and TankManager.my_tank.live:
                # 判断我方坦克的移动开关状态
                # if TankManager.my_tank.stop == False:   # 不要停一直移动
                if not TankManager.my_tank.stop:  # None.stop
                    # 调用move方法
                    TankManager.my_tank.move()
                    # 检测我方坦克是否与墙壁发生碰撞
                    TankManager.my_tank.tank_hit_wall()
                    # 检测我方坦克是否与敌方坦克发生碰撞
                    TankManager.my_tank.myTank_hit_enemyTank()

            # 刷新敌方坦克
            for enemy_tank in TankManager.enemy_tank_list:
                # 首先判断敌方坦克的状态是否为存活状态
                if enemy_tank.live:
                    # 调用Tank类的display_tank 方法
                    enemy_tank.display_tank()
                    # 让敌方坦克实现移动
                    enemy_tank.move()
                    # 检测敌方坦克是否与墙壁发生碰撞
                    enemy_tank.tank_hit_wall()
                    # 检测敌方坦克是否与我方坦克发生碰撞
                    enemy_tank.enemyTank_hit_myTank()
                    # 实现敌方坦克随机发射子弹, shoot_bullet仅有5%的概率返回子弹对象
                    enemy_bullet = enemy_tank.shoot_bullet()
                    # 判断 enemy_bullet 是否有返回结果
                    if enemy_bullet:
                        # 有返回结果, 将子弹对象添加到敌方坦克的子弹列表中
                        TankManager.enemyTank_bullet_list.append(enemy_bullet)
                    # else:
                    #     # 没有返回结果
                else:
                    # 敌方坦克消亡
                    TankManager.enemy_tank_list.remove(enemy_tank)

            # 刷新我方坦克的子弹列表
            for my_Bullet in TankManager.myTank_bullet_list:
                # 判断我方坦克的子弹状态
                if my_Bullet.live:
                    # 存活状态, 需要展示子弹
                    my_Bullet.display_bullet()
                    # 调用子弹的移动方法
                    my_Bullet.move()
                    # 检测我方子弹是否碰撞了墙壁
                    my_Bullet.bullet_hit_wall()
                    # 检测我方子弹是否碰撞了敌方坦克
                    my_Bullet.myBullet_hit_enemyTank()
                else:
                    # 消亡状态, 需要将子弹从子弹列表中移除
                    TankManager.myTank_bullet_list.remove(my_Bullet)

            # 刷新敌方坦克的子弹列表
            for enemy_bullet in TankManager.enemyTank_bullet_list:
                # 判断敌方子弹是否为存活状态
                if enemy_bullet.live:
                    # 存活状态, 展示子弹, 移动子弹
                    enemy_bullet.display_bullet()
                    enemy_bullet.move()
                    # 检测敌方子弹是否碰撞到了墙壁
                    enemy_bullet.bullet_hit_wall()
                    # 检测敌方子弹是否碰撞到了我方坦克
                    enemy_bullet.enemyBullet_hit_myTank()
                else:
                    # 消亡状态
                    TankManager.enemyTank_bullet_list.remove(enemy_bullet)

            # 刷新爆炸效果的列表
            for explode in TankManager.explode_list:
                # 首先判断爆炸效果的存活状态
                if explode.live:
                    # 展示爆炸效果
                    explode.display_explode()
                else:
                    # 爆炸效果播放完毕了, 需要将当前爆炸对象从爆炸列表中删除
                    TankManager.explode_list.remove(explode)

            # 刷新墙壁列表
            for wall in TankManager.wall_list:
                # 判断wall对象是否为存活状态
                if wall.live:
                    # 存活展示
                    wall.display_wall()
                else:
                    # 消亡
                    TankManager.wall_list.remove(wall)

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
                    '''我方坦克无限重生方案二'''
                    # 首先判断ESC键
                    if event.key == pygame.K_ESCAPE:
                        if not TankManager.my_tank:
                            # 我方坦克不存在,就创建
                            TankManager.my_tank = MyTank(350, 300)
                            # 播放音乐
                            Music.play_music('img/start.wav')
                    # 判断my_tank是否不为None, 并且为存活状态
                    if TankManager.my_tank and TankManager.my_tank.live:
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
                                # 播放音乐
                                Music.play_music('img/hit.wav')
                    '''
                    # 我方坦克无限重生方案一
                    elif event.key == pygame.K_ESCAPE:
                        # 创建我方坦克
                        if not TankManager.my_tank:
                            # 说明我方坦克不存在
                            TankManager.my_tank = MyTank(350, 300)
                    '''
                # 键盘松开事件
                elif event.type == pygame.KEYUP:
                    # 判断my_tank是否不为None, 并且为存活状态
                    if TankManager.my_tank and TankManager.my_tank.live:
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
        # 新增一个数据, 表示坦克的存活状态(默认为存活状态)
        self.live = True

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

    # 检测坦克是否与墙壁发生碰撞
    def tank_hit_wall(self):
        # 不是一堵墙, 遍历墙壁列表
        for wall in TankManager.wall_list:
            # 判断坦克是否与墙壁发生碰撞
            if pygame.sprite.collide_rect(self, wall):
                # 发生了碰撞, 坦克原地不动, 坐标不变
                self.rect.left = self.oldLeft
                self.rect.top = self.oldTop


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
        # 判断my_tank 不为None, 为存活状态
        if TankManager.my_tank and TankManager.my_tank.live:
            # 直接检测
            if pygame.sprite.collide_rect(self, TankManager.my_tank):
                # 敌方与我方坦克发生了碰撞, 让敌方坦克不移动
                self.rect.left = self.oldLeft
                self.rect.top = self.oldTop

    # 敌方坦克实现随机发射子弹, 5%概率有返回值
    def shoot_bullet(self):
        # 随机产生1~100之间的随机整数
        num = random.randint(1, 100)
        # 范围判断 5%的概率
        if num <= 5:
            # 创建一颗子弹, 并返回
            # self 是敌方坦克
            return Bullet(self)


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

    # 检测我方子弹与敌方坦克发生了碰撞
    def myBullet_hit_enemyTank(self):
        # 遍历敌方坦克的列表
        for enemy_tank in TankManager.enemy_tank_list:
            if pygame.sprite.collide_rect(self, enemy_tank):
                # 条件成立, 说明我方子弹碰撞到敌方坦克, 需要将我方子弹和敌方坦克的状态修改为消亡状态.
                self.live = False
                enemy_tank.live = False
                # 创建爆炸效果对象
                explode = Explode(enemy_tank)
                # 将爆炸效果对象添加到爆炸效果列表中
                TankManager.explode_list.append(explode)

    # 检测敌方子弹是否碰撞了我方坦克
    def enemyBullet_hit_myTank(self):
        # 判断my_tank 不为None, 为存活状态
        if TankManager.my_tank and TankManager.my_tank.live:
            # 直接检测
            if pygame.sprite.collide_rect(self, TankManager.my_tank):
                # 碰撞到了, 需要将敌方子弹和我方坦克设置为消亡状态
                self.live = False
                TankManager.my_tank.live = False
                # 创建爆炸效果
                explode = Explode(TankManager.my_tank)
                TankManager.explode_list.append(explode)

    # 检测子弹是否与墙壁发生了碰撞
    def bullet_hit_wall(self):
        # 遍历墙壁列表
        for wall in TankManager.wall_list:
            if pygame.sprite.collide_rect(self, wall):
                # 发生碰撞, 修改子弹状态
                self.live = False
                # 修改墙壁生命值
                wall.life -= 1
                # 判断墙壁的生命值
                if wall.life <= 0:
                    # 修改墙壁的状态
                    wall.live = False


# 定义一个爆炸类
class Explode(object):
    # 初始化方法
    def __init__(self, tank):
        # 爆炸效果的位置由当前子弹打中的坦克位置来决定的
        self.rect = tank.rect
        # 爆炸效果的图片加载(注意: 此处是列表, 不是子弹)
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif'),
        ]
        # 播放的步骤
        self.step = 0
        # 根据步骤获取对应的图片
        self.image = self.images[self.step]
        # 记录爆炸效果的展示状态, 默认为展示状态
        self.live = True

    # 展示爆炸效果
    def display_explode(self):
        if self.step < len(self.images):
            # 播放
            self.image = self.images[self.step]
            self.step += 1
            # 将图片展示到主窗口中
            TankManager.main_window.blit(self.image, self.rect)
        else:
            # 播放完毕了, 修改爆炸效果的图片展示状态
            self.live = False
            self.step = 0  # 将步骤数据复位


# 定义一个墙壁类
class Wall(Sprite):
    # 初始化方法
    def __init__(self, left, top):
        # 加载墙壁
        self.image = pygame.image.load('img/steels.gif')
        # 获取区域对象
        self.rect = self.image.get_rect()
        # 设置区域对象坐标
        self.rect.left = left
        self.rect.top = top
        # 设置存活状态
        self.live = True
        # 设置墙壁的生命值
        self.life = 10

    # 展示墙壁
    def display_wall(self):
        TankManager.main_window.blit(self.image, self.rect)


# 定义一个音乐类
class Music(object):
    # 播放音乐
    @staticmethod
    def play_music(filename):
        # 1. 初始化音乐混合器对象
        pygame.mixer.init()
        # 2. 加载音乐
        pygame.mixer.music.load(filename)
        # 3. 播放音乐
        pygame.mixer.music.play()


if __name__ == '__main__':
    # 游戏测试入口
    TankManager.show_menu()

# 如何控制坦克的移动速度呢?
# 使用speed不合理
# 屏幕的帧率控制 fps = frames per second
# 视频中每次展示的静态图像称为帧
# tick 摇摆, 钟摆
