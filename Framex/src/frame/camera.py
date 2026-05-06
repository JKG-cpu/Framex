from typing import Literal

from ..utils.imports import *

__all__ = [
    "Camera"
]

class Camera:
    def __init__(
            self, 
            camera_type: Literal["static", "follow", "lerp", "clamp"] = "static",
            lerp_speed: float = 5.0,
            bounds: pygame.Rect | None = None):
        self.camera_type = camera_type
        self.lerp_speed = lerp_speed
        self.bounds = bounds

        self.position = vector(0, 0)
        self._target: pygame.sprite.Sprite | pygame.Rect | None = None

    # Setting camera position / target
    def set_target(self, target: pygame.sprite.Sprite | pygame.Rect) -> None:
        self._target = target
        if self.camera_type in ("follow", "lerp", "clamp"):
            center = self._get_target_center()
            if center:
                self.position.update(center)

    def set_position(self, x: float | int, y: float | int) -> None:
        self.position.update(x, y)

    # Get offset
    def get_offset(self, screen: pygame.Surface) -> vector:
        sw, sh = screen.get_size()
        return vector(
            self.position.x - sw / 2,
            self.position.y - sh / 2
        )

    # Shake
    def shake(self, intensity: float, duration: float) -> None:
        # NEED TO ADD
        self.shake_itensity = intensity
        self._shake_timer = duration

    # Helpers
    def _get_target_center(self) -> tuple[float, float] | None:
        if self._target is None:
            return None
        if isinstance(self._target, pygame.Rect):
            return self._target.centerx, self._target.centery
        return self._target.rect.centerx, self._target.rect.centery

    def _apply_clamp(self, screen: pygame.Surface) -> None:
        sw, sh = screen.get_size()
        half_w, half_h = sw / 2, sh / 2

        self.position.x = max(
            self.bounds.left + half_w,
            min(self.position.x, self.bounds.right - half_w)
        )
        self.position.y = max(
            self.bounds.top + half_h,
            min(self.position.y, self.bounds.bottom - half_h)
        )

    # Update
    def update(self, dt: float, screen: pygame.Surface) -> None:
        target_center = self._get_target_center()

        match self.camera_type:
            case "static":
                pass

            case "follow":
                if target_center:
                    self.position.update(target_center)
                
            case "lerp":
                if target_center:
                    tx, ty = target_center
                    self.position.x += (tx - self.position.x) * self.lerp_speed * dt
                    self.position.y += (ty - self.position.y) * self.lerp_speed * dt

            case "clamp":
                if target_center:
                    self.position.update(target_center)

                if self.bounds:
                    self._apply_clamp(screen)