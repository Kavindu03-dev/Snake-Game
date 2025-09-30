#!/usr/bin/env python3
"""
Snake Game - A simple implementation using pygame and deque

A classic Snake game with:
- Grid-based movement using collections.deque
- Progressive speed increase with score
- High score persistence
- Game over screen with restart functionality
"""

import pygame
import sys
import random
from collections import deque

# =============================================================================
# GAME SETTINGS - Easy to modify colors, sizes, and gameplay parameters
# =============================================================================

# Window and Grid Settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
BASE_FPS = 10  # Base speed for snake movement (moves per second)

# Color Settings (RGB values)
COLORS = {
    'background': (0, 0, 0),           # Black background
    'grid_lines': (50, 50, 50),        # Dark gray grid lines
    'snake_head': (0, 255, 0),         # Bright green snake head
    'snake_body': (0, 200, 0),         # Darker green snake body
    'food': (255, 0, 0),               # Red food
    'text': (255, 255, 255),           # White text
}

# Gameplay Settings
SPEED_INCREASE_INTERVAL = 5  # Score interval for speed increase
DISPLAY_FPS = 60  # Fixed display refresh rate
ENABLE_SOUND = True  # Set to False to disable sound effects

# Initialize Pygame
pygame.init()

# Initialize sound mixer if sound is enabled
if ENABLE_SOUND:
    pygame.mixer.init()

# =============================================================================
# GAME CLASSES
# =============================================================================

class Snake:
    """Represents the snake in the game using deque for efficient head/tail operations."""
    
    def __init__(self, start_position):
        """Initialize snake with starting position.
        
        Args:
            start_position (tuple): (x, y) grid coordinates for snake head
        """
        self.body = deque([start_position])
    
    def move(self, direction, should_grow=False):
        """Move snake in given direction.
        
        Args:
            direction (tuple): (dx, dy) movement direction
            should_grow (bool): If True, snake grows by one segment
        """
        current_head_x, current_head_y = self.body[0]
        new_head_position = (current_head_x + direction[0], current_head_y + direction[1])
        
        # Add new head to front of deque
        self.body.appendleft(new_head_position)
        
        # Remove tail if not growing
        if not should_grow:
            self.body.pop()
    
    def get_head_position(self):
        """Get the current head position.
        
        Returns:
            tuple: (x, y) coordinates of snake head
        """
        return self.body[0]
    
    def contains_position(self, position):
        """Check if snake body contains the given position.
        
        Args:
            position (tuple): (x, y) coordinates to check
            
        Returns:
            bool: True if position is occupied by snake
        """
        return position in self.body


class Food:
    """Represents the food that the snake can eat."""
    
    def __init__(self, snake_body):
        """Initialize food at a random position not occupied by snake.
        
        Args:
            snake_body (deque): Current snake body positions to avoid
        """
        self.position = self._find_random_position(snake_body)
    
    def _find_random_position(self, snake_body):
        """Find a random position not occupied by the snake.
        
        Args:
            snake_body (deque): Snake body positions to avoid
            
        Returns:
            tuple: (x, y) coordinates for food position
        """
        grid_width = WINDOW_WIDTH // CELL_SIZE
        grid_height = WINDOW_HEIGHT // CELL_SIZE
        
        # Generate all possible grid positions
        all_positions = [(x, y) for x in range(grid_width) for y in range(grid_height)]
        
        # Filter out positions occupied by snake
        available_positions = [pos for pos in all_positions if pos not in snake_body]
        
        return random.choice(available_positions)
    
    def respawn(self, snake_body):
        """Respawn food at a new random position.
        
        Args:
            snake_body (deque): Current snake body to avoid
        """
        self.position = self._find_random_position(snake_body)

# =============================================================================
# SOUND EFFECTS
# =============================================================================

def create_sound_effects():
    """Create simple sound effects using pygame's sound generation."""
    if not ENABLE_SOUND:
        return None, None
    
    # Create a simple beep sound for eating food
    eat_sound = pygame.sndarray.make_sound(
        pygame.sndarray.array(
            [[int(4096 * (1 + 0.5 * (i % 100) / 100)) for _ in range(2)] 
             for i in range(1000)]
        )
    )
    
    # Create a lower pitched sound for game over
    game_over_sound = pygame.sndarray.make_sound(
        pygame.sndarray.array(
            [[int(2048 * (1 + 0.3 * (i % 200) / 200)) for _ in range(2)] 
             for i in range(2000)]
        )
    )
    
    return eat_sound, game_over_sound


