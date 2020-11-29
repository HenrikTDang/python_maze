from views.endgame_view import EndGameView
from models.maze import Maze
import pytest

def test_init_correct_backpack():
    """1001- Test if the construct of the backpack is valid"""
    maze_object = Maze("test1.txt", "P")
    view = EndGameView(maze_object.player.backpack, maze_object)
    assert view._backpack == []

def test_endgame_display():
    """2001 - Tests if the endgame display maze structure correctly"""
    maze_object = Maze("test1.txt", "P")
    view = EndGameView(maze_object.player.backpack, maze_object)
    assert "xPx  x" in view.display_maze()