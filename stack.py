#using collections module
import collections

stack1 = collections.deque()
# to add element
stack1.append(10)
stack1.append(20)
stack1.append(30)
print(stack1)
# to check the top element of the stack
stack1[-1]
# to delete element
stack1.pop()
print(stack1)
# to check whether stack is empty or not
if stack1:
    print('true')
else:
    print('false')


#using the lists
stack2 = []
def push(num):
    stack2.append(num)
def pop():
    if not stack2:
        print('stack is empty')
    else:
        stack2.pop()
        
push(10)
push(20)
push(30)
print(stack2)
pop()
print(stack2)