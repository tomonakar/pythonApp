count = 0

# -------------------------------------------------- #
# whileループの基本
# -------------------------------------------------- #
# while count < 5:
#     print(count)
#     count += 1
#

# -------------------------------------------------- #
# while True
# -------------------------------------------------- #
# while True:
#     if count >= 5:
#         break
#     print(count)
#     count += 1

# -------------------------------------------------- #
# while break と continueの違い
# -------------------------------------------------- #
# while True:
#     # break はループを抜ける
#     if count >= 5:
#         break
#
#     # continue は次の行を飛ばして次のループに移動
#     if count == 2:
#         count += 1
#         continue
#
#     print(count)
#     count += 1

# -------------------------------------------------- #
# while else は breakで抜けなければ elseで実行
# -------------------------------------------------- #
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')
