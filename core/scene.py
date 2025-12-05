from __future__ import annotations

import pygame


class Scene:
    """Base class for all scenes/screens in the game."""

    def handle_event(self, event: pygame.event.Event) -> None:
        """Handle a single pygame event."""
        raise NotImplementedError

    def update(self, dt: float) -> None:
        """Update scene logic.

        Args:
            dt: Delta time in seconds since the last update.
        """
        raise NotImplementedError

    def render(self, surface: pygame.Surface) -> None:
        """Render the scene to the given surface."""
        raise NotImplementedError
