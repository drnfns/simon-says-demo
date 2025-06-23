import pygame

# Initialize pygame
pygame.init()


class Button(pygame.sprite.Sprite):
    # The __init__ method is the constructor for the class.
    # It runs when a new Button object is created.
    # TODO: Add the required properties as parameters: color_on, color_off, sound, x, y
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # TODO: Initialize properties from the parameters

        # This creates the visual representation of the button
        self.image = pygame.Surface((230, 230))
        # TODO: Fill the image with its "off" color
        self.image.fill(self.color_off)

        # This gets the rectangular area of the image
        self.rect = self.image.get_rect()

        # TODO: Assign the x, y coordinates to the top left of the sprite's rect

    # Draws the button sprite onto the pygame window when called
    def draw(self, screen):
        # TODO: Blit the button's image onto the screen at its rect position
        pass

    # Checks if this button was clicked/selected by the player
    def selected(self, mouse_pos):
        # TODO: Check if the mouse_pos is inside the button's rect.
        # Return True if it is, False if it's not.
        pass

    # Illuminates the button and plays its sound.
    def update(self, screen):
        # TODO: "Turn on" the button by filling its image with the "on" color

        # TODO: Blit the image to the screen to show the color change

        # Refresh the display to make the change visible
        pygame.display.update()

        # TODO: Play the button's sound

        # Fill the image with the "off" color again
        self.image.fill(self.color_off)
        # Blit the "off" image to the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # Wait for 500 milliseconds (0.5 seconds)
        pygame.time.wait(500)
        # Refresh the display again
        pygame.display.update()
