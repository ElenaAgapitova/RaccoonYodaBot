"""Модуль данных для игр"""

db_dict = {}

default_for_user = {
    'candy': {
        'game_status': False,
        'game_amount': 0,
        'step': None,
        'total': None,
        'current': None,
        'turn': None,
        'win_amount': 0,
    },
    'hangman': {
        'test': None
    }
}