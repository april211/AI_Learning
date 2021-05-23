import matplotlib.pyplot as plt
import numpy as np
import datetime
from matplotlib.dates import DayLocator, DateFormatter


x = [datetime.date.today() + datetime.timedelta(i) for i in range(30)]      # 从今天开始，接下来大的30天
y = np.sin(np.arange(30))

plt.figure(figsize=(12,6))
plt.plot(x, y)

# 设置X轴的时间间隔，MinuteLocator、HourLocator、DayLocator、WeekdayLocator、MonthLocator、YearLocator
# gca: Get Current Axes
plt.gca().xaxis.set_major_locator(DayLocator(interval=3))                   # 设置时间间隔为 3天，所以共有 10个标签

# 设置X轴的时间显示格式
plt.gca().xaxis.set_major_formatter(DateFormatter('%y/%m/%d'))

# 自动旋转X轴的刻度，适应坐标轴
# gcf: Get Current Figure
plt.gcf().autofmt_xdate()

plt.show()


# https://blog.csdn.net/Dontla/article/details/98327176
# https://blog.csdn.net/cmzsteven/article/details/64906245
