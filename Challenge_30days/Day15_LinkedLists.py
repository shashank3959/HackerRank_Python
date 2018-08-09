# https://www.hackerrank.com/challenges/30-linked-list/problem


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        if head == None:
            head = Node(data)
            head.next = None
            return head
        else:
            current = head
            while current.next != None:
                current = current.next

            newNode = Node(data)
            newNode.next = None
            current.next = newNode
            return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);