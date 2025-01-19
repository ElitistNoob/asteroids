import pygame
import pygame.freetype

class TextRenderer:
    def __init__(self, path=None, font_size=24, color=(255,255,255)):
        self.font = pygame.freetype.Font(path, font_size)
        self.color = color

    def render(self, surface, text, position):
        self.font.render_to(surface, position, text, self.color)
