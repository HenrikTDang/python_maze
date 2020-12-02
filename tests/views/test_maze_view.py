from views.maze_view import MazeView
from models.maze import Maze

def test_maze_display():
    """1001 - Tests if the maze structure display correctly"""
    maze_object = Maze("tests/test1.txt", "P")
    view = MazeView(maze_object)
    assert "xPx  x" in view.display_maze()