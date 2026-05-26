from machine import Pin
from time import ticks_ms, ticks_diff


class pedestrian_button:
    """
    Class used to control a button and store its state using a Raspberry Pi Pico.

    Args:
        pin (int): GPIO pin number for the button.
        debug (bool): Whether debug is on or off.

    Example:
        button = pedestrian_button(23, False)
        button.button_state
    """

    def __init__(self, pin, debug):
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0  # Track the last time the button was pressed
        self.__pedestrian_waiting = False

        # Initialize the pin as an input with a pull-down resistor
        self.__button = Pin(pin, Pin.IN, Pin.PULL_DOWN)

        # Set up an interrupt on the rising edge
        self.__button.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

    def button_state(self, value=None):
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
            return self.__pedestrian_waiting
        else:
            # Setter
            self.__pedestrian_waiting = bool(value)
            if self.__debug:
                print(
                    f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}"
                )

    def callback(self, pin):
        current_time = ticks_ms()  # Get the current time in milliseconds

        if ticks_diff(current_time, self.__last_pressed) > 200:  # Debounce for 200ms
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
