"""
HipMonsters.com 2024
See more at www.HipMonsters.com
This code is for a RaspberryPi and sends random commands to a robots.
Set up two motors:
pins: 17 & 22 Right motors
pins: 24 & 23 Left motors
"""
import datetime
import time
import random
import RPi.GPIO as gpio

# List of valid movements for the robot
MOVEMENT_DIRECTIONS = ["f","b", "r", "l"]

# Define minium length of time to robot should go in any one direction
MOVE_LENGTH_MIN = 3

# Intial direction
CURRENT_DIRECTION = "f"

# Set last time movement changed to now
LAST_MOVE_TIME = datetime.datetime.now()

def init(): 
    """
    Tells the RaspberryPi the ports are for outputing commands
    """   
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

def move(direction, wait_len):
    """
    Sends commands to the robot using gpio 
    """ 
    init()
    #if directions is "f"
    if direction == "f":
        # Send command False (off) to port 17.
        gpio.output(17, False)
        # Send command True (on) to port 22.
        gpio.output(22, True)
        gpio.output(23, True)
        gpio.output(24, False)

        # Print direction to screen for debug
        print("forwards")

    elif direction == "b":
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, False)
        gpio.output(24, True)
        print("backwards")

    elif direction == "l": 
        gpio.output(17, True)
        gpio.output(22, False)
        gpio.output(23, True)
        gpio.output(24, False)
        print("left")

    elif direction == "r": 
        gpio.output(17, False)
        gpio.output(22, True)
        gpio.output(23, False)
        gpio.output(24, True)
        print("right")
     
    # Release control
    gpio.cleanup() 

    # sleep before finishing up commands
    time.sleep(wait_len)
 
# Loop forever
while True:
   
   # Find the time in secods since the last movement change
   time_since_last_change = (datetime.datetime.now() - LAST_MOVE_TIME).total_seconds ()

   # If time since lats change exceeds movement length run the code
   if time_since_last_change  < MOVE_LENGTH_MIN: 
       
       # Filter out current move from valid moves
       valid_moves = [v for v in MOVEMENT_DIRECTIONS if v != CURRENT_DIRECTION]

       # Pick a movement randomly
       CURRENT_DIRECTION = random.choice(valid_moves)
       
       # Random wait time
       rnd_pause = random.randint(0, 2)
    
       #Change direction
       move(CURRENT_DIRECTION,rnd_pause )

       # Set last movment time
       LAST_MOVE_TIME = datetime.datetime.now()

# Happy Coding