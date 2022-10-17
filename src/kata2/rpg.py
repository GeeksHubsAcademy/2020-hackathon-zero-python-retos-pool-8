#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    p =  "".join(random.sample(s,passLen ))
    #
    #
    print(p)
    return p
