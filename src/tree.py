from collections import deque

from .tree_node import TreeNode


class Tree:
    """
    Base family tree class
    """

    def __init__(self, root_name, root_gender) -> None:
        self.root = TreeNode(root_name, root_gender)

    def find_node(self, name: str) -> "TreeNode":
        """
        Find node in tree with given name
        """
        seen = set()

        queue = deque([self.root])
        node = None
        while queue:
            node = queue.popleft()
            if node and node not in seen:
                seen.add(node)
                if node.get_name() == name:
                    break
                queue.append(node.spouse())
                queue.extend(node.get_children())
        return node

    def add_spouse(self, to: str, spouse_name: str) -> None:
        """
        Add a spouse node to given node name
        """
        node = self.find_node(to)
        if not node:
            return "PERSON_NOT_FOUND"

        spouse_gender = TreeNode.GENDER_MALE
        if node.is_male():
            spouse_gender = TreeNode.GENDER_FEMALE

        spouse = TreeNode(
            spouse_name,
            spouse_gender,
            node,
            node.get_children(),
        )
        node.set_spouse(spouse)
        return "SPOUSE_ADDITION_SUCCEEDED"

    def add_child(self, to: str, child_name: str, child_gender: str) -> None:
        """
        Add a child node to given mother node name
        """
        node = self.find_node(to)
        if not node:
            return "PERSON_NOT_FOUND"

        if node.is_male():
            return "CHILD_ADDITION_FAILED"

        child = TreeNode(child_name, child_gender, None, [], node, node.spouse())
        node.add_child(child)
        return "CHILD_ADDITION_SUCCEEDED"
