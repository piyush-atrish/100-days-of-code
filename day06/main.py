# Day 6- Reeborg's World Maze Solution - Key Concepts:
# - Function creation with def to encapsulate repeated actions (turn_right)
# - While loops for unknown iteration counts (until goal reached)
# - Conditional logic (if/elif/else) for path decision making
# - Boolean checks for wall/clear path detection (right_is_clear(), front_is_clear())
# - Problem-solving with sequential robot commands (move(), turn_left())
# - Top-down execution flow with nested function calls
# - Edge case handling (dead ends via turn_left when blocked)

# Note: This implements a "wall follower" algorithm (right-hand rule)
# for maze navigation problems in Reeborg's World

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while at_goal()== False:

    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear()== True:
        move()
    else:
        turn_left()
       