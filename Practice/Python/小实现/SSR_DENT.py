# 将以逗号 `,` 分隔的 SSR 链接转换成以换行分隔，并直接在终端输出

# 目标文件位置
source = r"C:\Users\lenovo\Desktop\fast_ts1.txt"

# 打开文件
f = open(source, 'r', encoding="UTF-8")
lines = f.readlines()

# 关闭文件
f.close()

# 将 List 转换为 Str
text = ''.join(lines)

# 按照逗号拆分成列表元素
anslist = list(text.split(','))

# 输出链接列表
for ssr in anslist:
    print(ssr, end='\n')
