from src.logger import logger
from src.utils import get_btn, click_btn, double_click_btn

image_folder = './images'

def do_go_game():
    game_fo4 = get_btn('game_fo4')
    click_btn(game_fo4)

    logger.info('GO FO4')

def play_game():
    play = get_btn('play')
    click_btn(play)

    logger.info('PLAY')

def go_garena():
    garena = get_btn('garena')
    click_btn(garena)

    logger.info('GO GARENA')

def start_game():
    go_garena()

    game_fo4 = get_btn('game_fo4')
    play = get_btn('play')

    if game_fo4:
        do_go_game()
        play_game()
    elif play:
        play_game()

