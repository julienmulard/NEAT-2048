# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:57:29 2017

@author: Julien
"""

import NEATOrganism as Org

#node_list tests
#print('The basic: self.addNode(11, "youpi"), not for user:')
#org = Org.NEATOrganism(0,0)
#org.addNode(11, 'youpi')
#org.addNode(0, 'caca')
#org.addNode(25, 'this is a rather long character string maybe, I dont know, you tell me')
#
#
#org.printNodes()
#
#print()
#
#input("Brace yourselfs, intialiseNodes()!")
#
#for i in range(10):
#    org = Org.NEATOrganism(i,1)
#    org.initializeNodes()
#    org.printNodes()
#
#for i in range(10):
#    org = Org.NEATOrganism(1,i)
#    org.initializeNodes()
#    org.printNodes()
#
print("Adding nodes and sorting them")
org = Org.NEATOrganism(2,2)
org.initializeNodes()
org.addHiddenNode()
org.addHiddenNode()
org.printNodes()
print()
org.sortNodeListByIndex()
org.printNodes()


print("\n"+"---------Test getNode()---------")
node = org.getNode(0)
node.printNode()
node = org.getNode(1000001)
node.printNode()
node = org.getNode(1)
node.printNode()
node = org.getNode(4)
node.printNode()


print()
print('------Test Random node:---------')
print('Test random input')
for i in range(100):
    node = org.getRandomInputNode()
    node.printNode()
print()
print('Test random output')
for i in range(100):
    node = org.getRandomOutputNode()
    node.printNode()
    
print()
print("Test getFirstOutputNodeIndex")
org.printNodes()
ind = org.getFirstOutputNodeIndex()
print(ind)
org.node_list[ind].printNode()