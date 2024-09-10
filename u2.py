from greenroad import ConnectHandler

with open('iplist.txt') as f:
    for ips in f.readlines():
        ip = ips.strip()
        connection_info = {
                'device_type': 'huawei',
                'ip': ip,
                'username': 'huangyangxu',
                'password': 'Huawei12#$',
        }
        with ConnectHandler(**connection_info) as conn:
            print (f'已经成功登陆交换机{ip}')
            output = conn.send_command('display current-configuration interface LoopBack')
            print(output)