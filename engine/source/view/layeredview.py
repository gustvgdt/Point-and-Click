# -*- coding: utf-8 -*-
import pygame

from ..exception import GetError

class LayeredView(pygame.sprite.LayeredUpdates):
    """
    manage the different layers of the game, display or hide them when required

    layers
    0 : background
    1 : elements
    2 : menu
    3 : more text

    """
    def __init__(self):
        pygame.sprite.LayeredUpdates.__init__(self)
        self.font = pygame.font.SysFont("helvetica", 20)
        # blank_label = pygame.sprite.Sprite()
        # blank_label.image = pygame.Surface((400, 30), flags=pygame.SRCALPHA)
        # blank_label.rect = (20, 400, 400, 30)
        # self.add(blank_label, layer=3)  # initialize void text
        self.reset()

    def reset(self):  ## debug ?
        self.empty()
        # this should be set manually (at least position)
        blank_label = pygame.sprite.Sprite()
        # blank_label.image = pygame.Surface((400, 30), flags=pygame.SRCALPHA)
        blank_label.image = pygame.Surface((400, 30))  # to see it more easily
        blank_label.rect = pygame.rect.Rect(20, 290, 100, 30)
        self.add(blank_label, layer=3)  # initialize void text
        # donner un nom au label pour l'identifier plus facilement ?

    def loadArea(self, area):
        """
        Charge une zone en fond (couche 0)
        et tous ses objets en mid (couche 1)

        """
        self.remove_sprites_of_layer(0)  # clear bg layer
        self.remove_sprites_of_layer(1)  # clear item layer
        self.add(area, layer=0)
        self.add(area.clickable_group.sprites(), layer=1)
        print 'loaded area'

    def remove_item(self, item):
        self.remove(item)

    def remove_item_by_name(self, item_name):
        self.remove(self.get_sprite_by_name(item_name))  # or in two steps to ensure it exists

    def clearMenuLayer(self):
        pass

    def fillMenuLayer(self, menu):
        # same layer but what is added after is above
        self.add(menu, layer=2)
        for button in menu.buttons:
            self.add(button, layer=2)

    def displayText(self, text, position=None, textcolor=(255, 255, 255), bgcolor=(0, 0, 0)):
        label_image = self.font.render(text, True, textcolor, bgcolor)
        label = self.get_sprites_from_layer(3)[0]
        label.image = label_image
        # if rect is not None:  # if no rect is passed, keep it!
        #     label.rect = rect
        # rect may be preserved by default or something (static text)
        # for now, let's adjust the rect whatever
        if position is not None:
            label.rect.topleft = position
        label.rect.size = label_image.get_size()

    def clearText(self):
        pass

    def displayCursor(self):
        pass

    def hideCursor(self):
        pass

    def get_sprite_by_name(self, sprite_name):
        for sprite in self:
            if sprite.codename == sprite_name:
                return sprite
        raise GetError(sprite_name, "layered view")