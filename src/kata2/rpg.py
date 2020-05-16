#!/usr/bin/python
import random
#from random import randint
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    
    #
    #   

    letters = string.ascii_letters
    digits =  string.digits
    alpahnum = letters + digits   

    #print(len(alpahnum))

    pwd = ''.join(random.choices(alpahnum, k=passLen))    
    
    #print(pwd)

    return pwd


# if __name__ == '__main__':
#     RandomPasswordGenerator()

