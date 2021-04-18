# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:59:03 2021

@author: danyal.hassan
"""


stuff={"food":15,"clothes":16}
print(stuff)

newstuff={"car":18}
stuff.update(newstuff)

print(stuff)

stuff.update(food=18,clothes=20)
print(stuff)

print(stuff.setdefault("jax", 123))
print(stuff)

print(stuff.items())

print(stuff.get("food"))

