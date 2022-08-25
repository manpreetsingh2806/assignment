# 1.	Write a Python program to convert kilometers to miles?
import logging

logging.basicConfig(filename="test.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(lineno)d %(message)s")
logging.info("this is the start of my code")
"""
def converter():
    while True:
        try:
            k=int(input("Enter kilometers you want to convert in miles"))
            break

        except ValueError as v:
            logging.exception(v)
            continue
        
    m=k*0.621371
    logging.info("we have completed required conversion from kms to miles")
    logging.info("the number of miles are %s",m)

converter()
"""
# 2.	Write a Python program to convert Celsius to Fahrenheit?

"""def temperature():
    while True:
        try:
            c=float(input("enter temperature in celsius"))
            break

        except ValueError as v:
             logging.exception(v)
             continue
        
        else:
            f=(c*1.8+32)
            logging.info("we have completed conversion of temperature from Celsius to Fahrenheit")
            logging.info("temperature in Fahreheit is %.1f" %f)
    
temperature()"""

# 3.	Write a Python program to display calendar?
"""import calendar
def display():
    while True:
        try:
            yy=int(input("enter the year for which you want to see calendar"))
            break

        except ValueError as v:
            logging.info(v)
            continue
            
    logging.info(calendar.calendar(yy))
display()"""

#4.	Write a Python program to solve quadratic equation?
"""def solvequation():
    try:
        a=int(input("enter value of a:"))
        b=int(input("enter value of b:"))
        c=int(input("enter value of c:"))

    except BaseException as e:
        logging.exception(e)
    
    else:
        if a==0:
            logging.info("you have entered a as 0")
        else:
            d= (b*b) - (4*a*c)

        if(d>0):
            root1=( (-b+ 0.5*d)/(2*a))
            root2 = ((-b - 0.5 * d) /( 2 * a))
            logging.info("the roots are real and different, root1 is %.2f & root 2 is %.2f",root1,root2)

        elif (d==0):    
            root= -b/(2*a)
            logging.info("the roots are real and equal, root is %.2f",root)

        elif (d<0):
            root  = -b / (2 * a)
            second=(0.5*d)/(2*a)
            logging.info("the roots are complex and different, root1 is %.2f %.2f and root 2 is %.2f %.2f " % (root,second,root,second))

solvequation()"""

#5.	Write a Python program to swap two variables without temp variable
"""def swap():
    try:
        x=int(input("enter first number"))
        y = int(input("enter second number"))

    except Exception as v:
        logging.exception(v)
    else:
        logging.info("first number entered is %d" %x)
        logging.info("Second  number entered is %d" %y)
        x,y=y,x
        logging.info("first number now is %d" % x)
        logging.info("Second  number now is %d" % y)

swap()"""