import os
import pyautogui

path_belum1 = os.path.join(r'C:/Users/Doni/Desktop/NEW/hand/', 'belum1.png')
path_belum2 = os.path.join(r'C:/Users/Doni/Desktop/NEW/hand/', 'belum2.png')

while True:                               
    #mencari semua gambar png di folder animal
    animal_images = pyautogui.locateAllOnScreen(os.path.join(r'C:/Users/Doni/Desktop/NEW/animal/', '*.png'))
    #mencari semua gambar png di folder hand
    hand_images = pyautogui.locateAllOnScreen(os.path.join(r'C:\Users\Doni\Desktop\NEW\hand', '*.png'))

    #jika kedua gambar ditemukan
    if animal_images and hand_images:
        for animal_image in animal_images:
            for hand_image in hand_images:
                #mendapatkan koordinat kedua gambar
                animal_x, animal_y = pyautogui.center(animal_image)
                hand_x, hand_y = pyautogui.center(hand_image)

                #mendapatkan perbedaan koordinat kedua gambar
                diff_x = animal_x - hand_x
                diff_y = animal_y - hand_y

                #jika kedua gambar searah
                if abs(diff_x) < 20 and abs(diff_y) < 20:
                    #klik gambar oke
                    pyautogui.click(os.path.join(r'C:/Users/Doni/Desktop/NEW/animal/', 'oke.png'))
                else:
                    #klik gambar belum
                    pyautogui.click(os.path.join(r'C:/Users/Doni/Desktop/NEW/hand/',))
                    pyautogui.click(path_belum1)
                    pyautogui.click(path_belum2)
    else:
        print("Gambar tidak ditemukan, mencari lagi...")
