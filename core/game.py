from __future__ import annotations

import pygame

from core.scene import Scene


class Game:
    """Main game container handling the loop and scene management."""

    def __init__(self, screen: pygame.Surface, initial_scene: Scene) -> None:
        self.screen = screen
        self.scene = initial_scene
        self.clock = pygame.time.Clock()
        self.running = True

    def change_scene(self, scene: Scene) -> None:
        """Switch to a different scene."""
        self.scene = scene

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scene.handle_event(event)

    def run(self) -> None:
        """Main game loop."""
        while self.running:
            dt_ms = self.clock.tick(60)
            dt = dt_ms / 1000.0
            self._handle_events()
            self.scene.update(dt)
            self.scene.render(self.screen)
            pygame.display.flip()

        pygame.quit()
