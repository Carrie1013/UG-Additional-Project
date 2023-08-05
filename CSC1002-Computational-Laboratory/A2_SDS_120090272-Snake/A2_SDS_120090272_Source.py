from turtle import *
from functools import partial
import random
import time

intro = '''
Welcome to 120090272's version of 'Snaker Game'!

You are supposed to use the 4 arrows to control the snaker.
You can press the 'space' key to pause the game.
As soon as you consumed all the foods, you will win the game.
Notice that you will fail the game if chased up by the monster!

Now click the screen to start the game! Good Luck!
'''
L_snake = []
Time = 0
cnt_contact = 0
g_keypressed = '' 
pos_head = (0, 0) # Tuple to denote the position of the head of snake
pos_monster = (0, 0) # Tuple to denote the position of monster
pos_food = {} # Dictionary to store the number of 1 to 9 and their positions
g_length = 5 # The total length of the snake, with a initial length of 5
# Game status
gameStart = False
gamePause = False
gameOver = False
# Key press
direction = {'Up': 90, 'Down': 270, 'Left': 180, 'Right': 0} # Dictionary to store the key and their values of angle
# Set the whole screen and its size
s = Screen()
s.setup(660, 740)

# Initialize
def generate_turtle(): # use the function to generate turtle
    turt = Turtle()
    turt.penup()
    turt.speed(0)
    turt.hideturtle()
    return turt 


def init_state(): # generate the initial state before starting the game
    global tt, monster, food, g_time, g_status, g_contact, g_intro, upper_a, motion_a
    tt = generate_turtle() # turtle of snake head
    monster = generate_turtle() # turtle of monster
    food = generate_turtle() # turtle of the food item
    g_time = generate_turtle() # turtle as a time keeper
    g_status = generate_turtle() # turtle as a status keeper
    g_contact = generate_turtle() # turtle as a contact keeper
    g_intro = generate_turtle() # turtle to write introduction
    upper_a = generate_turtle() # turtle as the upper status area 
    motion_a = generate_turtle() # turtle as the motion area
    tt.shape('square')
    tt.color('blue', 'pink') # define the color of turtle
    tt.showturtle()
    monster.shape('square')
    monster_place() # randomly place the monster
    g_time.setpos(-10, 240) # set the positions
    g_status.setpos(160, 240)
    g_contact.setpos(-180, 240)
    g_intro.setpos(0, 10)
    g_intro.write(intro, False, 'center', font=('Arial', 12, 'normal'))
    g_time.write('Time:0', False, 'center', font=('Arial', 14, 'normal'))
    g_status.write('Status:Pause', False, 'center', font=('Arial', 14, 'normal'))
    g_contact.write('Contact:0', False, 'center', font=('Arial', 14, 'normal'))
    upper_a.shape('square') 
    upper_a.color('black', '')
    upper_a.setpos(0, 250) # set up the upper area
    upper_a.shapesize(4, 25, 2) 
    upper_a.showturtle()
    motion_a.shape('square')
    motion_a.color('black', '')
    motion_a.setpos(0, -40) # set up the motion area
    motion_a.shapesize(25, 25, 2)
    motion_a.showturtle()

# Snake
def snake_update():
    global L_snake, pos_head, pos_food, gamePause, gameOver, gameStart, g_keypressed, g_length
    t = 300
    game_over() # judge whether the game over
    game_win() # judge whether the game win
    if gameStart == True and is_bounded(tt) == True and gameOver == False and gamePause == False:
        tt.color('blue', 'black') # change the turtle color the same as body
        tt.stamp() # make a stamp of turtle as body
        pos_head = tt.position() # note the position of turtle now
        tt.forward(20) # move forward the snake
        tt.color('blue', 'pink') # change the turtle color back the same as head
        L_snake.append(pos_head) # append the position of body into a list
        if len(L_snake) > g_length:
            L_snake.pop(0) # keep the length of snake in control
        if len(tt.stampItems) > g_length:
            tt.clearstamps(1)
        elif len(tt.stampItems) < g_length:
            t = 350 # slower the speed of snake when it is expanding
        for number, position in list(pos_food.items()): # consume the food when needed
            food_consume(tt.position(), position, number)
    status_update() # update the state of current snake 
    s.ontimer(snake_update, t) # set an ontimer to control the speed of snake
    s.update() # update the screen

