#using collections
import collections
queue1 = collections.deque()
# to add element
queue1.appendleft(10)
queue1.appendleft(20)
queue1.appendleft(30)
print(queue1)
# remove element
queue1.pop()
print(queue1)

#method 2
import collections
queue2 = collections.deque()
# to add element
queue2.append(10)
queue2.append(20)
queue2.append(30)
print(queue2)
# remove element
queue2.popleft()
print(queue2)


# using list
queue3 = []
def push1(num):
    queue3.append(num)
def pop1():
    if not queue3:
        print('stack is empty')
    else:
        queue3.pop(0)

push1(10)
push1(20)
push1(30)
print(queue3)
pop1()
print(queue3)

# method 2
queue4 = []
def push2(num):
    queue4.insert(0,num)
def pop2():
    if not queue4:
        print('stack is empty')
    else:
        queue4.pop()
push2(10)
push2(20)
push2(30)
print(queue4)
pop2()
print(queue4)