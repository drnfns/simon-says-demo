import pygame
import random
import time
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
GREEN_SOUND = pygame.mixer.Sound("assets/bell1.mp3")
RED_SOUND = None
BLUE_SOUND = None
YELLOW_SOUND = None


# --- Button Sprite Objects ---
# TODO: Create the red, blue, and yellow Button objects.
# Use the green button as a reference.
# The PDF provides the x, y coordinates:
# red: (260, 10)
# blue: (10, 260)
# yellow: (260, 260)
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 10, 10)
red = None
blue = None
yellow = None

# A list to hold all our button objects for easier access
all_buttons = [green, red, blue, yellow]

# --- Game Variables ---
cpu_sequence = []
player_sequence = []
colors = ["green", "red", "blue", "yellow"]
score = 0

# Draws the initial game board
def draw_board():
  # TODO: Call the .draw() method on all four button objects
  # Pass in SCREEN as the argument.
  # example: green.draw(SCREEN)
  pass # Remove this pass statement when you add your code

# --- Game Logic Functions ---

# Computer takes its turn
def cpu_turn():
  # Pick a random color and add it to the sequence
  choice = random.choice(colors)
  cpu_sequence.append(choice)

  # Illuminate the chosen button
  if choice == "green":
    green.update(SCREEN)
  # TODO: Add the 'elif' conditions for "red", "blue", and "yellow"
  # elif choice == "red":
  #   red.update(SCREEN)
  
  # Allow the player to start their turn
  player_turn()

# Repeats the current CPU sequence for the player to see
def repeat_cpu_sequence():
  if not cpu_sequence:
    return # Do nothing if the sequence is empty
  
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
  global player_sequence
  player_sequence = [] # Reset player's sequence for this round

  # Loop until the player has matched the CPU's sequence length
  while len(player_sequence) < len(cpu_sequence):
    waiting_for_input = True
    while waiting_for_input:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over()
        
        # Check for a mouse click
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
          # TODO: Get the current position of the mouse
          # pos = ...
          
          # Check if the green button was selected
          if green.selected(pos):
            green.update(SCREEN)
            player_sequence.append("green")
            waiting_for_input = False # Exit the inner loop
          # TODO: Add the 'elif' conditions for the other three buttons
          # elif red.selected(pos):
          #   ...
          
    # After each player click, check if the sequence is correct so far
    check_sequence(player_sequence)


# Checks if the player's move matches the CPU sequence
def check_sequence(player_sequence):
  global score
  # Compare the player's sequence to the corresponding part of the CPU's sequence
  if player_sequence != cpu_sequence[:len(player_sequence)]:
    print("Wrong! Final Score:", score)
    game_over()
  else:
    # If the player completes the whole sequence correctly
    if len(player_sequence) == len(cpu_sequence):
      score += 1
      print("Correct! Score:", score)
      # Give a small delay before the next round
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

  # Clear the screen
  SCREEN.fill((40, 40, 40)) # A dark grey background

  # Draw the buttons
  draw_board()
  
  # Show the CPU sequence
  repeat_cpu_sequence()
  
  # Let the CPU choose a new color and start the player's turn
  cpu_turn()
  
  # A brief pause before the next round starts
  pygame.time.wait(1000)

  pygame.display.update()
  clock.tick(60)

# Quit the game properly when the loop ends
game_over()
