import pyautogui
import time
from src.start_game import start_game
from src.detect_started_game import detect_started_game
from src.utils import press_hotkey, get_btn, click_btn, double_click_btn
from src.logger import logger

def forcus_game():
    in_game = get_btn('in_game')
    if in_game is None:
        click_btn(in_game)
    
def press_key_s():
    pyautogui.keyDown('s')
    pyautogui.keyUp('s')

def press_key_esc():
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

def press_key_space():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

def do_step(step, callback = None):
    btn = get_btn(f'step_{step}')

    if btn:
        forcus_game()
        if callback:
            callback()
        else:
            click_btn(btn)
        logger.info(f'START STEP {step}')

def detect_steps():
    do_step(1)
    do_step(2)
    do_step(3)
    do_step(4, press_key_s)
    do_step(5, press_key_esc)
    do_step(6, press_key_space)
    do_step(7)
    do_step(8)


def main():
    # start_game()
    
    # time.sleep(10)
    
    # press_hotkey(['ctrl', 'tab'])

    # Waiting start game

    forcus_game()
    while True:
        detect_steps()
        time.sleep(1) 

main()
