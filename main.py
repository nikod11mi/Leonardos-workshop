import pygame

from core.game import Game
from ui.workshop_scene import WorkshopScene
from world.workshop_state import WorkshopState


def main() -> None:
    pygame.init()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Leonardo's Workshop: Renaissance Genius Simulator")

    workshop_state = WorkshopState()
    initial_scene = WorkshopScene(workshop_state)
    game = Game(screen, initial_scene, workshop_state)
    game.run()


if __name__ == "__main__":
    main()
