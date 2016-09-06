#coding:utf-8

l1=[1,4,2,4,5,3,2,8]
print sorted(l1)
#set去重
def sqc(s):
    l2=list(set(l1))
    l3=l2.sort(l1.index())

    print list(set(l1))


#for循环无序
def qc1(x):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)

    sorted(l2)
    print l2
qc1(l1)


#字典key

def qc2(y):
    d1={}
    d1=d1.fromkeys(l1).keys()
    print d1

qc2(l1)

#编程排序后从最后一个字符开始判断

def qc3(z):
    l2=sorted(l1)
    a=l2[-1]

    for i in range(len(l2)-2,-1,-1):
        if a==l2[i]:
            del l2[i]
        else:a=l2[i]

    print l2


qc3(l1)