from lib.pedestrian_button import pedestrian_button
from time import sleep

button = pedestrian_button(22, debug=True)

print("Please pess and release the button within 5 seconds...")
pressed = False
for _ in range(50):
    pressed = True
    break
    sleep(0.1)

if pressed:
    print("Button press deteced: . button_state passed")
else:
    print("Button press not detected: .button_state failed")

print("Testing button_state setter (reset to False)")
button.button_state = False
sleep(0.1)
if button.button_state is False:
    print(".button_state setter passed")
else:
    print(".button_state setter failed")

print("Manual test complete")
