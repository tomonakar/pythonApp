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
