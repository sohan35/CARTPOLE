import pygame
import time
import numpy as np
from cartpole_env import CustomCartPoleEnv

# Create the custom CartPole environment
env = CustomCartPoleEnv()

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CartPole Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define function to draw cartpole
def draw_cartpole(screen, state):
    cart_x = int(state[0] * screen_width / 4) + screen_width / 2
    cart_y = screen_height // 2
    pole_length = 100
    pole_end_x = cart_x + pole_length * np.sin(state[2])
    pole_end_y = cart_y - pole_length * np.cos(state[2])
    pygame.draw.line(screen, BLACK, (0, cart_y), (screen_width, cart_y), 2)
    pygame.draw.line(screen, BLACK, (cart_x, cart_y), (pole_end_x, pole_end_y), 4)
    pygame.draw.circle(screen, BLACK, (int(cart_x), int(cart_y)), 10)

# Reset the environment
obs = env.reset()

# Set the duration of the game in seconds
game_duration = 10  # 10 seconds

start_time = time.time()
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Take a random action
    action = env.action_space.sample()

    # Perform the action in the environment
    obs, reward, done, _ = env.step(action)

    # Draw the CartPole
    draw_cartpole(screen, obs)

    # Update the display
    pygame.display.flip()

    # Check if the game duration has elapsed
    if time.time() - start_time >= game_duration:
        running = False

    # Slow down the loop to see the animation
    time.sleep(0.02)

    if done:
        obs = env.reset()

# Close the environment
env.close()
pygame.quit()
