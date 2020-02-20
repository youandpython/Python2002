import json


dic = {1:'abc', 2:'def', 3: 'deg'}

dj = json.dumps(dic)
ds = str(dic)
print(dic)
print(dj)
print(ds)
js = json.loads(dj)
print(js)