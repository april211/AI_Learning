
dict0 = {'x': 2, 'y': 3}
dict1 = {'x': 4, 'y': 1}
points = [dict0, dict1]

points.sort(key=lambda i: i['y'], reverse=False)    # 指定排序对象 && 升序（默认）
print(points)

# Output:
# [{'x': 4, 'y': 1}, {'x': 2, 'y': 3}]

# https://github.com/swaroopch/byte-of-python
