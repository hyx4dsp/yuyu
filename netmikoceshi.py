from netmiko import ConnectHandler

with open('iplist.txt') as f:
    for ips in f.readlines():
        ip = ips.strip()
        connection_info = {
                'device_type': 'hp_comware',
                'ip': ip,
                'username': 'huangyangxu',
                'password': 'Huawei12#$',
        }
        with ConnectHandler(**connection_info) as conn:
            print (f'已经成功登陆交换机{ip}')
            output = conn.send_config_from_file('config.txt')
            print(output)
            save = conn.save_config()
            print(save)