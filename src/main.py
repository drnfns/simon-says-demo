import pygame
import random
from button import Button  # Allows us to use our Button class

pygame.init()
clock = pygame.time.Clock()

# --- Constants ---
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simon Says")

# --- Color Definitions ---
GREEN_ON = (0, 255, 0)
GREEN_OFF = (0, 150, 0)
RED_ON = (255, 0, 0)
RED_OFF = (150, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 150)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (150, 150, 0)

# --- Sound Loading ---
# Load the sounds for red, blue, and yellow
GREEN_SOUND = pygame.mixer.Sound("../assets/bell1.mp3")
RED_SOUND = pygame.mixer.Sound("../assets/bell2.mp3")
BLUE_SOUND = pygame.mixer.Sound("../assets/bell3.mp3")
YELLOW_SOUND = pygame.mixer.Sound("../assets/bell4.mp3")

# --- Button Sprite Objects ---
# Create the red, blue, and yellow Button objects.
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 10, 10)
red = Button(RED_ON, RED_OFF, RED_SOUND, 260, 10)
blue = Button(BLUE_ON, BLUE_OFF, BLUE_SOUND, 10, 260)
yellow = Button(YELLOW_ON, YELLOW_OFF, YELLOW_SOUND, 260, 260)

# --- Game Variables ---
cpu_sequence = []
player_sequence = []
colors = ["green", "red", "blue", "yellow"]
score = 0


# Draws the initial game board
def draw_board():
    # Call the .draw() method on all four button objects
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)


# --- Game Logic Functions ---


# Computer takes its turn
def cpu_turn():
    # Pick a random color and add it to the sequence
    choice = random.choice(colors)
    cpu_sequence.append(choice)

    if choice == "green":
        green.update(SCREEN)
    elif choice == "red":
        red.update(SCREEN)
    elif choice == "blue":
        blue.update(SCREEN)
    else:
        yellow.update(SCREEN)

    # Small delay for the player to see the sequence
    pygame.time.wait(500)

    player_turn()


# Repeats the current CPU sequence for the player to see
def repeat_cpu_sequence():
    if len(cpu_sequence) == 0:
        return  # Do nothing if the sequence is empty

    # A small delay before the sequence starts
    pygame.time.wait(500)

    for color in cpu_sequence:
        if color == "green":
            green.update(SCREEN)
        elif color == "red":
            red.update(SCREEN)
        elif color == "blue":
            blue.update(SCREEN)
        else:
            yellow.update(SCREEN)

        # Wait a little between button flashes
        pygame.time.wait(200)


# Handles the player's turn
def player_turn():
    global player_sequence  # Use the global player_sequence variable
    player_sequence = []  # Reset player's sequence for this round

    # Loop until the player has matched the CPU's sequence length
    while len(player_sequence) < len(cpu_sequence):
        clicked = False
        # Listen for click event
        while not clicked:
            for event in pygame.event.get():
                # Check if player wants to quit
                if event.type == pygame.QUIT:
                    game_over()  # Quit immediately

                # Ignore events other than a mouse click
                if event.type != pygame.MOUSEBUTTONUP or event.button != 1:
                    continue

                # Get the current position of the mouse
                pos = pygame.mouse.get_pos()

                # Check if the green button was selected
                if green.selected(pos):
                    green.update(SCREEN)
                    player_sequence.append("green")
                    clicked = True  # Exit the while loop, go to check_sequence
                elif red.selected(pos):
                    red.update(SCREEN)
                    player_sequence.append("red")
                    clicked = True
                elif blue.selected(pos):
                    blue.update(SCREEN)
                    player_sequence.append("blue")
                    clicked = True
                elif yellow.selected(pos):
                    yellow.update(SCREEN)
                    player_sequence.append("yellow")
                    clicked = True

        # After each player click, check if the sequence is correct so far
        check_sequence(player_sequence)


# Checks if the player's move matches the CPU sequence
def check_sequence(player_sequence):
    global score  # Use the global score variable
    # Compare the player's sequence to the corresponding part of the CPU's sequence
    if player_sequence != cpu_sequence[:len(player_sequence)]:
        print("Wrong! Final Score:", score)
        game_over()
    else:
        if len(player_sequence) == len(cpu_sequence):
            score += 1
            print("Correct! Score:", score)
            pygame.time.wait(500)


# Quits the game
def game_over():
    pygame.quit()
    quit()


# --- Main Game Loop ---
running = True
while running:
    # Handle the quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((40, 40, 40))  # Dark grey colour for background

    draw_board()
    repeat_cpu_sequence()
    cpu_turn()

    # A brief pause before the next round starts
    pygame.time.wait(1000)

    pygame.display.update()
    clock.tick(60)

# Quit the game properly when the loop ends
game_over()
