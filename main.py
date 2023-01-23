import time
from PIL import Image, ImageGrab
import pyautogui


def click(key):
    pyautogui.keyDown(key)
    return


time.sleep(3)


def is_collision(data):
    for i in range(710, 760):
        for j in range(490, 530):
            if data[i, j] < 180:
                click("up")
                return
    return


while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    is_collision(data)
   # for i in range(710, 760):
    #    for j in range(490, 530):
     #       data[i, j] = 0
    #image.show()
    #break

