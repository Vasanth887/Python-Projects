from re import search
a=input("enter the month: ").capitalize()
b=int(input("enter the day: "))
c=search("December|January|February",a)
d=search("March|April|May",a)
e=search("June|July|August",a)
f=search("September|October|November",a)
month={
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}
if a not in month or b <1 or b>month.get(a):
    print("enter valid details:")
else:
    if c and 1<=b<=31:
        print("winter ")
    elif d and 1<=b<=31:
        print("spring")
    elif e and 1<=b<=31:
        print("summer")
    elif f and 1<=b<=31:
        print("fall")
    else:
        print("enter valid day and mon")