# Monster
def monster_place(): # randomly place the monster and make sure their positions can
    global pos_monster
    monster.color('skyblue')
    monster.showturtle()
    while True:
        pos_mons = (random.randint(-240, 240), random.randint(-280, 200)) # randomly choose number as coordinates in range 
        # make sure that the monster can contact with snake in corner and has an initial distance with it
        if pos_mons[0] % 20 == 10 and pos_mons[1] % 20 == 10 and distance(pos_mons, pos_head) > 80: 
            pos_monster = pos_mons
            monster.setpos(pos_monster)
            break


def monster_dir():  # set the direction of monster
    dx, dy = pos_head[0] - pos_monster[0], pos_head[1] - pos_monster[1]
    if dx > 0:
        if dx > abs(dy):  # go right
            monster.setheading(0)
        elif dy > 0:  # go up
            monster.setheading(90)
        else:
            monster.setheading(270)
    elif dx < 0:
        if abs(dx) > dy:  # go left
            monster.setheading(180)
        elif dy > 0:  # go up
            monster.setheading(90)
        else:
            monster.setheading(270)
    next_step = generate_turtle()
    next_step.goto(pos_monster[0]-20, pos_monster[1])
    if is_bounded(next_step) == False:
        monster.setheading(tt.heading())


def monster_update(): # function to control and update the state of monster
    global pos_monster
    t = random.randint(330, 400)
    if gameStart == True and gameOver == False:
            pos_monster = monster.position() # get the position of monster
            monster_dir() # set the direction of monster
            monster.forward(20) # move the monster forward
            s.update() # update the screen
            s.ontimer(monster_update, t) # set a ontimer to control the speed of monster


# Food
def get_number(): # get the food items in number on the screen
    global pos_food, food, number
    radius = 60 # make sure that the food has distance with each other
    deltas = set()
    for x in range(-radius, radius+1):
        for y in range(-radius, radius+1):
            if x*x + y*y <= radius*radius:
                deltas.add((x, y))
    excluded = set()
    number = 0
    while number <= 8:
        x, y = random.randint(-230, 230), random.randint(-260, 180) # randomly choose number to denote the coordinates of position
        if x % 20 == 0 and y % 20 == 10 and (x, y) not in excluded: # make sure the snake can eat the food in directly direction
            pos_food[number] = (x, y)
            number += 1
            excluded.update((x+dx, y+dy) for (dx, dy) in deltas)
            food.goto(x, y) # put the food in the certain place
            food.write(number, False, 'center', font=('Arial', 12, 'normal')) # write the number on food
        else:
            continue


def food_consume(pos_1, pos_2, num): # define the way of consuming food items
    global g_length, pos_food, food
    if distance(pos_1, pos_2) < 20: # eat when the distance of food and snake head is smaller than 20
        del pos_food[num] # delete the number in dictionary
        food.clear() # clear the food item that has been consumed
        for value, position in list(pos_food.items()): # write the rest of food items
            food.goto(position)
            food.write(value+1, False, 'center', font=('Arial', 12, 'normal'))
            s.update()
        g_length += num # increse the length of snake when eat food

# Game status
def game_start(): # start the game
    global gameStart # global the state the gameStart
    if pos_food != {}:
        arrow_key('Right')
        gameStart = True


def game_over(): # judge whether the game is over
    global gamePause, gameOver
    if distance(pos_head, pos_monster) < 20 and gamePause == False and gameStart == True: # if distance of head and monster smaller than 20
        gamePause = True
        gameOver = True
        tt.write('Game Over!!', False, 'right', font=('Arial', 12, 'normal')) # write the information of game over
        s.update()


