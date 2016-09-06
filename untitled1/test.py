a=[1,5,2,3,4,5,3,]
b={}
a.sort()
last=a[-1]
for i in range(len(a)-2,-1,-1):
    print i
    print a[i]
    if last==a[i]:

        del a[i]
    else:last=a[i]

print a


print range(5,-1,-1)