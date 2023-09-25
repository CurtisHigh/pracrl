# this statement imports the optional type hint from the typing module. This allows for the use of the 'Optional' type, which is used to indicate that a variable or function argument can have a particular type or be 'None' as a valid value. For example the 'ev_keydown' method returns an 'Optional[Action]' which means that it can return either an 'Action' or 'None'. The '->' indicates that the method returns a value of the type that follows the arrow.
from typing import Optional

# import tcod.event to handle events
import tcod.event

# import Action, EscapeAction, and MovementAction from actions.py
from actions import Action, EscapeAction, MovementAction

# The EventHandler class inherits from or is a subclass of 'tcod.event.EventDispatch[Action]' which means that  is extends the generic event dispatcher to handle events specific to the 'Action' class
class EventHandler(tcod.event.EventDispatch[Action]):

    # The 'ev_quit' method is overriden from the 'tcod.event.EventDispatch' class. This method is called when the user closes the window or presses the escape key. It returns an 'Action' that will be returned by the 'dispatch' method.
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # The 'ev_keydown' method is overriden from the 'tcod.event.EventDispatch' class. This method is called when the user presses a key. It returns an 'Action' that will be returned by the 'dispatch' method. It returns 'None' if the key pressed doesn't match any of the keys that are handled.
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:

        # The 'action' variable is set to 'None' by default. If a key is pressed that matches one of the keys that are handled, then 'action' will be set to the corresponding 'Action' subclass.
        action: Optional[Action] = None

        # 'event.sym' returns the key code of the key that was pressed. This is used to determine which key was pressed.
        key = event.sym

        # The 'if' statements check if the key pressed matches one of the keys that are handled. If it does, then 'action' is set to the corresponding 'Action' subclass.
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed which means that action defualts to 'None'
        return action