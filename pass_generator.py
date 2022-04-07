#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 

import random, string

size = input("Type the size of your pass: ")
chars = string.ascii_letters + string.digits + '!@#$%*'
rnd = random.SystemRandom()

print 'Pass: '.join(rnd.choice(chars) for i in range(size))