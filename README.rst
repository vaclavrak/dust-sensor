=====
Django DUST sensor
=====

Read data from dust sensor connected via RPi Serial port. This is proprietary software for customized hardware used by WebEye.services

 - version 0.2.34 fixed avg_unit counting regarding http://www.howmuchsnow.com/arduino/airquality/

Quick start
-----------

1. Add "dust_sensor" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'dust_sensor',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^dust_sensor/', include('dust_sensor.urls')),

3. update settings
        - DUST_SENSOR_VENTIOLATION_GPIO: number of GPIO to enable/disable ventilation
        - DUST_SENSOR_SERIAL_PORT: should be "/dev/ttyAMA0"
        - DUST_SENSOR_SERIAL_SPEED: should be 9600

4. set up loggers
    for fluentd or td-agent  use handler name fluend.dust_sensor
    for django human readable logger handler use django.dust_sensor

5. add celery beat schedule settings

    CELERYBEAT_SCHEDULE = {
        'refresh_dust_measure': {
            'task': 'dust_sensor.tasks.refresh_dust_measure',
            'schedule': timedelta(minutes=1)
        }
    }


