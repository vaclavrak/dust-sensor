# django-dust-sensor

reading data from dust sensor and integrate it in django application. 

## requirement settings in django app:

 * DUST_SENSOR_VENTILATION_GPIO: number of GPIO to enable/disable ventilation
 * DUST_SENSOR_SERIAL_PORT: should be "/dev/ttyAMA0"
 * DUST_SENSOR_SERIAL_SPEED: should be 9600

## set up loggers
 * for fluentd or td-agent  use handler name fluend.dust_sensor
 * for django human readable logger handler use django.dust_sensor
    
### settings.py
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'fluent': {
                'level': 'INFO',
                'db': '[your DB name]',
                'table': '[your table name]',
                'class': 'tdlog.logger.TreasureDataHandler'
            }
        },
        'loggers': {
            'django.dust_sensor': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'fluend.dust_sensor': {
                'handlers': ['fluent'],
                'level': 'INFO',
                'propagate': True
            }
        },
    }


## setup CELERY BEAT scheduler (optional)

    CELERYBEAT_SCHEDULE = {
        'refresh_dust_measure': {
            'task': 'dust_sensor.tasks.refresh_dust_measure',
            'schedule': timedelta(minutes=1)
        }
    }
