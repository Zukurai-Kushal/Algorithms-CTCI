import random

# Graph Nodes have a value and a log of other nodes it points to
class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.children = []

class BinaryTreeNode():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

# In-order, Pre-order and Post-order traversals for binary Trees
def inOrderTraversals(root:BinaryTreeNode, func = lambda x:print(x)) -> None:
    if(root != None):
        inOrderTraversals(root.left)
        func(root.value)
        inOrderTraversals(root.right)

def preOrderTraversals(root:BinaryTreeNode, func = lambda x:print(x)) -> None:
    if(root != None):
        func(root.value)
        preOrderTraversals(root.left)
        preOrderTraversals(root.right)

def postOrderTraversals(root:BinaryTreeNode, func = lambda x:print(x)) -> None:
    if(root != None):
        postOrderTraversals(root.left)
        postOrderTraversals(root.right)
        func(root.value)

def generateRandomAdjList(size):
    adjList = []
    for index in range (size):
        currSet = set()
        for runs in range(random.randint(0,size-1)):
            currSet.add(random.randint(0,size-1))
        adjList.append(currSet)
    return adjList

def printAdjList(adjList):
    for index in range(len(adjList)):
        print(index,': ',end='')
        print(*adjList[index], sep=', ')

#Q4.1 (Graph is represented as an Adjacent List)
def getRouteBetweenNodes(a, b, graph):
    markedForA = {a}
    queueA = [([a],a)]
    markedForB = {b}
    queueB = [([b],b)]

    while(len(queueA) != 0 or len(queueB) != 0):
        if(len(queueA) != 0):
            (currPath,currNode) = queueA.pop(0)
            if(currNode == b):
                return currPath
            for child in graph[currNode]:
                if child not in markedForA:
                    markedForA.add(child)
                    newPath = currPath + [child]
                    queueA.append((newPath,child))
        if(len(queueB) != 0):
            (currPath,currNode) = queueB.pop(0)
            if(currNode == a):
                return currPath
            for child in graph[currNode]:
                if child not in markedForB:
                    markedForB.add(child)
                    newPath = currPath + [child]
                    queueB.append((newPath,child))
    return False

# Graph is randomly generated, lets check between node 0 and 5
def test_Q4_1():
    myGraph = generateRandomAdjList(size = 6)
    print("Randomized Adjacency List Graph:")
    printAdjList(myGraph)
    print("Route between nodes 0 and 5?")
    route = getRouteBetweenNodes(0,5,myGraph)
    if(route):
        print(*route, sep=' -> ')
        print("Ans : Exists")
    else:
        print("Ans : Does not Exist")

#Q4.2
def getMinimalBST(sortedList):
    if(len(sortedList) == 0):
        return None
    if(len(sortedList) == 1):
        return BinaryTreeNode(sortedList[0])
    midIndex = (round(len(sortedList)/2))-1
    leftArray = sortedList[:midIndex]
    rightArray = sortedList[midIndex+1:]
    node = BinaryTreeNode(sortedList[midIndex])
    node.left = getMinimalBST(leftArray)
    node.right = getMinimalBST(rightArray)
    return node

def test_Q4_2():
    mySortedList = [1,2,5,10,15,17]
    print("Sorted Array: ",mySortedList)
    myBinaryTree = getMinimalBST(mySortedList)
    print("In order traversal of resulting Binary Search Tree:")
    inOrderTraversals(myBinaryTree)

#Q4.3 
#Helper Class:
class LinkedListNode():
    def __init__(self, d) -> None:
        self.d = d
        self.next = None

    def append(self, node):
        n = self
        while(n.next != None):
            n = n.next
        n.next = node

def printLinkedList(h):
    n = h
    while(n != None):
        print(n.d,"->",end=" ")
        n = n.next
    print("Null")

def getListOfDepths_BFS(binaryTree:BinaryTreeNode):
    depthCounter = 0
    linkedLists = []
    linkedList = LinkedListNode('[D:'+str(depthCounter)+']')
    myQueue = [binaryTree, "new-depth"]
    while(myQueue):
        node = myQueue.pop(0)
        if(node == "new-depth"):
            linkedLists.append(linkedList.next)
            if(myQueue):
                depthCounter+=1
                linkedList = LinkedListNode('[D:'+str(depthCounter)+']')
                myQueue.append("new-depth")
            else:
                return linkedLists
        else:
            linkedList.append(LinkedListNode(node.value))
            if(node.left != None):
                myQueue.append(node.left)
            if(node.right != None):
                myQueue.append(node.right)
    return linkedLists

def getListOfDepths_DFS(binaryTree:BinaryTreeNode):
    linkedLists = {}
    def preOrderTraversalsMod(currDepth, node:BinaryTreeNode):
        if(node != None):
            if(currDepth not in linkedLists):
                linkedLists[currDepth] = LinkedListNode(node.value)
            else:
                linkedLists[currDepth].append(LinkedListNode(node.value))    
            preOrderTraversalsMod(currDepth + 1, node.left)
            preOrderTraversalsMod(currDepth + 1, node.right)
    preOrderTraversalsMod(0, binaryTree)
    return linkedLists

