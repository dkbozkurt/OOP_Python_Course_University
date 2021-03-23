# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 01:02:31 2021

@author: Doğukan Bozkurt
"""

m=int(input("Please enter the Month code(0-12): "))
d=int(input("Please enter the Day code(0-31): "))
y=int(input("Please enter the Year code: "))

y_= y-((14-m)//12)
x=y_+(y_//4)-(y_//100)+(y_//400)
m_=m+12*(((14-m)//12))-2
d_=(d+x+((31*m_)//12))%7

#Way1-(with list and round)
days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
print(days[d_])


#Way2 - (with if-elif-else)
if(d_==0):
    print("Sunday")
elif(d_==1):
    print("Monday")
elif(d_==2):
    print("Tuesday")
elif(d_==3):
    print("Wednesday")
elif(d_==4):
    print("Thursday")
elif(d_==5):
    print("Friday")
elif(d_==6):
    print("Saturday")
else:
    print("Wrong date values!")
