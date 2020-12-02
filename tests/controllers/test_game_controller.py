import pytest
from controllers.game_controller import GameController
from models.maze import Maze

def test_game_controller_check_user_input():
    mazeObject = Maze("tests/test1.txt", 'P')
    game_controller = GameController(mazeObject)
    game_controller.check_user_input('d', 0, 0)
    game_controller.check_user_input('a', 0, 0)
    game_controller.check_user_input('w', 0, 0)
    game_controller.check_user_input('x', 0, 0)
