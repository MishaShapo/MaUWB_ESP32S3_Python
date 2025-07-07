# Import all board pins.
import busio
import board
import time
from digitalio import DigitalInOut, Direction, Pull

# Import the SSD1306 module.
import adafruit_ssd1306

RXD2 = 18
TXD2 = 17

UWB_INDEX = 0
UWB_TAG_COUNT = 1

reset = DigitalInOut(board.GPIO16)
reset.direction = Direction.OUTPUT
reset.value = True

# Create the I2C interface.
i2c = busio.I2C(board.GPIO38, board.GPIO39)
uart = busio.UART(baudrate=115200, timeout=1, tx=board.GPIO17,rx=board.GPIO18, bits=8, parity=None, stop=1)

def logoshow(display):
    display.fill(0);
    textToShow = f"""Get Range
JSON: A0"""
    display.text(textToShow,0,0,1,size=2);
    display.show();

    time.sleep(1);

def sendData(cmd, timeout: int = 2, debug = True) -> None:
    if debug:
        print("--->",cmd)
    uart.write(bytes(f"{cmd}\r\n", "utf-8"))

def sendDataAndReadResponse(cmd, timeout: int = 2, debug = True) -> Union[str,None]:
    sendData(cmd, timeout, debug)
    
    stamp = time.monotonic()
    response = b""
    while (time.monotonic() - stamp) < timeout:
        if  uart.in_waiting:
            response += uart.readline();
    
    if debug:
        print("<---", response)
        
    return str(response)
    

def config_cmd():
    """
    AT+SETCFG=(x1),(x2),(x3),(x4)
    x1:Device ID(Anchor 0-7,Tag 0-63)
    x2:Device Role(0:Tag / 1:Anchor)
    x3:Equipment communication rate(0:850K/1:6.8M,Default:6.8M)
    x4:Range filtering is enabled(0:Close / 1:Open)
    """
    return f"AT+SETCFG={UWB_INDEX},0,1,1"
    

def cap_cmd():
    """
    AT+SETCAP=(x1),(x2),(x3)
    x1:Tag capacity (default: 10, maximum: 64)
    x2:Time of a single time slot (6.8M not less than 10ms,850K not less than 15ms)
    X3:extMode, whether to increase the passthrough command when transmitting
        0: normal packet when communicating,
        1: extended packet when communicating
    """
    return f"AT+STETCAP={UWB_TAG_COUNT},10,1"
    
    


# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
# Alternatively you can change the I2C address of the device with an addr parameter:
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()

# Setup UART AT
sendDataAndReadResponse("AT")
time.sleep(1)

logoshow(display)

while True:
    if uart.in_waiting:
        print(uart.readline())
    