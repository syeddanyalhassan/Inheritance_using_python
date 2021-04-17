# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:26:43 2021

@author: danyal.hassan
"""

on=True
def addition():
    num=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    print("sum is {}".format(num+num2))
    
def subtract():
    num=float(input("number to be subtracted"))
    num2=float(input("From the number to be subtracted"))
    print("sum is {}".format(num2-num1))

def multiply():
    num=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    print("sum is {}".format(num*num2))

def divide():
    num=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    print("sum is {}".format(num/num2))
    
while on:
    operation=input("Enter any operation +,-,/,*,q")
    if operation=="+":
        addition()
    elif operation=="-":
        subtract()
    elif operation=="/":
        divide()
    elif operation=="*":
        multiply()
    else:
        calc_on=False
        print("Exited..")
   
    
    
 