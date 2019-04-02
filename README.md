CoopDoor
========
Collection of scripts to operate a chicken door system.

- Based on code from https://github.com/beardymcbeards/robocoop 
- The wiring design in https://github.com/ericescobar/Chicken_Door
- Ansible config removed for simplicity and to create a python only app

Setup
-----
 
Run ```setup.py```


Notable Files
-------------
- coopdoor.py - interface to open and close the door
- coopdoor.cfg - required config for gpio settings
- poller.py - returns a json dictionary of the door sensor's data

Todo
----
- [ ] build setup.py#2
- [ ] build timers.py#1
- [ ] build camera snapshot process
