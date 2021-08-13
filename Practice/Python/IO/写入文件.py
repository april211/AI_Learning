filename = '2021_03/programming.txt'

with open(filename, 'w') as file_object:    # 写入模式，清空原文件内容
    file_object.write("I love programming!\n")
    file_object.write("I love creating new games!\n")

with open(filename, 'a') as file_object:    # 附加模式，附加到末尾或创建新文件（当目标文件不存在时）
    file_object.write("I love creating apps that can run in a browser!\n")
    file_object.write("I also love finding meaning in large datasets!\n")
