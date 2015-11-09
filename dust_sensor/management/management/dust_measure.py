

from django.core.management.base import BaseCommand, CommandError
from dust_sensor.DustSensor import DustSensor
from django.conf import settings


class Command(BaseCommand):
    help = 'Custom measure dust'

    def handle(self, *args, **options):
        ds = DustSensor(settings.DUST_SENSOR_VENTILATION_GPIO, settings.DUST_SENSOR_SERIAL_PORT,
                        settings.DUST_SENSOR_SERIAL_SPEED)
        data = ds.measure()
        print "Raw value: %0.2f" % data[0]
        print "Unit value: %0.2f" % data[1]
