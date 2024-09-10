#data='   2132323  1      '
#print(data)
#print(data.strip())

#cmd=' c:  ping 192.168.1.1'
#print(cmd.split('ping')[1])

#list=['123','a','b','cd']
#print(list[:2])
#print(range(3))
'''
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
'''

'''
a=range(1,10,2)
print(list(a))
for i in a:
    print(f'{i}')
'''
'''
port =1
while port <= 24:
    if port == 10:
        break #提前退出循环
    if port %2 == 0:
        port += 1
        continue #跳过偶数端口
    print(f"端口 {port}正在检查")
    port += 1

def welcome():
    print('欢迎使用PYTHON')


for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print (f'当前字母 :{letter}') 

var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print(f'当前变量值 :{var}')
print("Good bye!")
'''

# 接口数据

interfaces_msg = [{name: "ge0/0", "description": "manager", "status": "up"},
                  {name: "ge0/1", "description": "core01", "status": "up"},
                  {name: "ge0/2", "description": "core02", "status": "up"},
                  {name: "ge0/3", "description": "branch01", "status": "up"},
                  {name: "ge0/4", "description": "branch02", "status": "up"}]
# IP数据
ip_datas = {"interface0": 10.10.10.1,
            "interface1": 172.16.1.1,
            "interface2": 172.17.1.1,
            "interface3": 172.18.1.1,
            "interface4": 192.168.25.1}
# -------------------作业区域结束------------------------

# 命令行输出数据
for int_index in range(5):
    int_name = list(interfaces_msg[int_index].values())[0]
    int_des = list(interfaces_msg[int_index].values())[1]
    int_status = list(interfaces_msg[int_index].values())[2]
    int_ip = list(ip_datas.values())[int_index]
    print(f"{int_des} 接口 {int_name} 目前的状态是 {int_status}，其IP地址为：{int_ip}")
