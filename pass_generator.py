#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 

import random, string

size = input("Enter your password length: ")
chars = string.ascii_letters + string.digits + '!@#$%*'
rnd = random.SystemRandom()

print ''.join(rnd.choice(chars) for i in range(size))