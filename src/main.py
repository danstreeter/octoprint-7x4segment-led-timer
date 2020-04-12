# System Imports
import board
import busio
from multiprocessing import Process
import time

# Framework / Library Imports
# Import the HT16K33 LED matrix module.
import adafruit_ht16k33.segments

# Application Imports

# Local Imports
import config
from led_encoder import (
    custom_char,
    encode
)
from octoprint.printer import Printer


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)

# Create the display
display = adafruit_ht16k33.segments.Seg7x4(i2c)

# Create a Printer

printer = Printer(
    url=config.OCTOPRINT_URL,
    apikey=config.OCTOPRINT_APIKEY
)

# Clear the display
display.fill(0)

check_timer = 0
do_action = True
display_proc = False

def idle_status():
    while True:
        states = [
            '.   ',
            ' .  ',
            '  . ',
            '   .',
            '  . ',
            ' .  ',
        ]
        for state in states:
            display.fill(0)
            display.print(state)
            display.show()
            time.sleep(0.375)

def off_status():
    display.fill(0)
    display.print(' 0FF')
    # display.marquee(' 0FF')
    display.show()

def _sec_to_mmss(seconds):
    m, s = divmod(seconds, 60)
    # h, m = divmod(m, 60)
    return '{:02d}{:02d}'.format(m, s) # Returns MMSS String
    # return '{:02d}:{:02d}'.format(m, s) # Returns MM:SS String
    # return (m, s) # Returns Tuple

def printing_status(secs_remaining):
    display.fill(0)
    process_secs = secs_remaining
    while True:
        time_display = _sec_to_mmss(process_secs)
        display.print(time_display + ':')
        display.show()
        time.sleep(0.5)
        display.print(time_display + ';')
        display.show()
        time.sleep(0.5)
        if process_secs > 0:
            process_secs -= 1



def paused_status():
    display.fill(0)
    display.set_digit_raw(0, custom_char('p'))
    display[1] = 'A'
    display.set_digit_raw(2, custom_char('u'))
    display[3] = '5'
    display.show()

def cancelled_status():
    display.fill(0)
    display[0] = 'C'
    display[1] = 'A'
    display.set_digit_raw(2, custom_char('n'))
    display[3] = 'C'
    display.show()

def other_status():
    display.fill(0)
    display[0] = '0'
    display.set_digit_raw(1, custom_char('t'))
    display.set_digit_raw(2, custom_char('h'))
    display.set_digit_raw(3, custom_char('r'))
    display.show()


try:
    while True:
        check_timer += 1
        # print('Working... [' + str(config.LOOP_TIMER) + '] ' + str(check_timer))

        if do_action is True:
            status = printer.status()
            if status == 'off':
                # display_proc = Process(target=idle_status, args=())
                display_proc = Process(target=off_status, args=())
                display_proc.start()
            elif status == 'idle':
                display_proc = Process(target=idle_status, args=())
                display_proc.start()
            elif status == 'printing':
                secs_remaining = printer.remaining()
                display_proc = Process(
                    target=printing_status,
                    args=(
                        [secs_remaining]
                    )
                )
                display_proc.start()
            elif status == 'paused':
                display_proc = Process(target=paused_status, args=())
                display_proc.start()
            elif status == 'cancel':
                display_proc = Process(target=cancelled_status, args=())
                display_proc.start()
            elif status == 'other':
                display_proc = Process(target=other_status, args=())
                display_proc.start()
            else:
                display.print('E. 01')

            do_action = False

        if check_timer == config.LOOP_TIMER:
            check_timer = 0
            do_action = True
            display_proc.terminate()
            display_proc = False
        time.sleep(1)

except KeyboardInterrupt:
    print('Quitting')
    if display_proc is not False and display_proc.is_alive():
        display_proc.terminate()
    display.print('  :  ')

except Exception as e:
    if display_proc is not False and display_proc.is_alive():
        display_proc.terminate()
    print(e)
    display.print(' . .: . .')
