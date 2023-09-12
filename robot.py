
class Robot:
    def __init__(self):
        self.direction = "N"
        self.x = 0
        self.y = 0

    def get_direction(self, turn):
        new_directions = ["N", "W", "S", "E"]*2  # simple solution

        index = new_directions.index(self.direction)

        if turn == "L":
            index += 1

        if turn == "R":
            index -= 1

        self.direction = new_directions[index]
        return self.direction

    def start(self):

        print("Hello! Robot coming online")

        print("""Command the robot with:
      L - turn left
      R - turn right
      M - move forward
      ? - this message
      Q - quit """)

        while True:

            instructions = input("> ").upper()

            if instructions in ("L", "R"):
                self.get_direction(instructions)

            if instructions == "M":
                if self.direction == "N":
                    self.y += 1

                if self.direction == "S":
                    self.y -= 1

                if self.direction == "W":
                    self.x -= 1

                if self.direction == "E":
                    self.x += 1

            if instructions == "?":
                print("""Command the robot with:
              L - turn left
              R - turn right
              M - move forward
              ? - this message
              Q - quit """)
                continue

            if instructions == "Q":
                print("Robot shutting down")
                return False

            print(f"Robot at ({self.x}, {self.y}) facing {self.direction}")
            continue


robot = Robot()
robot.start()


"""

Create a command line app that prompts for commands and moves a rover around a 2D plane.
The robot should point in a direction, turn to face different directions, and move in the direction it is facing.

Demo:
_________________________
Hello! Robot coming online.
Command the robot with:
  L - turn left TURN
  R - turn right TURN
  M - move forward
  ? - this message
  Q - quit

> M
Robot at (0, 1) facing North

> L
Robot at (0, 1) facing West

> M
Robot at (-1, 1) facing West

> ?
Command the robot with:
  L - turn left
  R - turn right
  M - move forward
  ? - this message
  Q - quit

> Q
Robot shutting down.
"""
