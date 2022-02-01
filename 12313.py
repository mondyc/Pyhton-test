import random

# 偶数和
oushuhe = 0
for i in range(101):
    if i % 2 != 0:
        oushuhe = i + oushuhe
print(oushuhe)
print(i)

print('-----------------------------------------------------------')

# he = 0
# geiqian = [1.5, 2, 2.5]
# for tian in range(1000):
#     suiji = random.randint(0, 2)
#     zcdq = geiqian[suiji]
# #    print(zcdq)
#     he = he + zcdq
# print('田应该给多少钱:',he/len(range(1000)),'万元')
# print(len(range(1000)))

print('-----------------------------------------------------------')

he = 0
geiqian = [1.5, 2, 2.5]
for tian in range(1000):
    tian1 = geiqian[random.randint(0, 2)]
    #    print(zcdq)
    he = he + tian1
print('田应该给多少钱:', he / 1000, '万元')

print('-----------------------------------------------------------')

# 猜数字游戏
initNum = 32
minNum = 1
maxNum = 100
while True:
    userNum = int(input("请输入一个%d-%d 的数字" % (minNum, maxNum)))
    if userNum == initNum:
        print("bingo!")
        break
    userAns = input("猜错了，是否继续(y/n)？")
    if userAns != 'y':
        print("玩的愉快！")
        break
    if userNum > initNum:
        maxNum = userNum
    else:
        minNum = userNum

print('-----------------------------------------------------------')

# 10内阶乘
he = 1
for tian in range(1, 11):
    he = he * tian
print('10内阶乘结果：', he)

print('10内阶乘结果：', 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10)

print('-----------------------------------------------------------')

s = 'I love you more than i can say'
for i in s:
    print(i)
