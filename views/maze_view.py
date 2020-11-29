import pygame
import os

class MazeView:
    def __init__(self, maze):
        self._maze = maze
        self._display_surf = pygame.display.set_mode((1250,400), pygame.HWSURFACE)
        self._block_img = pygame.image.load(os.path.join("images","block.png")).convert()
        self._player_img = pygame.image.load(os.path.join("images","player.png")).convert()
        self._player_img.set_colorkey((0,0,0))
        self._letter_A = pygame.image.load(os.path.join("images","A.png")).convert()
        self._letter_B = pygame.image.load(os.path.join("images","B.png")).convert()
        self._letter_C = pygame.image.load(os.path.join("images","C.png")).convert()
        self._letter_D = pygame.image.load(os.path.join("images","D.png")).convert()
        self._letter_H = pygame.image.load(os.path.join("images","H.png")).convert()
        self._exit_door = pygame.image.load(os.path.join("images","door.png")).convert()
        self.end_game = False

        self._font = pygame.font.Font(None, 40)
        # gray = pygame.Color('gray19')
        self._red = pygame.Color('red')
        self._clock = pygame.time.Clock()
        self._timer = 30  # Decrease this to count down.
        self._dt = 0  # Delta time (time since last tick).

    @property
    def counter(self):
        return int(self._timer)

    def display_maze(self):
        """ Template pattern: main text - show the maze structure
        Returns:
            str: the maze structure and everything inside it
        """
        text = "="*15 + "MAZE" + "="*15 + '\n'
        for row in self._maze.maze:
            line = ''
            for element in row:
                line += element 
            line += '\n'
            text += line
        self.image_to_pygame()
        self.timer()
        self.show_score()
        return text

    def get_position(self, x,y):
        return (x*32+64,y*32+64)

    def timer(self):
        self._timer -= self._dt
        if self._timer <= 0:
            self.end_game = True

        # draws text on new surface
        txt = self._font.render(str(round(self._timer, 2)), True, self._red)
        #draws txt on pygame
        self._display_surf.blit(txt, (1100, 350))
        #displays screen

        img = self._font.render('Time remaining', True, self._red)
        self._display_surf.blit(img, (1000, 300))

        pygame.display.flip()
        
        self._dt = self._clock.tick(30) / 1000  # / 1000 to convert to seconds.

    def show_score(self, score= 0):
        if self.end_game == True:
            print("this is time: ", self._timer)

    def image_to_pygame(self):
        pygame.event.pump()
        self._display_surf.fill((0,0,0))
        for y,row in enumerate(self._maze.maze):
            for x,element in enumerate(row):
                if element == 'x':
                    self._display_surf.blit(self._block_img, self.get_position(x,y))
                if element == "P":
                    self._display_surf.blit(self._player_img, self.get_position(x,y))
                if element == "A":
                    self._display_surf.blit(self._letter_A, self.get_position(x,y))
                if element == "B":
                    self._display_surf.blit(self._letter_B, self.get_position(x,y))
                if element == "C":
                    self._display_surf.blit(self._letter_C, self.get_position(x,y))
                if element == "D":
                    self._display_surf.blit(self._letter_D, self.get_position(x,y))
                if element == "H":
                    self._display_surf.blit(self._letter_H, self.get_position(x,y))
                if element == "E":
                    self._display_surf.blit(self._exit_door, self.get_position(x,y))
        pygame.display.update()
