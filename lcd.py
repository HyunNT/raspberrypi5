#!/usr/bin/env python3
import LCD1602
import time    

def setup():
    # Initialize LCD with I2C address 0x27 and enable backlight
    LCD1602.init(0x27, 1)
    # Display the message 'Greetings!' at the top-left corner (row 0, column 0)
    LCD1602.write(1, 0, 'HI Devicemart!')
    # Display the message 'From SunFounder' on the second line (row 1, column 1)
    LCD1602.write(2, 1, 'I2C LCD1602!')
    time.sleep(2)  # Display messages for 2 seconds

try:
    setup()  # Run the setup function to initialize the LCD and display messages

except KeyboardInterrupt:
    # Clear the LCD display if a keyboard interruption (e.g., Ctrl+C) occurs
    LCD1602.clear()
    pass  # Proceed with no further action
