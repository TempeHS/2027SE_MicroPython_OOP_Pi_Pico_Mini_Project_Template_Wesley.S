from lib.controller import Controller
from time import sleep
from lib.pedestrian_button import PedestrianButton
from lib.led_light import Led_Light
from lib.audio_notification import AudioNotification

led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)
led_pedestrian_button = PedestrianButton(22, True)
buzzer = AudioNotification(27, True)

controller = Controller(
    led_pedestrian_red,
    led_pedestrian_green,
    led_traffic_red,
    led_traffic_amber,
    led_traffic_green,
    led_pedestrian_button,
    buzzer,
    True,
)

while True:
    controller.update()
    sleep(0.1)
