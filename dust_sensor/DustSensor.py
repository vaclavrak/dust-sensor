"""

 Read data from dust sensor and store it to statsite

 by Vaclav Rak  <me@vena.cz>

"""


class DustSensor(object):
    _serial_port = ""
    _serial_speed = 9600
    _ventilation_gpio = None

    def __init__(self, ventilation_gpio, serial_port='/dev/ttyAMA0', serial_speed=9600):
        self._serial_port = serial_port
        self._serial_speed = serial_speed
        self._ventilation_gpio = ventilation_gpio

