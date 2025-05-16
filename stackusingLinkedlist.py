#stack using linkedlist :
class Node:
   def __init__(self,value):
      self.value=value
      self.next=None
class stack:
    def __init__(self):
       self.top=None
       self.count=0
    def push(self,item):
       New_node=Node(item)
       New_node.next=self.top
       self.top=New_node
       self.count+=1
    def pop(self):
       returned_value=self.top.value  
       self.top=self.top.next
       self.count-=1
       return returned_value  
    def display(self):
       current=self.top
       if current is None:
            print("Stack is empty")
            return
       else:
        while (current):
          
          print(current.value) 
          current=current.next    

if __name__== "__main__" :
  Stack=stack()
  Stack.push(5)
  Stack.display()
