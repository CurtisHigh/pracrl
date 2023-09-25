#!/usr/bin/env python3
#importing the necessary modules
import tcod

from engine import Engine

from entity import Entity

from input_handlers import EventHandler

from procgen import generate_dungeon

# main is the entry point of the program "-> None" indicates that there should be no return type
def main() -> None:
    
    # defines the screen size.
    screen_width = 80
    screen_height = 50

    # defines the map size 
    map_width = 80
    map_height = 50

    # defines the room min and max size alone with max rooms 
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # defines and loadsthe tileset used for the game
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # creates an instance of the EventHandler class
    event_handler = EventHandler()

    # creates instances of the Entity class to serve as the player and npc then adds them to a set called entities
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (0, 255, 0))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 0, 0))
    entities = {npc, player}

    #creates an instance of the generate_dungeon function and passes in the necessary parameters which are defined above
    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        player=player
    )
    
    # creates an instance of the Engine class and passes in the necessary parameters with are defined above
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # creates an instance of the tcod.context.new_terminal function and passes in the necessary parameters and assigns it to a variable called context. The code after "context:" will run as long as the context is open (which is the game window)
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Pracrl",
        vsync=True,
    ) as context:
        # defines the console instance and passes in the necessary parameters. the console is what is displayed inside of the context window
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # while true, this loop will run the game and render and update the console
        while True:
            # Game Loop
            engine.render(console=root_console, context=context)

            # tcod.event.wait() waits for events to register then stores them as an object
            events = tcod.event.wait()

            engine.handle_events(events)


# this code ensures that the main function is run when the program is run and not when it is imported as a module
if __name__ == "__main__":
    main()