def play_sound(sound):
    """Play a sound effect if sound is enabled."""
    if ENABLE_SOUND and sound:
        sound.play()


# =============================================================================
# OBSTACLE SYSTEM
# =============================================================================

class Obstacle:
    """Represents a fixed obstacle block on the grid."""
    
    def __init__(self, position):
        """Initialize obstacle at given position.
        
        Args:
            position (tuple): (x, y) grid coordinates
        """
        self.position = position
    
    def draw(self, surface):
        """Draw the obstacle on the surface.
        
        Args:
            surface: pygame surface to draw on
        """
        x, y = self.position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, (100, 100, 100), rect)  # Gray obstacle


def create_level_obstacles(level):
    """Create obstacles for different levels.
    
    Args:
        level (int): Current level number
        
    Returns:
        list: List of Obstacle objects
    """
    obstacles = []
    
    if level == 1:
        # Level 1: Simple border obstacles
        grid_width = WINDOW_WIDTH // CELL_SIZE
        grid_height = WINDOW_HEIGHT // CELL_SIZE
        
        # Add some corner obstacles
        obstacles.extend([
            Obstacle((5, 5)),
            Obstacle((grid_width - 6, 5)),
            Obstacle((5, grid_height - 6)),
            Obstacle((grid_width - 6, grid_height - 6))
        ])
    
    elif level == 2:
        # Level 2: More complex pattern
        grid_width = WINDOW_WIDTH // CELL_SIZE
        grid_height = WINDOW_HEIGHT // CELL_SIZE
        
        # Create a cross pattern in the middle
        center_x, center_y = grid_width // 2, grid_height // 2
        for i in range(-2, 3):
            obstacles.extend([
                Obstacle((center_x + i, center_y)),
                Obstacle((center_x, center_y + i))
            ])
    
    elif level >= 3:
        # Level 3+: Random obstacles
        grid_width = WINDOW_WIDTH // CELL_SIZE
        grid_height = WINDOW_HEIGHT // CELL_SIZE
        num_obstacles = min(level * 3, 20)  # Cap at 20 obstacles
        
        for _ in range(num_obstacles):
            x = random.randint(2, grid_width - 3)
            y = random.randint(2, grid_height - 3)
            obstacles.append(Obstacle((x, y)))
    
    return obstacles


# =============================================================================
# INITIALIZATION FUNCTIONS
# =============================================================================

def initialize_pygame():
    """Initialize pygame display and return screen and clock objects.
    
    Returns:
        tuple: (screen, clock) pygame objects
    """
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("ByteSnake")
    clock = pygame.time.Clock()
    return screen, clock


# =============================================================================
# DRAWING FUNCTIONS
# =============================================================================

def draw_background(surface):
    """Draw the game background and grid.
    
    Args:
        surface: pygame surface to draw on
    """
    # Fill background
    surface.fill(COLORS['background'])
    
    # Draw grid lines
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, COLORS['grid_lines'], (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, COLORS['grid_lines'], (0, y), (WINDOW_WIDTH, y))


def draw_text(surface, text, position, font_size=36):
    """Draw text on the surface at the given position.
    
    Args:
        surface: pygame surface to draw on
        text (str): Text to display
        position (tuple): (x, y) coordinates for text
        font_size (int): Font size for the text
    """
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, COLORS['text'])
    surface.blit(text_surface, position)


def draw_snake(surface, snake_body):
    """Draw the snake with different colors for head and body.
    
    Args:
        surface: pygame surface to draw on
        snake_body (deque): Snake body positions
    """
    for segment_index, segment_position in enumerate(snake_body):
        x, y = segment_position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        
        if segment_index == 0:  # Head
            pygame.draw.rect(surface, COLORS['snake_head'], rect)
        else:  # Body
            pygame.draw.rect(surface, COLORS['snake_body'], rect)


