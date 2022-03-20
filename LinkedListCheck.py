#Node class
class Node:
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

#Linked list class
class LinkedList:
  def __init__(self):  
    self.head = None
      
  #Linked list head setter
  def setHead(self, newNode):
      self.head = newNode
  
  #Print linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

#Check for cycles in linked list
def checkCycle(LL):
    if (LL.head == None):
        return False
        
    firNode = LL.head
    secNode = LL.head
    
    while (firNode != None and firNode.next != None):
        firNode = firNode.next.next
        secNode = secNode.next
        
        if (firNode == secNode):
            return True
    
    return False

#Main function
def main():
    #Let's create our first linked list and set of nodes
    LL = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n1
    LL.setHead(n1)
    
    print("First Linked List:\n", checkCycle(LL)) #Check for cycles
    
    #Let's create our second linked list and set of nodes
    newLL = LinkedList()
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    
    n5.next = n6
    n6.next = n7
    n7.next = n8
    newLL.setHead(n5)
    
    print("Second Linked List:\n", checkCycle(newLL)) #Check for cycles
    

if __name__ == "__main__":
    main()

