# Vehicle_Tracking

<h3>Click to see Live Implementation: ☛ http://159.89.165.35/anil_soln/ </h3><br>

Live Vehicle tracking using Google Maps Javascipt  API, Django, Python, Firebase.

Tools and API used:

* Google Maps Javascript API -- Accessing google maps.
* Django                -- Python Framework as backend for fetching data and retreiving data from database.
* Firebase              -- For getting realtime updates from the driver and his location.
* Javascript            -- Refreshing the map (not the page) every 30 sec to be updated for the current position of vehicle.


Note : "This folder need to be kept inside the django-main-project folder and shold be installed in setting.py file."<br>

Other functionalities and scope:

*I have hosted it on digitalocean server as a django app.<br>
*If the vehicle is scheduled, running or stopped, its symbol will change in map accordingly as blue,green,red respectively.<br>
*Marker has also infoWindow, so that we can know the exact location of the vehicle.<br>
*In firebase, one dummy database has been taken, but as it is a realtime database, so can be updated by the driver about his location.<br>
*Javascript is used for refreshing the map, every 30 sec., its better with overlay function of Google Maps Javascript API.<br>