def draw_food(surface, food_position):
    """Draw the food as a rectangle.
    
    Args:
        surface: pygame surface to draw on
        food_position (tuple): (x, y) grid coordinates of food
    """
    x, y = food_position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, COLORS['food'], rect)


def draw_game_ui(surface, current_score, current_speed, high_score, level, is_paused):
    """Draw the game UI elements (score, speed, high score, level, pause status).
    
    Args:
        surface: pygame surface to draw on
        current_score (int): Current game score
        current_speed (int): Current game speed
        high_score (int): High score
        level (int): Current level
        is_paused (bool): Whether the game is paused
    """
    draw_text(surface, f"Score: {current_score}", (10, 10))
    draw_text(surface, f"Speed: {current_speed}", (10, 50))
    draw_text(surface, f"High Score: {high_score}", (10, 90))
    draw_text(surface, f"Level: {level}", (10, 130))
    
    if is_paused:
        center_x = WINDOW_WIDTH // 2
        center_y = WINDOW_HEIGHT // 2
        draw_text(surface, "PAUSED", (center_x - 50, center_y - 20), 48)
        draw_text(surface, "Press P to Resume", (center_x - 100, center_y + 20))


def draw_game_over_screen(surface):
    """Draw the game over screen with restart instructions.
    
    Args:
        surface: pygame surface to draw on
    """
    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2
    
    draw_text(surface, "GAME OVER", (center_x - 100, center_y - 30), 48)
    draw_text(surface, "Press R to Restart or Q to Quit", 
              (center_x - 150, center_y + 10))

# =============================================================================
# INPUT HANDLING FUNCTIONS
# =============================================================================

