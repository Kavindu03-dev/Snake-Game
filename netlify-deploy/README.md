# ByteSnake - Netlify Deployment

This folder contains the web version of ByteSnake ready for Netlify deployment.

## Files Included

- `index.html` - Main HTML file with game interface
- `snake.js` - JavaScript game logic
- `_redirects` - Netlify configuration for SPA routing
- `netlify.toml` - Netlify build configuration and headers
- `README.md` - This file

## How to Deploy to Netlify

### Method 1: Drag and Drop
1. Go to [netlify.com](https://netlify.com)
2. Sign up or log in to your account
3. Drag this entire `netlify-deploy` folder to the Netlify dashboard
4. Your game will be deployed automatically!

### Method 2: Manual Upload
1. Go to [netlify.com](https://netlify.com)
2. Sign up or log in to your account
3. Click "New site from deploy"
4. Choose "Deploy manually"
5. Upload all files from this folder
6. Your game will be live!

### Method 3: Git Repository (Recommended)
1. Push this folder's contents to a Git repository
2. Connect your repository to Netlify
3. Set publish directory to the root or this folder
4. Netlify will automatically deploy on commits

## Game Features

- Classic Snake gameplay with modern enhancements
- Progressive difficulty with speed increase and levels
- Obstacle system with different patterns per level
- Sound effects for eating food and game over
- Pause/Resume functionality (Press P)
- Level progression every 10 points
- High score persistence
- Multiple control schemes (Arrow keys + WASD)

## Controls

- **Movement**: Arrow Keys or WASD
- **Pause**: P key
- **Restart**: R key (when game over)
- **Quit**: Q key (when game over)

Enjoy playing ByteSnake!
