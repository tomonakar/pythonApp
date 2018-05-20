# 変数は直接代入して使える（型宣言はしなくても型を認識してくれる)
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 変数の中身を入れ替えるとその変数の型は動的に変わる
num = name
print(name, type(num))

# 明示的に型を変換することもできる
name2 = '1'
new_num = int(name2 )
print(name2, type(new_num))

# python3.6から型を宣言可能
num2: int = 1
name3: str = '1'
new_num2 = int(name3)

print(new_num2, type(new_num2))

# 変数の先頭に数字は使えない
# if などの予約文字も変数では使えない
