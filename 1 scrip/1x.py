import os
import pyautogui
import time

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