def handle_events(snake_direction, is_game_over, is_paused):
    """Handle keyboard input and pygame events.
    
    Args:
        snake_direction (tuple): Current snake direction (dx, dy)
        is_game_over (bool): Whether the game is in game over state
        is_paused (bool): Whether the game is paused
        
    Returns:
        tuple: (is_running, new_direction, should_restart, new_pause_state)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, snake_direction, False, is_paused
        elif event.type == pygame.KEYDOWN:
            if is_game_over:
                running, direction, restart = _handle_game_over_input(event)
                return running, direction, restart, is_paused
            else:
                snake_direction, new_pause_state = _handle_game_input(event, snake_direction, is_paused)
                return True, snake_direction, False, new_pause_state
    
    return True, snake_direction, False, is_paused


def _handle_game_over_input(event):
    """Handle input during game over screen.
    
    Args:
        event: pygame event object
        
    Returns:
        tuple: (is_running, direction, should_restart)
    """
    if event.key == pygame.K_r:
        return True, (1, 0), True  # Restart game
    elif event.key == pygame.K_q:
        return False, (1, 0), False  # Quit game
    return True, (1, 0), False


def _handle_game_input(event, current_direction, is_paused):
    """Handle input during gameplay.
    
    Args:
        event: pygame event object
        current_direction (tuple): Current snake direction
        is_paused (bool): Current pause state
        
    Returns:
        tuple: (new_direction, new_pause_state)
    """
    # Pause toggle
    if event.key == pygame.K_p:
        return current_direction, not is_paused
    
    # Only handle movement if not paused
    if is_paused:
        return current_direction, is_paused
    
    # Arrow keys and WASD mapping with 180° turn prevention
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        # Can't go up if currently going down
        if current_direction != (0, 1):
            return (0, -1), is_paused
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        # Can't go down if currently going up
        if current_direction != (0, -1):
            return (0, 1), is_paused
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        # Can't go left if currently going right
        if current_direction != (1, 0):
            return (-1, 0), is_paused
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        # Can't go right if currently going left
        if current_direction != (-1, 0):
            return (1, 0), is_paused
    
    return current_direction, is_paused

# =============================================================================
# GAME LOGIC FUNCTIONS
# =============================================================================

def check_wall_collision(snake_head_position):
    """Check if snake head hits the wall boundaries.
    
    Args:
        snake_head_position (tuple): (x, y) coordinates of snake head
        
    Returns:
        bool: True if collision with wall detected
    """
    x, y = snake_head_position
    grid_width = WINDOW_WIDTH // CELL_SIZE
    grid_height = WINDOW_HEIGHT // CELL_SIZE
    
    return (x < 0 or x >= grid_width or y < 0 or y >= grid_height)


def check_self_collision(snake_body):
    """Check if snake head collides with its own body.
    
    Args:
        snake_body (deque): Snake body positions
        
    Returns:
        bool: True if self-collision detected
    """
    head_position = snake_body[0]
    body_positions = list(snake_body)[1:]  # Exclude head from body check
    return head_position in body_positions


def check_obstacle_collision(snake_head_position, obstacles):
    """Check if snake head collides with any obstacle.
    
    Args:
        snake_head_position (tuple): (x, y) coordinates of snake head
        obstacles (list): List of Obstacle objects
        
    Returns:
        bool: True if collision with obstacle detected
    """
    for obstacle in obstacles:
        if snake_head_position == obstacle.position:
            return True
    return False


def calculate_game_speed(score):
    """Calculate current game speed based on score.
    
    Args:
        score (int): Current game score
        
    Returns:
        int: Current speed in moves per second
    """
    return BASE_FPS + score // SPEED_INCREASE_INTERVAL


def load_high_score():
    """Load high score from persistent storage.
    
    Returns:
        int: High score value, 0 if file doesn't exist
    """
    try:
        with open('highscore.txt', 'r') as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    """Save high score to persistent storage.
    
    Args:
        score (int): Score to save as high score
    """
    try:
        with open('highscore.txt', 'w') as file:
            file.write(str(score))
    except IOError:
        pass  # Silently fail if can't write file


def update_high_score_if_needed(current_score, current_high_score):
    """Update high score if current score is higher.
    
    Args:
        current_score (int): Current game score
        current_high_score (int): Current high score
        
    Returns:
        int: Updated high score
    """
    if current_score > current_high_score:
        new_high_score = current_score
        save_high_score(new_high_score)
        return new_high_score
    return current_high_score

# =============================================================================
# GAME STATE MANAGEMENT
# =============================================================================

def initialize_game_state():
    """Initialize a new game state with default values.
    
    Returns:
        dict: Game state dictionary with all initial values
    """
    center_x = WINDOW_WIDTH // CELL_SIZE // 2
    center_y = WINDOW_HEIGHT // CELL_SIZE // 2
    
    return {
        'snake_direction': (1, 0),  # Start moving right
        'score': 0,
        'level': 1,
        'is_game_over': False,
        'is_paused': False,
        'snake': Snake((center_x, center_y)),
        'food': None,  # Will be initialized after snake
        'obstacles': [],
        'high_score': load_high_score(),
        'last_move_time': 0,
        'eat_sound': None,
        'game_over_sound': None
    }


def reset_game_state(game_state):
    """Reset game state to initial values.
    
    Args:
        game_state (dict): Current game state to reset
        
    Returns:
        dict: Reset game state
    """
    center_x = WINDOW_WIDTH // CELL_SIZE // 2
    center_y = WINDOW_HEIGHT // CELL_SIZE // 2
    
    game_state['snake_direction'] = (1, 0)
    game_state['score'] = 0
    game_state['level'] = 1
    game_state['is_game_over'] = False
    game_state['is_paused'] = False
    game_state['snake'] = Snake((center_x, center_y))
    game_state['food'] = Food(game_state['snake'].body)
    game_state['obstacles'] = create_level_obstacles(1)
    game_state['high_score'] = load_high_score()
    game_state['last_move_time'] = 0
    
    return game_state

# =============================================================================
# GAME UPDATE FUNCTIONS
# =============================================================================

def update_game_logic(game_state, current_time):
    """Update game logic including movement, collisions, and scoring.
    
    Args:
        game_state (dict): Current game state
        current_time (int): Current time in milliseconds
        
    Returns:
        bool: True if game should continue, False if game over
    """
    if game_state['is_game_over'] or game_state['is_paused']:
        return True
    
    current_speed = calculate_game_speed(game_state['score'])
    time_since_last_move = current_time - game_state['last_move_time']
    move_interval = 1000 // current_speed
    
    # Only move if enough time has passed (grid-locked movement)
    if time_since_last_move >= move_interval:
        _handle_snake_movement(game_state)
        _check_collisions(game_state)
        _check_level_progression(game_state)
        game_state['last_move_time'] = current_time
    
    return True


def _handle_snake_movement(game_state):
    """Handle snake movement and food consumption.
    
    Args:
        game_state (dict): Current game state
    """
    snake = game_state['snake']
    food = game_state['food']
    direction = game_state['snake_direction']
    
    # Check if snake eats food
    if snake.get_head_position() == food.position:
        # Snake ate food - grow and respawn food
        food.respawn(snake.body)
        game_state['score'] += 1
        snake.move(direction, should_grow=True)
        # Play eat sound
        play_sound(game_state['eat_sound'])
    else:
        # Normal movement without growth
        snake.move(direction, should_grow=False)


def _check_collisions(game_state):
    """Check for wall, self, and obstacle collisions.
    
    Args:
        game_state (dict): Current game state
    """
    snake = game_state['snake']
    head_position = snake.get_head_position()
    
    # Check wall collision
    if check_wall_collision(head_position):
        game_state['is_game_over'] = True
        game_state['high_score'] = update_high_score_if_needed(
            game_state['score'], game_state['high_score'])
        play_sound(game_state['game_over_sound'])
    
    # Check self collision
    elif check_self_collision(snake.body):
        game_state['is_game_over'] = True
        game_state['high_score'] = update_high_score_if_needed(
            game_state['score'], game_state['high_score'])
        play_sound(game_state['game_over_sound'])
    
    # Check obstacle collision
    elif check_obstacle_collision(head_position, game_state['obstacles']):
        game_state['is_game_over'] = True
        game_state['high_score'] = update_high_score_if_needed(
            game_state['score'], game_state['high_score'])
        play_sound(game_state['game_over_sound'])


def _check_level_progression(game_state):
    """Check if player should advance to next level.
    
    Args:
        game_state (dict): Current game state
    """
    # Advance level every 10 points
    new_level = (game_state['score'] // 10) + 1
    if new_level > game_state['level']:
        game_state['level'] = new_level
        game_state['obstacles'] = create_level_obstacles(new_level)


def render_game(screen, game_state):
    """Render all game elements to the screen.
    
    Args:
        screen: pygame screen surface
        game_state (dict): Current game state
    """
    # Draw background and grid
    draw_background(screen)
    
    # Draw obstacles
    for obstacle in game_state['obstacles']:
        obstacle.draw(screen)
    
    # Draw game objects
    draw_snake(screen, game_state['snake'].body)
    draw_food(screen, game_state['food'].position)
    
    # Draw UI elements
    current_speed = calculate_game_speed(game_state['score'])
    draw_game_ui(screen, game_state['score'], current_speed, game_state['high_score'], 
                 game_state['level'], game_state['is_paused'])
    
    # Draw game over screen if needed
    if game_state['is_game_over']:
        draw_game_over_screen(screen)


# =============================================================================
# MAIN GAME LOOP
# =============================================================================

def run_game():
    """Main game function that initializes and runs the game loop."""
    screen, clock = initialize_pygame()
    game_state = initialize_game_state()
    
    # Initialize sound effects
    eat_sound, game_over_sound = create_sound_effects()
    game_state['eat_sound'] = eat_sound
    game_state['game_over_sound'] = game_over_sound
    
    # Initialize food and obstacles
    game_state['food'] = Food(game_state['snake'].body)
    game_state['obstacles'] = create_level_obstacles(1)
    
    is_running = True
    
    while is_running:
        current_time = pygame.time.get_ticks()
        
        # Handle input events
        is_running, new_direction, should_restart, new_pause_state = handle_events(
            game_state['snake_direction'], game_state['is_game_over'], game_state['is_paused'])
        
        # Update snake direction and pause state
        game_state['snake_direction'] = new_direction
        game_state['is_paused'] = new_pause_state
        
        if should_restart:
            game_state = reset_game_state(game_state)
            game_state['last_move_time'] = current_time
            continue
        
        # Update game logic
        if not update_game_logic(game_state, current_time):
            break
        
        # Render everything
        render_game(screen, game_state)
        pygame.display.flip()
        clock.tick(DISPLAY_FPS)
    
    pygame.quit()
    sys.exit()


def main():
    """Entry point for the game."""
    run_game()


if __name__ == "__main__":
    main()
