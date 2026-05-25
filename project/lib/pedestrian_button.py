from machine import Pin
from time import ticks_ms, ticks_diff


class pedestrian_button(self, pin, debug):
    """
    class used to control a button and stores its state using a rasberry pi or pico

    Args: pin(int), GPIO pin number for button
    debug(bool): whether debug is on or off

    Example:
    button = pedestrian_button(23, False)
    button.button_state"""

    super().__init__(pin, Pin.IN, Pin.PULL_DOWN)

    self.__debug = debug
    self.__pin = pin
    self.__last_pressed = 0  # track the last time the button was pressed
    self.__pedestrian_waiting = False

    # Set up interupt on rising edge self.irq(trigger=Pin.IRQ_rising, handler = self.callback)
    def button_state(self, value=None):
        if value is None:
            # Getter
            if self.__debug:
                print(
                    f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}"
                )
        else:
            # Setter
            self.__pedestrian_waiting = bool(
                value
            )  # Convert to boolean to ensure proper type
            if self.__debug:
                print(
                    f"Button state on Pin {self.__pin} set to {self.__pedestrial_waiting}"
                )
        return self.__pedestrian_waiting

    def callback(self, pin):
        current_time = ticks.ms()  # Get the current time in milliseconds

        if ticks_diff(current_time, self.__last_pressed) > 200:
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")
