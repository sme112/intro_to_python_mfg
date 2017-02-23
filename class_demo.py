# Define the class.
# Note the naming convention of the class and how it differs from a variable
# or a function name. Good examples? 'Machine' or 'GantryMachine' are good
# choices for Python classes.
class Machine(object):

    def __init__(self, x_travel, y_travel, z_travel):
        self.x_travel = x_travel
        self.y_travel = y_travel
        self.z_travel = z_travel
        self.x_axis_pos = 0.0
        self.y_axis_pos = 0.0
        self.z_axis_pos = 0.0

    def move_x_axis(self, x_move):
        print("The x-axis is currently at", self.x_axis_pos)
        temporary_move = self.x_axis_pos + x_move
        # Perform some validation.
        if temporary_move > self.x_travel or temporary_move < 0.0:
            print("Invalid move.")
        else:
            self.x_axis_pos = temporary_move
            print("The x-axis is now at", self.x_axis_pos)

# -----------------------------------------------------------------

# EXECUTION STARTS HERE!

# Create a class instance.
my_machine = Machine(12, 12, 12)

# Move the X-axis of the machine we created. Valid move.
print("Let's move 1 unit in the positive X-direction.")
my_machine.move_x_axis(1)
print()

# Overtravel the X-axis of the machine in the negaitve X-direction. Invalid move.
print("Let's now move 2 units in the negative X-direction.")
my_machine.move_x_axis(-2)
print()

# Overtravel the X-axis of the machine in the positive X-direction. Invalid move.
print("Let's now move 13 units in the positive X-direction.")
my_machine.move_x_axis(13)
print()

# Ok. Let's do a good move.
print("Let's try to move 5 units in the positive X-direction.")
my_machine.move_x_axis(5)
