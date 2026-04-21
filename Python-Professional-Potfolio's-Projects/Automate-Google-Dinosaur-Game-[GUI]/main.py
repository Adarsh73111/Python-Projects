import pyautogui
import time
from PIL import ImageGrab

def is_obstacle_clear():
    box = (200, 400, 250, 430)
    image = ImageGrab.grab(box)
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x, y))[0] < 100:
                return True
    return False

def play_game():
    time.sleep(3)
    pyautogui.press('space')
    time.sleep(0.1)

if __name__ == "__main__":
    play_game()

