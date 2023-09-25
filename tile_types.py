# Imports the Tuple type from the typing module. A tuple is an ordered collection of elements, enclosed in parentheses '()'. It is an immutable data type, meaning its elements cannot be modified once the tuple is created. Tuples can contain elements of different types, such as integers, floats, strings, boolean, or even other tuples.
from typing import Tuple

# This imports numpy as the variable 'np' and the '# type: ignore' comment tells the type checker to ignore any type errors raised by the import statement
import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.

# This statement defines 'graphic_dt'as a numpy data type object. This creates a structured array and allows you to specify the data type of each field or element within the array. The syntax for defining a structured array is 'np.dtype([("field1", type), ("field2", type), ...])'. The graphic_dt data type consist of three fields, 'ch', 'fg', and 'bg'. 'ch' this field stores a unicode codepoint of the character representing the tile, the 'fg' field stores the RBG color values representing the foreground color of the tile, and the 'bg' field stores the RBG color values representing the background color of the tile. Using the 'graphic_dt' data type, you can create and work with arrays of tiles where each tile is represented by a unicode character and two colors.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data. The 'walkable' field is a boolean value that indicates whether the tile can be walked over. The 'transparent' field is a boolean value that indicates whether the tile blocks FOV. The 'dark' field represents an instance of the 'graphic_dt' data type that stores the tile's graphics when it is not in FOV. 'graphic_dt' is the data type of the 'dark' field. The 'dark' field stores the unicode codepoint of the character representing the tile, the RBG color values representing the foreground color of the tile, and the RBG color values representing the background color of the tile. So it will be an array of three values, one for each field in the 'graphic_dt' data type.
tile_dt = np.dtype(
    [
        ("walkable", bool),  # True if this tile can be walked over.
        ("transparent", bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
    ]
)

# This function is a helper function for defining individual tile types. It takes three keyword-only arguments, 'walkable', 'transparent', and 'dark'. The 'walkable' argument is a boolean value that indicates whether the tile can be walked over. The 'transparent' argument is a boolean value that indicates whether the tile blocks FOV. The 'dark' argument represents an instance of the 'graphic_dt' data type that stores the tile's graphics when it is not in FOV. 'graphic_dt' is the data type of the 'dark' argument. The 'dark' argument stores the unicode codepoint of the character representing the tile, the RBG color values representing the foreground color of the tile, and the RBG color values representing the background color of the tile. So it will be an array of three values, one for each field in the 'graphic_dt' data type. The function returns a numpy array of the 'tile_dt' data type.
def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    # this specifies that the return type of this method will be a numpy array of the 'tile_dt' data type. Which is a multi-dimensional array of tiles.

    """Helper function for defining individual tile types """

    # np.array is a function of numpy that creates a new numpy array object from given input data. It can take various data types such as tuples, list, or other array-like objects and convert them into numpy arrays. The 'tile_dt' data type is passed as the 'dtype' argument to the np.array function. The 'dtype' argument specifies the data type of the array's elements.
    return np.array((walkable, transparent, dark), dtype=tile_dt)

# These methods construct the individual tile types using the 'new_tile' method and the 'tile_dt' data type structure.
floor = new_tile(
    walkable=True, transparent=True, dark=(ord("."), (102, 51, 0), (192, 139, 98)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord("#"), (255, 229, 204), (102, 0, 0)),
)