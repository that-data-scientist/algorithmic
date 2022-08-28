# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!
import unittest


# Num words - n
# Num letters in each word - n

class SuffixTrie:
    def __init__(self) -> None:
        self.root_node = {}
        self.end_symbol = '*'

    # Time complexity - O(nm)
    # Space complexity - O(nm)
    def add_word(self, word):
        current_node = self.root_node

        for character in word:
            if character not in current_node:
                current_node[character] = {}
            current_node = current_node[character]

        current_node[self.end_symbol] = word


# Time complexity - O(8^s)
# Space complexity - O(wh)
def explore(board, i, j, trie_node, visited, final_words):
    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
        return

    if visited[i][j]:
        return

    letter = board[i][j]

    if letter not in trie_node:
        return

    trie_node = trie_node[letter]
    if "*" in trie_node:
        final_words[trie_node["*"]] = True

    visited[i][j] = True

    explore(board, i + 1, j, trie_node, visited, final_words)
    explore(board, i - 1, j, trie_node, visited, final_words)
    explore(board, i, j + 1, trie_node, visited, final_words)
    explore(board, i, j - 1, trie_node, visited, final_words)
    explore(board, i + 1, j - 1, trie_node, visited, final_words)
    explore(board, i - 1, j + 1, trie_node, visited, final_words)
    explore(board, i + 1, j + 1, trie_node, visited, final_words)
    explore(board, i - 1, j - 1, trie_node, visited, final_words)

    visited[i][j] = False


def boggleBoardV2(board, words):
    trie = SuffixTrie()
    for word in words:
        trie.add_word(word)

    final_words = {}
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            explore(board, i, j, trie.root_node, visited, final_words)

    return list(final_words.keys())


# Time complexity - O(n*w*h*8^s)
# Space complexity - O(wh * nm)
def boggleBoard(board, words):
    valid_words = []

    for word in words:
        optional_word_found = check_word(board, word)

        if optional_word_found is not None:
            valid_words.append(optional_word_found)

    return valid_words


def check_word(board, word):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            is_word_found = dfsUtil(board, i, j, word, 0, visited)

            if is_word_found:
                return word
    return None


def dfsUtil(board, i, j, word, index, visited):
    if index >= len(word):
        return False

    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
        return False

    if visited[i][j]:
        return False

    if board[i][j] != word[index]:
        return False

    if index == len(word) - 1:
        return True

    visited[i][j] = True

    is_word_found = (
            dfsUtil(board, i + 1, j, word, index + 1, visited) or
            dfsUtil(board, i - 1, j, word, index + 1, visited) or
            dfsUtil(board, i, j + 1, word, index + 1, visited) or
            dfsUtil(board, i, j - 1, word, index + 1, visited) or
            dfsUtil(board, i + 1, j + 1, word, index + 1, visited) or
            dfsUtil(board, i - 1, j - 1, word, index + 1, visited) or
            dfsUtil(board, i + 1, j - 1, word, index + 1, visited) or
            dfsUtil(board, i - 1, j + 1, word, index + 1, visited)
    )

    visited[i][j] = False
    return is_word_found


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        board = [
            ["t", "h", "i", "s", "i", "s", "a"],
            ["s", "i", "m", "p", "l", "e", "x"],
            ["b", "x", "x", "x", "x", "e", "b"],
            ["x", "o", "g", "g", "l", "x", "o"],
            ["x", "x", "x", "D", "T", "r", "a"],
            ["R", "E", "P", "E", "A", "d", "x"],
            ["x", "x", "x", "x", "x", "x", "x"],
            ["N", "O", "T", "R", "E", "-", "P"],
            ["x", "x", "D", "E", "T", "A", "E"],
        ]
        words = ["this", "is", "not", "a", "simple", "boggle", "board", "test",
                 "REPEATED", "NOTRE-PEATED"]
        expected = ["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]
        actual = boggleBoardV2(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)

    def test_case_2(self):
        board = [
            ['c', 'a', 't'],
            ['a', 'p', 'a'],
            ['t', 'u', 'l'],
            ['x', 'x', 't']
        ]
        words = ["cat", "catapult"]
        expected = ["cat", "catapult"]
        actual = boggleBoardV2(board, words)
        self.assertEqual(len(actual), len(expected))
        for word in actual:
            self.assertTrue(word in expected)
