# this line allows for the future resolution of type hints, which is a fancy way of saying that it allows for the use of type hints before the actual definition of the type.
from __future__ import annotations

# this line imports the random module, which is used to generate random numbers.
import random

# this imports the Iterator, List, Tuple and TYPE_CHECKING. Iterator is a type hint used to indicate that an object is an iterator which can be iterated over using a loop or other iteration mechanism. It represents a sequence of values that can be accessed one by one. List if a generic type hint used to indicate a list, which is an ordered collection of items. It represents a mutable sequence. Tuple is a generic type hint used to indicate a tuple which is an ordered collection of elements. It represents an immutable sequence. TYPE_CHECKING is a special constant used to indicate that a type hint should be resolved as if the code was being run by the type checker rather than the interpreter. This is used to avoid circular imports. For example, if module A imports module B and module B imports module A, then the interpreter will fail to import either module. However, if module A imports module B and module B imports module A but only uses type hints from module A, then the interpreter will be able to import both modules.
from typing import Iterator, List, Tuple, TYPE_CHECKING

# import tcod
import tcod

# import GameMap from game_map.py
from game_map import GameMap

# import tile_types.py
# Once imported, you can access the names defined in tile_types.py using the syntax tile_types.name, where name is the specific name defined in the module. For example, if tile_types.py defines a variable floor, you can access it as tile_types.floor
import tile_types

# this statement is used to conditionally import the Entity class from the Entity module. In Python when the interpreter encounters an import statement, it immediately imports the specified module and exectes its code. However, during static type checking with tools like mypy (which is a static type checker for Python, static type checking is the process of verifying of variables, function, and parameters, and return values at compile time or before the code is executed. It helps catch typ-related errors and proovides better code understanding and documentation. Python is a dynamically typed language, variable types are typically determined at runetime. However, by using type hints, you can add type annotationd to your code to procide hints about the expected typed of variables, function parameters, and return values.). Mypy is a tool that analyzes Python code with type hints and performs static type checking to detect type errors and provide more comprehensive type-related information. It analyzes the type hints and flags potential type inconsistencies, such as assigning a value of the wrong type to a variable or passing incorrect types of arguments to functions. So the reason for this statement is to check to see if Entity is used as a type hint and if it is, then import it. This is done to avoid circular imports.
if TYPE_CHECKING:
    from entity import Entity

# defining variables with self creates an instance variable unique to each instance object, so each instance will have their own indivudual copy of the variable.
class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    # the '@property' decoration allows us to access the function as if it were an attribute of the class or the object of the class (so we can do 'room.center' instead of 'room.center()')
    # the Tuple[int, int] is a type hint that indicates that the function returns a tuple of two integers. A tuple is an ordered, immutable collection of values enclosed in parentheses.
    @property
    def center(self) -> Tuple[int, int]:
        # this is a variable declaration center_x is set equal to the value of self.x1 + self.x2 / 2 and type cast as an int. x1 and x2 (x1 + height) represent the left and right boundaries of the room. y1 and y2 (y1 + height) represent the vertical boundaries of the room. this method calculates the center of the room and returns the center point as a tuple
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    # the '@property' decoration allows us to access the function as if it were an attribute of the class or the object of the class (so we can do 'room.inner' instead of 'room.inner()')

    # Tuple[slice, slice] is a return type hint that indicates that the method will return a tuple of two slice objects. A slice object represents a range of indices used for slicing sequences like strings, lists, or arrays. Here each slice would correspond to the inner area of the rectangular room. The first slice would represent the x-coordinate range(left to right) of the inner area and the second slice represents the y-coordinate range (top to bottom) of the inner area
    @property
    def inner(self) -> Tuple[slice, slice]:
        # A slice is an object that represents a range of indices used for slicing like strings, lists, or arrays

        # The inner method returns a tuple of two slices where each slice corresponds to the inner area of the rectangular room. The first slice represents the x-coordinate range(left-to-right) and the second slice represents the y-coordinate range(top-to-bottom)

        """Return the inner area of this room as a 2D array index."""
        
        # this returns a slice object that represents coordinates of the inner area of the rectangular room. It is calculated by slice(self.x1, self.x2) this represents the coordinate point for the left and right boundaries of the room. "self.x1 + 1" takes x1 and adds 1 because x1 represents the leftmost column of the room and we want to exculde that from the inner area so we move one step to the right. We do the same thing with "self.y1 + 1"
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)
    
    def intersects(self, other: RectangularRoom) -> bool:
        """Return True if this room overlaps with another RectangularRoom."""
        return (
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 <= other.y2
            and self.y2 >= other.y1
        )
    
def tunnel_between(
    start: Tuple[int, int], end: Tuple[int, int]
) -> Iterator[Tuple[int, int]]:
    """Return an L-shaped tunnel between these two points."""
    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:  # 50% chance.
        # Move horizontally, then vertically.
        corner_x, corner_y = x2, y1
    else:
        # Move vertically, then horizontally.
        corner_x, corner_y = x1, y2

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y
    
def generate_dungeon(
    max_rooms: int,
    room_min_size: int,
    room_max_size: int,
    map_width: int,
    map_height: int,
    player: Entity,
) -> GameMap:
    """Generate a new dungeon map."""
    dungeon = GameMap(map_width, map_height)

    rooms: List[RectangularRoom] = []

    for r in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_height - 1)

        # "RectangularRoom" class makes rectangles easier to work with
        new_room = RectangularRoom(x, y, room_width, room_height)

        # Run through the other rooms and see if they intersect with this one.
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue  # This room intersects, so go to the next attempt.
        # If there are no intersections then the room is valid.

        # Dig out this rooms inner area.
        dungeon.tiles[new_room.inner] = tile_types.floor

        if len(rooms) == 0:
            # The first room, where the player starts.
            player.x, player.y = new_room.center
        else:  # All rooms after the first.
            # Dig out a tunnel between this room and the previous one.
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tile_types.floor

        # Finally, append the new room to the list.
        rooms.append(new_room)

    return dungeon