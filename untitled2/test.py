#coding:utf-8

#4个数字1234能组成多少个3位数

def paixu():
    for x in range(1,5):
        for y in range(1,5):
            for z in range(1,5):
                if (x!=y) and (x!=z) and (y!=z):
                    print x,y,z





"""企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。"""



def lirun():
    zonge=int(raw_input("输入金额："))
    arr=[1000000,600000,400000,200000,100000,0]
    per=[0.01,0.015,0.03,0.05,0.075,0.1]
    li=0
    for i in range(0,6):
        if zonge>arr[i]:
            li+=(zonge-arr[i])*per[i]
            zonge=arr[i]

    print li



"""题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，
如果开方后的结果满足如下条件，即是结果。请看具体分析："""



def kaifang():
    import math
    l=[]
    for n in range(10000):
        x=int(math.sqrt(n+100))
        y=int(math.sqrt(n+268))
        if x*x==n+100 and y*y==n+268:
            l.append(n)
    return l





"""Python 练习实例14


题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

程序源代码(输出不换行最后加,或者用stdout.write)"""


def zhiyinshufenjie():
    import sys
    n=int(raw_input("输入一个整数:"))
    print "%d="%n,
    for i in range(2,n+1):
        while i!=n:
            if n%i==0:
                sys.stdout.write(str(i))
                sys.stdout.write("*")
                n=n/i
            else:break
    print "%d"%n







"""Python 练习实例15


题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

程序源代码："""


def tiaojianyunsuan():
    n=int(raw_input("输入成绩："))
    if n>=90:
        grade="A"
    elif 90>n>=60:
        grade="B"
    else:grade="C"
    print grade

#tiaojianyunsuan()


"""Python 练习实例16


题目：输出指定格式的日期。

程序分析：使用 datetime 模块。

程序源代码："""

def zdtime():
    import datetime
    import time
# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    today=datetime.date.today().strftime("%d/%m/%Y")
    today1=time.strftime("%d/%m/%Y")
    today3=datetime.datetime.strftime(datetime.datetime.now(),"%d/%m/%Y")
    today4=str(datetime.datetime.now())[:19]


# 创建日期对象


# 日期算术运算

 # 日期替换

    print today,today1,today3,today4



#zdtime()




"""Python 练习实例17


题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

程序分析：利用while语句,条件为输入的字符不为'\n'。

程序源代码："""

def fenbian():
    import string
    n=raw_input("输入一串字符：")
    #list(n)
    zimu=0
    shuzi=0
    kongge=0
    oth=0
    for i in n:
        if i.isalpha():
            zimu+=1
        elif i.isdigit():
            shuzi+=1
        elif i.isspace():
            kongge+=1
        else:oth +=1

    print '字母=%d,数字=%d,空格=%d,其他=%d' %(zimu,shuzi,kongge,oth)

fenbian()

