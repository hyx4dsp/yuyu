import yaml
from pprint import pprint
f = open('info.yaml')
temp = yaml.safe_load(f)
print(temp)
print('\n')
pprint(temp)
