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


"""题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，
如果开方后的结果满足如下条件，即是结果。请看具体分析："""

import math

def kaifang():
    for i in range(100000):
        x=int(math.sqrt(i+100))
        y=int(math.sqrt(i+268))
        if x*x==i+100 and y*y==i+268:
            print "这个数是%s"%i
        else:pass



"""题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
情况，闰年且输入月份大于3时需考虑多加一天："""

def nian():
    year=int(raw_input("输入年份:"))
    mouth=int(raw_input("输入月份:"))
    data=int(raw_input("输入几号:"))

#非闰年
    mouths1=[0,31,59,90,120,151,181,212,243,273,304,334]


#判断是否为闰年
    if 0 < mouth <= 12:

        if year%4==0 and year%400 !=0 or year%400==0:
            x=mouths1[mouth-1]+data
            if mouth>=3:
                x=x+1

            print x
        else:
            x=mouths1[mouth-1]+data
            print x


    else:
        print "输入错误月份"






"""题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，
如果x>y则将x与y的值进行交换，然后再用x与z进行比较，
如果x>z则将x与z的值进行交换，这样能使x最小。
"""


def paixu():


    l1=[]
    for i in range(3):
        m=int(raw_input("输入一个数："))
        l1.append(m)

    print sorted(l1)



"""题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：（后一个数的前2个数字相加！）
F（0）=0，F（1）=1，F（n）=F(n-1)+F(n-2)（n≥2，n∈N*）"""

def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)





def bona(n):
    l=[]
    if n ==1:
        l=[1]
    if n==2:
        l=[1,1]
    if n>2:
        l=[1,1]
        for i in range(2,n):
            l.append(l[-1]+l[-2])


    return l



"""Python 练习实例8

题目：输出9*9乘法口诀表。
程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
程序源代码："""


def chengfa():
    for i in range(1,10):
        for j in range(1,i+1):
            x=i*j
            print "%d * %d = %d"%(i,j,x),

        print(" ")




"""Python 练习实例9

题目：暂停一秒输出。
程序分析：time模块的time.sleep()。
程序源代码："""


import time
def tsl():
    for i in range(2):
        time.sleep(1)

        print i

    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    time.sleep(2)
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


"""Python 练习实例11

题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
程序源代码：斐波那契数列"""


def tuzi(n):
    l=[]
    if n==1:
        l=[1]
    if n==2:
        l=[1,1]
    if n>2:
        l=[1,1]
    for i in range(2,n):
        l.append(l[-1]+l[-2])

    zongshu=l[-1]*2
    return zongshu





"""Python 练习实例12

题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
程序源代码："""

def sushu():
    l=[]
    for i in range(101,200):
        s=int(math.sqrt(i)+1)
        for x in range(2,s):
            if i%x==0:
                break
            if x==s-1:
                l.append(i)

    return l,len(l)




"""
Python 练习实例13

题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
程序源代码："""


def shuixianhuashu():
    l=[]
    for i in range(100,1000):
        x=str(i)
        gewei=int(x[2])
        shiwei=int(x[1])
        baiwei=int(x[0])
        #if gewei*gewei*gewei + shiwei*shiwei*shiwei + baiwei*baiwei*baiwei == i:
        if gewei**3 + shiwei**3 +baiwei**3==i:
            l.append(i)


    return l








"""Python 练习实例14

题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
程序源代码："""


def fen():
    x=int(raw_input("输入一个整数:"))
    l=[]
    m=int(math.sqrt(x))
    for i in range(3,x):
        while i>2:

            for y in range(2,i/2+1):
                if i%y==0:
                    break

            l.append(i)

    return l

    print fen()






"""Python 练习实例18

题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。
程序分析：关键是计算出每一项的值。
程序源代码："""


def jiafa():
    num=int(raw_input("输入一个数："))
    frequency=int(raw_input("输入相加次数："))
    ln=[]
    ln1=[]
    nSum=0
    Tn=0
    #方法一加入列表
    for i in range(1,frequency+1):
        ln.append(str(num)*i)
    print ln



    for x in ln:
        nSum+=int(x)
    print nSum

    sss=reduce(lambda x,y:int(x)+int(y),ln)

    print sss

    # 方法二加入列表
    for count in range(frequency):
        Tn += num
        num = num * 10
        ln1.append(Tn)
    print ln1
    zonghe=reduce(lambda x,y:x+y,ln1)
    print zonghe

#jiafa()





"""Python 练习实例19

题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
程序分析：请参照程序Python 练习实例14。
程序源代码：

"""


def wanshu():
    l=[]
    li=[]
    for i in  range(2,1000):
        for n in range(1,i/2+1):
            if i%n==0:
                l.append(n)

        if reduce(lambda x,y:x+y,l)==i:
            li.append(i)
            print li,l
        l=[]
        li=[]

    print li

