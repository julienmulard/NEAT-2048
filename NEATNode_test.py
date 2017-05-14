# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:38:32 2017

@author: Julien
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 14:38:33 2017

@author: Julien
"""

import NEATNode as Nod

#Test init and print
print('Test init and print:')
print()
nod = Nod.NEATNode(0,'input')
print('nod.PrintNode():')
nod.printNode()
print()
print('nod.PrintNodeFull()')
nod.printNodeFull()
print()
nod = Nod.NEATNode(2,'hidden')
print('nod.PrintNode():')
nod.printNode()
print()
print('nod.PrintNodeFull()')
nod.printNodeFull()
print()

#Test copy
print('Test copy')
nod1 = Nod.NEATNode(1,'Output')
nod2 = nod1
print('nod1:')
nod1.printNodeFull()
print('nod2 = nod1:')
nod2 = nod1
nod2.printNodeFull()
print('if nod1/2 is modified, is nod2/1 too?')
print('nod1.type = "Youpi" -> nod1:')
nod1.type = 'Youpi'
nod1.printNodeFull()
print('nod2:')
nod2.printNodeFull()
print('Yes...')
print('nod2.value = 50 -> nod2:')
nod2.value = 50
nod2.printNodeFull()
print('nod1:')
nod1.printNodeFull()
print()
print('Now with copy: nod2 = nod1.copyNode()')
nod2 = nod1.copyNode()
print('nod1:')
nod1.printNodeFull()
print('nod2:')
nod2.printNodeFull()
print('nod1.index = 10 -> nod1:')
nod1.index = 10
nod1.printNodeFull()
print('nod2:')
nod2.printNodeFull()