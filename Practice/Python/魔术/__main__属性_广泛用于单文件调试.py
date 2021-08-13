
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')

""" 每一个 Python 模块都定义了它的 `__name__` 属性。如果它与 `__main__` 属性相同则代表这一模块是由用户独立运行的，因此我们便可以采取适当的行动。 """
