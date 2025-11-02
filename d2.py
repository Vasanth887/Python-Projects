#  2
# from datetime import datetime
# now=datetime.now()
# print(now)

# 4
# a=input("Enter value separated by commas: ").split(",")
# print(a)
# print(tuple(a))
# # 5
# from datetime import date

# a=int(input("Enter year"))
# b=int(input("Enter mon"))
# c=int(input("Enter day"))
# date1=date(a,b,c)
# print(f"the examination start from",date1)
# n=input("")
# nn=n*2
# nnn=n*3
# print(int(n)+int(nn)+int(nnn)). 7

# 8
# from datetime import datetime,timedelta
# date1=input("dd-mm-y")
# date2=input("dd-mm-y")

# dat1=datetime.strptime(date1,"%d-%m-%Y")
# dat2=datetime.strptime(date2,"%d-%m-%Y")

# dat=abs(dat1-dat2)
# print(dat)

# 11

# a=int(input(""))
# if abs(1000-a) <=100 or abs(2000-a) <= 100:

# 13

# a=input("Enter the string: ")

# if a.startswith("is"):
#     print("hi")
# else:
#     print(f" is{a}")

# a=[4,44,4,23]
# count=0
# for i in a:
#     if i==4:
#         count+=1
# print(count) 

# 16
# a=input("").lower()
# if a in "aeiou":
#     print("hi")

# 17

# a=[1,2,8,3]
# b=int(input("s: "))
# if b in a:
#     print("hi")
# else:
#     print("bye")

# 18

# a=["hi","by3","hii"]
# print(" ".join(a))

# 19
# a=[12,23,44,123,220,240,2,280]
# count=0
# for i in a:
#     if i%2==0 and i<=237:
#         count+=1
# print(count)

# 24
for i in range(5):
    for j in range(5,i):
        print("*",end="")
    print()
