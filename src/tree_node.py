from typing import List


class TreeNode:
    """
    Tree node for family tree
    """

    def __init__(
        self,
        name: str,
        gender: str,
        spouse: "TreeNode" = None,
        children: List["TreeNode"] = [],
        mother: "TreeNode" = None,
        father: "TreeNode" = None,
    ) -> None:
        self.name = name
        self.gender = gender
        self.spouse = spouse
        self.children = children
        self.mother = mother
        self.father = father
