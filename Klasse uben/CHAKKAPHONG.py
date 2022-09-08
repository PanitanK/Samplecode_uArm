class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
      self.prevval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thu")
e5 = Node("Fri")
# Link Nodes
list1.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5

# revval addition

list1.headval.prevval = e5 
e2.prevval = list1.headval
e3.prevval = e2
e4.prevval = e3 
e5.prevval = e4

print(e5.prevval.dataval)