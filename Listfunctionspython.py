# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:54:07 2021

@author: danyal.hassan
"""


fruits = ["apples","oranges","mangoes"]
years=[1997,12.0,13]

print(fruits,years)

fruits.append("pineapple")

print(fruits,years)

fruits.extend(years)

print(fruits)

fruits.remove("pineapple")

print(fruits)

fruits.pop(0)

print(fruits)

print("oranges" in fruits)

print(fruits.index("oranges"))
