# # a=[1,2,3,4,5,6,7,8,9]
# # c,s=0,0
# # for i in a:
# #     if i%2==0:
# #         c+=1
        
# #     else:
# #         s+=1
# # print(c,s).           4


# # 5

# for i in range(0,7):
#     if i==3 or i==6:
#         continue
#     print(i)

# 6

# a,b=0,1
# while a <=50:
#     print(a,end=" ")
#     a,b=b,a+b


# 7
# a=[]
# while True:
#     line=input().lower()
#     if line=="":
#         break
#     a.append(line)
# for i in a:
#     print(i)
  

# 8
# a=input("")
# b=a.split(",")
# for i in b:
#     if int(i,2)%5==0:
#         print(i)

# 9
# from re import search

# def passcheck(password):
    
#     if not 6<= len(password)<=16:
#         return False
#     if  not search("[a-z]",password):
#         return False
#     if not search("[A-Z]",password):
#         return False
#     if not search("[0-9]",password):
#         return False
#     if not search("[$@#%&]",password):
#         return
#     return True
# a=input("Enter the pass: ")
# if passcheck(a)==True:
#     print(2)
# else:
#     print(3)

# a=int(input("Enter the dog age: "))
# if a<=2:
#     b=a*10.5
#     print(b)
# else:
#     b=21+(a-2)*4
#     print(b)                  11


# 12

# a=input("enter the alphabet: ")

# if a in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonent")

# 13
# a={"jan":31,"march":31}

# b=input("Enter the months: ")

# if b in a:
#     print(a.get(b))
# if b=="feb":
#     print("28 or 29")
# 14

# from re import search
# a={"jan":31,"feb":28,"april":30}
# b=input("enter the month")
# c=int(input("enter the day"))
# d=a.get(b)
# if 1<= c<=d:
#     if search("jan|mar",b):
#         print("summer")
#     if search("feb|april",b):
#         print("fall")
# else:
#     print(3)

# 16

# from datetime import date,timedelta

# a=int(input("Enter date(year): "))
# b=int(input("Enter date(month): "))
# c=int(input("Enter date(day): "))

# date1=date(a,b,c)
# date2=date1+timedelta(days=1)
# print(date2)

