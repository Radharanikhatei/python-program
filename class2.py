#variable 0f python

name="radha"
age=23
salary=23000.00
onTime=False
a=None

print(type(name)) #string
print(type(age)) #intiger
print(type(salary)) #float
print(type(onTime)) #boolean
print(type(a)) #none

#comments;-
#single line comment


"""
 today is a day 
 we just learn python
 and do some code etc...
"""


# print a sum of 2 no.
a=40
b=60
sum=a+b
print("my total sum is:", sum) #100


#arithmatic operator
a=5
b=3
print(a+b) #8
print(a-b)#2
print(a*b)#15
print(a%b)#1.6
print(a/b)#2


#relation operator
a=5
b=3
print(a==b) # false
print(a!=b) #true
print(a<=b) #true
print(a>=b) #false
print(a<b)  #true
print(a>b) #false


#assignment operator
num=10
num=num+10
print("num:",num)


#logical operator
val1=True
val2=False
print("AND operator:", val1 and val2) #false
print("OR operator:" ,val1 or val2)  #true

#True + True=True
#True + false=false
#false+ false=false
#false+ True=false

#input
name=str(input("enter your name:"))
value=int(input("enter your age:")) 
mySalary=float(input("enter your salary:"))
print("wellcome",name)
print("my age is ",value)
print("my salary is",mySalary)





#home work
# Write a program to input 2 number & print their sum
p=input("enter a number")
q=input("enter a number")
sum=int(p)+int(q)
print("my total sum is:", sum) #100



