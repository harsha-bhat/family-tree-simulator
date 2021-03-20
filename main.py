import sys

from src.relationship_tree import RelationshipTree
from src.util import command

INIT_FILE = "data/init.txt"

if __name__ == "__main__":
    tree = None

    # Initialize tree
    for line in open(INIT_FILE).readlines():
        line = line.strip()
        if line:
            op, *args = line.split()
            if op == "INIT":
                tree = RelationshipTree(*args)
            else:
                command(tree, op, args)

    # Run with test data
    for line in open(sys.argv[1]).readlines():
        line = line.strip()
        if line:
            op, *args = line.split()
            command(tree, op, args, silent=False)
