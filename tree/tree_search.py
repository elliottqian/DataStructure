# -*- coding: utf-8 -*-

"""
the
Pre-Order Traversal,
In-Order Traversal
and Post-Order Traversal
of binary tree
"""


class Stack(object):

    data_list = []
    point = -1

    def __init__(self, point=-1):
        self.init(point)

    def init(self, point=-1):
        self.data_list = []
        self.point = point

    def push(self, data):
        """
        进栈操作
        :param data: 进栈数据
        """
        self.point += 1
        self.data_list.append(data)

    def pop(self):
        if self.point <= -1:
            print("the stack is empty")
            return
        r = self.data_list[self.point]
        self.point -= 1
        self.data_list = self.data_list[:-1]
        return r

    def is_empty(self):
        if len(self.data_list) == 0:
            return True
        else:
            return False


class Queue(object):

    def __init__(self):
        self.queue = []

    def go_in(self, data):
        self.queue.append(data)

    def go_out(self):
        r = self.queue[0]
        self.queue = self.queue[1:]
        return r


def pre_order_traversal(root_node):
    stack = Stack()
    temp_node = root_node
    while True:
        print()
        print("----------loop-----------------")
        if temp_node is not None:
            print("show search:", temp_node.weight)
            if temp_node.right is not None:
                stack.push(temp_node.right)
            temp_node = temp_node.left
        else:
            if stack.is_empty():
                break
            temp_node = stack.pop()
            pass


def in_order_traversal(root_node):
    stack = Stack()
    temp_node = root_node
    while True:
        while temp_node is not None:
            stack.push(temp_node)
            temp_node = temp_node.left
        temp_node = stack.pop()
        if temp_node is None:
            break
        print("show search:", temp_node.weight)
        temp_node = temp_node.right
        pass
    pass


if __name__ == "__main__":

    from tree.huffman_tree import Node, HuffmanTree
    node_1 = Node(weight=7, name='A')
    node_2 = Node(weight=5, name='B')
    node_3 = Node(weight=2, name='C')
    node_4 = Node(weight=4, name='D')

    in_node = [node_1, node_2, node_3, node_4]

    huffman_tree = HuffmanTree(in_node)
    root = huffman_tree.make_huffman_tree()

    print(root.right.right.right.weight)

    print("----------------------")
    in_order_traversal(root)
