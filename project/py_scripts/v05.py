from lib.pedestrian_button import pedestrian_button
from time import sleep

button = pedestrian_button(22, debug=True)

print("Please pess and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    pressed = Truebreak
    sleep(0.1)

if pressed:
    print("Button press deteced: . button_state passed")
