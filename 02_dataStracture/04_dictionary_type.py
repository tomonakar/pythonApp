# -------------------------------------------- #
# 辞書型の生成
# -------------------------------------------- #

d = {'x': 10, 'y': 20}
print(type(d))
print(d)

d['x'] = 'xxxx'
print(d)

d['z'] = 200
print(d)

d[1] = 9999
print(d)

x = (dict(a=10, b=20))
print(x)

y = dict([('a', 10), ('b', 20)])
print(y)