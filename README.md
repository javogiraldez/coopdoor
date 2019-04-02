 ____                            ____                            
/\  _`\                         /\  _`\                          
\ \ \/\_\    ___     ___   _____\ \ \/\ \    ___     ___   _ __  
 \ \ \/_/_  / __`\  / __`\/\ '__`\ \ \ \ \  / __`\  / __`\/\`'__\
  \ \ \ \ \/\ \ \ \/\ \ \ \ \ \ \ \ \ \_\ \/\ \ \ \/\ \ \ \ \ \/ 
   \ \____/\ \____/\ \____/\ \ ,__/\ \____/\ \____/\ \____/\ \_\ 
    \/___/  \/___/  \/___/  \ \ \/  \/___/  \/___/  \/___/  \/_/ 
                             \ \_\                               
                              \/_/                               

CoopDoor
========
Collection of scripts to operate a chicken door system.

Based on code from https://github.com/beardymcbeards/robocoop and the wiring design in https://github.com/ericescobar/Chicken_Door
    (ansible config removed for simplicity and to create a python only app)

Setup
-----
Run setup.py


Notable Files
-------------
- coopdoor.py - interface to open and close the door
- coopdoor.cfg - required config for gpio settings
- poller.py - returns a json dictionary of the door sensor's data
