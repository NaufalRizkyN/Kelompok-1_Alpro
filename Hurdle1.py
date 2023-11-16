def turn_right():
    turn_left()
    turn_left()
    turn_left()

def zigzag():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        zigzag()
    else:
        move()