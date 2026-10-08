# 🐍 Snake Game

A simple classic **Snake Game built with Python and Pygame**. The player controls the snake using the arrow keys, eats food to increase the score, and must avoid hitting the walls or itself.

## 📌 Features

* 🎮 Keyboard controls
* 🍎 Randomly generated food
* 🐍 Snake grows after eating food
* 💥 Collision detection
* 🏆 Score tracking
* 🔄 Restart after game over
* 🚪 Quit option
* ⚡ Simple and lightweight
* 🖥️ Runs on Windows, macOS, and Linux

## 🛠️ Technologies Used

* **Python 3**
* **Pygame**

### Python Built-in Modules

The project also uses:

* `random` — generates random food positions
* `sys` — exits the application

### External Package

Only one external package is required:

```text
pygame
```

## 📁 Project Structure

```text
snake-game/
│
├── snake_game.py
├── requirements.txt
└── README.md
```

## 📦 Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd snake-game
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Game

Run:

```bash
python snake_game.py
```

The game window will open and the snake will start moving.

## 🎮 Controls

| Key            | Action                  |
| -------------- | ----------------------- |
| ⬆️ Up Arrow    | Move Up                 |
| ⬇️ Down Arrow  | Move Down               |
| ⬅️ Left Arrow  | Move Left               |
| ➡️ Right Arrow | Move Right              |
| `R`            | Restart after Game Over |
| `Q`            | Quit after Game Over    |

## 🧠 How the Game Works

### 1. Snake

The snake is represented using a Python list containing its body coordinates.

Example:

```python
snake = [
    (300, 200),
    (280, 200),
    (260, 200)
]
```

The first coordinate represents the snake's head.

### 2. Movement

Every game frame, a new head position is calculated based on the current direction.

```python
new_head = (
    head_x + direction[0],
    head_y + direction[1]
)
```

The new head is inserted at the beginning of the snake.

### 3. Food

Food is generated randomly using Python's `random` module.

```python
x = random.randrange(0, WIDTH, CELL_SIZE)
y = random.randrange(0, HEIGHT, CELL_SIZE)
```

The food is never generated inside the snake.

### 4. Eating Food

When the snake's head reaches the food:

```python
if new_head == food:
    score += 1
    food = create_food(snake)
```

The snake grows because its tail is not removed.

### 5. Normal Movement

If the snake does not eat food, the last segment is removed:

```python
snake.insert(0, new_head)
snake.pop()
```

This creates the movement effect.

### 6. Collision Detection

The game ends when the snake:

* Hits the left wall
* Hits the right wall
* Hits the top wall
* Hits the bottom wall
* Hits its own body

Example:

```python
if new_head[0] < 0 or new_head[0] >= WIDTH:
    game_over_state = True
```

## 🏆 Scoring System

The player receives **1 point for every food item eaten**.

Example:

```text
Food eaten: 1  → Score: 1
Food eaten: 2  → Score: 2
Food eaten: 10 → Score: 10
```

## ⚙️ Game Configuration

The game can be customized from the top of `snake_game.py`.

```python
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20
FPS = 10
```

### Configuration

| Variable    | Description               |
| ----------- | ------------------------- |
| `WIDTH`     | Game window width         |
| `HEIGHT`    | Game window height        |
| `CELL_SIZE` | Size of snake/food blocks |
| `FPS`       | Snake movement speed      |

Increasing `FPS` makes the snake move faster.

## 📋 Requirements

The `requirements.txt` file contains:

```text
pygame>=2.5.0
```

Install it using:

```bash
pip install -r requirements.txt
```

## 🔄 Game Flow

```text
Start Game
    ↓
Initialize Snake
    ↓
Generate Food
    ↓
Read Keyboard Input
    ↓
Move Snake
    ↓
Check Collision
    ↓
     ┌───────────────┐
     │ Collision?    │
     └───────┬───────┘
             │
        Yes  │  No
         ↓   │   ↓
    Game Over│ Check Food
             │
             ↓
       Food Eaten?
         /       \
       Yes        No
        ↓          ↓
 Increase Score   Remove Tail
        ↓          ↓
        └──────┬───┘
               ↓
          Continue Game
```

## 💡 Concepts Demonstrated

This project is useful for learning basic game development concepts in Python:

* Python functions
* Lists and tuples
* Loops
* Conditional statements
* Random number generation
* Event handling
* Keyboard input
* Coordinate systems
* Collision detection
* Game loops
* Game states
* Score management
* Basic object movement

## 🚀 Future Improvements

The current version is intentionally simple. Possible improvements include:

* [ ] Start menu
* [ ] Pause/resume functionality
* [ ] High-score system
* [ ] Increasing difficulty
* [ ] Multiple levels
* [ ] Sound effects
* [ ] Background music
* [ ] Different food types
* [ ] Special power-ups
* [ ] Obstacles
* [ ] Multiple themes
* [ ] Wrap-around walls
* [ ] Persistent high scores
* [ ] Improved graphics and animations

## 📸 Game Screenshot

Add a screenshot of the running game here:

```markdown
![Snake Game Screenshot](screenshots/game.png)
```

Recommended project structure:

```text
snake-game/
├── snake_game.py
├── requirements.txt
├── README.md
└── screenshots/
    └── game.png
```

## 👩‍💻 Author

**Sunita Bashyal**

## 📄 License

This project is created for **learning and educational purposes**.
