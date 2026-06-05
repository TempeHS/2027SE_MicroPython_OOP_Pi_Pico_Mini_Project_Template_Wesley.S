from lib.led_light import Led_Light
from lib.controller import PedestrianLightSubsystem
from lib.pedestrian_button import PedestrianButton
from lib.audio_notification import AudioNotification
from time import sleep

red = Led_Light(19, True, True)
green = Led_Light(17, False, True)
button = PedestrianButton(22, True)
buzzer = AudioNotification(27, True)

light = PedestrianLightSubsystem(red, green, button, buzzer, True)


def Pedestrian_Subsystem_driver():
    print("Testing Pedestrian Subsystem in 5 seconds")
    sleep(5)
    light.show_stop()
    print("Pass if: Red ON, Green OFF")
    sleep(10)
    light.show_walk()
    print("Pass if: Green ON, Red OFF")
    sleep(10)


def test_button():
    passed = False
    print("Press button within 5 seconds")
    sleep(5)

    if light.is_button_pressed():
        print("Test passed")
        light.reset_button()
        passed = True
    else:
        print("Test failed, check button")

    if passed:
        print("Checking reset function")
        if light.is_button_pressed() == False:
            print("Reset test passed")
        else:
            print("Test failed")


test_button()
Pedestrian_Subsystem_driver()
