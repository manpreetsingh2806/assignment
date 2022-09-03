import logging
logging.basicConfig(filename="test5.log",level=logging.INFO, format="%(asctime)s %(levelname)s %(lineno)d %(message)s ")

#1.	Write a Python Program to Find LCM?
def lcm():
    try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))

    except Exception as e:
        logging.info(e)

    else:
        if a>b:
            max=a
        else:
            max=b

        while(True):
            if (max%a==0) and (max%b==0):
                lcm=max
                break
            max+=1
        logging.info("lcm of two numbers %d & %d is %d" %(a,b,lcm))
lcm()

#2.	Write a Python Program to Find HCF?
def hcf():
    try:
        a=int(input("enter first number"))
        b=int(input("enter second number"))

    except Exception as e:
        logging.info(e)

    else:
        if a<b:
            min=a
        else:
            min=b

        for i in range(1,min+1):
            if (a%i==0) and (b%i==0):
                hcf=i
            i+=1

        logging.info("hcf of two numbers %d & %d is %d" %(a,b,hcf))
hcf()
#3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
def converter():
    try:
        num=float(input("enter a decimal number which you want to get converted"))

    except Exception as e:
        logging.exception(e)

    else:
        logging.info("number %.1f in binary is %s" %(num,bin(num)))
        o=oct(num)
        h=hex(num)
converter()


#4.	Write a Python Program To Find ASCII value of a character?
def val():
    try:
        a=input("enter character for which you want to find ASCII Value")

    except Exception as e:
        logging.exception(e)

    else:
        logging.info(f"ASCII value of character {a} is {ord(a)}")

val()

#5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
class calculator:
    def add(self,a,b):
        return a+b

    def subtraction(self,a,b):
        return abs(a-b)

    def multiplication(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

calc=calculator()
logging.info(calc.add(10,4))
logging.info(calc.subtraction(10,4))
logging.info(calc.multiplication(10,4))
logging.info(calc.divide(10,4))
