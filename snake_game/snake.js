/**
 * Snake Game - Web Version
 * Enhanced with sound effects, pause/resume, levels, and obstacles
 */

// Game Configuration
const CONFIG = {
    CANVAS_WIDTH: 800,
    CANVAS_HEIGHT: 600,
    CELL_SIZE: 20,
    BASE_SPEED: 10,
    SPEED_INCREASE_INTERVAL: 5,
    LEVEL_ADVANCE_SCORE: 10,
    ENABLE_SOUND: true
};

// Colors
const COLORS = {
    BACKGROUND: '#000000',
    GRID_LINES: '#333333',
    SNAKE_HEAD: '#00ff00',
    SNAKE_BODY: '#00cc00',
    FOOD: '#ff0000',
    OBSTACLE: '#666666',
    TEXT: '#ffffff'
};

// Game State
let gameState = {
    snake: [],
    direction: { x: 1, y: 0 },
    food: { x: 0, y: 0 },
    obstacles: [],
    score: 0,
    level: 1,
    highScore: 0,
    isGameOver: false,
    isPaused: false,
    lastMoveTime: 0,
    speed: CONFIG.BASE_SPEED
};

// Canvas and Context
let canvas, ctx;

// Sound Effects
let eatSound, gameOverSound;

// Initialize the game
function initGame() {
    canvas = document.getElementById('gameCanvas');
    ctx = canvas.getContext('2d');
    
    // Load high score from localStorage
    gameState.highScore = parseInt(localStorage.getItem('snakeHighScore') || '0');
    updateUI();
    
    // Initialize sound effects
    initSounds();
    
    // Initialize game objects
    resetGame();
    
    // Start game loop
    gameLoop();
}

// Initialize sound effects
function initSounds() {
    if (!CONFIG.ENABLE_SOUND) return;
    
    // Create audio context for sound generation
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    // Create eat sound (high pitch beep)
    eatSound = () => {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
        oscillator.type = 'square';
        
        gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.1);
    };
    
    // Create game over sound (low pitch beep)
    gameOverSound = () => {
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.setValueAtTime(200, audioContext.currentTime);
        oscillator.type = 'sawtooth';
        
        gainNode.gain.setValueAtTime(0.2, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.5);
    };
}

// Reset game to initial state
function resetGame() {
    const centerX = Math.floor(CONFIG.CANVAS_WIDTH / CONFIG.CELL_SIZE / 2);
    const centerY = Math.floor(CONFIG.CANVAS_HEIGHT / CONFIG.CELL_SIZE / 2);
    
    gameState.snake = [{ x: centerX, y: centerY }];
    gameState.direction = { x: 1, y: 0 };
    gameState.score = 0;
    gameState.level = 1;
    gameState.isGameOver = false;
    gameState.isPaused = false;
    gameState.speed = CONFIG.BASE_SPEED;
    gameState.obstacles = createLevelObstacles(1);
    gameState.food = generateFood();
    gameState.lastMoveTime = Date.now();
    
    updateUI();
    hideOverlays();
}

// Create obstacles for different levels
function createLevelObstacles(level) {
    const obstacles = [];
    const gridWidth = CONFIG.CANVAS_WIDTH / CONFIG.CELL_SIZE;
    const gridHeight = CONFIG.CANVAS_HEIGHT / CONFIG.CELL_SIZE;
    
    if (level === 1) {
        // Level 1: Corner obstacles
        obstacles.push(
            { x: 5, y: 5 },
            { x: gridWidth - 6, y: 5 },
            { x: 5, y: gridHeight - 6 },
            { x: gridWidth - 6, y: gridHeight - 6 }
        );
    } else if (level === 2) {
        // Level 2: Cross pattern
        const centerX = Math.floor(gridWidth / 2);
        const centerY = Math.floor(gridHeight / 2);
        for (let i = -2; i <= 2; i++) {
            obstacles.push(
                { x: centerX + i, y: centerY },
                { x: centerX, y: centerY + i }
            );
        }
    } else if (level >= 3) {
        // Level 3+: Random obstacles
        const numObstacles = Math.min(level * 3, 20);
        for (let i = 0; i < numObstacles; i++) {
            let x, y;
            do {
                x = Math.floor(Math.random() * (gridWidth - 4)) + 2;
                y = Math.floor(Math.random() * (gridHeight - 4)) + 2;
            } while (isPositionOccupied(x, y));
            obstacles.push({ x, y });
        }
    }
    
    return obstacles;
}

