=====
Django DUST sensor
=====

Read data from dust sensor connected via RPi Serial port. This is proprietary software for customized hardware used
by WebEye.services


Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'dust_sensor',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^dust_sensor/', include('dust_sensor.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/dust_sensor/ to read data.