import logging

logging.basicConfig(filename="test1.log",level=logging.INFO, format=" %(asctime)s %(levelname)s %(lineno)d %(message)s")

#1: Write a Python Program to Check if a Number is Positive, Negative or Zero?
def check():
    try:
        a=int(input("enter a number"))

    except Exception as e:
        logging.exception(e)
    else:
        if (a==0):
            logging.info("entered number is zero")

        elif (a>0):
            logging.info("entered number is positive")

        elif(a<0):
            logging.info("entered number is negative")
    logging.info("function check has ended")

check()

#2.	Write a Python Program to Check if a Number is Odd or Even
def oddeven():
    try:
        a=int(input("enter a number"))

    except Exception as e:
        logging.info(e)

    else:
        if(a%2)==0:
            logging.info("number entered is even")

        else:
            logging.info("number entered is odd")
    logging.info("function oddeven has ended")
oddeven()


#3.	Write a Python Program to Check Leap Year?
def leap():
    try:
        y=int(input("enter the year for which you want to check if it is leap or not"))

    except Exception as e:
        logging.info(e)

    else:
        if(y%400==0) and (y%100==0):
            logging.info("entered year:%d is a century year and leap year" %y)

        elif (y%4==0) and (y%100!=0):
            logging.info("entered year:%d is a leap year" %y)
        else if (y%400!=0) and (y%4!=0):
            logging.info("entered year:%d is not a leap year" % y)
    finally:
        logging.info("function leap has ended")

leap()


#4.	Write a Python Program to Check Prime Number?
def prime():
    try:
        p=int(input("enter a number"))

    except Exception as e:
        logging.exception(e)
    else:
        if(p>1):
            for i in range(2,p):
                if(p%i==0):
                    logging.info("number %d is not a prime number" %p)
                    break
            else:
                 logging.info("number %d is a prime number" %p)
        else:
            logging.info("number %d is not a prime number" % p)
    logging.info("prime function has ended")

prime()

#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
def prime1():
    for i in range(2,10000):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            logging.info("%d" %i)


prime1()



