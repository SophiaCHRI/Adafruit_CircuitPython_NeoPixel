import time
from apa102_pi.driver import apa102
 
def display_clock(seconds, minutes, hours):
    clock = [0x808080, 0x000000, 0x000000, 0x000000, 0x000000 ] * 12 # gray, black, black, black, black
    clock[0] = clock[15] = clock[30] = clock[45] = 0xFFFFFF # white
 
    if hours >= 12:
        hours = hours-12
 
    clock[hours * 5 + minutes // 12] = 0xFF0000 # Red
    clock[minutes] = 0x0000FF # Blue
    clock[seconds] = 0x00FF00 # Green
 
    # Display the clock
    strip = apa102.APA102(num_led=60)
    # Turn off all pixels (sometimes a few light up when the strip gets power)
    strip.clear_strip()
 
    # Prepare a few individual pixels
   
    for i in range(len(clock)):
        print("i: " + str(i) + " color: " + str(clock[i]))
        strip.set_pixel_rgb(i + 1, clock[i])
    print()  
   
    # Copy the buffer to the Strip (i.e. show the prepared pixels)
    strip.show()
   
 
while True:
    # Get current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour
 
    print("hours: " + str(hours))
    print("minutes: " + str(minutes))
    print("seconds: " + str(seconds))
 
 
    # Display the clock
    display_clock(seconds, minutes, hours)
 
    # Wait for one second before updating again
    time.sleep(1)