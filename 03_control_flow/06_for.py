some_list = [1, 2, 3, 4, 5]

# whileで書く場合
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1

# for ループで書く場合
for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'mike']:
    print(word)

for word in ['My', 'name', 'is', 'mike']:
    if word == 'name':
        break
    print(word)

for word in ['My', 'name', 'is', 'mike']:
    if word == 'name':
        continue
    print(word)

for fruit in ['apple', 'banana', 'orange']:
    # if fruit == 'banana'
    #     print('stop eating')
    #     break
    print(fruit)
else:
    print('I ate all')

# -------------------------------------------- #
# range
# -------------------------------------------- #

for i in range(2, 10, 3):
    print(i)

for i in range(10):
    print(i, 'hello')

for _ in range(10):
    print('hello')

# -------------------------------------------- #
# enumerate
# -------------------------------------------- #

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)
