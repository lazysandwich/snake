

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228) 
APPLE_COLOR = (255, 0, 0) 
SNAKE_COLOR = (0, 255, 0) 

SPEED = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("Змейка") 

clock = pygame.time.Clock()


class GameObject :

    def init(self)->None :
    self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = None

        def draw(self)->None:
pass


class Apple(GameObject) :

    def init(self)->None :
    super().init()
    self.position = self.randomize_position()
    self.body_color = APPLE_COLOR

    def randomize_position(self)->tuple :
    x_cord = choice(range(0, SCREEN_WIDTH, GRID_SIZE))
    y_cord = choice(range(0, SCREEN_HEIGHT, GRID_SIZE))
    self.position = (x_cord, y_cord)
    return self.position

    def draw(self)->None:
rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
pygame.draw.rect(screen, self.body_color, rect)
pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject) :

    def init(self)->None :
    super().init()
    self.length = 1
    self.positions = [self.position]
    self.direction = RIGHT
    self.next_direction = None
    self.body_color = SNAKE_COLOR
    self.last = None

    def update_direction(self)->None:
if self.next_direction :
    self.direction = self.next_direction
    self.next_direction = None

    def move(self)->None :
    head_position = self.get_head_position()
    new_head_position = (
        (head_position[0] + self.direction[0] * GRID_SIZE) % SCREEN_WIDTH,
        (head_position[1] + self.direction[1] * GRID_SIZE) % SCREEN_HEIGHT,
        )

    if new_head_position in self.positions[2:]:
self.reset()
return

self.positions.insert(0, new_head_position)
if len(self.positions) > self.length:
self.last = self.positions.pop()

def draw(self)->None :
    for position in self.positions[:-1] :
        rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        if self.last:
last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

def get_head_position(self)->tuple :
    return self.positions[0]

    def reset(self)->None :
    screen.fill(BOARD_BACKGROUND_COLOR)
    self.length = 1
    self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.positions = [self.position]
        self.direction = choice((RIGHT, LEFT, UP, DOWN))
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        def handle_keys(game_object: Snake)->None:
for event in pygame.event.get() :
    if event.type == pygame.QUIT :
        pygame.quit()
        raise SystemExit
        elif event.type == pygame.KEYDOWN :
        if event.key == pygame.K_UP and game_object.direction != DOWN:
            game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
            game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT 
                and game_object.direction != RIGHT:
            game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT 
                and game_object.direction != LEFT:
            game_object.next_direction = RIGHT


            def main()->None :
            """Основная функция игры."""
            pygame.init()
            snake = Snake()
            apple = Apple()

            while True:
clock.tick(SPEED)

handle_keys(snake)
snake.update_direction()
snake.move()
if snake.get_head_position() == apple.position:
snake.length += 1
apple.randomize_position()
snake.draw()
apple.draw()
pygame.display.update()


if name == "main":
main()
