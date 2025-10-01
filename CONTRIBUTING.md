# Contributing to ByteSnake

Thank you for your interest in contributing to ByteSnake! 🐍 We welcome contributions from the community and appreciate your help in making this project better.

## How to Contribute

### Reporting Issues

Before creating an issue, please check if it has already been reported by searching the [Issues](https://github.com/yourusername/Snake-Game/issues) page.

When creating an issue, please include:
- **Clear title** describing the problem
- **Detailed description** of the issue
- **Steps to reproduce** the problem
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **System information** (OS, Python version, browser version for web issues)

### Suggesting Enhancements

We love new ideas! When suggesting enhancements:
- Use the "Enhancement" issue template
- Provide a clear description of the proposed feature
- Explain why this feature would be beneficial
- Consider implementation complexity and maintainability

### Code Contributions

#### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/Snake-Game.git
   cd Snake-Game
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Setup

**For Python Development:**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r snake_game/requirements.txt

# Run the game to test
python snake_game/main.py
```

**For Web Development:**
```bash
# Serve the web version locally
cd snake_game
python -m http.server 8000
# Open http://localhost:8000 in your browser
```

#### Making Changes

1. **Follow the existing code style**:
   - Use meaningful variable and function names
   - Add comments for complex logic
   - Follow PEP 8 for Python code
   - Use consistent indentation (4 spaces for Python, 2 spaces for JavaScript)

2. **Test your changes**:
   - Test both Python and Web versions if applicable
   - Ensure all existing functionality still works
   - Test edge cases and error conditions

3. **Update documentation**:
   - Update README.md if you add new features
   - Add docstrings for new functions
   - Update comments for modified code

#### Submitting Changes

1. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Fill out the PR template
   - Link any related issues

## Pull Request Guidelines

### Before Submitting

- [ ] Code follows the project's style guidelines
- [ ] Self-review of your code has been performed
- [ ] Code has been commented, particularly in hard-to-understand areas
- [ ] Corresponding changes to documentation have been made
- [ ] Changes generate no new warnings or errors
- [ ] New and existing unit tests pass locally
- [ ] Any dependent changes have been merged and published

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Code refactoring

## Testing
Describe the tests you ran to verify your changes.

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Use meaningful variable names

**JavaScript:**
- Use ES6+ features
- Follow consistent naming conventions (camelCase for variables, PascalCase for classes)
- Add JSDoc comments for functions
- Use const/let instead of var

### File Organization

- Keep related functionality together
- Separate concerns into different functions/classes
- Use descriptive file and function names
- Maintain consistent project structure

### Testing

Before submitting, please test:
- [ ] Game starts and runs without errors
- [ ] All controls work as expected
- [ ] Game mechanics function correctly
- [ ] No performance regressions
- [ ] Cross-platform compatibility (if applicable)

## Areas for Contribution

### High Priority
- **Bug fixes** - Any issues reported in the Issues section
- **Performance improvements** - Optimize game loop, rendering, or memory usage
- **Mobile support** - Touch controls for web version
- **Accessibility** - Screen reader support, keyboard navigation

### Medium Priority
- **New features** - Power-ups, different game modes, themes
- **Code refactoring** - Improve code organization and maintainability
- **Documentation** - Improve code comments and user documentation
- **Testing** - Add unit tests or automated testing

### Low Priority
- **UI/UX improvements** - Better visual design, animations
- **Sound effects** - More audio feedback
- **Localization** - Multi-language support
- **Advanced features** - Multiplayer, leaderboards, achievements

## Getting Help

If you need help or have questions:
- Check the [Issues](https://github.com/yourusername/Snake-Game/issues) for similar questions
- Create a new issue with the "Question" label
- Review the code comments and documentation

## Recognition

Contributors will be recognized in:
- The project's README.md
- Release notes for significant contributions
- GitHub's contributors list

Thank you for contributing to ByteSnake! Your efforts help make this project better for everyone. 🎮✨
