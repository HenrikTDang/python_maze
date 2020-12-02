from views.welcome_view import WelcomeView
from models.maze import Maze

def test_welcome_display():
    """"Tests if  welcome display maze structure correctly"""
    maze_object = Maze("tests/test1.txt", "P")
    view = WelcomeView(maze_object)
    assert "xPx  x" in view.display_maze()
