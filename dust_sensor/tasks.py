

from celery import shared_task
from logging import getLogger
from DustSensor import DustSensor
from django.conf import settings

logger = getLogger("django.dust_sensor")
logger_fd = getLogger("fluend.dust_sensor")


@shared_task
def refresh_dust_measure():
    ds = DustSensor(settings.DUST_SENSOR_VENTILATION_GPIO, serial_port=settings.DUST_SENSOR_SERIAL_PORT,
                    serial_speed=settings.DUST_SENSOR_SERIAL_SPEED)
    data = ds.measure()

    logger_fd.info({"dust.raw_avg": data[0], "dust.unit_avg": data[1]})
    logger.debug("Average RAW: %0.2f, Average ug/m2: %0.2f" % (data[0], data[1]))
