import re

from .tree import Tree
from .tree_node import TreeNode

SON = "Son"
DAUGHTER = "Daughter"
SIBLINGS = "Siblings"
PATERNAL = "Paternal"
MATERNAL = "Maternal"
UNCLE = "Uncle"
AUNT = "Aunt"
BROTHER = "Brother"
SISTER = "Sister"
IN_LAW = "In-Law"


class RelationshipTree(Tree):
    """
    Family tree that supports finding relationships between tree nodes.
    """

    def __init__(self, root_name, root_gender) -> None:
        super().__init__(root_name, root_gender)

    def get_direct_relation(self, node: "TreeNode", relationship: str):
        if relationship == SON:
            return node.get_children(TreeNode.GENDER_MALE)

        if relationship == DAUGHTER:
            return node.get_children(TreeNode.GENDER_FEMALE)

        if relationship == SIBLINGS:
            return node.get_siblings()

    def get_parent_relation(self, node: "TreeNode", relationship: str):
        result = []

        parent = node.get_father()
        if MATERNAL in relationship:
            parent = node.get_mother()

        gender = TreeNode.GENDER_MALE
        if AUNT in relationship:
            gender = TreeNode.GENDER_FEMALE

        if parent:
            result = parent.get_siblings(gender)

        return result

    def get_in_laws(self, node: "TreeNode", relationship: str):
        result = []
        spouse = node.spouse()

        gender = TreeNode.GENDER_MALE
        if re.search(SISTER, relationship):
            gender = TreeNode.GENDER_FEMALE

        if spouse:
            result += spouse.get_siblings(gender)

        siblings = node.get_siblings()
        result += [
            sibling.spouse() for sibling in siblings if not sibling.is_gender(gender)
        ]

        return result

    def get_relationship(self, name: str, relationship: str):
        """
        Get related node name
        """
        node = self.find_node(name)
        result = []

        if not node:
            return "PERSON_NOT_FOUND"

        if relationship in [SON, DAUGHTER, SIBLINGS]:
            result = self.get_direct_relation(node, relationship)

        if re.search(f"{UNCLE}|{AUNT}", relationship):
            result = self.get_parent_relation(node, relationship)

        if re.search(IN_LAW, relationship):
            result = self.get_in_laws(node, relationship)

        if not result:
            return "NONE"

        return " ".join([node.get_name() for node in result if node])
