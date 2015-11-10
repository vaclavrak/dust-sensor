

from django.core.management.base import BaseCommand, CommandError
from dust_sensor.DustSensor import DustSensor
from django.conf import settings
from logging import getLogger


logger = getLogger("django.dust_sensor")
logger_fd = getLogger("fluend.dust_sensor")



class Command(BaseCommand):
    help = 'Custom measure dust'

    def handle(self, *args, **options):
        ds = DustSensor(settings.DUST_SENSOR_VENTILATION_GPIO, settings.DUST_SENSOR_SERIAL_PORT,
                        settings.DUST_SENSOR_SERIAL_SPEED)
        data = ds.measure()
        logger_fd.info({"dust.raw_avg": data[0], "dust.unit_avg": data[1]})
        logger.debug("Average RAW: %0.2f, Average ug/m2: %0.2f" % (data[0], data[1]))
        print "Raw value: %0.2f" % data[0]
        print "Unit value: %0.2f" % data[1]
