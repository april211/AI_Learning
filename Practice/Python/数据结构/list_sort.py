# coding=utf-8

# 获取列表中每个坐标（元组）的第二个元素
def takeSecond(elem):
    return elem[1]
 
# 包含若干二维坐标的列表
coordinate_list = [(2, 2), (3, 4), (4, 1), (1, 3)]
 
# 指定按照第二个坐标值进行排序（默认为升序）
coordinate_list.sort(key=takeSecond, reverse=False)
 
# 输出排序后的坐标列表
print ('排序列表：', coordinate_list)

# https://github.com/swaroopch/byte-of-python
