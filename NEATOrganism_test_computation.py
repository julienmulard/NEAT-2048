# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:39:08 2017

@author: Julien
"""

import NEATOrganism as Org

input("Computation test")
org = Org.NEATOrganism(2,2)
org.initializeNodes()
org.addGeneFull(0,1000001,1,True,-1)
org.addGeneFull(1,1000001,-1, True,-1)

org.addGeneFull(1,1000002,1,True,-1)
org.addGeneFull(2,1000002,1, True,-1)


#org.addGeneFull(2,3,1,True,-1)
org.drawOrganism()
output = org.computeOutput([1,1])
print(output)
print([org.sigmoid(0), org.sigmoid(2)])
