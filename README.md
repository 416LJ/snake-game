# Snake Game

A classic Snake game implementation in Python using the Turtle graphics library.

## How to Play

Use the arrow keys to control the snake:

- **Up Arrow**: Move Up
- **Down Arrow**: Move Down
- **Left Arrow**: Move Left
- **Right Arrow**: Move Right

The goal is to eat the red food pellets to grow the snake and increase your score. Avoid hitting the walls or your own tail. The game keeps track of your high score between sessions.

## Setup

This game requires Python 3.x and the Turtle graphics library (which is included in the standard Python library).

1.  Make sure you have Python installed.
2.  Clone or download this repository.
3.  Navigate to the project directory in your terminal.
4.  Run the game:

```bash
python main.py
```

## Project Structure

- `main.py`: The main entry point of the game. Handles screen setup, game loop, and event listening.
- `snake.py`: Contains the `Snake` class, responsible for snake movement, creation, and growth.
- `food.py`: Contains the `Food` class, handles random placement of food on the screen.
- `scoreboard.py`: Manages the current score and high score. Reads/writes the high score to `high_score.txt`.
- `high_score.txt`: A text file used to store the highest score achieved.

## Features

- **Classic Gameplay**: Familiar snake mechanics.
- **Score Tracking**: Displays current score and high score.
- **Persistence**: High score is saved to a file so it persists after closing the game.
- **Dynamic Difficulty**: The snake gets longer and the game continues until a collision occurs.
