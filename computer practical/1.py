def swap(l):
    k=len(l)
    if k%2!=0:
        a=l[:k//2]
        b=l[k//2+1:k]
        b.append( l[k//2])
        c=b+a
        print(c)
    else:
        a=l[:k//2]
        b=l[k//2:]
        c=b+a
        print(c)
n=int(input("Enter number of elements of list"))
l1=[]
for i in range(n):
    e=int(input("Enter element"))
    l1.append(e)
swap(l1)
