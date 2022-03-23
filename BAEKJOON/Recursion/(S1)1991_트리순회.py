import sys
import string

class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right

def preorder(n):
    if n is not None:
        print(n.item, end = '')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.item, end = '')        
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)             
        postorder(n.right)
        print(n.item, end = '')


input = sys.stdin.readline
N = int(input())
li = [map(str, input().rstrip().split()) for _ in range(N)]
alphabet = string.ascii_uppercase

alpha_list = [alphabet[i] for i in range(N)]
node_list = [i for i in range(N)]
alpha_index = dict(zip(alpha_list, node_list))

while li:
    p, left, right = li.pop()
    p_node = Node(p)
    if left != '.':
        p_node.set_left(alpha_list[alpha_index[left]])
    if right != '.':
        p_node.set_right(alpha_list[alpha_index[right]])
    alpha_list[alpha_index[p]] = p_node
    
preorder(alpha_list[0])
print()
inorder(alpha_list[0])
print()
postorder(alpha_list[0])
print()