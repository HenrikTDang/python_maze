from controllers.app import App
import pygame

if __name__ == "__main__":
    pygame.init()
    app = App('maze2.txt','P')
    app.run()