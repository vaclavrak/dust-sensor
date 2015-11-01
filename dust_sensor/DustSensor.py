"""

 Read data from dust sensor and store it to statsite

 by Vaclav Rak  <me@vena.cz>

"""

import RPi.GPIO as GPIO
from serial import Serial
from serial.serialutil import SerialException
from time import sleep, time
from datetime import timedelta, datetime
from logging import getLogger

logger = getLogger("DustSensor")


class DustSensor(object):
    _serial_port = ""
    _serial_speed = 9600
    _ventilation_gpio = None
    _timeout = None
    state = "N/A"

    def __init__(self, ventilation_gpio, serial_port='/dev/ttyAMA0', serial_speed=9600):
        self._serial_port = serial_port
        self._serial_speed = serial_speed
        self._ventilation_gpio = ventilation_gpio
        self._timeout = timedelta(seconds=30)
        self.state = "INITIATED"

    def timeout(self, timeout):
        """
        change measure time
        :param timeout: timedelta
        """
        self._timeout = timeout


    @property
    def ventilation(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._ventilation_gpio, GPIO.OUT)
        value = GPIO.input(self._ventilation_gpio)
        logger.debug("Ventilation is %s" % value)
        return value

    def ventilation(self, state):
        logger.debug("Ventilation turning %s" % state)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._ventilation_gpio, GPIO.OUT)
        GPIO.output(self._ventilation_gpio, state)

    def read_data(self):
        _serial = Serial(self._serial_port, self._serial_speed)
        if _serial.isOpen():
            _serial.close()

        _serial.open()
        i = 0
        raw_value = []
        unit_value = []
        start_time = datetime.now()

        while (start_time + self._timeout) > datetime.now():
            try:
                ch = _serial.readline().strip()
                if ch == "0000":
                    self.state = "STARTING_VENTILATOR"
                else:
                    self.state = "MEASURING"
                    if i == 0:
                        raw_value.append(float(ch))
                    if i == 1:
                        unit_value.append(float(ch))
                    if i > 2 or ch.strip() == "":
                        i = 0
                    i += 1
                self.state = "DONE"
            except OSError:
                _serial.close()
                self.state = "ERROR_SERIAL"
                break

        if _serial.isOpen():
            _serial.close()

        if len(raw_value) == 0 or len(unit_value) == 0:
            raise Exception("Measurement was not successful, last state %s" % self.state)

        avg_raw = sum(raw_value) / float(len(raw_value))
        avg_unit = sum(unit_value) / float(len(unit_value))

        return [avg_raw, avg_unit]

    def measure(self):
        self.ventilation(1)
        data = self.read_data()
        self.ventilation(0)
        return data