# タプル型は丸括弧で囲んだ形になっている
# 値の変更はできない
t = (1, 2, 3, 4, 1, 2)
print(type(t))

# タプル型は値を変更できない
# 下はエラーとなる
# t[0] = 100

print(t[0])
print(t[-1])
print(t[2:4])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
print(help(list))
print(help(tuple))

# タプルにリストを入れることはできる
t = ([1, 2, 3], [4, 5, 6])
print(t)

# タプルの中のリスト自体を書き換えることは値の変更と見なされて出来ない
#t[0] = [1]

# タプルの中の変数の値は変更できる
t[0][0] = 100
print(t)

# タプルの()は省略できる
t = 1, 2, 3
print(type(t))

# カンマをつけた時点でタプルになる
t = 1,
print(type(t))
print(t)

# パレンティスのカッコだけでもタプルになる
t = ()
print(type(t))
print(t)

# パレンティスの中にカンマなしで値を入れるとタプルでなくなる
t = (1)
print(type(t))
print(t)

# タプルでは値の変更は出来ないが、新しいタプルを宣言した際はタプルを足すことはできる
new_tuple = (1, 2, 3) + (4, 5, 6)
print(type(new_tuple))
print(new_tuple)

# カンマを忘れるとタプル扱いでは無くなりエラーになるから気をつける
# 以下はエラー
new_tuple = (1) + (2, 3, 4)
print(type(new_tuple))
