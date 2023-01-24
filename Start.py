import os
import pyautogui
import time

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
                    

