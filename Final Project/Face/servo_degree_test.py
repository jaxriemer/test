import time
from adafruit_servokit import ServoKit

# Set channels to the number of servo channels on your kit.
# There are 16 channels on the PCA9685 chip.
kit = ServoKit(channels=16)

# Name and set up the servo according to the channel you are using.
eye_vertical_servo= kit.servo[4]
eye_horizontal_servo = kit.servo[1]
eyelid_upper_servo = kit.servo[2]
eyelid_lower_servo = kit.servo[0]
eyebrow_servo_servo = kit.servo[3]

# Set the pulse width range of your servo for PWM control of rotating 0-180 degree (min_pulse, max_pulse)
# Each servo might be different, you can normally find this information in the servo datasheet
servo.set_pulse_width_range(500, 2500)

while True:
    try:
        # Set the servo to 180 degree position
        eyebrow_servo_servo.angle = 60
        time.sleep(0.27)
        # Set the servo to 0 degree position
        eyebrow_servo_servo.angle = 90
        time.sleep(0.27)

    except KeyboardInterrupt:
        # Once interrupted, set the servo back to 0 degree position
        servo.angle = 0
        time.sleep(0.5)
        break


    """
    eyelid_upper:
    open:30
    close:3
    
    eyelid_lower: 
    open
    close
    
    eyebrow:
    open: 25
    close: 0
    
    
    eye_horizotal:
    left: 85
    right: 0
    
    
    eye_vertical:
    top:40
    bottom:5
    
    """

