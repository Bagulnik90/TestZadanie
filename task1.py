num = int(input())
base = int(input("Base (2-9): "))
if not(2 <= base <= 9):
    quit()

newNum = ''

while num > 0:
    newNum = str(num % base) + newNum
    num //= base

print(newNum)

from random import random

N = 255
a = [0]*N
summa = 0
for i in range(N):
    a[i] = int(random()*20)
    print('%3d' % a[i], end='')
    b = a[i]
    while b > 0:
        summa += b % 10
        b //= 10
print()
print(summa)