#wanshu()



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

#fenbian()



"""Python 练习实例20


题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

程序分析：无

程序源代码：

"""

def luoti():
    #方法一：
    top=100.0
    allTop=-100.0
    l=[]
    for i in range(1,11):

        allTop+=top*2
        top=top/2

    print allTop,top

    #方法二：
    sn=100.0
    hn=sn/2

    for i in range(2,11):

        sn+=hn*2
        hn/=2
    print sn,hn


#luoti()



"""
Python 练习实例21


题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

程序分析：采取逆向思维的方法，从后往前推断。

程序源代码：
"""

def houzi():
    #range正序
    sn=1

    for i in range(2,11):
        sn=(sn+1)*2

    print sn

    #range倒序

    xn=1
    for x in range(9,0,-1):
        xx=(xn+1)*2
        xn=xx
    print xx

#houzi()



"""Python 练习实例22


题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

程序源代码：
"""


def pb():

    for a in range(ord("x"),ord("z")+1):
        for b in range(ord("x"),ord("z")+1):
            if a!=b:
                for c in range(ord("x"),ord("z")+1):
                    if a!=c and b!=c:
                        if a!=ord("x") and c!=ord("x") and c!= ord("z"):
                            print "a-%s,b-%s,c-%s"%(chr(a),chr(b),chr(c))




#pb()



"""Python 练习实例23


题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *

程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

程序源代码：
   """


def linxing():

    from sys import stdout
    for i in range(4):
        for x in range(3-i):
            stdout.write(" ")
        for j in range(i*2+1):
            stdout.write("*")
        print

    for n in range(3):
        for m in range(n+1):
            stdout.write(" ")
        for k in range(5-2*n):
            stdout.write("*")

        print




#linxing()


"""
Python 练习实例24

题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

程序分析：请抓住分子与分母的变化规律。

程序源代码：
"""

#方法1
def qiuhe():
    fm=[2.0,3.0]
    fz=[1.0,2.0]
    he=0

    for i in range(18):
        fm.append(fm[-1]+fm[-2])
        fz.append(fz[-1]+fz[-2])

    for m in range(20):
        he+=fm[m]/fz[m]

    #print he

    #print fm,fz

#方法2

    m=2.0#分母
    z=1.0#分子
    t=0#和
    for i in range(20):
        t+=m/z         #和=和+分母除以分子
        s=m            #分母赋值给一个变量（因为下一个分子总是上一个分母）
        m=m+z           #下一个分母为善一个分子加上上一个分母
        z=s             #变量S上一个分母赋值给现在的分子
    #print t


#方法3（方法一个简化版）
    x=2.0
    y=1.0
    l=[]
    for i in range(20):

        l.append(x/y)
        k=x
        x=x+y
        y=k
    print reduce(lambda x,y:x+y,l)


#qiuhe()


"""
Python 练习实例25


题目：求1+2!+3!+...+20!的和。

程序分析：此程序只是把累加变成了累乘。

程序源代码：（递归）5!表示1×2×3×4×5
"""


def digui(n):
    if n==1:
        return 1
    else:
        return n*digui(n-1)

def qiuji():
    l=[]
    for i in range(1,21):
        l.append(digui(i))

    print sum(l)
#qiuji()

#匿名函数加递归一句话解决
#print((lambda n,_xf=lambda N:(lambda a,r=lambda x,z:x>N or z(x+1,z)*x:r(a,r))(1):(lambda a,r=lambda x,z:x>n or z(x+1,z)+_xf(x):r(a,r))(1)-1)(20))

"""
Python 练习实例26


题目：利用递归方法求5!。

程序分析：递归公式：fn=fn_1*4!

程序源代码：(同上！)
"""

def chengjihe(n):
    if n==1:
        return 1
    else:return n*chengjihe(n-1)

#print chengjihe(4)
#print reduce(lambda x,y:x*y,range(1,6))

#防止栈溢出（递归循环超过998就会溢出）使用尾递归回推

def huitui(n,total):
    if n ==1:
        return total
    else:return huitui(n-1,total*n)

#print huitui(5,1)





"""
Python 练习实例27


题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

程序分析：无。

程序源代码：
"""

def fanda(x,y):
    if y==0:
        return
    else:print x[y-1]
    fanda(x,y-1)


def dydg():
    l=raw_input("输入几个字符")
    n=len(l)
    fanda(l,n)



#dydg()



"""
Python 练习实例28


题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

程序分析：利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，
需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

程序源代码：
"""

def huitui(n):
    if n ==1:a=10
    else:a=huitui(n-1)+2
    return a

#print huitui(5)




"""
Python 练习实例29


题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析：学会分解出每一位数。

程序源代码：
"""

