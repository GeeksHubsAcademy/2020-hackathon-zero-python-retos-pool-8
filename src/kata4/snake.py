import pygame, sys, time, random
from pygame.locals import *


screen_width = 500
screen_height = 500

pygame.init()

play_surface = pygame.display.set_mode((screen_width,screen_height))
fps = pygame.time.Clock()

class Snake():
    position = [100,50]
    body = [[100,50], [90,50],[80,50]]
    body_length = 3 # se va modificando
    direction = "RIGHT"
    change = direction
    x1_change = 0
    y1_change = 0
    snake_block=10
    speed = 15
    

    # Manejo del pressed [KEYDOWN] de las teclas [K_RIGHT - K_LEFT - K_UP -K_DOWN ]
    def controller(self, event, pygame):
        
    # Controla el cambio de  las direcciones
    # Orientaciones
    # Vertical      -> Movimientos [RIGHT - LEFT]
    # Horizontal    -> Movimientos [UP - DOWN]
    # Incremento del movimiento
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            self.x1_change = -self.snake_block
            self.y1_change = 0
        elif event.key == pygame.K_RIGHT:
            self.x1_change = self.snake_block
            self.y1_change = 0
        elif event.key == pygame.K_UP:
            self.y1_change = -self.snake_block
            self.x1_change = 0
        elif event.key == pygame.K_DOWN:
            self.y1_change = self.snake_block
            self.x1_change = 0
    


    def changeDirection(self):
        
        #
        #      

        self.position[0] +=  self.x1_change
        self.position[1] += self.y1_change
       

        self.body.insert(0, list(self.position))

        #Con esto dejamos el snake con el tamano original sino crece a medida que se mueve
        self.body.pop()
        

class Game():
    run = True
    food_pos = [0,0]
    score = 0

    def __init__(self):
        self.food_spawn()

    # función de salida
    def exit(self, event, pygame):
        #
        #
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

    # Posición aleatorio entre el ranto [0,49] * 10  
    def food_spawn(self):
        self.food_pos[0] = (random.randrange(0,49))*10
        self.food_pos[1] = (random.randrange(0,49))*10

    # Si colisionas con una fruta, sumas 1
    # Sino decrementas en 1 el body del snake
    def eat(self, snake):

        if snake.position[0] == self.food_pos[0] and snake.position[1] == self.food_pos[1]:
            self.food_pos[0] = (random.randrange(0,49))*10
            self.food_pos[1] = (random.randrange(0,49))*10
            snake.body.insert(0, list(snake.position))
            snake.body_length += 1


       
    # Mensajes de salida cuando el snake muere
    # Posición snake[0] >= 500 ó snake[0] <= 0                  -> Muere
    # Posición snake[1] >= 500 ó snake[1] <= 0                  -> Muere
    # Posición del snake choca con sigo mismo menos la cabeza   -> Muere
        return # borrar
    def dead(self, snake):
        #
        #Choque con el propio cuerpo
        #
        

        #Si 
        
        if snake.body_length > 3:
            print("snake.body = " + str(snake.body))
            for x in snake.body[2:-1]:
                print("snake.position = " + str(snake.position))
                print("x = " + str(x))
                if x == snake.position:
                    self.run = False
                    #pass
        
        #
        #
        #Choque con bordes
        if snake.position[0] >= screen_width or snake.position[0] < 0 or snake.position[1] >= screen_height or snake.position[1] < 0:
             self.run = False
        #
        #

        #
        
            
# Entry Point
def main():
    # Descomentar para lanzar el juego en local
    # Comentar para validar con el oráculo
    #pygame.init()
    #play_surface = pygame.display.set_mode((500, 500))
    #fps = pygame.time.Clock()

    snake = Snake()
    game = Game()

    # Bucle principal
    while game.run:
        for event in pygame.event.get():
            game.exit(event, pygame)
            snake.controller(event, pygame)
            
        
        snake.changeDirection()

        game.eat(snake)

        # Dibujar Snake
        play_surface.fill((0,0,0))
        #print ((snake.body))
        for pos in snake.body:
            pygame.draw.rect(play_surface, (200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        
        
        pygame.draw.rect(play_surface, (255,160,60), pygame.Rect(game.food_pos[0], game.food_pos[1], 10, 10))
        
        pygame.display.update()
        game.dead(snake)

        pygame.display.flip()
        fps.tick(10)

       
        
# Comienza la aventura!!!!
# Descomentar para lanzar el juego en local
# Comentar para validar con el oráculo
# if __name__ == '__main__':
#     main() 
#     pygame.quit()

