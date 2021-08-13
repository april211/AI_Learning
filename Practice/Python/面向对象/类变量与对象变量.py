# coding=UTF-8

class Robot:
    """表示有一个带有名字的机器人"""

    # 一个类变量，用来计数机器人的数量
    population = 0

    # 定义初始化函数
    def __init__(self, name):
        """初始化数据"""

        # 通过 self 分配对象变量
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人
        # 将会增加人口数量
        Robot.population += 1   # OR: self.__class__.population
    # 结束

    # 定义对象方法（默认）
    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))
    # 结束

    # 定义对象方法
    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到"""
        print("Greetings, my masters call me {}.".format(self.name))
    # 结束

    # 定义类方法，使用 `cls` 作为参数。需要使用装饰器（Decorator）额外进行标识：@classmethod（对应类变量）
    # 等价于：how_many = classmethod(how_many)
    @classmethod
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))
    # 结束
# 结束：Robot类的定义


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()


# 注意：当一个对象变量与一个类变量名称相同时，类变量将会被隐藏。
# `how_many` 实际上是一个属于类而非属于对象的方法。这就意味着我们可以将它定义为一个 `classmethod（类方法）` 或是一个 `staticmethod（静态方法）`，这取决于我们是否需要知道这一方法属于哪个类。由于我们已经引用了一个类变量，因此我们使用 `classmethod（类方法）`。

""" 所有的类成员都是公开的。但有一个例外：如果你使用数据成员并在其名字中_使用双下划线作为前缀_，形成诸如 `__privatevar` 这样的形式，Python 会使用名称调整（Name-mangling）来使其有效地成为一个私有变量。

因此，你需要遵循这样的约定：任何在类或对象之中使用的变量其命名应以下划线开头，其它所有非此格式的名称都将是公开的，并可以为其它任何类或对象所使用。请记得这只是一个约定，Python 并不强制如此（除了双下划线前缀这点）。 """


# https://github.com/swaroopch/byte-of-python
