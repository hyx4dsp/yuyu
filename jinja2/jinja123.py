from jinja2 import Template
temp = Template("i am {{name}} i am {{number}} years old")
print(temp.render(name="huangyangxu",number="35"))

test = open('test.j2')
str= ""
temp1 = Template(test.read(),keep_trailing_newline=True)
str = temp1.render(vlan="ss",trunkvlan="1000")
print(str)