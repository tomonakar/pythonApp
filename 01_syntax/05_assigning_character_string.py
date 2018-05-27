# ----------------------- #
# 文字列の代入
# ----------------------- #

# formatメソッドでブラケットに文字列を代入出来る
hoge = 'a is {}'.format('a')
print(hoge)

# ブラケットは複数書ける. ちなみに、引数で渡した数字は、文字列に型変換されて出力される
fuga = 'a is {} {} {}'.format(1, 2, 3)
print(fuga)

# ブラケットには引数のインデックスを紐づけることができる
foo = 'a is {0} {1} {2}'.format(1, 2, 3)
print(foo)

# インデックスを逆から指定すると、引数を逆順に表示してくれる
bar = 'a is {2} {1} {0}'.format(1, 2, 3)
print(bar)

hogehoge = 'My name is {0} {1}'.format('tomo', 'naka')
print(hogehoge)

# ブラケットに変数を指定し、formatの引数に変数を初期値を与えて渡すことができる
fugafuga = 'My name is {name} {family}'.format(name='tomo', family='naka')
print(fugafuga)

# strで文字列に変換
x = str(1)
print(type(x))
