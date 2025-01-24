Problem Description

Implement a Stack Using a Linked List

You are tasked with implementing a stack data structure using a linked list. A stack is a linear data structure that follows the Last In First Out (LIFO) principle, where the last element added to the stack is the first to be removed.

The stack should support the following operations:

Operations:
Push
Add a new element to the top of the stack.
Input: An integer or any value (val) to be pushed onto the stack.
Behavior: The new element becomes the top of the stack.
Complexity: O(1)


Pop
Remove and return the top element from the stack.
Output: The value of the element removed from the stack.
Behavior: The second-to-top element (if any) becomes the new top of the stack.
Error Case: Raise an exception if the stack is empty.
Complexity: O(1)

Peek
Get the value of the top element without removing it from the stack.
Output: The value of the top element.
Behavior: The stack remains unchanged.
Error Case: Raise an exception if the stack is empty.
Complexity: O(1)

Is Empty
Check if the stack is empty.
Output: Boolean (True if the stack is empty, otherwise False).
Complexity: O(1)

Length
Return the number of elements in the stack.
Output: An integer representing the size of the stack.
Complexity: O(1)

Input Format:
The input will be a series of operations performed on the stack. Each operation will be one of the following:

"push X": Push the value X onto the stack.
"pop": Remove the top value from the stack and return it.
"peek": Return the top value of the stack without removing it.
"is_empty": Check if the stack is empty.
"length": Return the number of elements in the stack.

Output Format:
The output will depend on the operations performed:

For "push X", no output is generated.
For "pop", "peek", "is_empty", and "length", output the corresponding result or raise an error if the operation is invalid (e.g., popping from an empty stack).

Example:
Input:

push 10
push 20
push 30
peek
pop
length
is_empty
pop
pop
is_empty
Output:

30
30
2
False
20
10
True

Constraints:

The stack will contain at most 10⁵ elements at any point.
Each operation will be executed in constant time O(1).
The stack must use a linked list as the underlying data structure, not an array or list.

Notes:
Handle edge cases, such as attempting to pop or peek from an empty stack.
Optimize for efficiency and memory usage, as the stack might grow very large.



========================
CODE:
========================
class Node:
  def __init__(self, X):
    self.data = X
    self.next = None

class Stack:
  def __init__(self ):
    self.head = None
    self.size = 0

  #append element to stack
  def push(self, val):
    newnode = Node(val) #create new Node
    newnode.next = self.head #point haed to topmost element already present in stack
    self.head = newnode #point head to new node created
    self.size += 1 #increment the size

  #pop from  stack
  def pop(self):

    if self.size == 0:
      raise IndexError("Can't pop from empty stack")

    item = self.head.data #store value of last append value in stack
    self.head = self.head.next #move pointer to next adress
    self.size -= 1 #decrement the size

    return item

  #print the topmost element from stack
  def peek(self):
    if self.size == 0:
      raise IndexError("Can't pop from empty stack")

    return self.head.data

  #check if stack is empty
  def is_empty(self):
    return self.size == 0

  #print size of stack
  def length(self):
    return self.size


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

# Check the stack size
print(stack.length())  # Output: 2

# Check if the stack is empty
print(stack.is_empty())  # Output: False

      
      
    

