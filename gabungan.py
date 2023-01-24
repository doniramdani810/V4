import threading
import pyautogui
from PIL import ImageGrab
import keyboard
import os
import time
import cv2
import numpy as np
import glob
import pytesseract
import mss



def koding1():
    
    folder_path = r"C:\Users\Doni\Desktop\NEW\1x" # ganti dengan path folder yang diinginkan
    image_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.png')]

    while True:
            for image_path in image_list:            # Mencari gambar
                image = pyautogui.locateOnScreen(image_path, confidence = 0.7)

                # Jika gambar ditemukan
                if image:
                    # Mendapatkan posisi gambar
                    x, y = pyautogui.center(image)
                    # Klik pada posisi gambar
                    original_position = pyautogui.position()
                    pyautogui.click(x, y)
                    pyautogui.moveTo(original_position)
                    break
            else:
                time.sleep(1)



def koding2():
    folder_path = r"C:\Users\Doni\Desktop\NEW\x"
    images = [f for f in os.listdir(folder_path) if f.endswith(".png")] 

    while True:
        for image in images:
            full_path = os.path.join(folder_path, image)
            location = pyautogui.locateCenterOnScreen(full_path, confidence=0.7)
            if location:
                    region = (location[0]-200, location[1]-100, location[0]+200, location[1]+100)
                    location = pyautogui.locateOnScreen(r"C:\Users\Doni\Desktop\NEW\keypres\silang.png", region=region, grayscale=False, confidence=0.7)
                    if location:
                        original_position = pyautogui.position()
                        pyautogui.click(location)
                        pyautogui.moveTo(original_position)
                        time.sleep(2)   

def koding3():
    path = r"C:\Users\Doni\Desktop\NEW\kancil baru\*.png"
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

def koding4():
    path = r"C:\Users\Doni\Desktop\NEW\kudanil baru\*.png"
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


def koding5():
    path = r"C:\Users\Doni\Desktop\NEW\Kancil\*.png"
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
def koding6():
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
def koding7():

    def find_cross_image():
                image_path = r"C:\Users\Doni\Desktop\NEW\keypres\silang.png"
                current_position = pyautogui.position()
                image_location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)
                if image_location:
                    pyautogui.moveTo(image_location)

    def find_box_text_image():
                image_path = r"C:\Users\Doni\Desktop\NEW\keypres\text.png"
                image_location = pyautogui.locateOnScreen(image_path)
                if image_location:
                    pyautogui.moveTo(image_location)
                    
    def find_play_image():
                image_path = r"C:\Users\Doni\Desktop\NEW\keypres\play.png"
                image_location = pyautogui.locateOnScreen(image_path)
                if image_location:
                    pyautogui.moveTo(image_location)

    def find_berhenti_image():
                image_path = r"C:\Users\Doni\Desktop\NEW\keypres\berhenti.png"
                image_location = pyautogui.locateOnScreen(image_path)
                if image_location:
                    pyautogui.moveTo(image_location)

    keyboard.add_hotkey('esc', find_cross_image)
    keyboard.add_hotkey('tab', find_box_text_image)
    keyboard.add_hotkey('`', find_play_image)
    keyboard.add_hotkey('*', find_berhenti_image)
    keyboard.add_hotkey('-', lambda: pyautogui.click())

    print("Tekan esc/tab silang/gambar.")
    keyboard.wait()




if __name__ == "__main__":
    t1 = threading.Thread(target=koding1)
    t2 = threading.Thread(target=koding4)
    t3 = threading.Thread(target=koding5)
    t4 = threading.Thread(target=koding5)
    t5 = threading.Thread(target=koding5)
    t6 = threading.Thread(target=koding5)
    t7 = threading.Thread(target=koding5)

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