// Check if position is occupied by snake or obstacles
function isPositionOccupied(x, y) {
    return gameState.snake.some(segment => segment.x === x && segment.y === y) ||
           gameState.obstacles.some(obstacle => obstacle.x === x && obstacle.y === y);
}

// Generate food at random position
function generateFood() {
    const gridWidth = CONFIG.CANVAS_WIDTH / CONFIG.CELL_SIZE;
    const gridHeight = CONFIG.CANVAS_HEIGHT / CONFIG.CELL_SIZE;
    
    let x, y;
    do {
        x = Math.floor(Math.random() * gridWidth);
        y = Math.floor(Math.random() * gridHeight);
    } while (isPositionOccupied(x, y));
    
    return { x, y };
}

// Update game logic
function updateGame() {
    if (gameState.isGameOver || gameState.isPaused) return;
    
    const currentTime = Date.now();
    const moveInterval = 1000 / gameState.speed;
    
    if (currentTime - gameState.lastMoveTime >= moveInterval) {
        moveSnake();
        checkCollisions();
        checkLevelProgression();
        gameState.lastMoveTime = currentTime;
    }
    
    // Update UI on every frame for live updates
    updateUI();
}

// Move snake
function moveSnake() {
    const head = { ...gameState.snake[0] };
    head.x += gameState.direction.x;
    head.y += gameState.direction.y;
    
    gameState.snake.unshift(head);
    
    // Check if food was eaten
    if (head.x === gameState.food.x && head.y === gameState.food.y) {
        gameState.score++;
        gameState.food = generateFood();
        if (eatSound) eatSound();
    } else {
        gameState.snake.pop();
    }
}

// Check for collisions
function checkCollisions() {
    const head = gameState.snake[0];
    const gridWidth = CONFIG.CANVAS_WIDTH / CONFIG.CELL_SIZE;
    const gridHeight = CONFIG.CANVAS_HEIGHT / CONFIG.CELL_SIZE;
    
    // Wall collision
    if (head.x < 0 || head.x >= gridWidth || head.y < 0 || head.y >= gridHeight) {
        gameOver();
        return;
    }
    
    // Self collision
    for (let i = 1; i < gameState.snake.length; i++) {
        if (head.x === gameState.snake[i].x && head.y === gameState.snake[i].y) {
            gameOver();
            return;
        }
    }
    
    // Obstacle collision
    for (const obstacle of gameState.obstacles) {
        if (head.x === obstacle.x && head.y === obstacle.y) {
            gameOver();
            return;
        }
    }
}

// Check level progression
function checkLevelProgression() {
    const newLevel = Math.floor(gameState.score / CONFIG.LEVEL_ADVANCE_SCORE) + 1;
    if (newLevel > gameState.level) {
        gameState.level = newLevel;
        gameState.obstacles = createLevelObstacles(newLevel);
    }
    
    // Update speed based on score
    gameState.speed = CONFIG.BASE_SPEED + Math.floor(gameState.score / CONFIG.SPEED_INCREASE_INTERVAL);
}

// Handle game over
function gameOver() {
    gameState.isGameOver = true;
    
    // Update high score
    if (gameState.score > gameState.highScore) {
        gameState.highScore = gameState.score;
        localStorage.setItem('snakeHighScore', gameState.highScore.toString());
    }
    
    // Play game over sound
    if (gameOverSound) gameOverSound();
    
    // Show game over overlay
    document.getElementById('finalScore').textContent = `Score: ${gameState.score}`;
    document.getElementById('gameOverOverlay').style.display = 'block';
    
    updateUI();
}

