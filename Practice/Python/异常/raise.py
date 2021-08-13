# encoding=UTF-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
# end

least = 3
try:
    text = input('Enter something --> ')
    # 若字符串太短，则抛出异常
    if len(text) < least:
        raise ShortInputException(len(text), least)
    # 其他工作能在此处继续正常运行
except EOFError:
    print('Why did you do an EOF on me?!')
except ShortInputException as ex:   # 将该类存储 `as（为）` 相应的错误名或异常名
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

# https://github.com/swaroopch/byte-of-python
