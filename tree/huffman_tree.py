# -*- coding: utf-8 -*-

"""
用Python来定义一个Huffman树

输入例子:
A:13,B:11,C:4,D:22

"""


class Node(object):
    """
    The Huffman Tree's Node Structure.
    """
    weight = None
    left = None
    right = None

    def __init__(self, left=None, right=None, weight=None, name=None):
        self.left = left
        self.right = right
        self.weight = weight
        self.name = name

    @staticmethod
    def sort_list(node_list):
        """
        Need to study the sorted function.
        :param node_list:
        :return:排好的列表
        """
        return sorted(node_list, key=lambda node: node.weight)


class HuffmanTree(object):

    def __init__(self, node_list):
        self.node_list = node_list

    def make_huffman_tree(self):
        while len(self.node_list) > 1:
            self.node_list = Node.sort_list(self.node_list)

            print("debug: before make node")
            for x in self.node_list:
                print(x.weight)

            temp_weight = self.node_list[0].weight + self.node_list[1].weight
            new_node = Node(weight=temp_weight)
            new_node.left = self.node_list[0]
            new_node.right = self.node_list[1]

            self.node_list.append(new_node)
            self.node_list = self.node_list[2:]

            print("debug: one time")
            for x in self.node_list:
                print(x.weight)
        print("debug: the loop is over!")
        return self.node_list[0]

if __name__ == "__main__":
    node_1 = Node(weight=7, name='A')
    node_2 = Node(weight=5, name='B')
    node_3 = Node(weight=2, name='C')
    node_4 = Node(weight=4, name='D')

    in_node = [node_1, node_2, node_3, node_4]

    huffman_tree = HuffmanTree(in_node)
    root = huffman_tree.make_huffman_tree()

    print(root.left.name)
    print(root.right.left.name)
    print(root.right.right.left.name)
    print(root.right.right.right.name)
    pass
