from typing import List
from hashlib import md5


class TreeNode:
    """
    Tree node for family tree
    """

    GENDER_MALE = "Male"
    GENDER_FEMALE = "Female"

    def __init__(
        self,
        name: str,
        gender: str,
        spouse: "TreeNode" = None,
        children: List["TreeNode"] = [],
        mother: "TreeNode" = None,
        father: "TreeNode" = None,
    ) -> None:
        self.__name = name
        self.__gender = gender
        self.__spouse = spouse
        self.__children = children
        self.__mother = mother
        self.__father = father

    def __eq__(self, o: "TreeNode") -> bool:
        return self.__name == o.__name

    def __hash__(self) -> int:
        return int(md5(self.__name.encode("utf-8")).hexdigest(), 16)

    def get_name(self) -> str:
        return self.__name

    def is_female(self) -> bool:
        return self.__gender == TreeNode.GENDER_FEMALE

    def is_male(self) -> bool:
        return not self.is_female()

    def is_gender(self, gender) -> bool:
        return self.__gender == gender

    def spouse(self) -> "TreeNode":
        return self.__spouse

    def set_spouse(self, spouse: "TreeNode"):
        self.__spouse = spouse

    def get_children(self, gender=None, exclude=None) -> List["TreeNode"]:
        children = self.__children
        if gender:
            return [child for child in children if child.__gender == gender]
        if exclude:
            children.remove(exclude)
        return children

    def add_child(self, child: "TreeNode"):
        self.__children.append(child)

    def get_mother(self) -> "TreeNode":
        return self.__mother

    def get_father(self) -> "TreeNode":
        return self.__father

    def get_siblings(self, gender=None) -> List["TreeNode"]:
        siblings = []
        parent = self.get_mother() or self.get_father()
        if parent:
            return parent.get_children(gender, self)
        return siblings