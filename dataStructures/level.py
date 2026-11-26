class Node:
    def __init__(self,value):
        self.left = None         #left side of node 
        self.data = value       
        self.right = None        # right side of node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,new_node):
        if self.root is None:     #check if tree is empty if yes new_node becomes root , creating root node
            self.root = new_node
            return 

        else:
            temp = self.root   #we need to traverse tree to find correct position for new_node ,so we cant loose root value so we are storing it 

            while True:        #cause we dont need how many iterations it will take to find correct position
                if new_node.data < temp.data:        #for left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return    #once node is inserted successfully we can return   
                    else:         #if it is not empty we will travel next branch 
                        temp=temp.left
                elif new_node.data >=temp.data:            #for right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self,temp):  #recursive method
        if temp is None:
            return
        else:
            self.inorder(temp.left)  
            print(temp.data,end=" ")
            self.inorder(temp.right)

             
    def level_order(self,rt):
        if rt is None:
            print("BST is empty")
            return
        arr=[]   #for keeping all nodes level wise

        cnt=0  #for counting visited nodes
        # for getting number of level on which the nodes are present
        level=0  
        
        arr.append(rt)
        while cnt<len(arr):
            node_count=len(arr)-cnt  # number of nodes to be visited
            print("\n Level:",level,end=" ")
            for i in range(node_count):   #will run until the number of noes in the loop



                temp=arr[cnt]
                cnt+=1
                print(temp.data, end=" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right) 
            level+=1           
        print("\nHeight of the tree is :",level)
   

BST=BinarySearchTree()
BST.insert(Node(100))
BST.insert(Node(10))
BST.insert(Node(450))
BST.insert(Node(4))
BST.insert(Node(65))
BST.insert(Node(300))
BST.insert(Node(500))


print("level order")
BST.level_order(BST.root)


