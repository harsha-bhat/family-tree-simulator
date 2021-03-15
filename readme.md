# Family Tree Simulator

This project simulates generating a family tree and find various relationships between nodes.

## Supported Commands

```
ADD_CHILD "Mother_Name" "Child_Name" "Gender"
ADD_SPOUSE "Node_Name" "Spouse_Name"
GET_RELATIONSHIP "Node_Name" "Relationship"
```

Supported Relationships

```
Mother
Father
Husband
Wife
Spouse
Son
Daughter
Siblings
Mother-In-Law
Father-In-Law
Daughter-In-Law
Son-In-Law
Maternal-Uncle
Paternal-Uncle
Maternal-Aunt
Paternal-Aunt
Sister-In-Law
Brother-In-Law
```

Examples

```
ADD_CHILD Satya Ketu Male
GET_RELATIONSHIP Kriya Paternal-Uncle
GET_RELATIONSHIP Satvy Brother-In-Law
```

## Running the Project

The project is initialized with the initialization data in `data\init.txt` and further commands could be passed
in as a text file into the command line.

```
python -m main data/test.txt
```
