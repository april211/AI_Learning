from decimal import Decimal

# 四舍五入保留一位小数
a = 1.26
print(round(a, 1))   
print('%.1lf' % a)    
print(Decimal('5.009').quantize(Decimal('0.00')))

# 精确计算 参考：https://blog.csdn.net/weixin_37989267/article/details/79473706
