from views.game_view import GameView
from models.maze import Maze

def test_game_display():
    """1001 - Tests if the game display maze structure correctly"""
    maze_object = Maze("test1.txt", "P")
    view = GameView(maze_object)
    assert "xPx  x" in view.display_maze()