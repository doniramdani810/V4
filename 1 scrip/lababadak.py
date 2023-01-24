import glob
import cv2
import pyautogui
import time
import numpy as np

path = r"C:\Users\Doni\Desktop\NEW\lababadak\*.png"
images = glob.glob(path)

while True:
    for img in images:
        template = cv2.imread(img, 0)
        screenshot = pyautogui.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        threshold = 0.7

        result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            x, y = max_loc
            w, h = template.shape[1], template.shape[0]
            center = (x + w/2, y + h/2)

            original_position = pyautogui.position()
            pyautogui.click(center)
            pyautogui.moveTo(original_position)
            time.sleep(1)



