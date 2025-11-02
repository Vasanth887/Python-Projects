from random import choice

a=("r","p","s")
emoji={"r":"🗿","p":"📃","s":"✂️"}

while True:
    user=input("r,p,s: ")
    if user not in a:
        print("enter valid: ")
        continue
    comp=choice(a)

    print(f"You chose {emoji[user]}")
    print(f"Comp chose {emoji[comp]}")

    if user==comp:
        print("Tie!!!!")
    elif(
        (user=="r" and comp=="p") or 
        (user=="p" and comp=="s") or
        (user=="s" and comp=="r")
    ):
        print("You lose: 😥")
    else:
        print("You win..🏆")
    cont=input("continue ?(y/n): ").lower()
    if cont=="n":
        break
    