# Ans using BFS implementation
def test_Q4_3_BFS():
    #Let's reuse Q4.2 to generate our input Binary Tree
    myBinaryTree = getMinimalBST([1,2,5,10,15,17])
    linkedLists = getListOfDepths_BFS(myBinaryTree)
    for linkedList in linkedLists:
        printLinkedList(linkedList)

# Ans using DFS implementation
def test_Q4_3_DFS():
    myBinaryTree = getMinimalBST([1,2,5,10,15,17])
    linkedLists = getListOfDepths_DFS(myBinaryTree)
    for depth in linkedLists:
        print("[D:",depth,end='] ')
        printLinkedList(linkedLists[depth])

#We can use the getListOfDepths_BFS() function to create a print function to visualize our Binary Tree (Which I find to be so sick :D)
def printBinaryTree(binaryTree):
    linkedLists = getListOfDepths_BFS(binaryTree)
    height = len(linkedLists)
    padding = height
    for depth in range(len(linkedLists)):
        print("[D:",depth,end="] ")
        print(' '*(padding//2),end='')
        node = linkedLists[depth]
        while(node != None):
            print(node.d,end=' ')
            node = node.next
        print('')
        padding -= 1

#Q4.4
def isTreeBalanced(root:BinaryTreeNode):
    def postOrderTraversal_Q4_4(node:BinaryTreeNode):
        if(node == None):
            return 0
        else:
            leftHeight = postOrderTraversal_Q4_4(node.left)
            if(leftHeight == -1):
                return -1
            rightHeight = postOrderTraversal_Q4_4(node.right)
            if(rightHeight == -1):
                return -1
            difference = abs(leftHeight - rightHeight)
            if(difference > 1):
                return -1
            else:
                return max(leftHeight, rightHeight)+1
    rootHeight = postOrderTraversal_Q4_4(root)
    if(rootHeight == -1):
        return False
    else:
        return True
    
def test_Q_4_4():
    myBinaryTree = getMinimalBST([1,2,5,10,15,17])
    printBinaryTree(myBinaryTree)
    print("Is the Tree Balanced?:",isTreeBalanced(myBinaryTree))

    #Make the tree unbalanced
    print("\nAfter adding a new node:")
    myBinaryTree.left.right.right = BinaryTreeNode(12) 
    printBinaryTree(myBinaryTree)
    print("Is the Tree Balanced?:",isTreeBalanced(myBinaryTree))

    #An empty tree is balanced by definition
    print("\nEmpty Tree:")
    print("Is the Tree Balanced?:",isTreeBalanced(None))

#Q4.5
def isBST(root:BinaryTreeNode):
    if(root == None):
        return True
    def inOrderTraversal_Q_4_4(node):
        if(node != None):
            leftNode = inOrderTraversal_Q_4_4(node.left)
            if(leftNode == "Invalid"):
                return "Invalid"
            currValue = node.value
            rightNode = inOrderTraversal_Q_4_4(node.right)
            if(rightNode == "Invalid"):
                return "Invalid"
            if(leftNode == None and rightNode == None):
                return (currValue, currValue)
            elif(leftNode == None):
                if(currValue < rightNode[0]):
                    return (currValue, rightNode[1])
                else:
                    return "Invalid"
            elif(rightNode == None):
                if(leftNode[1] <= currValue):
                    return (leftNode[0], currValue)
                else:
                    return "Invalid"
            else:
                if(leftNode[1] <= currValue and currValue < rightNode[0]):
                    return (leftNode[0], rightNode[1])
                else:
                    return "Invalid"
    maxValue = inOrderTraversal_Q_4_4(root)
    if(maxValue == "Invalid"):
        return False
    else:
        return True

# Note: This method only works if we assume the tree cannot have duplicate values, 
#       if the right child has the same value as the parent then it would be an invalid BST.
#       left value <= current < right
def isBST_InOrderTraversal(root:BinaryTreeNode):
    if(root == None):
        return True
    sequence = []
    def inOrderTraversal_Q_4_4(node):
        if(node != None):
            inOrderTraversal_Q_4_4(node.left)
            sequence.append(node.value)
            inOrderTraversal_Q_4_4(node.right)
    inOrderTraversal_Q_4_4(root)
    prev = sequence[0]
    for i in sequence:
        if(i < prev):
            return False
        prev = i
    return True

def test_Q_4_5():
    myBinaryTree = getMinimalBST([1,2,5,10,15,17])
    printBinaryTree(myBinaryTree)
    print("Is it a Binary Search Tree?:",isBST(myBinaryTree))

    #Make the tree not a Binary Search Tree
    print("\nAfter adding a new node:")
    myBinaryTree.left.right.right = BinaryTreeNode(12) 
    printBinaryTree(myBinaryTree)
    print("Is it a Binary Search Tree?:",isBST(myBinaryTree))

    #An empty tree is a Binary Search Tree by definition
    print("\nEmpty Tree:")
    print("Is the Tree Balanced?:",isTreeBalanced(None))

test_Q_4_5()