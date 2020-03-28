#条件变量是线程同步最复杂的锁, 用于复杂的线程同步
#启动顺序很重要
#只有在调用with方法之后才能调用 wait，notify方法
#不使用with方法，可以使用condition.acquire condition.release方法
#condition有2层锁，一把底层锁会在线程调用了wait方法时候释放，
#上层锁会在每次调用wait的时候分配一把并放入condition的等待队列中，等待notify方法的唤醒

# condition 是在Lock与Rlock的基础上实现的，
# semaphore 是在condition的实际上实现的

# from threading import Condition
import threading


class  XiaoAi(threading.Thread):
    def __init__(self, condition):
        self.condition = condition
        super().__init__(name='小爱')

    def run(self) -> None:
        with self.condition:
            self.condition.wait()
            print("{}:在".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{}:好啊".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{}:君住长江尾".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{}:共饮长江水".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{}:此恨何时已".format(self.name))
            self.condition.notify()
            self.condition.wait()
            print("{}:定不负相思意".format(self.name))
            self.condition.notify()

class TianMao(threading.Thread):
    def __init__(self, condition):
        self.condition = condition
        super().__init__(name='天猫精灵')

    def run(self) -> None:
        self.condition.acquire()
        print("{}:小爱同学".format(self.name))
        self.condition.notify()
        self.condition.wait()
        print("{}:我们来对古诗吧".format(self.name))
        self.condition.notify()
        self.condition.wait()
        print("{}:我住长江头".format(self.name))
        self.condition.notify()
        self.condition.wait()
        print("{}:日日思君不见君".format(self.name))
        self.condition.notify()
        self.condition.wait()
        print("{}:此水几时休".format(self.name))
        self.condition.notify()
        self.condition.wait()
        print("{}:只愿君心似我心".format(self.name))
        self.condition.notify()
        self.condition.wait()
        self.condition.release()


if __name__ == '__main__':
    condition = threading.Condition()
    xiaoai = XiaoAi(condition)
    tianmao = TianMao(condition)
    #启动顺序很重要
    #只有在调用with方法之后才能调用 wait，notify方法
    #不使用with方法，可以使用condition.acquire condition.release方法
    #condition有2层锁，一把底层锁会在线程调用了wait方法时候释放，
    #上层锁会在每次调用wait的时候分配一把并放入condition的等待队列中，等待notify方法的唤醒
    xiaoai.start()
    tianmao.start()

