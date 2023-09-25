# Imports the numpy library and assigns it to the variable np. Numpy is a python library that provides support for numerical computations and array operations and mathematical functions.

# The 'type: ignore' comment tells type checkers to ignore any type errors related to the numpy import allowing the code to be checked for type errors without raising issues. This is necessary because numpy is not a pure python library and therefore does not have type hints.

import numpy as np  # type: ignore

# Imports the Console class from the tcod.console module. The Console class is used to create a console object which is used to display text and graphics on the screen.
from tcod.console import Console

# This statement imports the tile_types.py functions and variables, which allows for their use in this file.
import tile_types

# Declares the GameMap class with width and height as __init__ parameters, type hinted as integers. Also assigns them as instance attributes.
class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        # Creates a numpy array of the specified width and height and fills it with the value of tile_types.floor. The order="F" parameter tells numpy to store the array in column major order, which is the order that tcod expects. self.tiles is assigned as an instance attribute to a newly created numpy array (using np.full)of the specified width and height and filled with the value of tile_types.wall.
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")


    # This function takes x and y parameters and returns True if the x and y values are within the bounds of the map.
    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    # This function takes a console object as a parameter and renders the game map onto the console object.

    # The 'console.tiles_rgb' statement accesses a property of the console object called tiles_rgb. The value of the property accessed '[0:self.width, 0:self.height]' uses 'slicing' to access a subset of the tiles_rgb property. 0:self.width specifies the range of rows to select and 0:self.height specifies the range of columns to select. The syntax is 'start:stop' and indicates that the elements from the 'start' index up to, but not including the 'stop' index will be selected. So the statement selects a rectangular portion of the console.tiles_rgb array starting from the first row and column (index 0) up to self.width rows and self.height columns. The selected portion of the array is then assigned the value of self.tiles["dark"], and represents the area of the console where the game map will be rendered.

    """The self.tiles array represents the game map and contains elements of type tile_dt (a structured NumPy dtype) defined in the tile_types.py file. Each element of self.tiles consists of multiple fields, including the "dark" field that represents the tile's appearance when not in the field of view.

    On the other hand, console.tiles_rgb is a NumPy array of dtype graphic_dt, which represents the visual representation of tiles on the console. It contains information about the character, foreground color (RGB), and background color (RGB) for each tile.

    To update console.tiles_rgb with the "dark" values from self.tiles, the self.tiles["dark"] expression is used to extract the "dark" field values as a sub-array, which has the same shape as console.tiles_rgb. This sub-array is then assigned to the corresponding region of console.tiles_rgb, effectively updating the appearance of tiles on the console.

    The conversion of tile types to RGB values is not directly related to self.tiles["dark"]. The mapping between tile types and RGB values is typically defined separately, often in the tile_types.py file or a related module. self.tiles["dark"] assumes that the "dark" field of each tile element already contains the appropriate RGB values for the tile's appearance in the dark. """
    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]