s_1 = input()
s_2 = input()
flag = 0
for i in s_1:
     if i not in s_2:
        flag = 1
if flag == 0:
    print("OK")
else:
    print("KO")
