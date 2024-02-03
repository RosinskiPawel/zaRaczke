# import pygame
# from sys import exit
# import random


    
 

# pygame.init()
# clock = pygame.time.Clock()
# BOARD_SIZE = 800
# ELEMENT_SIZE = 30
# screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
# screen.fill('Black')


# class Snake():
#     def __init__(self):
#         self.color = "blue"
#         self.x = ELEMENT_SIZE
#         self.y = ELEMENT_SIZE
#         self.dirx=1
#         self.diry=0
#         self.direction = "right"
#         self.head = pygame.Rect(self.x, self.y, ELEMENT_SIZE, ELEMENT_SIZE)
#         self.body = [pygame.Rect(self.x - ELEMENT_SIZE, self.y, ELEMENT_SIZE, ELEMENT_SIZE)]
        
#     def update(self):
#         self.body.append(self.head)
#         for i in range(len(self.body)-1):
#             self.body[i].x = self.body[i+1].x
#             self.body[i].y = self.body[i+1].y
#         self.head.x += self.dirx*ELEMENT_SIZE
#         self.head.y += self.diry*ELEMENT_SIZE
#         self.body.remove(self.head)

# class Food():
#     def __init__(self):
#         self.x = random.randrange(0, BOARD_SIZE - ELEMENT_SIZE)

#         self.y = random.randrange(0, BOARD_SIZE - ELEMENT_SIZE)
#         self.rect = pygame.Rect(self.x, self.y, ELEMENT_SIZE, ELEMENT_SIZE)
#         # self.radius = ELEMENT_SIZE/2
#         # self.color = "red"

#     def update(self):
#         pygame.draw.rect(screen, "red", self.rect)  
#         # pygame.draw.circle(screen, self.color, (self.x + self.radius, self.y+ self.radius), self.radius)      
        
# snake = Snake()
# food = Food()
# # snake_direction = "right"

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
        
    
            
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT and snake.direction!="left":
#                 snake.direction = "right"
#                 snake.dirx = 1
#                 snake.diry = 0
#                 snake.color = tuple(random.sample(range(256), 3))
#             if event.key == pygame.K_LEFT and snake.direction!="right":
#                 snake.direction = "left"
#                 snake.dirx = -1
#                 snake.diry = 0
#                 snake.color = tuple(random.sample(range(256), 3))
#             if event.key == pygame.K_UP and snake.direction!= "down":
#                 snake.direction = "up"
#                 snake.dirx = 0
#                 snake.diry = -1
#                 snake.color = tuple(random.sample(range(256), 3))
#             if event.key == pygame.K_DOWN and snake.direction!= "up":
#                 snake.direction = "down"
#                 snake.dirx = 0
#                 snake.diry = 1
#                 snake.color = tuple(random.sample(range(256), 3))
                
              
        
#     snake.update()
#     screen.fill("Black")
#     food.update()  
#     pygame.draw.rect(screen, snake.color, snake.head)
#     for element in snake.body:
#         pygame.draw.rect(screen, snake.color, element)
        
#     if snake.head.x == food.x and snake.head.y==food.y:
#         print("HIT")
#         snake.body.append(pygame.Rect(snake.head.x, snake.head.y, ELEMENT_SIZE, ELEMENT_SIZE))
#         food = Food()
            
    
    
    
#     # snake.update()
    
    
#     pygame.display.update()
#     clock.tick(5)



import pygame
from sys import exit

import random

pygame.init()

BOARD_SIZE = 600

screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
screen.fill("Black")
clock = pygame.time.Clock()
text_font = pygame.font.SysFont("Arial", 40)
snake_color = "blue"
ELEMENT_SIZE = 20

position_snake = [400, 400]

# snake_body = []

snake_body = [pygame.Rect(400, 400, ELEMENT_SIZE, ELEMENT_SIZE),
              ]

# snake_body = [
#     [400, 400], [380,400], [360, 400], [340,400]
    
# ]  # Lista przechowująca segmenty ciała węża
direction = "right"
position_in_box = BOARD_SIZE - ELEMENT_SIZE

class Food():
    def __init__(self):
        self.x = random.randrange(0, BOARD_SIZE - ELEMENT_SIZE)

        self.y = random.randrange(0, BOARD_SIZE - ELEMENT_SIZE)
        self.rect = pygame.Rect(self.x, self.y, ELEMENT_SIZE, ELEMENT_SIZE)
        
        

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)
         
        

food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # zmiana kierunku
        if event.type == pygame.KEYDOWN:
            # warunek 'direction !=' zabezpiecza weza przed odwrócneiem się i zjedzeniem ogona
            if event.key == pygame.K_DOWN and direction != "up":
                
                snake_color = tuple(random.sample(range(256), 3))
                direction = "down"
                
            elif event.key == pygame.K_UP and direction != "down":
                
                snake_color = tuple(random.sample(range(256), 3))
                direction = "up"
                
            elif event.key == pygame.K_RIGHT and direction != "left":
                
                snake_color = tuple(random.sample(range(256), 3))
                direction = "right"
                
            elif event.key == pygame.K_LEFT and direction != "right":
                
                snake_color = tuple(random.sample(range(256), 3))
                direction = "left"
    #animacja ruchu             
    if direction == "right":
        position_snake[0] += 10
    if direction == "up":
        position_snake[1] -= 10
    if direction == "down":
        position_snake[1] += 10
    if direction == "left":
        position_snake[0] -= 10
    
    
    
           
    # Dodawanie nowego segmentu ciała na przód węża
    # new_head = [position_snake[0], position_snake[1]]
    # snake_body.append(new_head)
    # new_head_rect = pygame.Rect(new_head[0], new_head[1], ELEMENT_SIZE, ELEMENT_SIZE)
    new_head = pygame.Rect(position_snake[0], position_snake[1], ELEMENT_SIZE, ELEMENT_SIZE)
    snake_body.append(new_head)
    
    # if snake_body[0] in snake_body[1:]:
    #     print("Ugryzienie ogona!")
    
    for i in range(len(snake_body) - 1):
        snake_body[i][0] = snake_body[i + 1][0]
        snake_body[i][1] = snake_body[i + 1][1]
    snake_body.pop()
    
    
    screen.fill("Black")
    
 
    # Rysowanie wszystkich segmentów ciała węża
    for segment in snake_body:
        pygame.draw.rect(
            screen,
            snake_color, segment
        )
    
        for snakesegment in snake_body[:-2]:
            if position_snake[0]  == snakesegment[0] and position_snake[1] == snakesegment[1]:
                print("AUUUUUU")
    
        
    food.update()

    if new_head.colliderect(food.rect):
        snake_body.append(pygame.Rect(new_head[0], new_head[1], ELEMENT_SIZE, ELEMENT_SIZE))
            # print(snake_body[0])
        print(snake_body.index(new_head))
        print(f"dłgość {len(snake_body)}")   
        # for i in range(len(snake_body)-1):
        #     print(i, snake_body[i])   
        print(f"pierwszy el {snake_body[0]}")
        # print(food.rect)
        print(f"nowa głowa {new_head}")
        print(f"cały waz {snake_body}")
        print(f"position_snake {position_snake}")
       
        food = Food()
    
    #wyjście poza ramkę
    if new_head[0] not in range(0,BOARD_SIZE) or new_head[1] not in range(0,BOARD_SIZE):
        print("OUT!!! ") 
    
            
    pygame.display.update()
    clock.tick(10)
