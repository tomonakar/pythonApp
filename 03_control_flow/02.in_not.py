y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# 数字の比較をする場合は非推奨
if not a == b:
    print('Not equal')

if a != b:
    print('Not eqal')

if not a > b:
    print('Not equal')

is_ok = True

# booleanの判定でnotを使うことが多い
if is_ok:
    print('hello')

if not is_ok:
    print('hello hello')

# -------------------------------------------------- #
# 値が入っているかどうかを判定するTips
# -------------------------------------------------- #

# is_ok = True
# 1 は Trueとなる
is_ok = 1
# 0 は Falseとなる（0, 0.0, '', (), [] これらすべてFalse
is_ok = 0
# 値が入っていればTrueとなる
is_ok = 'dsafjalsdfjk'

# JSだと変数に値が入っているかどうかを hoge.length > 0 などで判定するが
# python だとシンプルに判定できる
if is_ok:
    print('OK')
else:
    print('No')
