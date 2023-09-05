import cozmo
from cozmo.util import degrees, distance_mm

# Define a constant for unit distance in millimeters
UNIT_DISTANCE_MM = 100

# Using a combination of vertical and horizontal movements.
##########################################################>
##########################################################> move_to_target_position()
def move_to_target_position(robot, start, end):
    distance_x = end[0] - start[0]
    distance_y = end[1] - start[1]
    robot.say_text("Now I will move vertically and horizontally").wait_for_completed()
    while distance_x != 0 or distance_y != 0:
        if distance_y != 0:
            ##########################> Move vertically
            direction = 1 if distance_y > 0 else -1
            robot.drive_straight(distance_mm((UNIT_DISTANCE_MM * direction)), cozmo.util.speed_mmps(100)).wait_for_completed()
            distance_y = distance_y - direction

        if distance_x != 0:
            ##########################> Turn and move horizontally
            direction = -1 if distance_x > 0 else 1
            robot.turn_in_place((degrees(90 * direction))).wait_for_completed()
            robot.drive_straight(distance_mm(UNIT_DISTANCE_MM), cozmo.util.speed_mmps(100)).wait_for_completed()
            robot.turn_in_place(degrees(-90 * direction)).wait_for_completed()
            distance_x = distance_x + direction
    ###################################> play_anim
    robot.say_text("Now I am at x and y").wait_for_completed()
    robot.play_anim(name="anim_petdetection_dog_03").wait_for_completed()


##########################################################>
##########################################################> cozmo_program()
def cozmo_program(robot: cozmo.robot.Robot):
    start_position = (0, 0)     # Starting position (0, 0)
    target_position = (2, 4)   # Set your target position (x, y)
    move_to_target_position(robot, start_position, target_position)

    # If you want to start from a different position, uncomment and use the following code:
    start_position = (2, 4)   # Set your starting position (a, b)
    target_position = (0, 0)  # Set your target position (x, y)
    move_to_target_position(robot, start_position, target_position)

##########################################################>
##########################################################> run_program ()
if __name__ == '__main__':
    cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)

