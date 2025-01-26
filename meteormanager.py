import os
import pygame

class MeteorManager():
    def __init__(self):
        self._meteors_by_color_size = {
            "Grey": {"small": [], "med": [], "big": []},
            "Brown": {"small": [], "med": [], "big": []},
        }

    def load_meteors(self):
        dir = os.path.dirname(__file__)
        meteors_dir = os.path.join(dir, "assets", "PNG", "Meteors")
        meteors_files = [f for f in os.listdir(meteors_dir) if f.endswith(".png")]

        for file in meteors_files:
            file_path = os.path.join(meteors_dir, file)
            image = pygame.image.load(file_path)

            if "Grey" in file:
                grey_meteors = self._meteors_by_color_size["Grey"]
                if "small" in file:
                    grey_meteors["small"].append(image)
                elif "med" in file:
                    grey_meteors["med"].append(image)
                else:
                    grey_meteors["big"].append(image)
            elif "Brown" in file:
                brown_meteors = self._meteors_by_color_size["Brown"]
                if "small" in file:
                    brown_meteors["small"].append(image)
                elif "med" in file:
                    brown_meteors["med"].append(image)
                else:
                    brown_meteors["big"].append(image)

    def get_meteors(self):
        return self._meteors_by_color_size
