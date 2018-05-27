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

# ----------------------------------------------- #
# 辞書型のメソッド
# ----------------------------------------------- #
d = {'x': 10, 'y': 20}
# キーのみ取り出す
print(d.keys())

# バリューのみ取り出す
print(d.values())

d2 = {'x': 1000, 'j': 500}
print(d2)

# dをd２でアップデートする
d.update(d2)
print(d)

# key 'x'の値を取り出す
print(d['x'])
print(d.get('x'))

# 無いキーを取り出すとNoneとなる
r = d.get('z')
print(r)
print(type(r))

# popで値を取り出す
print(d.pop('x'))
print(d)

# delでキーバリューを削除
del d['y']
print(d)

# clearで中身を空にする
d = {'a': 100, 'b': 200}
d.clear()
print(d)

# キーがあるか判定
d = {'a': 100, 'b': 200}
print('a' in d)
print('c' in d)
