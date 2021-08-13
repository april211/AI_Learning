"""简单的解决判断回文问题"""

def reverse(text):
    """倒转字符串"""
    return text[::-1]   # 使用切片功能反转字符串
# end

def is_palindrome(text):
    """检测字符串是否为回文"""
    # 建立 copy, 不改变原字符串
    copy = list(text)

    # 建立一个空列表，准备接收修正后的字符
    ans  = []

    # 保证全是字母
    for a in copy:
        if a.isalpha():
            ans.append(a)       # 尽量不在 for 里删去列表值，容易出问题

    # 清除不需要的拷贝
    copy.clear()

    # list 转 str
    t = ''.join(ans)

    # 无视大小写
    t = t.lower()

    print("经过修正后的字符串:", t)
    if t == reverse(t):
        return True
    else:
        return False
# end



something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome.")
else:
    print("No, it is NOT a palindrome.")

# https://github.com/swaroopch/byte-of-python
