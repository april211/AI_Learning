alien = {'color' : "green", 'speed' : 'slow'}

point_value = alien.get('points', 'No point value assigned.')
print(point_value)

"""
指定的键，指定的键不存在时返回的一个默认值
如果第二个参数未指定，而指定的键又不存在，将返回 None
如果指定的键有可能不存在，应该考虑使用方法 get()
"""

# https://github.com/swaroopch/byte-of-python
