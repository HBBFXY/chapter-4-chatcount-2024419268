string = input("请输入一行字符串：")
spa = 0  
num = 0  
alp = 0  
oth = 0  
for char in string:
    if char.isspace():  
        spa += 1
    elif char.isdigit():  
        num += 1
    elif char.isalpha():  
        alp += 1
    else:  
        oth += 1
print("空格数量:", spa)
print("数字数量:", num)
print("英文字符数量:", alp)
print("其他字符数量:", oth)
