s = 'My name is Mike. Hi Mike.'
print(s)

# 文字列の始まりをチェックしboolで返す
is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('x')
print(is_start)

# 引数で指定した文字列が最初に登場するのは、前から何番目かをカウント
print(s.find('Mike'))

# 引数で指定した文字列が最後に登場するのは、前から何番目かをカウント
print(s.rfind('Mike'))

# 引数で指定した文字列が何回登場するかカウント
print(s.count('Mike'))

# 最初の文字以外を小文字にする
print(s.capitalize())

# 単語の始まりを大文字にする
print(s.title())

# 全て大文字にする
print(s.upper())

# 全て小文字にする
print(s.lower())

# 文字列の置換
print(s.replace('Mike', 'Nancy'))
