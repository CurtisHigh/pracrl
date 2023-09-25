# importing Set, Iterable, and Any from the typing module which proveds support for type hints and annotations
from typing import Set, Iterable, Any

# importing Context and Console from the tcod module
from tcod.context import Context
from tcod.console import Console

# importing the EscapeAction and MovementAction classes from the actions module
from actions import EscapeAction, MovementAction

# importing the Entity class from the entity module
from entity import Entity

# importing the GameMap class from the game_map module
from game_map import GameMap

# importing the EventHandler class from the input_handlers module
from input_handlers import EventHandler

# Defining the Engine class and defining the __init__ method which is called when an instance of the class is created. The __init__ method takes in the following parameters: entities, event_handler, game_map, and player. The parameters are then assigned to the class instance variables of the same name (self.).
class Engine:
    def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
        self.entities = entities
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player

    # This function is called every frame and handles the events that are passed in from the main. The parameter 'events' is declared with a type hint specifying the expected type of the 'events' parameter it's indicated that it should be an iterable of any type (such as a list or a tuple) containing elements of any type ('Any', which is an official data type in python that is part of the 'typing' module which provides support for type hints and annotations. The 'Any' type essentially disables static type checking for the specific value and allows it to be compatible with any other type). 
    def handle_events(self, events: Iterable[Any]) -> None:

        # The function then iterates over the events and passes each event to the event_handler.dispatch function. The dispatch function returns an action which is then assigned to the variable 'action'. The function then checks if the action is None and if it is it continues to the next event. If the action is not None it calls the perform function of the action and passes in the engine and player as parameters. The perform function is defined in the actions.py file.

        # Here event is a variable that is assigned to each element in the events iterable. The iterable is a list of events that are passed in from the main.py file. The events are passed in from the main.py file by the tcod.event.wait() function which is called in the main.py file. The tcod.event.wait() function returns a list of events that are passed in to the handle_events function. The handle_events function then iterates over the list of events and passes each event to the event_handler.dispatch function. The event_handler.dispatch function then returns an action which is then assigned to the variable 'action'. The function then checks if the action is None and if it is it continues to the next event. If the action is not None it calls the perform function of the action and passes in the engine and player as parameters. The perform function is defined in the actions.py file.

        # event is a variable used as a placeholder to iterate through the events iterable
        for event in events:

            # self references the Engine class, event_handler references an instance of the EventHandler class, dispatch references the dispatch function in the EventHandler class (you can see this being passed or inherited from a tcod module or class in the EventHandler class of the input_handlers.py file 'class EventHandler(tcod.event.EventDispatch[Action]):'), and event references the event variable which is assigned to each element in the events iterable

            # The dispatch method is defined within the tcod.event.EventDispatch class and is responsible for calling the appropriate event handler method based on the type of event received
            action = self.event_handler.dispatch(event)

            # None is a special constant in python that represents the absence of a value or the lack of any value. It's often used to indicate that a variable or expression does not have a valid value assigned to it. A function that doesn't return any value explicitly returns 'None'. The 'continue' key word is used in loops. When the 'continue' statement is encountered it causes the program to skip the rest of the current iteration and move to the next iteration of the loop. The code that follows the 'continue' statement within the current iteration is not executed. It is often used to skip certain iterations or to selectively process specific elements in a loop.
            if action is None:
                continue

            # Here the perform function is being called on the action variable and the engine and player are being passed in as parameters. The perform function is defined in the actions.py file.
            action.perform(self, self.player)

    # This function is called every frame and renders the game map and entities to the console. The 'console' parameter is declared with a type hint specifying the expected type of the 'console' parameter it's indicated that it should be an instance of the 'Console' class. The 'context' parameter is declared with a type hint specifying the expected type of the 'context' parameter it's indicated that it should be an instance of the 'Context' class. The 'Console' class is defined in the tcod module and the 'Context' class is defined in the tcod.context module.
    def render(self, console: Console, context: Context) -> None:
        
        # The render function calls the render function of the game_map object and passes in the console as an argument. This allows the game map to render itself onto the console, displaying the current state of the map. The render function of the game_map is defined in the game_map.py file.
        self.game_map.render(console)

        # The render function then iterates over the entities and calls the console.print function for each entity. The console.print function is defined in the tcod module. The console.print function takes in the x and y coordinates of the entity, the character to be printed, and the color of the character. The x and y coordinates are accessed from the entity object using the dot operator. The character and color are accessed from the entity object using the dot operator and the 'char' and 'color' attributes of the entity object. The 'char' and 'color' attributes of the entity object are defined in the entity.py file. The 'fg=entity.color' statement is a part of the console.print function it accepts an optional foreground color, here we give it the value of the entity.color attribute. The entity.color attribute is defined in the entity.py file.
        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)


        # context.preset is a function that is defined in the tcod.context module. It takes in a console as an argument and then updates the console. The context.preset function is called here to update the console with the entities and game map that were rendered to the console.
        context.present(console)

        # The console.clear function is defined in the tcod module. It clears the console of all characters and colors. The console.clear function is called here to clear the console of all characters and colors. Since it is called every frame it clears the console of all characters and colors every frame and then the entities and game map are rendered to the console again by the render function and the context.preset function is called again to update the console with the entities and game map that were rendered to the console.
        console.clear()