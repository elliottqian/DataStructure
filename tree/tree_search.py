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
        self.data_list[self.point] = data

    def pop(self):
        if self.point <= -1:
            print("the stack is empty")
            return
        r = self.data_list[self.point]
        self.point -= 1
        return r


def pre_order_traversal(root):
    stack = Stack()

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


