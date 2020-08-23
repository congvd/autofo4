from src.logger import logger
from src.utils import get_btn, click_btn


def detect_started_game():
    is_started = False

    while is_started == False:
        game_icon = get_btn('fo4')

        if game_icon:
            is_started = True

        click_btn(game_icon)

    return is_started


    