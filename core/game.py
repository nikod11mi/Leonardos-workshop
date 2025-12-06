from __future__ import annotations

import pygame

from core.scene import Scene
from systems.time_system import TimeSystem
from world.workshop_state import WorkshopState


class Game:
    """Main game container handling the loop and scene management."""

    def __init__(
        self, screen: pygame.Surface, initial_scene: Scene, workshop_state: WorkshopState
    ) -> None:
        self.screen = screen
        self.scene = initial_scene
        self.workshop_state = workshop_state
        self.clock = pygame.time.Clock()
        self.running = True
        self.time_system = TimeSystem()

    def change_scene(self, scene: Scene) -> None:
        """Switch to a different scene."""
        self.scene = scene

    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scene.handle_event(event)

    def update(self, dt: float) -> None:
        """Update the active systems and scene."""
        self.time_system.tick(self.workshop_state)
        self.scene.update(dt)

    def run(self) -> None:
        """Main game loop."""
        while self.running:
            dt_ms = self.clock.tick(60)
            dt = dt_ms / 1000.0
            self._handle_events()
            self.update(dt)
            self.scene.render(self.screen)
            pygame.display.flip()

        pygame.quit()