def jiweishu():
    num=raw_input("输入一个数：")
    n=len(num)
    print "%d位数！"%n
    nixu(num,n)


def nixu(x,y):
    if y==0:
        return
    else:
        print x[y-1],
    nixu(x,y-1)


#分解每一位数(假设不超过5位)
def fenjieshu():
    num=int(raw_input("输入一个数："))
    a=num/10000
    b=num%10000/1000
    c=num%1000/100
    d=num%100/10
    e=num%10

    if a!=0:
        print  "5位数:%d%d%d%d%d"%(e,d,c,b,a)
    elif b!=0:
        print "4位数:%d%d%d%d"%(e,d,c,b)
    elif c!=0:
        print "3位数:%d%d%d"%(e,d,c)
    elif d!=0:
        print "2位数:%d%d"%(e,d)
    else:print "1位数:%d"%e

#fenjieshu()


#jiweishu()


"""
Python 练习实例30


题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

程序分析：无。

程序源代码：
"""


def huiwenshu():
    num=raw_input("输入一个5位数:")
    gewei=num[0]
    shiwei=num[1]
    qianwei=num[3]
    wanwei=num[4]
    if gewei==wanwei and shiwei==qianwei:
        print "这个数是回文数！"
    else:print "这个数不是回文数！"

#huiwenshu()




"""
Python 练习实例31


题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
星期一： Mon.=Monday
星期二： Tues.=Tuesday
星期三： Wed.=Wednesday
星期四： Thur.=Thursday
星期五： Fri.=Friday
星期六： Sat.=Saturday
星期天： Sun.=Sunday
程序源代码：
"""

def xingqiji():
    n=str(raw_input("输入星期几的英文："))
    uPn=n.upper()

    if len(uPn)>0:
        s=uPn[0]

        if s=="M":
                print "星期一： Mon.=Monday"
        elif s=="W":
                print "星期三： Wed.=Wednesday"
        elif s=="F":
                print "星期五： Fri.=Friday"

        elif s=='T'and len(uPn)>1:
            n=uPn[1]
            if n=="U":
                print "星期二： Tues.=Tuesday"
            elif n=="H":
                print "星期四： Thur.=Thursday"
            else:print "输入错误"
        elif s=="S"and len(uPn)>1:
            n=uPn[1]
            if n=="A":
                print "星期六： Sat.=Saturday"
            elif n=='U':
                print "星期天： Sun.=Sunday"
            else:print "输入错误"
        else:print "输入错误！"


#xingqiji()



"""
Python 练习实例32


题目：按相反的顺序输出列表的值。

程序分析：无。

程序源代码：

"""

def fanshuchu():
    l=["qqwe","wef",21,23,"22"]

    print l[::-1]

#fanshuchu()



"""
Python 练习实例33


题目：按逗号分隔列表。

程序分析：无。

程序源代码：
"""

def fengeliebiao():
    l=["qw","wef",1,2,45,5]
    l1=",".join(str(i) for i in l)
    print l1

#fengeliebiao()


"""
Python 练习实例35

Python 100例 Python 100例

题目：文本颜色设置。

程序分析：无。

 1 格式：\033[显示方式;前景色;背景色m
 2
 3 说明：
 4 前景色            背景色           颜色
 5 ---------------------------------------
 6 30                40              黑色
 7 31                41              红色
 8 32                42              绿色
 9 33                43              黃色
10 34                44              蓝色
11 35                45              紫红色
12 36                46              青蓝色
13 37                47              白色
14 显示方式           意义
15 -------------------------
16 0                终端默认设置
17 1                高亮显示
18 4                使用下划线
19 5                闪烁
20 7                反白显示
21 8                不可见
22
23 例子：
24 \033[1;31;40m    <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
25 \033[0m          <!--采用终端默认设置，即取消颜色设置-->


程序源代码：
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print bcolors.WARNING +"警告的字体颜色！"+ bcolors.ENDC





"""
Python 练习实例36

题目：求100之内的素数。

程序分析：无。

程序源代码：
"""



def sushu100():
    l=[]
    for s in range(2,101):
        c=0
        for i in range(2,s):
            if s%i==0:
                break
            else:c+=1
        if c==s-2:
            l.append(s)
    print l



#sushu100()



"""
Python 练习实例37


题目：对10个数进行排序。

程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

程序源代码：
"""


def xuanzejiaohuan():
    l=[2,3,1,5,7,9,4,6,10,8]
    N=len(l)

    for i in range(N):
        min=i
        for x in range(i+1,N):
            if l[x]<l[i]:
                min=x
                l[i],l[min]=l[min],l[i]
    print l






#xuanzejiaohuan()
"""
Python 练习实例38

题目：求一个3*3矩阵对角线元素之和。
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
程序源代码：
"""


def juzhen():
    pass












