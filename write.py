import json
a='{"age":"12"}'
dict=json.loads(a)
print(dict)

dict={
    456:'456',
    123:10,
    "abc":678
    }
print(dict)
print(type(dict))
dict1=json.dumps(dict)
print(dict1)
print(type(dict1))