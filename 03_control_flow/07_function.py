# -------------------------------------------------- #
# 関数定義
# -------------------------------------------------- #
def say_something():
    print('hi')


say_something()


def say_anything():
    return 'come on'


get_result = say_anything()
print(get_result)


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green tea'
    else:
        return 'this is something'


get_result2 = what_is_this('red')
print(get_result2)

# -------------------------------------------------- #
# 関数の引数と返り値の宣言
# -------------------------------------------------- #


# 引数に型を宣言できる。また->intで返り値の型を宣言している
def add_num(a: int, b: int) -> int:
    return a + b


# 型を無視して関数を使うと、動的に型変換をしてくれる
print(add_num('a', 'b'))

# -------------------------------------------------- #
# 位置引数とキーワード引数とデフォルト引数
# -------------------------------------------------- #


def menu(entree, drink, dessert):
    print('entree =', entree)
    print('drink = ', drink)
    print('dessert =', dessert)


# 位置引数
menu('肉', 'ジュース', 'ケーキ')

# キーワード引数
menu(entree='beef', dessert='ice', drink='beer')


# デフォルト引数
def second_menu(entree='鳥肉', dessert='モンブラン', drink='ジンジャーエール'):
    print('entree =', entree)
    print('drink = ', drink)
    print('dessert =', dessert)


second_menu()

# -------------------------------------------------- #
# デフォルト引数で気をつけること
# -------------------------------------------------- #


# pythonではリストを引数で渡すべきではない。（参照渡しなのでバグの温床になる）
def test_func(x, ll=[]):
    ll.append(x)
    return ll


# 値を毎回作っていればバグにはならない
y = [1, 2, 3]
r = test_func(100, y)
print(r)

y = [1, 2, 3]
rr = test_func(200, y)
print(rr)

# 以下の例だとバグに繋がる
rrr = test_func(100)
print(rrr)

rrrr = test_func(100)
print(rrrr)


# 空のリストを引数に使いたい場合はNoneを利用する
def test_func2(x, li=None):
    if li is None:
        li = []
    li.append(x)
    return li


print(test_func2(100))

res2 = test_func2(100)
print(res2)

# -------------------------------------------------- #
# 位置引数のタプル化
# -------------------------------------------------- #


# 引数の前にアスタリスクを置くと、全ての引数をタプルに入れて受け取ることができる
def taple_test(*args):
    print(args)


taple_test('aaa', 'bbb', 'ccc')


# ひとつずつ引数を扱いたい場合は以下のようにする
def say_something(word, *args):
    print('word', word)
    for arg in args:
        print(arg)


say_something('Hi!', 'Mike', 'Nancy')

# -------------------------------------------------- #
# キーワード引数の辞書化
# -------------------------------------------------- #


# アスタリスクを引数の前に２つつけることで、キーワード引数を辞書型データで受け取ることができる
def menu_test(**kwargs):
    print(kwargs)


menu_test(entree='beef', drink='coffee')


# 以下のように使える
def menu_test2(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


menu_test2(entree='beef', drink='coffee')

d = {'entree': 'beef', 'drink': 'ice coffee', 'dessert': 'ice'}

# 上記で作成した辞書型の変数を **d で引数にセットすると、展開されてキーワード引数の形で渡される
# 渡された後にまた辞書化されるので、コードの見やすさを意識してこのような書き方はよく行われる。
menu_test2(**d)


# 位置引数、タプル化、辞書化引数を全て渡すことも可能。ただし、引数を設置する順序はタプル化の後に辞書化にする必要がある
def menu_test3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu_test3('banana', 'apple', 'orange', entree='beef', drink='coffee')

# -------------------------------------------------- #
# Docstrings
# -------------------------------------------------- #


# pythonの関数のドキュメントは、関数宣言の後に記述する
def example_func(param1, param2):
    """Example function with types documented in the docstrings.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success. False otherwise.
    """
    print(param1)
    print(param2)
    return True


# 関数ないに記述したドキュメントは以下のように出力できる
print(example_func.__doc__)
help(example_func)
