# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        call_stack = [self]
        bfsUtil(call_stack, array)
        return array


# Time Complexity - O(v+e)
# Space complexity - O(v)
def bfsUtil(stack, array):
    if len(stack) == 0:
        return array

    node = stack[0]
    array.append(node.name)

    for child in node.children:
        stack.append(child)

    stack.remove(node)

    bfsUtil(stack, array)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        graph = Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]),
                         ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
