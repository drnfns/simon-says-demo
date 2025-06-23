import pygame
import random
from button import Button # Allows us to use our Button class

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
# TODO: Load the sounds for red, blue, and yellow
GREEN_SOUND = pygame.mixer.Sound("../assets/bell1.mp3")
RED_SOUND = None
BLUE_SOUND = None
YELLOW_SOUND = None

# --- Button Sprite Objects ---
# TODO: Create the red, blue, and yellow Button objects.
# Use the green button as a reference. Its width and height are 230.
# If the buttons are 230 pixels in width and height, and the spacing
# are 10 pixels, where should the red, blue and yellow be?
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 10, 10)
red = None
blue = None
yellow = None

# --- Game Variables ---
cpu_sequence = []
player_sequence = []
colors = ["green", "red", "blue", "yellow"]
score = 0

# Draws the initial game board
def draw_board():
  # TODO: Call the .draw() method on all four button objects
  pass

# --- Game Logic Functions ---

# Computer takes its turn
def cpu_turn():
  # Pick a random color and add it to the sequence
  choice = random.choice(colors)
  cpu_sequence.append(choice)

  if choice == "green":
    green.update(SCREEN)
  # TODO: Add the 'elif' conditions for "red", "blue", and "yellow"

  player_turn()

# Repeats the current CPU sequence for the player to see
def repeat_cpu_sequence():
  if len(cpu_sequence) == 0:
    return # Do nothing if the sequence is empty

  # A small delay before the sequence starts
  pygame.time.wait(500)

  for color in cpu_sequence:
    if color == "green":
      green.update(SCREEN)
    # TODO: Add the 'elif' conditions for "red", "blue", and "yellow"

    # Wait a little between button flashes
    pygame.time.wait(200)

# Handles the player's turn
def player_turn():
  global player_sequence # Use the global player_sequence variable
  player_sequence = [] # Reset player's sequence for this round

  # Loop until the player has matched the CPU's sequence length
  while len(player_sequence) < len(cpu_sequence):
    clicked = False
    # Listen for click event
    while not clicked:
      for event in pygame.event.get():
        # Check if player wants to quit
        if event.type == pygame.QUIT:
          game_over() # Quit immediately
        
        # Ignore events other than a mouse click
        if event.type != pygame.MOUSEBUTTONUP or event.button != 1:
          continue
        
        # TODO: Get the current position of the mouse
        # pos = ...
        
        # Check if the green button was selected
        if green.selected(pos):
          green.update(SCREEN)
          player_sequence.append("green")
          clicked = True # Exit the while loop, go to check_sequence
        # TODO: Add the 'elif' conditions for the other three buttons
        # elif red.selected(pos):
        #   ...

    # After each player click, check if the sequence is correct so far
    check_sequence(player_sequence)

# Checks if the player's move matches the CPU sequence
def check_sequence(player_sequence):
  global score # Use the global score variable
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

  SCREEN.fill((40, 40, 40)) # Dark grey colour for background

  draw_board()
  repeat_cpu_sequence()
  cpu_turn()

  # A brief pause before the next round starts
  pygame.time.wait(1000)

  pygame.display.update()
  clock.tick(60)

# Quit the game properly when the loop ends
game_over()
