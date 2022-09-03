import logging
logging.basicConfig(filename="test6.log", level=logging.INFO,format="%(asctime)s %(levelname)s %(lineno)d %(message)s ")

#1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
def fibo(a):
        if a<=1:
            return a

        else:
            return(fibo(a-1)+fibo(a-2))

length=5
logging.info("the fibonacci series for 30 terms is as follows")
for i in range(length):
    logging.info(fibo(i))

#2.	Write a Python Program to Find Factorial of Number Using Recursion?
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

try:
    num=int(input("enter a number"))

except Exception as e:
    logging.exception(e)

else:
    if num==0:
        logging.info("factorial of zero is 1")
    else:
        logging.info("the factorial of a number is %d" %factorial(num))


#3.	Write a Python Program to calculate your Body Mass Index?

def bmi():
    try:
        h=float(input("enter height in meters"))
        w=float(input("enter your weights in kilograms"))

    except Exception as e:
        logging.exception(e)

    else:
        bmi=w/(h*h)
        logging.info("the BMI is %.2f" %bmi)

bmi()
#4.	Write a Python Program to calculate the natural logarithm of any number?

from math import log
def nl():
    try:
        num=int(input("enter a number"))

    except Exception as e:
        logging.info(e)

    else:
        conv=log(num)
        logging.info("the natural log is %.2f"%conv)

nl()

#5.	Write a Python Program for cube sum of first n natural numbers?
def cube(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+(i*i*i)

    logging.info("the sum of first %i is %i" %(n,sum))

cube(5)