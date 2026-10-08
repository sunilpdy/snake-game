import pygame
import random
import sys


# -----------------------------
# Initialize Pygame
# -----------------------------
pygame.init()


# -----------------------------
# Game configuration
# -----------------------------
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

FPS = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


# -----------------------------
# Colors
# -----------------------------
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 130, 0)
RED = (220, 0, 0)


# -----------------------------
# Font
# -----------------------------
font = pygame.font.Font(None, 36)


# -----------------------------
# Create random food position
# -----------------------------
def create_food(snake):
    while True:
        x = random.randrange(
            0,
            WIDTH,
            CELL_SIZE
        )

        y = random.randrange(
            0,
            HEIGHT,
            CELL_SIZE
        )

        food = (x, y)

        if food not in snake:
            return food


# -----------------------------
# Draw snake
# -----------------------------
def draw_snake(snake):

    for index, segment in enumerate(snake):

        x, y = segment

        if index == 0:
            color = DARK_GREEN
        else:
            color = GREEN

        pygame.draw.rect(
            screen,
            color,
            (
                x,
                y,
                CELL_SIZE,
                CELL_SIZE
            )
        )


# -----------------------------
# Draw food
# -----------------------------
def draw_food(food):

    x, y = food

    pygame.draw.rect(
        screen,
        RED,
        (
            x,
            y,
            CELL_SIZE,
            CELL_SIZE
        )
    )


# -----------------------------
# Draw score
# -----------------------------
def draw_score(score):

    text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        text,
        (10, 10)
    )


# -----------------------------
# Game Over screen
# -----------------------------
def game_over(score):

    screen.fill(BLACK)

    game_over_text = font.render(
        "GAME OVER",
        True,
        RED
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    restart_text = font.render(
        "Press R to restart or Q to quit",
        True,
        WHITE
    )

    screen.blit(
        game_over_text,
        (
            WIDTH // 2 - game_over_text.get_width() // 2,
            HEIGHT // 2 - 60
        )
    )

    screen.blit(
        score_text,
        (
            WIDTH // 2 - score_text.get_width() // 2,
            HEIGHT // 2 - 20
        )
    )

    screen.blit(
        restart_text,
        (
            WIDTH // 2 - restart_text.get_width() // 2,
            HEIGHT // 2 + 30
        )
    )

    pygame.display.update()


# -----------------------------
# Main game
# -----------------------------
def main():

    snake = [
        (300, 200),
        (280, 200),
        (260, 200)
    ]

    direction = (CELL_SIZE, 0)

    food = create_food(snake)

    score = 0

    game_running = True
    game_over_state = False

    while game_running:

        # -------------------------
        # Handle events
        # -------------------------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.KEYDOWN:

                if not game_over_state:

                    if (
                        event.key == pygame.K_UP
                        and direction != (0, CELL_SIZE)
                    ):
                        direction = (0, -CELL_SIZE)

                    elif (
                        event.key == pygame.K_DOWN
                        and direction != (0, -CELL_SIZE)
                    ):
                        direction = (0, CELL_SIZE)

                    elif (
                        event.key == pygame.K_LEFT
                        and direction != (CELL_SIZE, 0)
                    ):
                        direction = (-CELL_SIZE, 0)

                    elif (
                        event.key == pygame.K_RIGHT
                        and direction != (-CELL_SIZE, 0)
                    ):
                        direction = (CELL_SIZE, 0)

                else:

                    if event.key == pygame.K_r:

                        snake = [
                            (300, 200),
                            (280, 200),
                            (260, 200)
                        ]

                        direction = (
                            CELL_SIZE,
                            0
                        )

                        food = create_food(snake)

                        score = 0

                        game_over_state = False

                    elif event.key == pygame.K_q:

                        game_running = False

        # -------------------------
        # Update game
        # -------------------------
        if not game_over_state:

            head_x, head_y = snake[0]

            new_head = (
                head_x + direction[0],
                head_y + direction[1]
            )

            # ---------------------
            # Wall collision
            # ---------------------
            if (
                new_head[0] < 0
                or new_head[0] >= WIDTH
                or new_head[1] < 0
                or new_head[1] >= HEIGHT
            ):
                game_over_state = True

            # ---------------------
            # Self collision
            # ---------------------
            elif new_head in snake:
                game_over_state = True

            else:

                snake.insert(
                    0,
                    new_head
                )

                # -----------------
                # Food collision
                # -----------------
                if new_head == food:

                    score += 1

                    food = create_food(
                        snake
                    )

                else:

                    # Remove tail
                    snake.pop()

        # -------------------------
        # Draw everything
        # -------------------------
        screen.fill(BLACK)

        draw_snake(snake)

        draw_food(food)

        draw_score(score)

        if game_over_state:
            game_over(score)

        else:
            pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


# -----------------------------
# Start game
# -----------------------------
if __name__ == "__main__":
    main()
