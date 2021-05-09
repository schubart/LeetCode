from typing import Dict


class Node:
    def __init__(self) -> None:
        self.children: Dict[str, Node] = {}
        self.terminal: bool = False


# noinspection PyPep8Naming
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            # Ensure next node exists.
            if char not in node.children:
                node.children[char] = Node()
            # Get next node.
            node = node.children[char]

        # Mark last node as terminal.
        node.terminal = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            node = node.children.get(char, None)
            if node is None:
                return False

        return node.terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            node = node.children.get(char, None)
            if node is None:
                return False

        return True
