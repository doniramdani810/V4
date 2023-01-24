import keyboard
import pyautogui

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
