from typing import List

from .relationship_tree import RelationshipTree

ADD_SPOUSE = "ADD_SPOUSE"
ADD_CHILD = "ADD_CHILD"
GET_RELATIONSHIP = "GET_RELATIONSHIP"


def command(
    tree: "RelationshipTree", op: str, args: List[str], silent=True, debug=False
):
    """
    Run command on tree
    """
    if debug:
        print(op, args)

    if op == ADD_SPOUSE:
        result = tree.add_spouse(*args)
    elif op == ADD_CHILD:
        result = tree.add_child(*args)
    elif op == GET_RELATIONSHIP:
        result = tree.get_relationship(*args)
    else:
        raise NotImplementedError(f"Operation {op} is not supported.")

    if not silent:
        print(result)
