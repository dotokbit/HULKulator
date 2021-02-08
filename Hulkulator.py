#Hulkulator 2.1

from colorama import init
from colorama import Fore, Back, Style
init ()
print (Fore.BLACK)
print (Back.RED)
print ("Hi! Let's do some MATHemagic!")
def loop ():
    while True:
        try:
            print (Fore.BLACK)
            print (Back.YELLOW)
            a=float(input ("Tell me the first number "))
            break
        except (TypeError, ValueError):
            print (Fore.BLACK)
            print (Back.CYAN)
            print ("Are you crazy? This is not a number!")
    while True:
        print (Fore.BLACK)
        print (Back.GREEN)
        what=input("What do you want to do? (+, -, *, /)")
        if what == "+" or what == "-" or what == "*" or what == "/":
            break
        print (Fore.BLACK)
        print (Back.CYAN)
        print ("What are you talking about? Let's try again!")
    while True:
        try:
            print (Fore.BLACK)
            print (Back.YELLOW)
            b=float(input ("Tell me the second number "))
            break
        except (TypeError, ValueError):
            print (Fore.BLACK)
            print (Back.CYAN)
            print ("Are you crazy? This is not a number!")
    if what == "+":
        c=a+b
        print (Fore.BLACK)
        print (Back.MAGENTA)
        print ("Answer is ", str(c)) 
    elif what == "-":
        c=a-b
        print (Fore.BLACK)
        print (Back.MAGENTA)
        print ("Answer is ", str(c))
    elif what == "*":
        c=a*b
        print (Fore.BLACK)
        print (Back.MAGENTA)
        print ("Answer is ", str(c))
    elif what == "/":
        c=a/b
        print (Fore.BLACK)
        print (Back.MAGENTA)
        print ("Answer is ", str(c))
loop ()
while True:
    print (Fore.BLACK)
    print (Back.BLUE)
    more = input ("Do you want more? (yes/no) ")
    if (more == "yes" or more == "Yes" or more == "YEs" or more == "YES"
    or more == "yES" or more == "yeS" or more == "yEs" or more == "YeS"
    or more == "Y" or more == "y"):
        loop()
    if (more == "no" or more == "No" or more == "NO" or more == "nO"
      or more == "N" or more == "n"):
        print (Fore.BLACK)
        print (Back.RED)
        bye = input ("Bye-bye! See you later!")
        break
    else:
        print (Fore.BLACK)
        print (Back.CYAN)
        print ("Where are you from? I don't understand you!")