def game_win(): # judge whether the game is win
    global gamePause, gameOver
    if pos_food == {}: # if all food items are consumed, the game win
        gamePause = True
        gameOver = True
        tt.write('Winner!!!', False, 'right', font=('Arial', 12, 'normal')) # write the information of game win


def game_pause(): # pause the game process when needed
    global gamePause, g_keypressed
    gamePause = not gamePause
    if gamePause == True:
        g_keypressed = 'Pause'
    elif gamePause == False: # use arrow key to restart the game after being paused
        a = int(tt.heading())
        b = list(direction.keys())[list(direction.values()).index(a)]
        arrow_key(b)

# Status_update
def time_update(): # update the time and show it in upper status area with an interval of 1 second
    global Time, g_time
    if gameStart == True and gameOver == False:
        g_time.clear()
        g_time.write('Time:{}'.format(Time), False, 'center', font=('Arial', 14, 'normal'))
        s.update()
        Time += 1 # time plus 1 when 1 second after
    s.ontimer(time_update, 1000)


def status_update(): # update the status of snake and show it when the state changes
    global gamePause, state, gameStart, g_keypressed
    g_status.clear()
    g_status.write('Status:{}'.format(g_keypressed), False, 'center', font=('Arial', 14, 'normal'))
    s.update()


def contact_update(): # update the contact of times that the monster contact with the snake body
    global cnt_contact
    b = monster.position() # get the tuple of position of monster
    if gamePause == False and gameStart == True:
        for pos in L_snake:
            if distance(pos, b) < 20:
                cnt_contact += 1
        g_contact.clear()
        g_contact.write('Contact:{}'.format(cnt_contact), False, 'center', font=('Arial', 14, 'normal'))
        s.update()
    s.ontimer(contact_update, 1000) # update by the time of 1 second

# Tools
def is_bounded(Object): # judge whether the object is in bounded range
    global gamePause, g_keypressed
    x, y = Object.position()
    if -240 <= x <= 240 and -280 <= y <= 200:
        if x >= 235 and Object.heading() == 0:
            return False
        elif x <= -235 and Object.heading() == 180:
            return False
        elif y >= 195 and Object.heading() == 90:
            return False
        elif y <= -275 and Object.heading() == 270:
            return False
        else:
            return True
    else:
        return False


def distance(a, b): # calculate the absolute distance of two tuples
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    return (dx*dx+dy*dy)**0.5


def arrow_key(key): # use arrow key to control the direction of snake
    global g_keypressed, gamePause
    g_keypressed = key # denote the current direction when keypressed
    if key in direction.keys():
        tt.setheading(direction[key])
    status_update() # update the state 
    if gamePause == True and g_keypressed != 'Paused':
        gamePause = False

# Main loop of the game
def game_on(x, y): # click to invoke the game_on function to start the game
    global g_intro, pos_food, gameStart
    s.onscreenclick(None) # close the onclick of screen
    s.tracer(0)
    g_intro.clear()
    get_number() # get numbers of food items on the screen
    game_start() # start the game
    game_loop()


def game_loop(): # define the loop of the game
    if gameStart == True and gameOver == False:
        snake_update()
        monster_update()


def main(): # main process of the code
    s.listen() # ask the screen to listen
    s.onkey(partial(arrow_key, 'Up'), 'Up') # onkey arrow keys to control the move of snake 
    s.onkey(partial(arrow_key, 'Down'), 'Down')
    s.onkey(partial(arrow_key, 'Left'), 'Left')
    s.onkey(partial(arrow_key, 'Right'), 'Right')
    s.onkey(game_pause, 'space') # user can use space key to pause or restart the game
    if gameStart == False:
        init_state() # initialize the original state and show the introduction
        s.tracer(0)
        s.onscreenclick(game_on) # click the screen to start the game
    time_update() # update the game
    contact_update() # update the number of contact
    s.mainloop() # close the game


main()