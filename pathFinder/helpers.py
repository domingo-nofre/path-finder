from typing import Set, Any, Union
from anytree import Node, RenderTree

col_letters: str = "0ABCDEFGH"


def letter_to_number(letter):
    if letter == "A":
        return 1
    elif letter == "B":
        return 2
    elif letter == "C":
        return 3
    elif letter == "D":
        return 4
    elif letter == "E":
        return 5
    elif letter == "F":
        return 6
    elif letter == "G":
        return 7
    elif letter == "H":
        return 8
    return


def number_to_letter(n):
    return col_letters[n]


def calculate_next_movements(position):
    row = letter_to_number(position[0])
    column = int(position[1])
    # print("Row and column:")
    # print(row)
    # print(column)
    combinations: Set[Union[str, Any]] = set([])
    if row + 2 < 9 and column + 1 < 9:
        combinations.add(number_to_letter(row + 2) + str(column + 1))
    if row + 2 < 9 and column - 1 > 0:
        combinations.add(number_to_letter(row + 2) + str(column - 1))
    if row + 1 < 9 and column + 2 < 9:
        combinations.add(number_to_letter(row + 1) + str(column + 2))
    if row - 1 > 0 and column + 2 < 9:
        combinations.add(number_to_letter(row - 1) + str(column + 2))
    if row - 2 > 0 and column + 1 < 9:
        combinations.add(number_to_letter(row - 2) + str(column + 1))
    if row - 2 > 0 and column - 1 > 0:
        combinations.add(number_to_letter(row - 2) + str(column - 1))
    if row + 1 < 9 and column - 2 > 0:
        combinations.add(number_to_letter(row + 1) + str(column - 2))
    if row - 1 > 0 and column - 2 > 0:
        combinations.add(number_to_letter(row - 1) + str(column - 2))

    return combinations


def print_tree(tree):
    current = tree
    line = ""
    while not current.is_root:
        line = current.name + " " + line
        current = current.parent
    line = current.name + " " + line
    return line.strip()


def calculate_path(origin, destination):
    parent = Node(origin)
    visited = set()
    current = set()
    next_movements = calculate_next_movements(origin)
    for movement in next_movements:
        visited.add(movement)
        current.add(Node(movement, parent=parent))

    while destination not in visited:
        new_current = set()
        for actual_node in current:
            next_movements = calculate_next_movements(actual_node.name)
            for movement in next_movements:
                if movement not in visited:
                    visited.add(movement)
                    new_current.add(Node(movement, parent=actual_node))
        current = new_current.copy()

    for actual_node in current:
        if actual_node.name == destination:
            return print_tree(actual_node)
    return
