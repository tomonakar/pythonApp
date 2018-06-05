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
