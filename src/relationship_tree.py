from .tree import Tree


class RelationshipTree(Tree):
    """
    Family tree that supports finding relationships between tree nodes.
    """

    def __init__(self, root_name, root_gender) -> None:
        super().__init__(root_name, root_gender)

    def get_relationship(self, name: str, relationship: str):
        """
        Get related node name
        """
        node = self.find_node(name)
        result = []

        if not node:
            return "PERSON_NOT_FOUND"

        if relationship == "Mother":
            result = [node.mother.name]
        elif relationship == "Father":
            result = [node.father.name]
        elif (
            relationship == "Husband"
            or relationship == "Wife"
            or relationship == "Spouse"
        ):
            result = [node.spouse.name]
        elif relationship == "Son":
            result = [child.name for child in node.children if child.gender == "Male"]
        elif relationship == "Daughter":
            result = [child.name for child in node.children if child.gender == "Female"]
        elif relationship == "Siblings":
            result = []
            if node.mother:
                result = [
                    child.name
                    for child in node.mother.children
                    if child.name != node.name
                ]
        elif relationship == "Mother-In-Law":
            result = []
            if node.spouse and node.spouse.mother:
                result = [node.spouse.mother.name]
        elif relationship == "Father-In-Law":
            if node.spouse and node.spouse.father:
                result = [node.spouse.father.name]
        elif relationship == "Daughter-In-Law":
            sons = [child for child in node.children if child.gender == "Male"]
            result = [son.spouse.name for son in sons if son.spouse]
        elif relationship == "Son-In-Law":
            daughters = [child for child in node.children if child.gender == "Female"]
            result = [daughter.spouse.name for daughter in daughters if daughter.spouse]
        elif relationship == "Paternal-Uncle":
            father = node.father
            if father and (father.mother or father.father):
                grandparent = father.mother or father.father
                result = [
                    sibling.name
                    for sibling in grandparent.children
                    if sibling.gender == "Male" and sibling.name != father.name
                ]
        elif relationship == "Maternal-Uncle":
            mother = node.mother
            if mother and (mother.mother or mother.father):
                grandparent = mother.mother or mother.father
                result = [
                    sibling.name
                    for sibling in grandparent.children
                    if sibling.gender == "Male"
                ]
        elif relationship == "Paternal-Aunt":
            father = node.father
            if father and (father.mother or father.father):
                grandparent = father.mother or father.father
                result = [
                    sibling.name
                    for sibling in grandparent.children
                    if sibling.gender == "Female"
                ]
        elif relationship == "Maternal-Aunt":
            mother = node.mother
            if mother and (mother.mother or mother.father):
                grandparent = mother.mother or mother.father
                result = [
                    sibling.name
                    for sibling in grandparent.children
                    if sibling.gender == "Female" and sibling.name != mother.name
                ]
        elif relationship == "Brother-In-Law":
            spouses_brothers = []
            if node.spouse and node.spouse.mother:
                spouses_brothers = [
                    sibling.name
                    for sibling in node.spouse.mother.children
                    if sibling.gender == "Male" and sibling.name != node.spouse.name
                ]
            siblings_husbands = []
            if node.mother:
                siblings_husbands = [
                    sibling.spouse.name
                    for sibling in node.mother.children
                    if sibling.gender == "Female" and sibling.spouse
                ]
            result = spouses_brothers + siblings_husbands
        elif relationship == "Sister-In-Law":
            spouses_sisters = []
            if node.spouse and node.spouse.mother:
                spouses_sisters = [
                    sibling.name
                    for sibling in node.spouse.mother.children
                    if sibling.gender == "Female" and sibling.name != node.spouse.name
                ]
            siblings_wives = []
            if node.mother:
                siblings_wives = [
                    sibling.spouse.name
                    for sibling in node.mother.children
                    if sibling.gender == "Male" and sibling.spouse
                ]
            result = spouses_sisters + siblings_wives
        else:
            raise NotImplementedError(f"Relationship {relationship} not supported.")

        return " ".join(result) if result else "NONE"
