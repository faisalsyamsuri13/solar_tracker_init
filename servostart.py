# Write your code here :-)
#from gpiozero import servo
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # Set the mode to use the physical pin number

servo_pin = 32  # Set the GPIO pin number to control the servo motor
delay = 0.1
GPIO.setup(servo_pin, GPIO.OUT)  # Set the servo_pin as output

# Set the PWM frequency and start the PWM instance
pwm_frequency = 50  # in Hz
pwm = GPIO.PWM(servo_pin, pwm_frequency)
pwm.start(0)

# Set the duty cycle for the servo motor position
def set_position(angle):
    duty_cycle = 2 + angle / 18
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Move the servo motor to the specified angle
while(True):
    try:
        angle_int = int(input("Enter angle: "))
        for i in range(2):
            set_position(angle_int)
            if angle_int > 180:
                raise ValueError

    except KeyboardInterrupt:
        #Clean the GPIO when exiting the loop
        for i in range(2):
            set_position(0)
        pwm.stop()
        GPIO.cleanup()
        print("\nSession has been interrupted. Return to zero position.")
        break