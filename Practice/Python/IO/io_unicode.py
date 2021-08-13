# encoding=utf-8

import io

# 使用 `io.open` 并提供了 “编码（Encoding）” 与 “解码（Decoding）” 参数来告诉 Python 我们正在使用 Unicode
# wt模式下，python写文件时会用\r\n来表示换行
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"神秘的帅哥")        # Imagine non-English language here
f.close()

# rt模式下，python在读取文本时会自动把\r\n转换成\n
text = io.open("abc.txt", "rt", encoding="utf-8").read()
print(text)


""" 每当我们诸如上面那番使用 Unicode 字面量编写一款程序时，我们必须确保 Python 程序已经被告知我们使用的是 UTF-8，
因此我们必须将 `# encoding=utf-8` 这一注释放置在我们程序的顶端。 """

# https://github.com/swaroopch/byte-of-python
