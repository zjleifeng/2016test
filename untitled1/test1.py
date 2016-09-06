# coding:utf-8

# 去重

a = [1, 7, 2, 3, 1, 3, 4, 2, 3, 4, 5]
# set
b = set(a)

print list(b)

# 字典

dc = {}
dc = dc.fromkeys(a)
dd = list(dc.keys())
print dd


#列表解析
res=[]
l=[res.append(x) for x in a if x not in res]


#del

def quchong(a):
    for x in a:
        while a.count(x)>1:
            del a[a.index(x)]
    return a

#n=quchong(a)
#print n


print a[:-1:-1]