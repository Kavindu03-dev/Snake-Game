# ByteSnake

Simple Snake game using deque for the snake body.

## Description

A classic Snake game implementation in Python using pygame for graphics and deque for efficient snake body management.

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate
   ```
   - On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Game

### Python Version (Enhanced)
```bash
python main.py
```

### Web Version (No Installation Required)
Simply open `index.html` in your web browser or run a local server:
```bash
# Using Python's built-in server
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

## Testing the Game

To verify all features work correctly, try these test scenarios:

1. **Food Consumption**: Use arrow keys or WASD to move the snake and eat the red food
2. **Wall Collision**: Move the snake into the walls to trigger game over
3. **Self-Collision**: Make the snake hit its own body to test collision detection
4. **Obstacle Collision**: Try hitting the gray obstacle blocks (appear in higher levels)
5. **Pause/Resume**: Press 'P' during gameplay to pause, press 'P' again to resume
6. **Level Progression**: Score 10+ points to advance to level 2 with more obstacles
7. **Restart Functionality**: Press 'R' on the game over screen to restart
8. **Speed Increase**: Notice how the game gets faster as your score increases
9. **High Score**: Check if your high score is saved and displayed correctly
10. **180° Turn Prevention**: Try pressing opposite direction keys quickly - should be ignored
11. **Sound Effects**: Listen for beep sounds when eating food and game over

## Features

- **Classic Snake gameplay** with modern enhancements
- **Efficient snake body management** using collections.deque
- **Progressive difficulty** with speed increase and levels
- **Obstacle system** with different patterns per level
- **Sound effects** for eating food and game over
- **Pause/Resume functionality** (Press P)
- **Level progression** every 10 points
- **High score persistence** with file storage
- **Grid-locked movement** with precise timing
- **180° turn prevention** for smooth gameplay
- **Multiple control schemes** (Arrow keys + WASD)
- **Professional UI** with score, speed, level, and high score display
