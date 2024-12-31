import pygame
import random
import abc
import sys

class GameObject(abc.ABC):
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @abc.abstractmethod
    def draw(self, surface):
        pass

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

class Ball(GameObject):
    def __init__(self, x, y, radius, gravitasi=0.5, tinggi_lompatan=-10):
        super().__init__(x, y, (255, 165, 0))
        self._radius = radius
        self._kecepatan = 0
        self._gravitasi = gravitasi
        self._tinggi_lompatan = tinggi_lompatan

    def draw(self, surface):
        pygame.draw.circle(surface, self._color, (int(self._x), int(self._y)), self._radius)

    def update(self):
        self._kecepatan += self._gravitasi
        self._y += self._kecepatan

    def lompat(self):
        self._kecepatan = self._tinggi_lompatan

    def get_radius(self):
        return self._radius
