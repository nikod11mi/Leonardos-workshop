from __future__ import annotations

import pygame

from core.scene import Scene
from world.workshop_state import WorkshopState


class WorkshopScene(Scene):
    """Simple overview scene showing the workshop status."""

    def __init__(self, workshop_state: WorkshopState) -> None:
        self.workshop_state = workshop_state
        self.font = pygame.font.Font(None, 28)
        self.panel_font = pygame.font.Font(None, 24)
        self.text_color = pygame.Color("white")
        self.bg_color = pygame.Color(26, 24, 22)
        self.panel_color = pygame.Color(45, 42, 38)
        self.should_quit = False

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.QUIT:
            self.should_quit = True

    def update(self, dt: float) -> None:
        # Placeholder for future update logic (contracts, events, etc.).
        if self.should_quit:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def render(self, surface: pygame.Surface) -> None:
        surface.fill(self.bg_color)

        stats_lines = [
            f"Day: {self.workshop_state.day}",
            f"Florins: {self.workshop_state.money:.0f}",
            f"Reputation: {self.workshop_state.reputation:.1f}",
            f"Inspiration: {self.workshop_state.inspiration:.1f}",
        ]
        materials = self.workshop_state.materials
        stats_lines.append(
            "Materials: "
            f"wood={materials.get('wood', 0)}, "
            f"metal={materials.get('metal', 0)}, "
            f"pigment={materials.get('pigment', 0)}"
        )

        for index, line in enumerate(stats_lines):
            text_surf = self.font.render(line, True, self.text_color)
            surface.blit(text_surf, (20, 20 + index * 30))

        panel_height = 140
        panel_rect = pygame.Rect(
            0, surface.get_height() - panel_height, surface.get_width(), panel_height
        )
        pygame.draw.rect(surface, self.panel_color, panel_rect)
        pygame.draw.rect(surface, pygame.Color("dimgray"), panel_rect, width=2)

        panel_text = self.panel_font.render(
            "Contracts will appear here", True, self.text_color
        )
        text_pos = panel_text.get_rect(center=panel_rect.center)
        surface.blit(panel_text, text_pos)
