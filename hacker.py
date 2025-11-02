# x=int(input())
# y=int(input())
# z=int(input())
# n=int(input())

# result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
# print(result)

n=int(input())
a=input()
b=map(int,a.split(" "))
c=set(b)
sorte=sorted(c,reverse=True)
print(sorte[1])
