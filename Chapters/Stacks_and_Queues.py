 #Stack and Queue implementation using linked lists
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class MyStack:
    def __init__(self) -> None:
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
    
    def pop(self):
        if(self.top):
            poppedNode = self.top
            self.top = self.top.next
            poppedNode.next = None
            return poppedNode.data
        else:
            return None
    
    def peek(self):
        if(self.top):
            return self.top.data
        return None
    
    def isEmpty(self):
        return(self.top == None)

class MyQueue:
    def __init__(self) -> None:
        self.input = None
        self.output = None
    
    def push(self, data):
        newNode = Node(data)
        if(self.isEmpty()):
            self.input = newNode
            self.output = newNode
        else:
            self.input.next = newNode
            self.input = newNode
    
    def pop(self):
        if(self.isEmpty()):
            return None
        else:
            poppedNode = self.output
            self.output = self.output.next
            poppedNode.next = None
            return poppedNode.data
        
    def peek(self):
        if(self.isEmpty()): return None
        return self.output.data
    
    def isEmpty(self):
        return(self.output == None or self.input == None)

#Q: 3.1
#Generalized into sub problem 
class ListStack():
    def __init__(self, size) -> None:
        self.size = size
        self.list = [0] * size
        self.top = 0

    def push(self, data):
        if(self.top < self.size):
            self.list[self.top] = data
            self.top += 1
        else:
            print("Stack Full")
    
    def pop(self):
        if(self.top > 0):
            self.top -= 1
            return self.list[self.top]
        else:
            print("Stack Empty")

    def peek(self):
        return self.list[self.top-1]
    
    def isEmpty(self):
        return (self.top == 0)
    
    def isFull(self):
        return (self.top >= self.size)
    
    def printList(self):
        for i in range(self.top):
            print(self.list[i])
    
#3.2
class MinStack(MyStack):
    def __init__(self) -> None:
        super().__init__()
        self.s2 = MyStack()

    def push(self, data):
        super().push(data)
        if(self.s2.isEmpty() or data<=self.min()):
            self.s2.push(data)
    
    def pop(self):
        data = super().pop()
        if(data == self.min()):
            self.s2.pop()
        return data

    def min(self):
        return self.s2.peek()
    
#Q3.3
#Let each sub stack be an array with max size n, we will reuse the list stack from Q3.1
class SetOfStacks:
    def __init__(self, size) -> None:
        if(size < 1): 
            print("Invalid Size!")
            return
        self.size = size
        self.stacks = [ListStack(self.size)]
    
    def push(self, data):
        if(self.stacks[-1].isFull()):
            self.stacks.append(ListStack(self.size))
        self.stacks[-1].push(data)  

    def pop(self):
        poppedItem = self.stacks[-1].pop()
        if(self.stacks[-1].isEmpty() and len(self.stacks)>1):
            self.stacks.pop()
        return poppedItem
        
    def isEmpty(self):
        return (self.stacks[-1].isEmpty() and len(self.stacks)==0)
    
    def peek(self):
        return self.stacks[-1].peek()
    
    def popAt(self, index):
        poppedItem = self.stacks[index].pop()
        print("Popped Item:",poppedItem)
        if(self.stacks[-1].isEmpty() and len(self.stacks)>1):
            self.stacks.pop()
        return poppedItem
    
    def printAll(self):
        for stack in self.stacks:
            stack.printList()
            print("--------")

#Q3.4
class QueueFromStack():
    def __init__(self) -> None:
        self.stackIn = MyStack()
        self.stackOut = MyStack()
        self.isStackInActive = True

    def flipStack(self):
        (stackA, stackB) = (self.stackIn, self.stackOut) if (self.isStackInActive) else (self.stackOut, self.stackIn)
        while(stackA.isEmpty() != True):
            stackB.push(stackA.pop())
        self.isStackInActive = not self.isStackInActive
    
    def push(self, data):
        if(self.isStackInActive):
            self.stackIn.push(data)
        else:
            self.flipStack()
            self.push(data)
    
    def pop(self):
        if(self.isStackInActive):
            self.flipStack()
            return self.pop()
        else:
            return self.stackOut.pop()
        
    def peek(self):
        if(self.isStackInActive):
            self.flipStack()
            return self.peek()
        else:
            return self.stackOut.peek()
        
    def isEmpty(self):
        return (self.stackIn.isEmpty() and self.stackOut.isEmpty())
        
#Q3.5
def sortStack(stack:MyStack):
    temp_stack = MyStack()
    while(not stack.isEmpty()):
        insertElement = stack.pop()
        while(temp_stack.isEmpty() == False and temp_stack.peek() > insertElement):
            stack.push(temp_stack.pop())
        temp_stack.push(insertElement)
    while(not temp_stack.isEmpty()):
        stack.push(temp_stack.pop())

class AnimalShelter():
    def __init__(self) -> None:
        self.dogQueue = MyQueue()
        self.catQueue = MyQueue()
        self.counter = 0
        
    def push(self, animal, name):
        if(animal.lower() == "dog"):
            self.dogQueue.push([self.counter, name])
            self.counter += 1
        else:
            self.catQueue.push([self.counter, name])
            self.counter += 1
    
    def pop(self):
        if(self.catQueue.isEmpty() and self.dogQueue.isEmpty()):
            return None

        if(not self.catQueue.isEmpty() and self.catQueue.peek()[0] < self.dogQueue.peek()[0]):
            return self.popCat()
        else:
            return self.popDog()
    
    def popCat(self):
        return self.catQueue.pop()[1]
    
    def popDog(self):
        return self.dogQueue.pop()[1]
    
