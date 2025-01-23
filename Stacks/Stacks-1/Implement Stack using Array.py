Problem Desciption

Implement a Stack Data Structure

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle, where the most recently added element is the first to be removed. Your task is to implement a stack with the following functionalities:

Push an Element (push): Add an element to the top of the stack.
Pop an Element (pop): Remove and return the top element from the stack. If the stack is empty, raise an error.
Peek (peek): Retrieve the top element of the stack without removing it. If the stack is empty, raise an error.
Check if Empty (is_empty): Return True if the stack is empty; otherwise, return False.
Get Stack Size (size): Return the number of elements currently in the stack.
Input:

The input to your program will consist of a sequence of operations performed on the stack, such as:

push x to push an integer x onto the stack.
pop to remove the top element.
peek to view the top element without removing it.
is_empty to check if the stack is empty.
size to get the number of elements in the stack.


Output:

For push, there is no output.
For pop and peek, return the corresponding element or raise an error if the stack is empty.
For is_empty, return True or False.
For size, return the count of elements in the stack.
Constraints:

The stack should handle a dynamic number of operations.
Operations like pop and peek should raise an appropriate error if performed on an empty stack.

  
==============================
CODE:
==============================

class Stack:
def __init__(self):
  self.stack = []

def push(self, val):
  #append val to stack
  self.stack.append(val)

def pop(self):
  #remove and print the top val from stack
  if len(self.stack) > 0:
    return self.stack.pop()
  else:
    raise IndexError("Can't pop from empty stack")

def peek(self):
  #print the topmost element fromthe stack
  if len(self.stack) > 0:
    return self.stack[-1]
  else:
    raise IndexError("Can't access an empty stack")

def is_empty(self):
  #check is stack is empty 
  return len(self.stack) == 0

def size(self):
  #check lenght of stack
  return len(self.stack)



# Create a stack instance
stack = Stack()

# Push elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Get the top element
print(stack.peek())  # Output: 30

# Pop an element
print(stack.pop())   # Output: 30

# Check size of the stack
print(stack.size())  # Output: 2

# Check if the stack is empty
print(stack.is_empty())  # Output: False