// Handle keyboard input
function handleKeyPress(event) {
    if (gameState.isGameOver) {
        if (event.key === 'r' || event.key === 'R') {
            restartGame();
        } else if (event.key === 'q' || event.key === 'Q') {
            quitGame();
        }
        return;
    }
    
    // Pause toggle
    if (event.key === 'p' || event.key === 'P') {
        togglePause();
        return;
    }
    
    // Only handle movement if not paused
    if (gameState.isPaused) return;
    
    // Movement controls
    const newDirection = { ...gameState.direction };
    
    switch (event.key) {
        case 'ArrowUp':
        case 'w':
        case 'W':
            if (gameState.direction.y !== 1) {
                newDirection.x = 0;
                newDirection.y = -1;
            }
            break;
        case 'ArrowDown':
        case 's':
        case 'S':
            if (gameState.direction.y !== -1) {
                newDirection.x = 0;
                newDirection.y = 1;
            }
            break;
        case 'ArrowLeft':
        case 'a':
        case 'A':
            if (gameState.direction.x !== 1) {
                newDirection.x = -1;
                newDirection.y = 0;
            }
            break;
        case 'ArrowRight':
        case 'd':
        case 'D':
            if (gameState.direction.x !== -1) {
                newDirection.x = 1;
                newDirection.y = 0;
            }
            break;
    }
    
    gameState.direction = newDirection;
}

// Toggle pause state
function togglePause() {
    gameState.isPaused = !gameState.isPaused;
    if (gameState.isPaused) {
        document.getElementById('pauseOverlay').style.display = 'block';
    } else {
        document.getElementById('pauseOverlay').style.display = 'none';
    }
}

// Restart game
function restartGame() {
    resetGame();
}

// Quit game
function quitGame() {
    window.close();
}

// Hide all overlays
function hideOverlays() {
    document.getElementById('pauseOverlay').style.display = 'none';
    document.getElementById('gameOverOverlay').style.display = 'none';
}

// Update UI elements
function updateUI() {
    document.getElementById('score').textContent = gameState.score;
    document.getElementById('speed').textContent = gameState.speed;
    document.getElementById('level').textContent = gameState.level;
    document.getElementById('highScore').textContent = gameState.highScore;
}

// Render game
function render() {
    // Clear canvas
    ctx.fillStyle = COLORS.BACKGROUND;
    ctx.fillRect(0, 0, CONFIG.CANVAS_WIDTH, CONFIG.CANVAS_HEIGHT);
    
    // Draw grid
    ctx.strokeStyle = COLORS.GRID_LINES;
    ctx.lineWidth = 1;
    for (let x = 0; x <= CONFIG.CANVAS_WIDTH; x += CONFIG.CELL_SIZE) {
        ctx.beginPath();
        ctx.moveTo(x, 0);
        ctx.lineTo(x, CONFIG.CANVAS_HEIGHT);
        ctx.stroke();
    }
    for (let y = 0; y <= CONFIG.CANVAS_HEIGHT; y += CONFIG.CELL_SIZE) {
        ctx.beginPath();
        ctx.moveTo(0, y);
        ctx.lineTo(CONFIG.CANVAS_WIDTH, y);
        ctx.stroke();
    }
    
    // Draw obstacles
    ctx.fillStyle = COLORS.OBSTACLE;
    for (const obstacle of gameState.obstacles) {
        ctx.fillRect(
            obstacle.x * CONFIG.CELL_SIZE,
            obstacle.y * CONFIG.CELL_SIZE,
            CONFIG.CELL_SIZE,
            CONFIG.CELL_SIZE
        );
    }
    
    // Draw snake
    gameState.snake.forEach((segment, index) => {
        ctx.fillStyle = index === 0 ? COLORS.SNAKE_HEAD : COLORS.SNAKE_BODY;
        ctx.fillRect(
            segment.x * CONFIG.CELL_SIZE,
            segment.y * CONFIG.CELL_SIZE,
            CONFIG.CELL_SIZE,
            CONFIG.CELL_SIZE
        );
    });
    
    // Draw food
    ctx.fillStyle = COLORS.FOOD;
    ctx.fillRect(
        gameState.food.x * CONFIG.CELL_SIZE,
        gameState.food.y * CONFIG.CELL_SIZE,
        CONFIG.CELL_SIZE,
        CONFIG.CELL_SIZE
    );
}

// Main game loop
function gameLoop() {
    updateGame();
    render();
    requestAnimationFrame(gameLoop);
}

// Event listeners
document.addEventListener('keydown', handleKeyPress);

// Initialize game when page loads
window.addEventListener('load', initGame);
