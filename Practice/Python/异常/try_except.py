try:    # 无条件执行
    text = input('Enter something --> ')
except EOFError:            # 通常是 ctrl + z
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:   # 通常是 ctrl + c
    print('You cancelled the operation.')
else:   # 无异常时
    print('You entered {}'.format(text))
