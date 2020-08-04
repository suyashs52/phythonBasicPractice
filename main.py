


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
uuyyuuy
"""
a=1
b="tsrt"
c=25j
print(a)
print(b[2])
print(len(b))
print(b.upper())
print(b[-1])
l=[10,20,"edu","test"]
print(l)
print(l[2:10])
l[2]=1
l.insert(1,"t1")
print(l)
l.reverse()
print(list)

ani={'1':'v1' , 2:455 , "asdf":133} #dictionary
print(ani["asdf"])
print(ani.get('1'))
ani['1']="test"
print(ani['1'])
animal=(10,20,30,"50")  #touple can't change next
print(animal[1])
#animal[1]="test"
print(animal)
print(animal.count(20))
#set
myset={1,20,12,3}   #set doen't have index
print(myset)

a={1,4,3}
b=[4,3,2]
c=[a,b]
print(c)

print(range(0,10))

a=10
b="name"
c=str(a)+b
print(c)

#list in []sqare bracker, access via get
#tuple in ()brace bracket orderd, immutable in nature, duplicate in nature, access can get index
#set declared {} in culy bracket, cannot access via get, not have duplicate entry
#dictionary {:}mutable ,key value, curly bracket,
from collections import  namedtuple
a=namedtuple('course','name ,technology,feature')
s=a('data scient','python','test') #tuple
b=a._make(['artific','python','t']) #list
print(s)
print(b)

from collections import  deque,ChainMap
a=['a','e','i']
b=deque(a);
print(b)
b.append("test")
print(b)
b.remove('e')
print(b)
b.pop() #remove last element
#chain map add multiple mapping
a={1:'edu',2:'asdf'}
b={2:'test',4:'ai'}
c=ChainMap(a,b)
print(c)

from collections import  Counter,OrderedDict,defaultdict
a=[1,3,5,4,3,2,1,3,4,5,6]
b=Counter(a)
print(b)
print(b.most_common()) #sorted by count
sub={3:1,1:1}
b.subtract(sub) #remove 3 by 1 time , 1 by 1 time
print(b.most_common())
a=OrderedDict();
a[1]=1
a[2]=2
a[3]='p'
print(a)
a=defaultdict(int) #if not put int you ll get error
a[1]='python'
a[2]='edu'
print(a[3])
#list can store any data type , array can store single data type
import  array as ar
c=ar.array('i',[1,2,3,4])   #i for integer
print(c[-1])
print(len(c))
#append add 1 element/extend add more element at end, insert(2,4)
c=ar.array('d',[2,3,4,5,2.0])
c.insert(3,3)
c.extend([1,2,3])
c.append(2)
c.pop() #remove last and return it pop(index)
c.remove(2) #remove key

print(c)
d=c+c #can't concatenate different data type array
print(d)
print(c[1:2])#slice array
print(c[::-1]) #print the revese array
#looping
print(c)
print("sdf")
for x in c[0:-2]:  #doesnt print last 2 element
    print(x)
temp=0
print("while loop")
while(temp<c[2]):
    print(c[temp])
    temp=temp+1

mydic={"dave":1,'ava':2,'job':3}
print(mydic)
print(type(mydic))

newdic=dict(dave=1,eva=3)
print(newdic)
emp_dtl={'Employee':{'dave':{'id':1,'salary':200,'designation':'team'}
    ,'dave1':{'id':1,'salary':200,'designati':'team'}}}
print(emp_dtl)
print(emp_dtl.keys())
for x in mydic:
    print(x)
for x in mydic.values():
    print(x)
for x,y in mydic.items():
    print(x,y)

mydic['dave']=10
print(mydic)
print(mydic.pop('dave')) #popitem() delete last item and return it
del mydic['ava']

a=10;
b=2
print(a**b)
print(b//a)
a=5
a+=3
c=a==5
print(c)

if a==5:
    print("true")
elif a>10:
    print("10")
else:
    print("asdf")

x=10
y=5

if x==10 and y==5 : #or
    print("true")
else :
    print("false")

print(not(x==9))

x=10
y=10
print(x is y)
list1=[1,2,3]
print(x is not list1) #not same object

print ([1,2] in list1)
print (1 not in  list1)

print(10 & 12)
print(1 | 2)


import  random

n=20
guess=10#int(n*random.random())+1 #random no to be generated between 0 to 20
g=0
print(guess)
while guess != g:
    g=10#int(input("number"))
    if g>0 :
            if g>guess:
                print("no too large")
            elif g<guess:
                print("no too small")
    else:
        print("sorry giving up");
        break

else:
    print("Congo you made it")


    from math import  sqrt

    n=5#int(input("numer is"))
    for a in range(1,n+1):
        for b in range(a,n):
            c_sqr=a**2+b**2;
            c=int(sqrt(c_sqr))
            if(c**2-c_sqr==0):
                print(a,b,c)

    def pattern(n):
        k=2*n-2;   #for 5 we need 8 space4*4, 3**3 6
        for i in range(0,n):
            for j in range(0,k):
                print(end=" ")
            k=k-1
            for j in range(0,i+1):
                print("* ",end="")
            print("\r")
    pattern(5)

    def patters(n):
        k=n-2;
        for i in range(n,-1,-1):
            for j in range(k,0,-1):
                print(end=" ")
            k=k+1
            for j in range(0,i+1):
                print("* ",end="")
            print("\r")
    patters(10)

def patter(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
    for i in range(n,0,-1):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
patter(5)

def patter(n):
    k=2*n-2
    for i in range(0,n-1):
        for j in range(0,k):
            print(end=" ")
        k=k-2
        for j in range(0,i+1):
            print("* ",end="")

        print("\r")
    k=-1
    for i in range(n-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k=k+2
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
patter(5)

import  os

file=open("C:/Users/suysingh/Desktop/test.txt",'w')
file.write("test1")
file.write("test2")
file.write("test3")
file.close()
fil=open("C:/Users/suysingh/Desktop/test.txt",'r')
#for line in fil:
print(fil.readline())
print(fil.read())
file.close()
#os.remove(filename) delete file os.path.exists os.rmdir(foldername)

def func1(name):
    return f"hello {name}";
def func2(name):
    return  f"{name}, how you are doing"
def func3(func4):
    return func4('dear learner')

print(func1("suyash"))
print(func3(func1))
print(func3(func2))

def func():
    print("first func")
    def func1():
        print("f child func")
    def func2():
        print("sec child func")
    func1()
    func2()
func()

def func(n):
    def fun1():
        return "edu"
    def fun2():
        return  "python"
    if n==1:
        return fun1
    else:
        return fun2

print(func(1))
print(func(2)())

def func(func2):
    def wrappe():
        print("helo")
        func2()
        print("welcome to decorator design")
    return  wrappe
def fun2():
    print("pyton")

func(fun2)()
fun2=func(fun2)
fun2()

@func
def fun3():
    print("t python")
fun3()  #same as calling


def func(fun):
    def wrapper(*args,**kwargs):
        print("hello")
        fun(*args,**kwargs)
        print("welcome to edu")
    return wrapper;

@func
def func2(name):
    print(f"{name}")

func2("pandora")
#decorator are reference to function

class Square:
    def __init__(self,side):
        self._side=side
    @property
    def side(self):
        return self._side
    @side.setter
    def side(self,value):
        if value>=0 :
            self._side=value;
        else:
            print("error")
    @property
    def area(self):
        return  self._side**2;
    @classmethod
    def unit_square(cls):
        return  cls(1)
s=Square(5)
print(s.side)
print(s.area)

import  functools
def singleton(cls): #define singleton class
    @functools.wraps(cls)
    def wrapper(*args,**kwargs):
        if not wrapper.instance:
            wrapper.instance=cls(*args,*kwargs)
        return wrapper.instance
    wrapper.instance=None
    return wrapper;
@singleton
class one:
    pass
first=one()
second=one()
print(first is second)

def repeat(num):
    def decor_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                value=func(*args,**kwargs)
            return value
        return  wrapper;
    return  decor_repeat

@repeat(num=4)
def function(name):
    print(f"{name}")

function("suyash")  #nested decorator

x=lambda a:a*a
print(x(10))

def a(x):
    return lambda y:x+y
print(a(10))
print(a(10)(4))

a=[1,2,3,4,5,6]
nlist=filter(lambda  a: a%3==0,a)
print(nlist)
print(list(nlist))

p=list(map(lambda a:(a/3!=2),a))
print(p)
#reduce return a single value
from functools import  reduce

c=reduce(lambda a,b: a+b,[1,2,3,4])
print(c)

s=lambda  a:a*a
print(s(4))
d=lambda x,y:3*x+4*y
print(d(2,3))
x=lambda a,b:(a+b)**2
print(x(3,4))

def dbl(a,b):
    return a*b

x=map(dbl,[1,2,3,4],[2,3,4,5])
print(x)
print(list(x))

ls=[1,2,3,4,5]
y=list(map(lambda a:a+3,ls))
print(y)

def grt(x):
    if x>3:
        return x
print(tuple(filter(grt,ls)))

def xy(x,y):
    return x+y
print(reduce(xy,ls))

print(reduce(lambda p,q:p*q,ls))

c=map(lambda x:x+x,filter(lambda x:x>2,[1,2,3,4]))
print(list(c))
d=filter(lambda  x:x>2,map(lambda x:x+x,[1,2,3,4,5,6]))
print(list(d))
r=reduce(lambda x,y:x+y,map(lambda x:x+x,filter( lambda  x: x>3,[1,3,4,5,6,7,8])))
print(r)


def ne(dict):
    for x,y in dict.items():
        yield x,y
a={1:'hi',2:'welcome'}
b=ne(a)
print(b)
print(next(b))

def myfunc(i):
    while i<3:
        yield i
        i+=1

j=myfunc(1)
print(next(j))
print(next(j))
#print(next(j)) ll give error

def ex():
    n=3
    yield n
    n*=n
    yield n

j=ex()
print(next(j))
print(next(j))
#print(next(j)) #give error
j=ex()
for x in j:
    print(x)


f=range(6)
print(f)
print("list com",end=":")
q=[x+2 for x in f]
print(q)
print("gen exp",end=":")
r=(x+2 for x in f)
print(r)
print(min(r))
for x in r:
    print(x)
#print(min(r)) error casue empty sequence now

def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s

for r in fib():
    if r> 50:
        break
    print(r,end=" ")

a=range(100)
b=(x for x in a)
print(b)
for y in b:
    print(y)

a=range(2,50,2)
b=(x for x in a)
print(b)
for y in b:
    print(y)

class Car():

    def __init__(self,model,year,price):
        self.model=model
        self.year=year
        self.price=price
    def price_inc(self):
        self.price=self.price*1.13

honda=Car("10",2018,1000)
tata=Car('bolt6',2018,20000)

honda.modelName='City'
honda.year=2017
honda.price=1000

tata.mode='Bolt'
tata.y=2020
tata.price=2000

print(honda.__dict__)
print(tata.y)
print(honda.price_inc())
print(honda.price)

class SuperCar(Car):
    def __int__(self,model,year,price,cc):
        super.__init__(model,year,price)
        self.cc=cc

honda=SuperCar('city',2019,2000)
honda.cc=1500


print(help(honda))


class parent:
    def __init__(self,fname,fage):
        self.fname=fname
        self.fage=fage
    def view(self):
        print(self.fname,self.fage)

class child(parent):
    def __init__(self,fname,fage):
        parent.__init__(self,fname,fage)
        self.lname='edu'

    def view(self):
        print(self.fname,self.lname,self.fage)

c=child('ph',24)
c.view()


class parent:
    def func1(self):
        print("this is func 1")
class parent2:  # parent2(parent):can't have this when we do child(parent,parent2):
    def func2(self):      #Cannot create a consistent method resolution
        print('this is func 2')
class child(parent,parent2):
    def func1(self):
        super().func1()
        print('this is func child')
ob=child()
ob.func1()
ob.func2()