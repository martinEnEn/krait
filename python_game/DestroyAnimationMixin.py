# 显示飞机自毁动画的Mixin类, 可用于飞机和敌机的自毁动画显示
class DestroyAnimationMixin():

    def show_destroy_animation(self, time_passed, destroy_time=200):
        '''
        显示自毁动画
        动画其实就是几张图片切换的比较快，我们的眼睛识别不出来，所以认为他是动态的，也就是动画
        :param time_passed: 距离上次绘制图像到现在的时间，单位ms
        :param destroy_time: 自毁动画总共显示时间，单位ms
        '''

        # 因为我们的自毁图片有四张，需要依次显示，首先动画的效果
        # self.destroy_image_position 表示第几章自毁图片，从零开始
        # 如果大于等于4了，说明自毁动画显示完成，设置self.destroyed变量为True, 方便别处调用
        if self.destroy_image_position >= 4:
            self.destroyed = True
            return

        # 依次加载自毁图片
        if self.time_passed >= destroy_time / 4:
            self.image = pygame.image.load(os.path.join(source_dir, self.destroy_images[self.destroy_image_position])).convert_alpha()
            self.destroy_image_position += 1
            self.time_passed = 0
        else:
            self.time_passed += time_passed