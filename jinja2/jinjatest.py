import csv
from jinja2 import Template
f = open("switch.csv")
jinjafile = open("interface.j2")
interface_template = Template(jinjafile.read(), keep_trailing_newline=True)

interface_configs = ''
dict = csv.DictReader(f)
for i in dict:
    print(i)
    interface_config = interface_template.render(
    interface = i['interface'],
    vlan = i['vlan'],
    trunkvlan = i['trunkvlan'],
    )
    interface_configs = interface_configs + interface_config
print(interface_configs)

  
