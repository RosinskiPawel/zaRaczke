
import pygame
from sys import exit
import time
import random

pygame.init()

BOARD_SIZE = 600
ELEMENT_SIZE = 40
GROUND_COLOR = "Black"
END_TEXT_COLOR = "White"
NEON_COLORS = [
    (255, 0, 0),
    (255, 172, 0),
    (11, 255, 0),
    (77, 238, 234),
    (116, 238, 21),
    (255, 231, 0),
    (240, 0, 255),
    (0, 30, 255),
]
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
screen.fill(GROUND_COLOR)
clock = pygame.time.Clock()
text_font = pygame.font.SysFont("Bradley Hand ITC", 100)
text_color = "White"
pygame.display.set_caption("SNAKE")
 


class Food:
    def __init__(self):
        # randomowa pozycja w zakresie 0 do krawedzi - rozmiar elementu i dodatkowo krok wielkości elementu, aby food miescił się w kratce

        self.x = random.randrange(0, BOARD_SIZE - ELEMENT_SIZE, ELEMENT_SIZE)
        self.y = random.randrange(0, BOARD_SIZE - ELEMENT_SIZE, ELEMENT_SIZE)
        self.rect = pygame.Rect(self.x, self.y, ELEMENT_SIZE, ELEMENT_SIZE)
        self.color = random.choice(NEON_COLORS)

    def random_position(self):
        pygame.draw.rect(screen, self.color, self.rect, 5)


class Snake:
    def __init__(self):
        self.color = "White"
        self.direction = "right"
        self.head_position = [280, 280]
        self.body = [
            pygame.Rect(
                self.head_position[0], self.head_position[1], ELEMENT_SIZE, ELEMENT_SIZE
            )
        ]

    # each snake's segment moves one cube forwards
    def move(self):
        self.new_head = pygame.Rect(
            self.head_position[0], self.head_position[1], ELEMENT_SIZE, ELEMENT_SIZE
        )
        self.body.append(self.new_head)
        for i in range(len(self.body) - 1):
            self.body[i][0] = self.body[i + 1][0]
            self.body[i][1] = self.body[i + 1][1]
        self.body.pop()

    # draw all snake's segments
    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, segment, 5)

    def gameOver(self):
        text2 = text_font.render("GAME OVER", True, END_TEXT_COLOR)
        screen.blit(text2, (BOARD_SIZE // 2 - text2.get_width() // 2, 200))
        text_points = text_font.render(f"Points: {counter}", True, END_TEXT_COLOR)
        screen.blit(text_points, (BOARD_SIZE // 2 - text_points.get_width() // 2, 250))
        pygame.display.update()
        time.sleep(2)
        exit()
    
                       
    # collision if snake's head in snake's body list
    def collision_body(self):
        for snakesegment in self.body[:-2]:
            if (
                self.head_position[0] == snakesegment[0]
                and self.head_position[1] == snakesegment[1]
            ):
                self.gameOver()
                               

    # head out of game's board
    def out_of_window(self):
        if snake.head_position[0] not in range(0, BOARD_SIZE) or snake.head_position[
            1
        ] not in range(0, BOARD_SIZE):
            self.gameOver()
           
            
while True:
    food = Food()
    snake = Snake()
    counter = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # zmiana kierunku
            if event.type == pygame.KEYDOWN:
                # warunek 'direction !=' zabezpiecza weza przed odwrócneiem się i zjedzeniem ogona
                if event.key == pygame.K_DOWN and snake.direction != "up":
                    snake.direction = "down"
                elif event.key == pygame.K_UP and snake.direction != "down":
                    snake.direction = "up"
                elif event.key == pygame.K_RIGHT and snake.direction != "left":
                    snake.direction = "right"
                elif event.key == pygame.K_LEFT and snake.direction != "right":
                    snake.direction = "left"
                    
        # animacja ruchu
        if snake.direction == "right":
            snake.head_position[0] += ELEMENT_SIZE
        if snake.direction == "up":
            snake.head_position[1] -= ELEMENT_SIZE
        if snake.direction == "down":
            snake.head_position[1] += ELEMENT_SIZE
        if snake.direction == "left":
            snake.head_position[0] -= ELEMENT_SIZE

        screen.fill(GROUND_COLOR)
        snake.move()
        snake.draw()
        snake.collision_body()
        snake.out_of_window()
        food.random_position()
        text = text_font.render(f"{counter}", True, text_color)
        screen.blit(text, (BOARD_SIZE // 2 - text.get_width() // 2, 0))

        # eating
        if snake.new_head.colliderect(food.rect):
            snake.color = food.color
            snake.body.append(
                pygame.Rect(
                    snake.new_head[0], snake.new_head[1], ELEMENT_SIZE, ELEMENT_SIZE
                )
            )
            counter += 1

            # zapobieganie pojawieniu sie jedzenia na wezu
            while True:
                food = Food()
                if food.rect not in snake.body:
                    break

        pygame.display.update()
        clock.tick(5)
