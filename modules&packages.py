#Import Math Module
import math
print(math.pi)

#Calculate Square Root
import math 
print(math.sqrt(56))

#Generate Random Number
import random
print(random.randint(1,100))

#Create Your Own Module
def add(a,b):
    return a+b

#Import Custom Module
import calculator

print(calculator.add(10,20))

#Use Datetime Module
from datetime import datetime
now = datetime.now()
print(now)

#Create Calculator Module

import calculator
print(calculator.mul(5, 4))

#Generate OTP
import random
otp = random.randint(100,999)
print("OTP",otp)

#Use Alias Imports
import math as m

print(m.sqrt(81))