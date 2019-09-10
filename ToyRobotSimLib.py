direction_tuple = ('NORTH', 'EAST', 'SOUTH', 'WEST')
commands_avail = ('PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT')
table_size = (5,5)
# table_size can be changed. 0,0 is the south-west corner, table_size[0] - 1, table_size[1] -1 is the north-east corner.
table_max_y = table_size[1] - 1
table_max_x = table_size[0] - 1


class ROBOT:
    """creates a class for the robot. This class stores the coordinates and direction of the Robot."""
    def input_discard(self):
        """This function takes the list of input from the user. If no PLACE command is issued on the first input given,
        the input is discarded. If there is an existing Robot position, any valid inputs will be processed on the robot.
        Input will stop when a REPORT command is issued, as the program will want to report the output of the Robot."""
        commands = []
        print("INPUT COMMANNDS FOR ROBOT:")
        while "REPORT" not in commands:
            hold = input()
            commands.append(hold)
            if not hold:
                hold = input()
                if not hold:
                    break
        for i in commands:
            if 'PLACE' in i:
                xyd = i.split(" ")
                xyd = xyd[1].split(",")
                x = int(xyd[0])
                y = int(xyd[1])
                d = xyd[2]
                if 0 <= x <= table_max_x and 0<= y <= table_max_y and d in direction_tuple:
                    return commands
        print("NO VALID PLACE COMMAND IN INPUT")
        try:
            if self.x and self.y and self.d:
                print("ROBOT POSITION EXISTS, PROCESSING INPUT ON EXISTING POSITION")
                return commands
        except AttributeError:
            print('NO VALID ROBOT POSITION EXISTS. INPUT DISCARDED')

    def place(self,x, y, direction):
        """Places the Robot at the location given by valid place command"""
        self.x = x
        self.y = y
        self.d = direction

    def move(self):
        """moves the robot one unit in the direction the robot is facing"""
        if self.d == 'NORTH' and (self.y + 1) <= table_max_y:
            self.y += 1
        elif self.d == 'EAST' and (self.x + 1) <= table_max_x:
            self.x += 1
        elif self.d == 'SOUTH' and (self.y - 1) >= 0:
            self.y -= 1
        elif self.d == 'WEST' and (self.x - 1) >= 0:
            self.x -= 1
        else:
            print("Edge of Table Reached!")

    def left(self):
        """rotates the robot to the left by 90 degrees."""
        if self.d in direction_tuple:
            index = direction_tuple.index(self.d)
            if index == 0:
                self.d = direction_tuple[3]
            else:
                self.d = direction_tuple[index - 1]
        else:
            print("NO VALID ROBOT POSITION")

    def right(self):
        """rotates the robot to the right by 90 degrees"""
        z = len(direction_tuple)
        if self.d in direction_tuple:
            index = direction_tuple.index(self.d)
            if index == (z-1):
                self.d = direction_tuple[0]
            else:
                self.d = direction_tuple[index + 1]
        else:
            print("NO VALID ROBOT POSITION")

    def report(self):
        print(self.x,',', self.y,',', self.d)


def main():
    """Prints instructions for program. Once receiving input from input_discard, it processes the input on the Robot,
    moving it around. It then reports the robots position in the command line. Once processed, program asks whether more
    input is to be given, hit 'Y' otherwise hit 'N' to exit the program. 'Y' allows more input to be added."""
    robot = ROBOT()
    print("COMMANDS AVAILABLE:", commands_avail)
    print("'PLACE' must be used in the form: PLACE x,y,direction")
    print("VALID DIRECTIONS:", direction_tuple)
    print("MOVE: moves the robot one unit in the direction its facing, unless it would fall of the tabletop")
    print("LEFT and RIGHT: rotates the robot 90 degrees anti-clockwise or clockwise respectively")
    print("REPORT: prints the position on the tabletop and which direction the robot is facing")
    print("NOTE: position 0,0 is south-west corner and 4,4 is  north-east corner. Size can be changed in source code")
    print("NOTE: if REPORT in input, all previous commands processed and reported. Option to enter more input given.")
    while True:
        commands = robot.input_discard()
        try:
            for i in commands:
                if commands_avail[0] in i:
                    xyd = i.split(' ')
                    xy = xyd[1].split(',')
                    x = int(xy[0])
                    y = int(xy[1])
                    d = xy[2]
                    robot.place(x, y, d)
                elif i == commands_avail[1]:
                    robot.move()
                elif i == commands_avail[2]:
                    robot.left()
                elif i == commands_avail[3]:
                    robot.right()
                elif i == commands_avail[4]:
                    robot.report()
        except TypeError:
            print("NO VALID PLACE OR EXISTING ROBOT POSITION")
        print("Would you like to enter more input: 'Y' for yes or 'N' to quit")
        cont = input()
        while cont != 'N' and cont != 'Y':
            print("INVALID COMMAND!\nWould you like to enter more input: 'Y' for yes or 'N' to quit")
            cont = input()
        if cont == 'N':
            break
    print("Exiting Program")


if __name__ == '__main__':
    main()

