import random
# Helper Functions:
class Node():

    def __init__(self, d) -> None:
        self.d = d
        self.next = None

    def append(self, node):
        n = self
        while(n.next != None):
            n = n.next
        n.next = node

def makeRandomLinkedList(l):
    if(l == 0): return None
    head = Node(random.randint(0,9))
    n = head
    for i in range(l-1):
        n.next = Node(random.randint(0,9))
        n = n.next
    return head

def printLinkedList(h):
    n = h
    while(n != None):
        print(n.d,"->",end=" ")
        n = n.next
    print("Null")

def makeLinkedList_String(input):
    head = Node(input[0])
    curr = head
    for i in range(1, len(input)):
        curr.next = Node(input[i])
        curr = curr.next
    return head

# Answers to Chapter questions:
def removeDups_with_buffer(h):
    if(h == None): return
    n = h
    encountered = dict()
    encountered[n.d] = 1
    while(n.next != None):
        if(n.next.d in encountered):
            n.next = n.next.next
        else:
            n = n.next
            encountered[n.d] = 1
# O(n)

def removeDups_without_buffer(h):
    p1 = h
    p2 = h
    while(p1.next != None):
        while(p2.next != None):
            if(p1.d == p2.next.d):
                p2.next = p2.next.next
            else:
                p2 = p2.next
        p1 = p1.next
        p2 = p1
# O(n**2)

# myHead = makeRandomLinkedList(10)
# printLinkedList(myHead)
# removeDups_with_buffer(myHead)
# printLinkedList(myHead)

def removeMiddleNode(h):
    p1 = h
    p2 = h.next
    incrementP1 = False
    while(p2.next != None):
        p2 = p2.next
        if(incrementP1): p1 = p1.next
        incrementP1 = ~(incrementP1)
        print("p1:",p1.d," p2:",p2.d)
    p1.next = p1.next.next

# myHead = makeRandomLinkedList(10)
# printLinkedList(myHead)
# removeMiddleNode(myHead)
# printLinkedList(myHead)

def sumLists(a: Node, b: Node) -> Node :
    sum_head = Node
    carry = 0
    a_Node = a
    b_Node = b
    sum_Node = sum_head
    while(a_Node != None or b_Node != None):
        sum_Node.d = carry
        if(a_Node != None):
            sum_Node.d += a_Node.d
            a_Node = a_Node.next
        if(b_Node != None):
            sum_Node.d += b_Node.d
            b_Node = b_Node.next
        carry = sum_Node.d // 10
        sum_Node.d = sum_Node.d % 10
        if(a_Node != None or b_Node != None):
            sum_Node.next = Node(0)
        if(carry):
            sum_Node.next = Node(carry)        
        sum_Node = sum_Node.next
    return sum_head

# myHead_A = makeRandomLinkedList(3)
# myHead_B = makeRandomLinkedList(3)
# print("A:")
# printLinkedList(myHead_A)
# print("B:")
# printLinkedList(myHead_B)
# print("sum:")
# mySum = sumLists(myHead_A,myHead_B)
# printLinkedList(mySum)

def reverseLinkedList(head: Node) -> Node:
    prev = None
    curr = head
    while(curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev

# myHead = makeRandomLinkedList(6)
# print("A:")
# printLinkedList(myHead)
# rev_myHead = reverseLinkedList(myHead)
# print("Reverse of A:")
# printLinkedList(rev_myHead)

def rev_sumLists(a: Node ,b: Node) -> Node:
    rev_a = reverseLinkedList(a)
    rev_b = reverseLinkedList(b)
    return reverseLinkedList(sumLists(rev_a, rev_b))

# myHead_A = makeRandomLinkedList(3)
# myHead_B = makeRandomLinkedList(3)
# print("A:")
# printLinkedList(myHead_A)
# print("B:")
# printLinkedList(myHead_B)
# print("sum in reverse:")
# mySum = rev_sumLists(myHead_A,myHead_B)
# printLinkedList(mySum)

def isPalindrome(a: Node) -> bool:
    rev_a = reverseLinkedList(a)
    a_Node = a
    while(a_Node != None):
        if(a_Node.d != rev_a.d): return False
        a_Node = a_Node.next
        rev_a = rev_a.next
    return True
#Time Complexity: O(n)

def getIntersect(a: Node, b: Node) -> Node:
    
    def getLLInfo(head: Node) -> list:
        itr = head
        length = 0
        rootNode = None
        while(itr):
            length += 1
            rootNode = itr
            itr = itr.next
        return [length, rootNode]
    
    a_Info = getLLInfo(a)
    b_Info = getLLInfo(b)

    if(a_Info[1] != b_Info[1]):
        return None
    
    a_itr = a
    b_itr = b

    if(a_Info[0] < b_Info[0]):
        for i in range( b_Info[0] - a_Info[0]):
            b_itr = b_itr.next
    
    if(a_Info[0] > b_Info[0]):
        for i in range( a_Info[0] - b_Info[0]):
            a_itr = a_itr.next
        
    while(True):
        if(a_itr == b_itr):
            return a_itr
        a_itr = a_itr.next
        b_itr = b_itr.next


# myHead1 = makeLinkedList_String("apple")
# myHead2 = makeLinkedList_String("pumpkin")
# myHead3 = makeLinkedList_String("Pie")

# myHead1.append(myHead3)
# myHead2.append(myHead3)

# print("Inputs:")
# printLinkedList(myHead1)
# printLinkedList(myHead2)

# print("Intersect:")
# intersectedNode = getIntersect(myHead1, myHead2)
# print(intersectedNode)
# printLinkedList(intersectedNode)

def loopDetection(head: Node):
    itr_slow = head
    itr_fast = head
    while(True):
        itr_slow = itr_slow.next
        itr_fast = itr_fast.next
        if(itr_fast == None): return False
        itr_fast = itr_fast.next
        if(itr_fast == None): return False
        if(itr_slow == itr_fast): break
    itr_slow = head
    while(True):
        itr_slow = itr_slow.next
        itr_fast = itr_fast.next
        if(itr_slow == itr_fast): return itr_slow
        

myHead1 = makeLinkedList_String("apple")
myHead2 = makeLinkedList_String("pumpkin")
myHead3 = makeLinkedList_String("Pie")

myHead1.append(myHead3)
myHead1.append(myHead2)
myHead1.append(myHead3)

print("Loop starts at:")
print(loopDetection(myHead1).d)
