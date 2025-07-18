API Usage Example
=================

Query the system status:

.. code-block:: bash

   curl http://localhost:8000/api/v1/status

Expected response:

.. code-block:: json

   {
     "cpu": 12.5,
     "ram": 45.3,
     "disk": 67.8,
     "disk_info": {"total": 32.0, "used": 21.7, "free": 10.3},
     "usb": [
       {"mount": "/media/pi/USB", "device": "/dev/sda1", ...}
     ],
     "temp": 48.2,
     "hostname": "raspberrypi",
     "ip": "192.168.1.100",
     "uptime": 123456,
     "battery": {"voltage": 3.7, "status": "NORMAL"}
   }
