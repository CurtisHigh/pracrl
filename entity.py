# importing Tuple from the typing module
from typing import Tuple


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    # Defining the inititial attributes of the Entity class, type hinting them and assigning them to instance variables
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    # the move method accepts parameters dx and dy which are type hinted as integers and returns nothing. It then adds the dx and dy parameters to the x and y instance variables defined above, which updates the position of the entitiy.
    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy