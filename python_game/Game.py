import pygame


class Game():
    def __init__(self, background_image_path, size=(480, 700), title='飞机大战', font_name='方正舒体', font_size=30, speed=2000):
        '''
        :param background_image_path: 背景图片的路径地址
        :param size: 游戏窗口的大小
        :param title: 游戏窗口的标题
        :param font_name: 指定字体
        :param font_size: 指定字体大小
        :param speed: 背景图滚动整个窗口一次所用时间，单位为ms
        '''
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.title = title
        self.background_image_path = background_image_path
        self.background = pygame.image.load(self.background_image_path).convert()
        # 设置字体对象，得到系统中自带的字体
        self.font = pygame.font.SysFont(font_name, font_size)
        # 得到Clock对象，我们可以使用它来获取距离上次绘制图像的时间
        self.clock = pygame.time.Clock()
        # 背景图初始位置
        self.height = 0
        # 使用窗口的高度处于滚动的时间，就能得到每ms滚动的距离
        self.every_ms_move_distance = self.size[1] / speed   # 2秒
        # 分数
        self.score = 0
        # 存放所有的敌机
        self.enemies = []


    def show_score(self):
        '''
        显示分数, 在窗口的的最上方距离上边距10px， 左右居中
        '''
        pass


    def set_time_passed(self):
        # 控制画 的帧， 越大越快
        # 得到上一次绘制图像到到现在的时间, ms
        self.time_passed = self.clock.tick()


    def draw_background(self):
        '''
        绘制背景图片，一直向下滚动，营造飞机一直往上面飞的感觉
        '''
        # 每次移动的距离 = 每ms移动的距离 * 上次到现在的时间（ms）
        pass


    def create_enemy(self, image_path=os.path.join(source_dir,'enemy1.png'), enemy_number=5):
        '''
        创建敌机
        :param image_path: 敌机的图片地址
        :param enemy_number: 最多有几个敌机在屏幕上
        '''
        pass


    def draw_enemies(self, time_passed, screen):
        '''
        绘制敌机到屏幕上，清理跑出窗口的敌机，
        :param time_passed: 上次绘制导向现在经过的时间
        :param screen: 绘制的窗口对象
        '''
        pass


    def bullet_and_enemy_crash_detection(self, bullets):
        '''
        检测子弹是否击中敌机
        :param bullets: 飞机的所有子弹
        '''
        pass


    def plan_and_enemy_crash_detection(self, plan, allow_crash_size=None):
        '''
        检测敌机与飞机是否相撞
        :param plan: 飞机对象
        :param allow_crash_size: 允许飞机碰撞的大小，只有左右有效
        '''
        pass


    def draw_plan(self, plan, time_passed):
        '''
        绘制飞机
        :param plan: 飞机对象
        :param time_passed: 距离上次绘制的时间
        :return:
        '''
        pass


    def game_over(self):
        '''
        游戏结束
        '''
        while True:
            # 绘制背景图
            pass


    def run(self):
        '''
        游戏入口函数，开始函数，主体函数
        :return:
        '''

        # 设置游戏窗口的大小
        pygame.display.set_caption(self.title)
        # 初始化一个飞机对象
        plan = Plan()

        while True:
            # 如果飞机自毁完成, 游戏结束, 调用game_over函数
            pass

            # 检测监听事件
            pass

            # 检测上下左右的移动案件.
            # w,a,s,d 和 上,下,左,右键都可以
            # 然后执行plan.update函数，改变飞机的位置
            pass

            # 子弹和敌机的碰撞检测
            self.bullet_and_enemy_crash_detection(plan.bullets)
            # 飞机与敌机的碰撞检测
            self.plan_and_enemy_crash_detection(plan)
            # 设置属性time_passed的值， 距离上次的时间，方便后面使用
            self.set_time_passed()
            # 绘制背景图片
            self.draw_background()
            # 显示分数
            self.show_score()
            # 生成敌机
            self.create_enemy()
            # 绘制敌机
            self.draw_enemies(time_passed=self.time_passed, screen=self.screen)
            # 绘制飞机
            self.draw_plan(plan=plan, time_passed=self.time_passed)
            # 绘制子弹
            plan.draw_bullets(time_passed=self.time_passed, screen=self.screen)
            # 显示我们的图像
            pygame.display.update()

