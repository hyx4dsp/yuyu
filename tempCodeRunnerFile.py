port=input('具体端口号输入')
port=int(port)
while port < 24:
    if port == 10:
        print('10号端口')
        break
    if port % 2 ==0:
        print(f'偶数端口号{port}')
        port += 1
        print(f'奇数号端口{port}正在检查')
        continue
    port += 1
    print(f'不匹配条件端口号{port}')
    print(port)
print('中断测试')