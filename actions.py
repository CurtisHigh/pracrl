# this line allows for the future resolution of type hints, which is a fancy way of saying that it allows for the use of type hints before the actual definition of the type. This is necessary because the Action class relies on the Engine class, and the Engine class relies on the Action class. This is called a circular dependency. When the Engine class is defined, the Action class is not yet defined, so the Engine class cannot use the Action class. When the Action class is defined, the Engine class is already defined, so the Action class can use the Engine class. This is why we need to use TYPE_CHECKING. When the code is actually run, the TYPE_CHECKING variable will be False, so the import will not be run. When the code is being type checked, the TYPE_CHECKING variable will be True, so the import will be run. This allows us to use type hints in the Action class before the Engine class is defined. When you include this line the type annotations will be treated as strings during the initial evaluation of the code, and postpone the actual evaluation of those annotations until runtime. This is called a forward reference. Forward references allow you to refer to a type that has not been defined yet. It's a way to mention a class or function in a type annotation before it's actual definition. In python 3.10 and later versions forward references are supported by default so this line is no longer needed.
from __future__ import annotations

# typing is a module in python that provides tools for features related to type hints. When you import TYPE_CHECKING from typing, it creates a special condition that allows you to import modules selectively only for type hinting purposes. This is useful when you have a circular dependency between two modules, and you need to use type hints in both modules. When you import a module normally, the code in the module is run. When you import a module for type hinting purposes, the code in the module is not run. This allows you to use type hints in a module before the module is defined. During actual runtime the TYPE_CHECKING constant is considered 'True' so the type hints can be evaluated. It allows you to write and check the type hints without encountering circular dependency errors.
from typing import TYPE_CHECKING

# if TYPE_CHECKING is true (which it will be at runtime) this evaluates to true and imports the Engine and Entity classes from the engine and entity modules respectively. If TYPE_CHECKING is false (which it will be during type checking) this evaluates to false and the import is not run. This allows you to use type hints in the Action class before the Engine class is defined.
if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

# Defines the Action class. This class does not have an __init__ method because the __init__ method is used to initialize the state of an object created by a class. The Action class is an abstract class, which means that it is not meant to be instantiated. It is meant to be inherited by other classes. The Action class is meant to be a base class for other classes to inherit from.
class Action:
    # The perform method here acts as an abstact method, which means that it is meant to be overriden by subclasses. It serves as a placeholder, defining a method's signature(name, parameters, and return type) withoud providing any implementation details. This defines the methods that a subclass should implement, therefore helping enforce a certain structure or behavior across multiple subclasses (of the Action class)
    def perform(self, engine: Engine, entity: Entity) -> None:
        """Perform this action with the objects needed to determine its scope.

        `engine` is the scope this action is being performed in.

        `entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """

        # This is a built in exception in Python that raises a NotImplementedError if an abstract method (the perform method) is not overriden by a subclass.
        raise NotImplementedError()

# The EscapeAction class inherits from the Action class via "(Action)". It overrides the perform method of the Action class.
class EscapeAction(Action):
    # The perform method of the EscapeAction class raises a SystemExit exception (which is a built in python exception). This exception is raised when the user presses the escape key. This exception is caught in the main function in the main.py file, which causes the game to exit.
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

# The MovementAction class is a subclass of the Action class. It overrides the perform method of the Action class.
class MovementAction(Action):
    # The __init__ method of the MovementAction class takes in two parameters, dx and dy, which are cast as integers.
    def __init__(self, dx: int, dy: int):
        # The super() function returns a temporary object of the superclass that allows you to call the superclass's methods. The Action class does not have an __init__ method so the super() function here does not return anything. It could be omitted and the code would still work.
        super().__init__()

        # The dx and dy parameters are assigned to the dx and dy attributes of the MovementAction class. This allows them to be used by the perform method by transferring the values of the parameters to the accessible instance attributes of the class.
        self.dx = dx
        self.dy = dy

    # The perform method here overrides the perform method of the Action class. It takes in two parameters, engine and entity, which are cast as the Engine and Entity classes respectively. The perform method of the MovementAction class is called when the player presses a movement key. The perform method of the MovementAction class takes in the engine and entity parameters, which are used to determine the scope of the action. The engine parameter is used to access the game_map attribute of the Engine class. The entity parameter is used to access the x and y attributes of the Entity class. The perform method of the MovementAction class checks if the destination tile is in bounds and walkable. If it is, the perform method of the MovementAction class calls the move method of the Entity class, which moves the entity to the destination tile. So the dest_x and dest_y calculations are made first. Then the destination tile is checked to see if it is in bounds (if not engine.game_map.in_bounds(dest_x, dest_y):) and walkable(engine.game_map.tiles["walkable"][dest_x, dest_y]). If it is, the entity is moved to the destination tile (entity.move(self.dx, self.dy)).
    def perform(self, engine: Engine, entity: Entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is out of bounds.
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination is blocked by a tile.

        entity.move(self.dx, self.dy)