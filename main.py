


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
list=[10,20,"edu","test"]
print(list)
print(list[2:10])
list[2]=1
list.insert(1,"t1")
print(list)
list.reverse()
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




