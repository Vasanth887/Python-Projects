# #while loop

# food=input("Enter your fav food (q to quit)")

# while  food == "q":
#     print("Bye")
# print(f"You like {food}")
    

num = int(input("Enter no between 1 to 10: "))

while  not 1<= num <= 10:
    print("enter between 1 to 10 only")
    num=int(input(""))
print(f"Your number is {num} ")