import pygame

# Initialize pygame
pygame.init()

class Button(pygame.sprite.Sprite):
    # The __init__ method is the constructor for the class.
    # It runs when a new Button object is created.
    # Add the required properties as parameters: color_on, color_off, sound, x, y
    def __init__(self, color_on, color_off, sound, x, y):
        pygame.sprite.Sprite.__init__(self)

        # Initialize properties from the parameters
        self.color_on = color_on
        self.color_off = color_off
        self.sound = sound

        # This creates the visual representation of the button
        self.image = pygame.Surface((230, 230))

        # Fill the image with its "off" color
        self.image.fill(self.color_off)

        # This gets the rectangular area of the image
        self.rect = self.image.get_rect()

        # Assign the x, y coordinates to the top left of the sprite's rect
        self.rect.topleft = (x, y)

    # Draws the button sprite onto the pygame window when called
    def draw(self, screen):
        # Blit the button's image onto the screen at its rect position
        screen.blit(self.image, self.rect)

    # Checks if this button was clicked/selected by the player
    def selected(self, mouse_pos):
        # Check if the mouse_pos is inside the button's rect.
        # Return True if it is, False if it's not.
        return self.rect.collidepoint(mouse_pos)

    # Illuminates the button and plays its sound.
    def update(self, screen):
        # "Turn on" the button by filling its image with the "on" color
        self.image.fill(self.color_on)

        # Blit the image to the screen to show the color change
        screen.blit(self.image, self.rect)

        # Refresh the display to make the change visible
        pygame.display.update()

        # Play the button's sound
        self.sound.play()

        # Fill the image with the "off" color again
        self.image.fill(self.color_off)

        # Blit the "off" image to the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Wait for 500 milliseconds (0.5 seconds)
        pygame.time.wait(500)

        # Refresh the display again
        pygame.display.update()
