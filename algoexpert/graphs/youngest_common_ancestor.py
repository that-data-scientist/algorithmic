# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class program:
    # This is an input class. Do not edit.
    class AncestralTree:
        def __init__(self, name):
            self.name = name
            self.ancestor = None

    # Time complexity - O(d1 + d2)
    # Space complexity - O(Max(d1, d2)
    def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
        depth_1 = getDepth(descendantOne)
        depth_2 = getDepth(descendantTwo)

        if depth_1 == 1:
            return descendantOne

        if depth_2 == 1:
            return descendantTwo

        if depth_1 > depth_2:
            for _ in range(depth_1 - depth_2):
                descendantOne = descendantOne.ancestor
        elif depth_2 > depth_1:
            for _ in range(depth_2 - depth_1):
                descendantTwo = descendantTwo.ancestor

        while descendantOne.ancestor is not None:
            if descendantOne == descendantTwo:
                return descendantOne

            descendantOne = descendantOne.ancestor
            descendantTwo = descendantTwo.ancestor

        if descendantOne == descendantTwo:
            return descendantOne


def getDepth(node):
    if node.ancestor is None:
        return 1

    return 1 + getDepth(node.ancestor)


class AncestralTree(program.AncestralTree):
    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        trees = new_trees()
        trees["A"].addDescendants(trees["B"], trees["C"])
        trees["B"].addDescendants(trees["D"], trees["E"])
        trees["D"].addDescendants(trees["H"], trees["I"])
        trees["C"].addDescendants(trees["F"], trees["G"])

        yca = program.getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"])
        print(yca)
        self.assertTrue(yca == trees["B"])
