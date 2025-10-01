# 🐍 ByteSnake - Multi-Platform Snake Game

A modern implementation of the classic Snake game available in both Python (pygame) and Web (HTML5/JavaScript) versions. Features progressive difficulty, obstacle systems, sound effects, and multiple control schemes.

![Game Preview](https://img.shields.io/badge/Game-Snake-brightgreen) ![Python](https://img.shields.io/badge/Python-3.7+-blue) ![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow) ![Pygame](https://img.shields.io/badge/Pygame-2.5.2-red) ![Web](https://img.shields.io/badge/Web-HTML5%2FCSS3%2FJS-orange)

## 🎮 Game Features

### Core Gameplay
- **Classic Snake mechanics** with modern enhancements
- **Progressive difficulty** - speed increases with score
- **Level system** - advance every 10 points with new obstacle patterns
- **Obstacle system** - different patterns per level (corners, cross, random)
- **Grid-locked movement** for precise control
- **180° turn prevention** for smooth gameplay

### Audio & Visual
- **Sound effects** for eating food and game over
- **Modern UI** with score, speed, level, and high score display
- **Pause/Resume functionality** (Press P)
- **Professional styling** with dark theme and neon colors
- **Responsive design** for web version

### Controls
- **Movement**: Arrow Keys or WASD
- **Pause**: P key
- **Restart**: R key (when game over)
- **Quit**: Q key (when game over)

## 📁 Project Structure

```
Snake-Game/
├── README.md                    # This file
├── snake_game/                  # Main project directory
│   ├── main.py                 # Python version (pygame)
│   ├── index.html              # Web version (HTML5)
│   ├── snake.js                # Web version (JavaScript)
│   ├── requirements.txt        # Python dependencies
│   ├── run_python.bat          # Windows Python launcher
│   ├── run_web.bat             # Windows Web launcher
│   └── run_byteSnake.bat       # Windows combined launcher
└── netlify-deploy/             # Ready-to-deploy web version
    ├── index.html              # Web game file
    ├── snake.js                # Game logic
    ├── _redirects              # Netlify configuration
    └── README.md               # Deployment instructions
```

## 🚀 Quick Start

### Web Version (No Installation Required)
1. **Local Play**: Open `snake_game/index.html` in your browser
2. **Local Server**: Run `python -m http.server 8000` and visit `http://localhost:8000`
3. **Deploy to Netlify**: Drag the `netlify-deploy` folder to [netlify.com](https://netlify.com)

### Python Version
1. **Install Python 3.7+** and pip
2. **Install dependencies**:
   ```bash
   pip install -r snake_game/requirements.txt
   ```
3. **Run the game**:
   ```bash
   python snake_game/main.py
   ```

### Windows Users
- **Python Version**: Double-click `snake_game/run_python.bat`
- **Web Version**: Double-click `snake_game/run_web.bat`
- **Both**: Double-click `snake_game/run_byteSnake.bat`

## 🛠️ Installation & Setup

### Prerequisites
- **Python 3.7+** (for Python version)
- **Modern web browser** (for web version)
- **pip** (Python package manager)

### Python Version Setup
```bash
# Clone or download the project
cd Snake-Game

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r snake_game/requirements.txt

# Run the game
python snake_game/main.py
```

### Web Version Setup
```bash
# No installation required! Just open in browser:
# Option 1: Direct file
open snake_game/index.html

# Option 2: Local server (recommended)
cd snake_game
python -m http.server 8000
# Then open http://localhost:8000
```

## 🎯 Game Mechanics

### Scoring System
- **+1 point** for each food consumed
- **Speed increase** every 5 points
- **Level advancement** every 10 points
- **High score persistence** across sessions

### Level Progression
- **Level 1**: Corner obstacles (4 blocks)
- **Level 2**: Cross pattern obstacles (9 blocks)
- **Level 3+**: Random obstacles (level × 3, max 20)

### Collision Detection
- **Wall collision**: Game over if snake hits boundaries
- **Self collision**: Game over if snake hits its own body
- **Obstacle collision**: Game over if snake hits obstacles

## 🔧 Technical Details

### Python Version (Pygame)
- **Framework**: Pygame 2.5.2
- **Data Structure**: `collections.deque` for efficient snake body management
- **Architecture**: Object-oriented design with separate classes for Snake, Food, and Obstacles
- **Performance**: 60 FPS display with variable game speed
- **Storage**: High score saved to `highscore.txt`

### Web Version (HTML5/JavaScript)
- **Technologies**: HTML5 Canvas, CSS3, ES6+ JavaScript
- **Audio**: Web Audio API for sound generation
- **Storage**: LocalStorage for high score persistence
- **Performance**: RequestAnimationFrame for smooth 60 FPS
- **Responsive**: Adapts to different screen sizes

## 🌐 Deployment

### Netlify Deployment (Web Version)
1. Go to [netlify.com](https://netlify.com)
2. Sign up or log in
3. Drag the `netlify-deploy` folder to the dashboard
4. Your game will be live instantly!

### Other Hosting Options
- **GitHub Pages**: Upload `snake_game/` contents to a GitHub repository
- **Vercel**: Connect your GitHub repository
- **Firebase Hosting**: Use Firebase CLI to deploy
- **Any static hosting**: Upload the web files

## 🧪 Testing

### Test Scenarios
1. **Food Consumption**: Move snake to eat red food
2. **Wall Collision**: Hit walls to trigger game over
3. **Self-Collision**: Make snake hit its own body
4. **Obstacle Collision**: Hit gray obstacles (higher levels)
5. **Pause/Resume**: Press P during gameplay
6. **Level Progression**: Score 10+ points to advance
7. **Restart**: Press R on game over screen
8. **Speed Increase**: Notice increasing speed with score
9. **High Score**: Verify persistence across sessions
10. **Turn Prevention**: Try opposite direction keys quickly

## 🎨 Customization

### Python Version
Edit `snake_game/main.py` to modify:
- **Colors**: Change `COLORS` dictionary
- **Speed**: Modify `BASE_FPS` and `SPEED_INCREASE_INTERVAL`
- **Window Size**: Adjust `WINDOW_WIDTH` and `WINDOW_HEIGHT`
- **Cell Size**: Change `CELL_SIZE` for different grid density

### Web Version
Edit `snake_game/snake.js` to modify:
- **Colors**: Update `COLORS` object
- **Speed**: Change `BASE_SPEED` and `SPEED_INCREASE_INTERVAL`
- **Canvas Size**: Modify `CANVAS_WIDTH` and `CANVAS_HEIGHT`
- **Level Progression**: Adjust `LEVEL_ADVANCE_SCORE`

## 🐛 Troubleshooting

### Common Issues

**Python Version:**
- **"pygame not found"**: Run `pip install pygame`
- **"No module named pygame"**: Activate virtual environment first
- **Sound not working**: Check system audio settings

**Web Version:**
- **Game not loading**: Check browser console for errors
- **No sound**: Ensure browser allows audio (click to enable)
- **Poor performance**: Close other browser tabs

**General:**
- **Controls not responding**: Click on game area first
- **High score not saving**: Check file permissions (Python) or browser settings (Web)

## 📝 Development

### Code Structure
- **Modular design** with separate functions for different concerns
- **Comprehensive documentation** with docstrings
- **Type hints** where applicable
- **Error handling** for file operations and edge cases

### Adding Features
1. **New obstacles**: Modify `create_level_obstacles()` function
2. **Power-ups**: Add new game objects and collision detection
3. **Multiplayer**: Implement network communication
4. **Mobile support**: Add touch controls for web version

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Open an issue on GitHub
3. Review the code comments for implementation details

## 🎉 Acknowledgments

- **Pygame Community** for the excellent game development framework
- **HTML5 Canvas API** for web graphics capabilities
- **Classic Snake Game** for the timeless gameplay mechanics

---

**Enjoy playing ByteSnake!** 🐍✨

*Made with ❤️ and lots of 🐍*