# ------------------- #
# 文字列の出力
# ------------------- #

print('hi', 'mike')
print('hi', 'mike', sep=',')
print('hi', 'mike', sep='\n')
print("I don't know")
print('I don\'nt know')
print('say "I don\'nt know"')
print("say \"I don\'nt know\"")

print('hello. \nHow are you?')

# ------------------- #
# 複数行で表示
# ------------------- #
print("############")
print("""
line1
line2
line3
""")
print("############")

# ------------------- #
# 改行を除去
# ------------------- #
print("############")
print("""\
line1
line2
line3\
""")
print("############")

print('hi.' * 3 + 'Mike.')

print('Py' 'thon')

prefix = 'Py'
print(prefix + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaa' 'bbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

v = 'aaaaaaaaaaaaaa'\
    'bbbbbbbbbbbbbb'

print(v)

# ------------------------- #
# 文字列のインデックス
# ------------------------- #
word = 'python'
print(word[0])
print(word[1])
print(word[-1])

# ------------------------- #
# 文字列のスライス
# ------------------------- #
print(word[0:2])
print(word[2:5])

# スライスの省略
# 0から２まで
print(word[:2])

# 2から最後まで
print(word[2:])

# 無いインデックスを指定するとエラーになる
#print(word[100])

# 文字の置き換えを行う場合は以下だとエラーになる
#word[0] = 'j'

# 以下のように置き換えたい文字を代入後、文字列をコピーして置き換えてやる
word = 'j' + word[1:]
print(word)

# インデックスの最初と最後を指定すると全てのインデックスのコピーとなる
print(word[:])

# 文字数のカウント
n = len(word)
print(n)
