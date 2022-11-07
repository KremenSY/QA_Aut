import os
import pyautogui

base_dir=os.path.dirname(__file__)
pic_dir=(os.path.join(base_dir, 'GUI'))
calc_path=r"C:\Windows\system32\win32calc.exe"

def load_GUI_images(path):
    GUI_POS={}
    for folder_name, sub_folder, img_files in os.walk(path):
        for image in img_files:
            full_path=os.path.join(path, image)
            name=full_path.split(os.sep)[-1].split(".")[0]
            pos=pyautogui.locateCenterOnScreen(full_path)
            GUI_POS[name]=pos
    return GUI_POS

GUI_POS=load_GUI_images(pic_dir)
print(GUI_POS)
