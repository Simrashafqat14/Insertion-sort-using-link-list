class Node: 
 def __init__(self, data): 
 self.data = data 
 self.next = None
 
def Insert(Start, new_data):
 new_node = Node(0)
 new_node.data = new_data 
 new_node.next = Start
 Start = new_node
 return Start 

def lstSortByInsertion(Start):
 sort = None
 temp = Start
 while (temp != None): 
 nxt = temp.next
 sort = ForSorted(sort,temp) 
 temp = nxt
 Start = sort
 return Start

def ForSorted(Start, new_node):
	 temp = None
 if (Start == None or Start.data >= new_node.data):
	 new_node.next = Start
	 Start = new_node
 else: 
	 temp = Start
 while (temp.next != None and
	 temp.next.data < new_node.data):
	 temp = temp.next
	 new_node.	next = temp.next
	 temp.next = new_node
 return Start

def printList(string,head):
	 temp = head
	 print(string)
	 while(temp != None):
	 print( temp.data, end = " ")
	 temp = temp.next
 
unsorted = None
unsorted = Insert(unsorted,7)
unsorted = Insert(unsorted,85)
unsorted = Insert(unsorted,89)
unsorted = Insert(unsorted,65)
unsorted = Insert(unsorted,8)
unsorted = Insert(unsorted,30)
unsorted = Insert(unsorted,50)
printList("Linked_List before sorting",unsorted)
Sorted = lstSortByInsertion(unsorted)
print()
printList("Linked_List after sorting",Sorted)