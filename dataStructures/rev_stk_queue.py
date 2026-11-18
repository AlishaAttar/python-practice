#stack using linked list
class Node:
    def __init__(self, value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self, new_node):
        new_node.next=self.top
        self.top=new_node  
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp=self.top
            popped_data=temp.data
            self.top=self.top.next
        
            temp=None
            return popped_data
    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next
class Lqueue:
    def __init__(self):
        self.front=self.rear=None
    def isempty(self):
        return self.front is None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        dqued_data=temp.data
        self.front=self.front.next
        temp=None        
        if self.front==None:   #if there is only one node
            print("Queue is empty")
            self.rear=None
            temp=None
        return dqued_data_
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next 
        print()         
    def print(self):
        temp=self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp=temp.next

    def reverse_stack(s1):
        q1=Lqueue() 
        while not s1.isempty():  #pop from stack ad enqueue to queue
            q1.enqueue(Node(s1.pop()))
        q1.print()  
        while not q1.isempty():
            s1.push(Node(q1.dequeue()))
        s1.print()




st=stack()
st1=stack()
st.push(Node(10))
st.push(Node(100))
st.push(Node(45))
st.push(Node(78))
st.push(Node(90))
st.print()
st.pop()
st.print()
st.reverse()
st1.print()
reverse_stack(st)