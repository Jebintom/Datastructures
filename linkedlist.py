class node:
    def __init__(self,data):
       self.data=data
       self.next=None
class LinkedList:
    def __init__(self):
               self.head=None
    def display(self):
          if not self.head:
                print("empty")
          current=self.head      
          while current:      
           
           print(current.data,"->",end=" ")
           current=current.next
    def addbegin(self,data):
              newnode=node(data)
              
              newnode.next=self.head
              self.head=newnode
    def addend(self,data):
          newnode=node(data)
          if not self.head:
                self.head=newnode
          current=self.head      
          while  current.next!=None:
                current=current.next
          current.next=newnode      
    def deleteend(self):
                
                current=self.head
                prev=None
                while current.next:
                       prev=current
                       current=current.next
                prev.next=None
    def addbtwn(self,data,key):
            newnode=node(data)
            current=self.head
            while current:
              if current.data==key:
                  newnode.next=current.next
                  current.next=newnode
                  return
              current = current.next
            else:
                  print("no key found") 
    def delstart(self):
          current=self.head
          self.head=current.next
if __name__=="__main__":
      ll=LinkedList()
      ll.addbegin(4)
      ll.addend(5)
      ll.addbtwn(7,5)
      ll.addbtwn(5,4)
      
      ll.display()

                             
                  
                  

          
                             
                     
                               
                      

        