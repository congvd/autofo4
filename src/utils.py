import pyautogui
import time


image_folder = './images'

def get_btn(name):
    location = pyautogui.locateCenterOnScreen(f'{image_folder}/{name}.png', grayscale=False, confidence=0.9)
    return location

def click_btn(location):
    if location is None:
        return None

    btn_x, btn_y = location
    pyautogui.moveTo(btn_x, btn_y)
    pyautogui.click(btn_x, btn_y)

def double_click_btn(location):
    if location is None:
        return None

    btn_x, btn_y = location
    pyautogui.moveTo(btn_x, btn_y, duration = 1)
    pyautogui.doubleClick(btn_x, btn_y)

def press_hotkey(keys):
    if len(keys) != 2:
        return None
    
    pyautogui.keyDown(keys[0])
    pyautogui.press(keys[1])
    pyautogui.keyUp(keys[0])